#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

import constants
import items.unique_items
from cities.city import City
from cities.inn import Inn
from cities.shop import Shop
from cities.square import Square
from commands.check_equipment_command import CheckEquipmentCommand
from commands.check_inventory_command import CheckInventoryCommand
from commands.check_money_command import CheckMoneyCommand
from commands.check_stats_command import CheckStatsCommand
from commands.command_words import CommandWords
from commands.describe_command import DescribeCommand
from commands.drop_command import DropCommand
from commands.east_command import EastCommand
from commands.enter_command import EnterCommand
from commands.equip_command import EquipCommand
from commands.help_command import HelpCommand
from commands.map_command import MapCommand
from commands.north_command import NorthCommand
from commands.pick_up_command import PickUpCommand
from commands.quit_command import QuitCommand
from commands.south_command import SouthCommand
from commands.unequip_command import UnequipCommand
from commands.use_potion_command import UsePotionCommand
from commands.west_command import WestCommand
from player import Player
from space import Space
from unique_places.argonath import Argonath
from unique_places.barad_dur import BaradDur
from unique_places.black_gate import BlackGate
from unique_places.derningle import Derningle
from unique_places.dol_guldur import DolGuldur
from unique_places.goblin_town import GoblinTown
from unique_places.isenguard import Isenguard
from unique_places.isenmouthe import Isenmouthe
from unique_places.minas_morgul import MinasMorgul
from unique_places.moria import Moria
from unique_places.ost_in_edhil import OstInEdhil
from unique_places.tharbad import Tharbad
from unique_places.tom_bombadil_house import TomBombadilHouse
from unique_places.tower_of_cirith_ungol import TowerOfCirithUngol
from unique_places.weathertop import Weathertop


def getWorld():
    """
    创造中土世界。中洲由一系列相连的地区组成。地区中可能有城市和独特地点。城市中可能有旅馆、广场和商店。

    @return:    创建的地区列表。
    """
    # 夏尔 - 霍比特人的故乡
    # 旅店
    description = "为旅客提供休息的地方。"
    greeting = "欢迎光临我们的旅店！我是托肯斯维尔-巴金斯家族的萨利。"
    sallyInn = Inn("萨利的旅店", description, greeting, 5)
    # 商店
    description = "按照霍比特人的标准，这是很奇特的选择。"
    greeting = "我们有奇特的商品。"
    sallyShop = Shop("萨利的商店", description, greeting, constants.RegionType.ERIADOR, 4, 0)
    # 广场
    description = "很多霍比特人，大多是闲话家常。"
    greeting = "你听到最新消息了吗？"
    talk = {
        "洛比莉亚·萨克维尔-巴金斯": "走开！",
        "纳夫特尔·图克": "去冒险是吗？请收下我的手杖。",
        "阿马兰斯·白兰地鹿": "吃点零食吧！",
        "巴尔博·巴金斯": "街上的消息是，洛比莉亚正试图收购巴金斯家的袋底洞！",
        "费迪南德·图克": "我想知道甘道夫什么时候来？"
    }
    hobbitonSquare = Square("霍比屯广场", description, greeting, talk, items.unique_items.hobbitonSquareItems)
    # 城市
    description = "霍比屯是夏尔中部西区界内的一个村庄。它坐落在小河的两岸，距离东南方的邻村傍水镇约一英里。"
    greeting = "“你听说过这个消息吗？”"
    hobbiton = City("霍比屯", description, greeting, [sallyInn, sallyShop, hobbitonSquare])
    # 夏尔
    description = """
    夏尔分为北、南、东、西四个区；它的首府是位于西区的白岗上的大洞镇。大洞镇市长是夏尔的霍比特人当中唯一真正的官员。
    夏尔主要依赖农业，其土地非常适合耕种。它的主要产物之一是烟斗草，其特别适合在远南部的温暖地区种植。
    """
    shire = Space("夏尔", description, constants.RegionType.ERIADOR, battleProbability=constants.SpaceSpawnProb.shire,
                  battleBonusDifficulty=constants.SpaceBonusDiff.shire, city=hobbiton)

    # 老林子 - 汤姆·邦巴迪尔的家
    # 独特地点
    description = "一所居住在柳条河山谷的神秘而强大的存在的房子。"
    greeting = """
    “老汤姆·邦巴迪尔是个快乐的人；
    他的夹克是亮蓝色的，他的靴子是黄色的。”
    """
    tomBombadil = TomBombadilHouse("汤姆·邦巴迪尔的家", description, greeting)
    # 老林子
    description = """
    老林子是中洲为数不多的原始森林之一，在第二纪元之前覆盖了伊利雅德的大部分地区。
    众所周知，老林子因霍比屯居民对其边界的焚毁而变得不欢迎外界之人并经常捉弄游客。
    """
    oldForest = Space("老林子", description, constants.RegionType.ERIADOR,
                      battleProbability=constants.SpaceSpawnProb.oldForest,
                      battleBonusDifficulty=constants.SpaceBonusDiff.oldForest, uniquePlace=tomBombadil)

    # 风云丘陵 - 风云顶
    # 独特地点
    description = "这里曾经是一座伟大的瞭望塔，守护着整个地区。"
    greeting = "风云顶废墟在低声诉说着它昔日的辉煌。"
    weathertop = Weathertop("风云顶", description, greeting)
    # 风云丘陵
    description = """
    风云丘陵是人类对位于伊利雅德中部的一系列山脉的叫法，这里在古代是雅西顿和鲁道尔之间边界的一部分。
    风云顶，即阿蒙苏尔，位于该山脉的南端。
    """
    weatherHills = Space("风云丘陵", description, constants.RegionType.ERIADOR,
                         battleProbability=constants.SpaceSpawnProb.weatherHills,
                         battleBonusDifficulty=constants.SpaceBonusDiff.weatherHills, uniquePlace=weathertop)

    # 食人妖森林
    description = """
    食人妖森林是伊利雅德东部一座小山丘上的茂密森林，它坐落在苍泉河与响水河之间、幽谷以西数日路程处。
    这里是食人妖的出没地，山丘的高处有一个食人妖的洞穴，其中三只在孤山探险中拦住了比尔博和他的同伴。
    """
    trollshaws = Space("食人妖森林", description, constants.RegionType.ERIADOR,
                       battleProbability=constants.SpaceSpawnProb.trollshaws,
                       battleBonusDifficulty=constants.SpaceBonusDiff.trollshaws)

    # 迷雾山脉北部 - 幽谷
    # 旅店
    description = "在风景秀丽的迷雾山脉中度过轻松愉快的时光！"
    greeting = "欢迎来到迷雾山脉客栈！今晚让我们为您服务......"
    mistyInn = Inn("迷雾山脉客栈", description, greeting, 5)
    # 商店
    description = "新的精灵器具! 看起来像你最喜欢的精灵！"
    greeting = ("欢迎来到精灵商店！在这里，我们有最新的精灵小玩意。")
    elvenWares = Shop("精灵商店", description, greeting, constants.RegionType.RHOVANION, 5, 4)
    # 广场
    description = "仅限热点话题。"
    greeting = "我们一直在等侯着你的到来...."
    talk = {
        "埃尔隆德": "曾经破碎的剑……现在重铸了！",
        "莱戈拉斯": "你觉得我的头发怎么样？",
        "阿拉贡": "看看这些刀法！",
        "吉姆利": "我敢打赌我能比你吃更多的热狗。",
        "甘道夫": "阿雷哈贝卡玛哈拉....",
        "比尔博": "请照顾好我的东西......"
    }
    councilOfElrond = Square("埃尔隆德议会", description, greeting, talk, items.unique_items.councilOfElrondItems)
    # 城市
    description = """
    幽谷是半精灵埃尔隆德的领地。也是第三纪元精灵在中洲仅存的领地之一。
    幽谷也被称为"大海以东最后的家园"。维林诺是精灵次东边的家园，它位于中洲以西的大海上的阿门洲。
    """
    greeting = ("幽谷是一个让人眼花缭乱的地方，是真正的山中天堂。")
    rivendell = City("幽谷", description, greeting, [mistyInn, elvenWares, councilOfElrond])
    # 迷雾山脉北部
    description = """
    迷雾山脉是一座巨大的山脉，位于西部的伊利雅德和东部的安都因河之间。
    它从最北边的贡达巴德山到南边的美塞德拉斯，长达795英里（1280公里）。
    """
    mistyMountainsNorth = Space("迷雾山脉北部", description, constants.RegionType.ERIADOR,
                                battleProbability=constants.SpaceSpawnProb.mistyMountainsNorth,
                                battleBonusDifficulty=constants.SpaceBonusDiff.mistyMountainsNorth, city=rivendell)

    # 高隘口 - 半兽人镇
    # 独特地点
    description = """
    半兽人镇是迷雾山脉中部山腹内的一座半兽人据点，一个被称作半兽人王的巨型半兽人统治着此地。
    所谓半兽人镇，实际上是一系列错综复杂的洞窟和隧道系统，它们遍布于迷雾山脉的山腹之内，咕噜所待过的洞穴就位于其中深处。
    """
    greeting = "“是潜伏过去还是直接攻入？”"
    goblinTown = GoblinTown("半兽人镇", description, greeting)
    # 高隘口
    description = """
    高隘口是少数几处可供跨越迷雾山脉的隘口之一，位于幽谷以东。
    它的范围向西止于幽谷，从那里东大道向上蜿蜒入山，途中经过半兽人镇。

    ***通过半兽人镇可以向南进入黑森林***
    """
    highPass = Space("高隘口", description, constants.RegionType.HIGH_PASS,
                     battleProbability=constants.SpaceSpawnProb.highPass,
                     battleBonusDifficulty=constants.SpaceBonusDiff.highPass, uniquePlace=goblinTown)

    # 黑森林 - 精灵国王的宫殿
    # 旅店
    description = "住在树林里的体验!"
    greeting = "欢迎来到昆塔-穆特法克！"
    sihirliMutfak = Inn("昆塔-穆特法克", description, greeting, 5)
    # 商店
    description = "当地的精灵商店！"
    greeting = "提供各种各样的精灵小玩意！"
    elvenWares = Shop("精灵商店", description, greeting, constants.RegionType.RHOVANION, 7, 10)
    # 广场
    description = "“瑟兰杜伊的酒宴！”"
    greeting = "你到达时发现有一大群喝得醉醺醺的精灵。"
    talk = {
        "卡兰希尔": "嘎啦嘎……",
        "库茹芬": "别介意卡兰希尔，他的生活很艰难",
        "戴隆": "让我们为莱戈拉斯干杯！",
        "埃克塞理安": "嘎嘎嘎嘎……",
        "埃雅玟": "[无视你。]"
    }
    thePit = Square("坑洞", description, greeting, talk, items.unique_items.thePitItems)
    # 广场
    description = "瑟兰杜伊的金銮殿。"
    greeting = "“是什么让你觉得你属于这里？”"
    talk = {
        "瑟兰杜伊": "哼！我是统治黑森林王国的精灵王！",
        "安格罗德": "这里的人对你的打扮气得几乎咬牙切齿。",
        "阿瑞蒂尔": "哼！人类！",
        "阿尔巩": "哼！你不知道你身上的着装已经落伍了吗？",
        "贝烈格·库沙理安": "哼！你应该穿着的更体面一点！"
    }
    elvenkingsThrone = Square("精灵王的宝座", description, greeting, talk, items.unique_items.elvenkingsThroneItems)
    # 城市
    description = """
    精灵国王的宫殿坐落在距离黑森林东北部边缘仅有几英里之处，它事实上是一座巨大而复杂的洞穴。
    这座宫殿是精灵国王瑟兰杜伊的住所、宝库和地牢，是黑森林王国对抗外敌的堡垒，但王国的臣民主要并不定居于此，而是生活在森林的深处。
    """
    greeting = "你来到这里后发现一个可供穿行且热闹非凡的洞穴网络。"
    elvenkingsHalls = City("精灵国王的宫殿", description, greeting,
                           [sihirliMutfak, elvenWares, thePit, elvenkingsThrone])
    # 黑森林
    description = """
    黑森林在辛达语中被称为“大恐怖之林”，它是罗瓦尼安的一大片森林，其原名为大绿林；
    第三纪元末年，因为邪恶力量的入侵，大绿林才被人们称为黑森林。索隆战败后，这里又被重新命名为绿叶森林。
    """
    mirkwood = Space("黑森林", description, constants.RegionType.RHOVANION,
                     battleProbability=constants.SpaceSpawnProb.mirkwood,
                     battleBonusDifficulty=constants.SpaceBonusDiff.mirkwood, city=elvenkingsHalls)

    # 黑森林南部 - 多古尔都
    # 独特地点
    description = """
    多古尔都是黑森林西南部的一座建有要塞的山丘，其周围裹着一片黑冷杉森林，那里的树木互相倾轧争斗，树枝腐败枯萎。
    第三纪元中，多古尔都要塞一度是魔君索隆的藏身巢穴；索隆离开多古尔都之后，此地依然是他在北方最主要的据点之一，驻扎着戒灵和大量军队。
    """
    greeting = "当你接近多古尔都要塞时，你被一种压倒性的恐惧感所折服。"
    dolGuldur = DolGuldur("多古尔都", description, greeting)
    # 黑森林南部
    description = "在魔戒大战期间，黑森林南部被索隆的北方要塞多古尔都所占领。"
    southernMirkwood = Space("黑森林南部", description, constants.RegionType.RHOVANION,
                             battleProbability=constants.SpaceSpawnProb.southernMirkwood,
                             battleBonusDifficulty=constants.SpaceBonusDiff.southernMirkwood, uniquePlace=dolGuldur)

    # 古冢岗-布理 - 布理
    # 旅店
    description = "一家安静的旅店，隐藏在布理的郊区。"
    greeting = "“你们好，我是旅馆老板琳达。”"
    lindasInn = Inn("琳达的旅店", description, greeting, 5)
    # 商店
    description = "来这挑选你杀戮奥克的装备吧！"
    greeting = "嗨，我是汉克！！！杀死奥克！！！！"
    hanksBattleGear = Shop("汉克的战斗装备", description, greeting, constants.RegionType.ERIADOR, 8, 2)
    # 广场
    description = "一座以争吵闻名的嘈杂的大型客栈。"
    greeting = "迎接你的是一片寂静。两个人短暂地盯着你看，然后转身继续喝酒。"
    talk = {
        "比尔·蕨尼": "我听说这一带有黑骑手出没。",
        "哈里·金银花": "整个小镇上的人都被黑骑手吓坏了....",
        "亨利·蓟羊毛": "阴影已经降临在这些地方......",
        "杜多·巴金斯": "我在这儿做什么？",
        "埃丝特拉·白兰地鹿": "是时候回家了，我想...."
    }
    prancingPony = Square("跃马客栈", description, greeting, talk, items.unique_items.prancingPonyItems)
    # 城市
    description = """
    布理位于夏尔以东、佛诺斯特·埃莱因以南。它在第三纪元早期属于卡多蓝王国。然而，
    尽管卡多蓝亲王声称拥有它，但布理在没有任何中央权威或政府的情况下持续繁荣发展了许多世纪。 
    """
    greeting = "“戒灵一直在夜间造访这附近！”"
    bree = City("布理", description, greeting, [lindasInn, hanksBattleGear, prancingPony])
    # 古冢岗-布理
    description = """
    古冢岗是坐落于夏尔东部的连绵矮山丘，在老林子的北部，布理村庄的西南部。
    山脉中的许多丘陵巨石遍布，坟冢到处可见，这也是其名由来。
    """
    barrowDowns = Space("古冢岗-布理", description, constants.RegionType.BARROW_DOWNS,
                        battleProbability=constants.SpaceSpawnProb.barrowDowns,
                        battleBonusDifficulty=constants.SpaceBonusDiff.barrowDowns, city=bree)

    # 布茹伊能河
    description = """
    布茹伊能河，又名响水河，是东伊利雅德的一条河流。
    它发源于迷雾山脉西麓，最终汇入米斯艾塞尔河，其南翼流经埃尔隆德建立的避难所幽谷。
    """
    bruinen = Space("布茹伊能河", description, constants.RegionType.ERIADOR,
                    battleProbability=constants.SpaceSpawnProb.bruinen,
                    battleBonusDifficulty=constants.SpaceBonusDiff.bruinen)

    # 米斯艾塞尔河 - 沙巴德
    # 独特地点
    description = "沙巴德曾经是格瓦斯罗河上的一座要塞城镇，现在已成为废墟。"
    greeting = "当你进入曾经伟大的沙巴德的废墟时，一股阴森的雾气迎面而来...."
    tharbad = Tharbad("沙巴德", description, greeting)
    # 米斯艾塞尔河
    description = """
    米斯艾塞尔河，又名苍泉河，是伊利雅德东部的一条河流。
    它发源于迷雾山脉北部群山的西麓，距离幽谷以北大约一百英里。
    """
    mitheithel = Space("米斯艾塞尔河", description, constants.RegionType.ERIADOR,
                       battleProbability=constants.SpaceSpawnProb.mitheithel,
                       battleBonusDifficulty=constants.SpaceBonusDiff.mitheithel, uniquePlace=tharbad)

    # 天鹅泽 - 欧斯特-因-埃第尔
    # 独特地点
    description = """
    这里曾经是一座埃瑞吉安的精灵工匠之城，现在已被索隆摧毁。
    十九枚力量之戒都是在这里由凯勒布林博等精灵工匠铸造的。
    """
    greeting = """你会看到一个奇怪的景象：曾经的伟大城市欧斯特-因-埃第尔现在成了一个古老的废墟。奇怪的符号遍布在这片土地上。"""
    ostInEdhil = OstInEdhil("欧斯特-因-埃第尔", description, greeting)
    # 天鹅泽
    description = """
    天鹅泽，又称“宁-因-艾尔芙”，是位于伊利雅德东部、格蓝都因河与苍泉河汇流处的沼泽。
    两条河流的交汇处形成了内陆三角洲，这里溪流诸多，水陆分界也不甚明确。
    """
    swanfleet = Space("天鹅泽", description, constants.RegionType.ERIADOR,
                      battleProbability=constants.SpaceSpawnProb.swanfleet,
                      battleBonusDifficulty=constants.SpaceBonusDiff.swanfleet, uniquePlace=ostInEdhil)

    # 黑蛮地
    description = """
    黑蛮地是一片山麓丘陵地区，面向迷雾山脉南部的西侧山坡。因其远离阿尔诺与刚铎的人口中心，居民多是被称为黑蛮地人的人类，一度也有流浪至此的矮人与霍比特人。
    黑蛮地源于洛汗语，意为“山丘地域”，由第三纪元搬至卡伦纳松的洛希尔人所起，是片美丽丰饶的地区，一些未成组织的牧人与山间居民零星居住在黑蛮地南部，北部则无人居住。
    """
    dunland = Space("黑蛮地", description, constants.RegionType.ENEDWAITH,
                    battleProbability=constants.SpaceSpawnProb.dunland,
                    battleBonusDifficulty=constants.SpaceBonusDiff.dunland)

    # 迷雾山脉南部 - 墨瑞亚
    # 独特地点
    description = """
    墨瑞亚曾是中洲大地上最强大且最为著名的矮人王国。在那里矮人繁荣发展，建造了有史以来最伟大的一座城市。
    它是坐落于迷雾山脉中南部的一个巨大的地下建筑群，横贯山脉的东西两侧，是穿越迷雾山脉的重要通道之一。
    """
    greeting = "当你进入墨瑞亚矿坑时，阴森恐怖的寂静迎面而来。"
    moria = Moria("墨瑞亚", description, greeting)
    # 迷雾山脉南部
    description = """
    迷雾山脉是中洲最大的山脉，由北向南绵延800公里，位于伊利雅德和安都因河之间，将伊利雅德与罗马尼安分隔开。
    墨瑞亚群山指迷雾山脉的三座连峰凯勒布迪尔、卡拉兹拉斯和法努伊索尔，矮人城邦墨瑞亚就挖凿在三座大山的底部。

    ***要向东进入罗瑞恩则必须通过墨瑞亚***
    """
    mistyMountainsSouth = Space("迷雾山脉南部", description, constants.RegionType.MORIA,
                                battleProbability=constants.SpaceSpawnProb.mistyMountainsSouth,
                                battleBonusDifficulty=constants.SpaceBonusDiff.mistyMountainsSouth, uniquePlace=moria)

    # 罗瑞恩 - 卡拉斯加拉松
    # 旅店
    description = "坐落在安都因河和凯勒布兰特河之间。"
    greeting = "精灵水域是一家真正美丽的旅馆，沐浴在薄雾之中。"
    elvenWaters = Inn("精灵水域旅馆", description, greeting, 5)
    # 商店
    description = "精灵商店！很多很棒的精灵装备！"
    greeting = "欢迎来到精灵商店！我们有很多稀有的收藏品！"
    elvenWares = Shop("精灵商店", description, greeting, constants.RegionType.RHOVANION, 8, 9)
    # 广场
    description = "为了预言以及简单的老式虚荣心。"
    greeting = "一个道亮丽的风景线：加拉德瑞尔本人！"
    talk = {
        "加拉德瑞尔": "看看这水镜吧！它能展示过去、现在以及可能的未来。"
    }
    galadrielsMirror = Square("加拉德瑞尔之镜", description, greeting, talk, items.unique_items.galadrielsMirrorItems)
    # 城市
    description = """
    卡拉斯加拉松是洛丝罗瑞恩的都城，这块宽阔草地的南部有一棵无与伦比的巨大瑁珑树，树下设有可供攀爬的白色梯子。攀爬虽然辛苦，但大树的枝干上建有高高低低许多平台，可以随时休息。
    在瑁珑接近树顶的极高处，有一座椭圆形殿堂绕树而造，这就是罗瑞恩领主凯勒博恩和领主夫人加拉德瑞尔的宫殿，两人的宝座在其中并排摆放，不分位次。
    """
    greeting = "欢迎来到卡拉斯加拉松！凯勒博恩和加拉德瑞尔住在这里。"
    carasGaladhon = City("卡拉斯加拉松", description, greeting, [elvenWaters, elvenWares, galadrielsMirror])
    # 罗瑞恩
    description = """
    洛丝罗瑞恩是位于迷雾山脉东面的西尔凡王国，简称罗瑞恩。
    在第三纪元，它被认为是中洲最美丽也最富于精灵特色的地方。
    在大海以东，洛丝罗瑞恩是瑁珑的唯一生长地点，只有夏尔的那棵例外。

    ***要向西进入迷雾山脉南部则必须通过墨瑞亚***
    """
    lorien = Space("罗瑞恩", description, constants.RegionType.RHOVANION,
                   battleProbability=constants.SpaceSpawnProb.lorien,
                   battleBonusDifficulty=constants.SpaceBonusDiff.lorien, city=carasGaladhon)

    # 范贡森林 - 秘林谷
    # 独特地点
    description = "此处是恩特们举行会议的地点"
    greeting = "“欢迎来到恩特大会！不必那么着急。”"
    derningle = Derningle("秘林谷", description, greeting)
    # 范贡森林
    description = """
    范贡森林是一片深邃而黑暗的林地，位于迷雾山脉南部的下方，该山脉的东侧。
    在洛汗，这片森林借用了老恩特范贡的名字，被洛汗人民称为“恩特森林”。
    """
    fangorn = Space("范贡森林", description, constants.RegionType.ROHAN,
                    battleProbability=constants.SpaceSpawnProb.fangorn,
                    battleBonusDifficulty=constants.SpaceBonusDiff.fangorn, uniquePlace=derningle)

    # 北高原
    description = """
    北高原是洛汗的最北部，也是人口最少的地区，位于范贡森林和安都因河之间，军事划分上属于东马克。
    此地适宜放牧，多风，但十分荒凉，很少有人居住。近年来，由于奥克的频繁出没，这里已经不再安全。
    """
    theWold = Space("北高原", description, constants.RegionType.MORDOR,
                    battleProbability=constants.SpaceSpawnProb.theWold,
                    battleBonusDifficulty=constants.SpaceBonusDiff.theWold)

    # 凯勒布兰特原野
    description = """
    凯勒布兰特原野是凯勒布兰特河与利姆清河之间的大片土地，位于洛丝罗瑞恩的东南部。
    第三纪元2510年，洛汗人奋起援助刚铎的凯勒布兰特原野之战在这里发生。
    """
    fieldOfCelebrant = Space("凯勒布兰特原野", description, constants.RegionType.MORDOR,
                             battleProbability=constants.SpaceSpawnProb.fieldOfCelebrant,
                             battleBonusDifficulty=constants.SpaceBonusDiff.fieldOfCelebrant)

    # 卡伦纳松 - 艾森加德
    # 独特地点
    description = """
    艾森加德是一个坐落于迷雾山脉最南端山谷中的伟大要塞，靠近洛汗豁口；岩石环场的中央矗立着欧尔桑克石塔。
    """
    greetings = "当你接近艾森加德时，焦黑的天空在迎接你。"
    isenguard = Isenguard("艾森加德", description, greetings)
    # 卡伦纳松
    description = """
    卡伦纳松，意为“绿色行省”，位于迷雾山脉以东、白色山脉以北，是安都因河与艾森河之间的一片人烟稀少的广阔草原。

    ***通过艾森加德可以向南进入西伏尔德***
    """
    calenardhon = Space("卡伦纳松", description, constants.RegionType.ENEDWAITH,
                        battleProbability=constants.SpaceSpawnProb.calenardhon,
                        battleBonusDifficulty=constants.SpaceBonusDiff.calenardhon, uniquePlace=isenguard)

    # 西伏尔德 - 海尔姆深谷
    # 旅店
    description = "人们来这里醒酒。"
    greeting = "没有人来迎接你。"
    sobrietyRoom = Inn("醒酒房", description, greeting, 0)
    # 商店
    description = "这里实际被称为酒铺"
    greeting = "我们有太阳底下所有的毒药...."
    theArmory = Shop("军械库", description, greeting, constants.RegionType.ROHAN, 8, 6)
    # 广场
    description = "这有大量喝醉的人。"
    greeting = "每个人都醉倒了。"
    talk = {
        "埃肯布兰德": "呜呜呜……",
        "老甘姆林": "呸呸呸呸呸……"
    }
    helmsDeepCommons = Square("海尔姆深谷广场", description, greeting, talk, items.unique_items.helmsDeepCommonsItems)
    # 城市
    description = """
    海尔姆深谷是白色山脉以北，西伏尔德南部的一个峡谷地区，就在三峰山的底下，谷口地带左右是白色山脉的悬崖峭壁，而面前是深谷宽谷的广阔平地，深谷的背后是晶辉洞。
    晶辉洞和深谷的存在使得此地成为了一个理想的防守处。山谷外围被海尔姆护墙与墙下的沟壑保护着，在高墙后面的是伟大的堡垒号角堡，有一条长长的斜坡从海尔姆护墙之后伸到号角堡的大门。
    """
    greeting = "“欢迎来到海尔姆深谷！哇哦！！！派对！”"
    helmsDeep = City("海尔姆深谷", description, greeting, [sobrietyRoom, theArmory, helmsDeepCommons])
    # 西伏尔德
    description = """
    西伏尔德位于洛汗的西部，指的是从洛汗隘口到埃多拉斯和白色山脉脚下的广阔土地，属于西马克。
    西伏尔德的主要堡垒是海尔姆深谷处的号角堡，它的西部边界是洛汗隘口，也被认为是艾森河。
    """
    westfold = Space("西伏尔德", description, constants.RegionType.ROHAN,
                     battleProbability=constants.SpaceSpawnProb.westfold,
                     battleBonusDifficulty=constants.SpaceBonusDiff.westfold, city=helmsDeep)

    # 西埃姆内特
    description = """
    西埃姆内特是位于恩特河以西的大片洛汗草原的名称，其向东延伸至艾森河，北面则与范贡森林接壤。
    """
    westemnet = Space("西埃姆内特", description, constants.RegionType.ROHAN,
                      battleProbability=constants.SpaceSpawnProb.westemnet,
                      battleBonusDifficulty=constants.SpaceBonusDiff.westemnet)

    # 东埃姆内特
    description = """
    东埃姆奈特是洛汗最东边的广袤土地，从恩特河以东一直延申至安都因河。
    东埃姆奈特上只有些许固定居所，但是不少洛希尔人游牧民在这片土地上放牧。
    """
    eastemnet = Space("东埃姆内特", description, constants.RegionType.ROHAN,
                      battleProbability=constants.SpaceSpawnProb.eastemnet,
                      battleBonusDifficulty=constants.SpaceBonusDiff.eastemnet)

    # 埃敏穆伊
    description = """
    埃敏穆伊是褐地以南、湿平野以北的一片崎岖的丘陵地带，安都因大河穿过其间深切的河谷，注入山区南端的能希斯艾尔湖。
    """
    emynMuil = Space("埃敏穆伊", description, constants.RegionType.MORDOR,
                     battleProbability=constants.SpaceSpawnProb.emynMuil,
                     battleBonusDifficulty=constants.SpaceBonusDiff.emynMuil)

    # 东伏尔德 - 埃多拉斯
    # 旅店
    description = "一家古色古香的客栈坐落在一片开阔的平原上。"
    greeting = "“旅行者！我们很高兴你能在这里过夜。”"
    sunsetVillage = Inn("草原风光", description, greeting, 5)
    # 商店
    description = "手工艺品和各种收藏品。"
    greeting = "我们这里有可以追溯到T.A.1497的物品！"
    twiceRemembered = Shop("双倍铭记", description, greeting, constants.RegionType.ROHAN, 10, 8)
    # 广场
    description = "一个乡村广场，里面大多是老年人。"
    greeting = "“我们热爱我们的土地。”"
    talk = {
        "海尔姆游击手": "我祝你在旅途中一切顺利。",
        "布里塔": "我有好几个像你这么大的女儿。",
        "“钢泽”墨玟": "如果你有时间，我很愿意教你锻造。",
        "弗雷亚拉夫": "这里大多是老年人，我的孩子们都去城里工作了。"
    }
    edorasCommons = Square("埃多拉斯广场", description, greeting, talk, items.unique_items.edorasCommonsItems)
    # 城市
    description = """
    埃多拉斯是洛汗王国的都城，它是洛汗初代国王年少的埃奥尔之子布雷戈建造的，他首先修筑了金殿美杜塞尔德，然后迁都于此地。
    """
    greeting = "“欢迎来到埃多拉斯！”"
    edoras = City("埃多拉斯", description, greeting, [sunsetVillage, twiceRemembered, edorasCommons])
    # 东伏尔德 - 奥德堡
    # 旅店
    description = "旅店老板是一个叫塞思的人。"
    greeting = "“我们很高兴你能在这里过夜。”"
    sethsHostel = Inn("塞思的旅馆", description, greeting, 5)
    # 商店
    description = "不要走！除了饼干之外还有其他东西。"
    greeting = "“你想来点饼干尝尝吗？”"
    milesCookieFactory = Shop("迈尔斯的饼干工坊", description, greeting, constants.RegionType.ROHAN, 10, 12)
    # 广场
    description = "这里有许多有意思的讨论。"
    greeting = "“我想知道这是怎么一回事......？”"
    talk = {
        "德米特里": "淡定。",
        "吉姆": "让我们把这一问题解决了吧！",
        "克里斯": "我来自中国。"
    }
    auburnSquare = Square("奥德堡广场", description, greeting, talk, items.unique_items.auburnSquareCommons)
    # 城市
    description = """
    奥德堡是洛汗历史最悠久的城镇之一，其建立于“年少的”埃奥尔统治时期。
    当埃多拉斯的金殿尚未落成时，奥德堡是洛汗国王的居所、洛汗的首都。
    """
    greeting = "“欢迎来到奥德堡！”"
    aldburg = City("奥德堡", description, greeting, [sethsHostel, milesCookieFactory, auburnSquare])
    # 东伏尔德
    description = """
    东伏尔德是洛汗东部的一个地区，其北临恩特河，南至白色山脉，东西边界分别为梅尔林溪和雪河。西大道横贯东伏尔德地区。
    """
    eastfold = Space("东伏尔德", description, constants.RegionType.ROHAN,
                     battleProbability=constants.SpaceSpawnProb.eastfold,
                     battleBonusDifficulty=constants.SpaceBonusDiff.eastfold, city=[edoras, aldburg])

    # 宁达尔夫
    description = """
    宁达尔夫又称湿平野，是埃敏穆伊丘陵南麓、安都因河东岸的一片广阔淤塞的沼泽。水流在沼地里曲曲绕绕，分支众多。
    它的水源主要来自两处：从埃敏穆伊丘陵流泄而下的、安都因河的涝洛斯大瀑布，和先从西面汇入安都因河、然后经由诸多河口注入沼泽的恩特河。
    """
    nindalf = Space("宁达尔夫", description, constants.RegionType.MORDOR,
                    battleProbability=constants.SpaceSpawnProb.nindalf,
                    battleBonusDifficulty=constants.SpaceBonusDiff.nindalf)

    # 死亡沼泽 - 魔栏农
    # 独特地点
    description = """
    魔栏农也叫黑门、魔多之门，是由索隆运用至尊戒的力量于第二纪元在魔多建造的巨门。
    其矗立在鬼影隘口，是一堵带有三个拱门的巨墙，四周有上百坑洞，面前是一片荒地和两座被恶臭的水潭和泥泽围绕的碎石荒山。
    魔栏农两侧的山脉上各有一座古时人们建造的高塔，如今是黑门的守卫塔尖牙之塔，日夜有奥克在其中守卫。
    """
    greetings = "“一个人不可能这么简单地走进魔多。”"
    blackGate = BlackGate("魔栏农", description, greetings)
    # 死亡沼泽
    description = """
    死亡沼泽是达戈拉德平原西北方、埃敏穆伊丘陵东南方的一片广阔沼泽。它是无数水塘、软泥潭和水道纵横交错形成的大网。
    
    ***通过魔栏农可以向东进入乌顿***
    """
    deadMarshes = Space("死亡沼泽", description, constants.RegionType.MORDOR,
                        battleProbability=constants.SpaceSpawnProb.deadMarshes,
                        battleBonusDifficulty=constants.SpaceBonusDiff.deadMarshes, uniquePlace=blackGate)

    # 乌顿山谷 - 艾森毛兹
    # 独特地点
    description = """
    艾森毛兹是魔多西北的一处峡谷，由埃斐尔度阿斯与埃瑞德砾苏伊的山脉交汇形成，沟通北部的乌顿山谷与南方的戈埚洛斯平原。它在辛达语中被称为“铁山口”。
    作为卫戍魔多北方的重要通道，艾森毛兹戒备森严，两侧的山坡上修筑了大量要塞和塔楼。在山口处修建了一堵土墙并挖了一条壕沟，其上只有一座桥将两端相连。
    """
    greetings = "“一个人不可能这么简单地走进魔多的腹地。”"
    isenmouthe = Isenmouthe("艾森毛兹", description, greetings)
    # 乌顿山谷
    description = """
    乌顿是魔多西北部的一处山谷，由埃斐尔度阿斯与埃瑞德砾苏伊的山脉环抱而成，是魔多的重要入口，山谷中有大批邪恶生物打通了无数地道。
    乌顿山谷的西北方有“黑门”魔栏农扼守，而南方则是“铁山口”艾森毛兹。杜尔桑堡垒位于埃斐尔度阿斯北坡，俯瞰着乌顿山谷。
    
    ***通过艾森毛兹可以向南进入戈埚洛斯平原***
    """
    udun = Space("乌顿", description, constants.RegionType.MORDOR, battleProbability=constants.SpaceSpawnProb.udun,
                 battleBonusDifficulty=constants.SpaceBonusDiff.udun, uniquePlace=isenmouthe)

    # 凯尔安德洛斯
    description = """
    凯尔安德洛斯是一个辛达语名称，意为“长沫之船”。是米那斯提力斯城以北的安都因河河段中的一座岛屿，岛上建有刚铎王国的防御工事。
    凯尔安德洛斯的东面是黑暗魔君的巢穴魔多，西面是刚铎首都米那斯提力斯城的所在地阿诺瑞恩，它是少数能够允许一支大军渡过安都因河天险的渡口之一。
    """
    cairAndros = Space("凯尔安德洛斯", description, constants.RegionType.GONDOR,
                       battleProbability=constants.SpaceSpawnProb.cairAndros,
                       battleBonusDifficulty=constants.SpaceBonusDiff.cairAndros)

    # 欧洛都因（末日山）
    description = """
    末日山是一座位于魔多境内的火山，又名“烈火之山”。其独自屹立在戈埚洛斯平原上，高约4500英尺，底部宽约3000英尺，通过索隆之路与邪黑塔相连。
    在辛达语中，其名为欧洛都因或阿蒙阿马斯，在它的火山锥内，是通向末日裂罅的“烈火诸室”萨马斯瑙尔，至尊戒便是在此铸造而成，这里也是唯一可以摧毁至尊戒的地方。
    """
    orodruin = Space("欧洛都因", description, constants.RegionType.MORDOR,
                     battleProbability=constants.SpaceSpawnProb.orodruin,
                     battleBonusDifficulty=constants.SpaceBonusDiff.orodruin)

    # 阿诺瑞恩 - 米那斯提力斯
    # 旅店
    description = "刚铎全境最优秀的医护人员工作的地方。"
    greeting = "“欢迎来到诊疗院。我能为你做什么？”"
    housesOfHealing = Inn("诊疗院", description, greeting, 5)
    # 商店
    description = "精锐的军械库，供最优秀的刚铎军队使用。"
    greeting = "欢迎来到国王铁匠铺！我们这的装备都闪耀着传奇功勋......"
    smithyOfKings = Shop("国王铁匠铺", description, greeting, constants.RegionType.GONDOR, 14, 14)
    # 广场
    description = "这里是米那斯提力斯城的广场。"
    greeting = "当你进入白城广场时，紧张的气氛迎面而来。"
    talk = {
        "卡尔马奇尔": "你想买点水果吗？",
        "卡斯塔米尔": "每个人都在害怕....",
        "奇尔扬迪尔": "边陲地区的奥克袭击正在不断增长......",
        "罗门达奇尔": "我想知道我们能为抵挡魔多做些什么......",
        "纳马奇尔": "我想知道国王是否会归来。",
        "塔隆多": "我希望洛汗会带来援助....",
        "阿塔那塔": "有消息说魔多正准备发动进攻...."
    }
    marketSquare = Square("白城广场", description, greeting, talk, items.unique_items.marketSquareItems)
    # 广场
    description = "刚铎皇室所在地。"
    greeting = "德内梭尔想要见你...."
    talk = {
        "德内梭尔": "给你，都给你！来，波洛米尔，堆起木柴。我们的时代结束了....",
        "法拉米尔": "应该被夺回最近被索隆窃取的土地....",
        "波洛米尔": "那戒指...尽管我知道这不可能，但我还是请求你把它给我！",
        "伊姆拉希尔": "索隆计划不久后进军....",
        "王城禁卫军": "这里有一份可以帮助你战斗的礼物！"
    }
    towerOfEcthelion = Square("埃克塞理安之塔", description, greeting, talk, items.unique_items.towerOfEchelionItems)
    # 城市
    description = """
    米那斯提力斯是刚铎的一座城市，原名为米那斯阿诺尔，于第二纪元3320年由忠贞派努曼诺尔人所建。
    它自第三纪元1640年起便是南方王国的首都，为诸王与宰相的居所。整座城市由白色的石块砌成，因此又常被称作“白城”。
    """
    greeting = "“欢迎来到刚铎最后的据点——米那斯提力斯。”"
    minasTirith = City("米那斯提力斯", description, greeting,
                       [housesOfHealing, marketSquare, towerOfEcthelion, smithyOfKings])
    # 阿诺瑞恩
    description = """
    阿诺瑞恩是刚铎王国位于白色山脉以北、卡伦纳松以南的一块封地。刚铎的首都米那斯提力斯城就坐落在阿诺瑞恩的东南角。
    阿诺瑞恩是刚铎王国最北方的封邑之一，自从刚铎放弃卡伦纳松之后，它就成为了王国仅有的一块完全位于白色山脉以北的领地。
    """
    anorien = Space("阿诺瑞恩", description, constants.RegionType.GONDOR,
                    battleProbability=constants.SpaceSpawnProb.anorien,
                    battleBonusDifficulty=constants.SpaceBonusDiff.anorien, city=minasTirith)

    # 安都因河 - 阿刚那斯
    # 独特地点
    description = """
    阿刚那斯又名“王者双柱”、“双王之门”、“刚铎之门”，是刚铎北方边界的地标。
    它是能希斯艾尔湖北端分列安都因河两岸的两座巨大的人像——伊熙尔杜与阿纳瑞安。
    """
    greeting = "“欢迎来到阿刚那斯！请呆在指定的区域内，并听从你的向导。”"
    argonath = Argonath("阿刚那斯", description, greeting)
    # 安都因河 - 欧斯吉利亚斯
    # 旅店
    description = "在战斗中休息的地方。"
    greeting = "“你的小床在左上角。”"
    soldierBarracks = Inn("兵营", description, greeting, 5)
    # 商店
    description = "存量正在迅速耗尽。"
    greeting = "你想要什么？我们这什么都缺...."
    osgiliathArmory = Shop("欧斯吉利亚斯军械库", description, greeting, constants.RegionType.GONDOR, 4, 12)
    # 广场
    description = "曾经是刚铎首都的辉煌广场。"
    greeting = "你发现广场已成废墟，空无一人。"
    talk = {}
    osgiliathCommons = Square("欧斯吉利亚斯广场", description, greeting, talk)
    # 城市
    description = """
    欧斯吉利亚斯是刚铎旧时的都城。它横跨安都因河，坐落于西南的米那斯阿诺尔与东北的米那斯伊希尔之间。
    然而欧斯吉利亚斯城于第三纪元1437年被劫掠又烧毁，自那之后便开始衰败。但它仍具有重要的战略意义！
    """
    greeting = "“保持警惕。我们正不断遭受攻击。”"
    osgiliath = City("欧斯吉利亚斯", description, greeting, [soldierBarracks, osgiliathArmory, osgiliathCommons])
    # 安都因河
    description = """
    安都因河是中洲迷雾山脉以东的大河，第三纪元中洲最长的河流，也是中洲大陆东西疆域的界河。
    安都因河发源于灰色山脉和迷雾山脉，流入埃希尔安都因，汇入贝烈盖尔，自北向南穿过广阔的土地，也因此获得各地居民对它的许多称呼。
    洛汗人的祖先称它为长川，幽谷和夏尔的西部语中称其为荒地大河，在刚铎安都因河就被称为大河。这些名字都与安都因河极长的河流长度有关。
    """
    anduin = Space("安都因河", description, constants.RegionType.GONDOR,
                   battleProbability=constants.SpaceSpawnProb.anduin,
                   battleBonusDifficulty=constants.SpaceBonusDiff.anduin, city=osgiliath, uniquePlace=argonath)

    # 埃斐尔度阿斯 - 米那斯魔古尔
    # 独特地点
    description = """
    米那斯魔古尔原名米那斯伊希尔，位于魔古尔山谷，曾经是米那斯提力斯的姐妹城市，但第三纪元被索隆的势力攻占，成为戒灵的要塞。
    米那斯魔古尔正门前的魔古尔路起自欧斯吉利亚斯，经过伊希利恩至魔古尔山谷，跨过阴影山脉进入魔多，将米那斯魔古尔和索隆的王国连接起来。
    """
    greeting = "“一个人不可能这么简单地走进魔多。”"
    minasMorgul = MinasMorgul("米那斯魔古尔", description, greeting)
    # 埃斐尔度阿斯
    description = """
    埃斐尔度阿斯亦称“阴影山脉”，是环抱魔多西南边境的山脉。翻越埃斐尔度阿斯进入魔多的通路有两条：
    其一为米那斯魔古尔要塞镇守的伊姆拉德魔古尔，另一处则是更为危险的“蜘蛛隘口”奇立斯乌苟。
    
    ***通过米那斯魔古尔可以向东进入戈埚洛斯平原***
    """
    ephelDuath = Space("埃斐尔度阿斯", description, constants.RegionType.MORDOR,
                       battleProbability=constants.SpaceSpawnProb.ephelDuath,
                       battleBonusDifficulty=constants.SpaceBonusDiff.ephelDuath, uniquePlace=minasMorgul)

    # 奇立斯乌苟 - 奇立斯乌苟之塔
    # 独特地点
    description = """
    奇立斯乌苟之塔是奇立斯乌苟隘口中的一道防御工事，矗立在魔多西侧边界之上。
    要想到达这里，必须先穿过尸罗的巢穴，那里错综复杂且黑暗至极而且臭气熏天。
    """
    greeting = "“愿你在黑暗之中有一盏明灯。”"
    towerOfCirithUngol = TowerOfCirithUngol("奇立斯乌苟之塔", description, greeting)
    # 奇立斯乌苟
    description = """
    奇立斯乌苟古称奇立斯度阿斯，是穿越埃斐尔度阿斯的隘口，这里是能从西方秘密进入魔多的唯一通路。
    奇立斯乌苟被奇立斯乌苟之塔把守着，该塔由刚铎人于最后联盟之战后建造，本是用来监视魔多，盯防索隆。
    但随后刚铎衰落，索隆东山再起，该塔便被其爪牙占据，成了米那斯魔古尔的前哨。
    
    ***要向东进入戈埚洛斯平原则必须通过奇立斯乌苟之塔（但之后无法返回）***
    """
    cirithUngol = Space("奇立斯乌苟", description, constants.RegionType.MORDOR,
                        battleProbability=constants.SpaceSpawnProb.cirithUngol,
                        battleBonusDifficulty=constants.SpaceBonusDiff.cirithUngol, uniquePlace=towerOfCirithUngol)

    # 戈埚洛斯平原 - 巴拉督尔
    # 独特地点
    description = """
    巴拉督尔是索隆在魔多的要塞，位于魔多北部边界灰烬山脉的长山坡尽头。从塔上可以俯瞰戈埚洛斯平原。从巴拉督尔到西北面的黑门有一条100哩长的路。
    巴拉督尔是一座高耸的大型堡垒，由铁和极其坚硬的石头搭建，大门则是由精钢铸成。索隆用阴影遮盖了这座漆黑的塔楼，并用大量的围墙，战斗器械和小塔楼将巴拉督尔搭建得非常高大。
    塔楼的最顶端是一尊铁王冠，那里面的窗口中是索隆凝视中洲的巨眼。黑塔楼里有巨大的庭院、地牢和没有窗洞的监狱，而这之下是深深的矿坑。
    """
    greeting = """
    乌云翻滚，云中有高耸如山的塔楼和城垛，坐落在压住无数坑洞的强大山基之上；
    巨大的庭院和地牢，没有窗洞的监狱如悬崖峭壁般耸立，牢不可破的钢门森然大张；
    耸立的黑塔楼，比它所投下的巨大阴影更黑更暗，巴拉督尔塔顶的残酷尖峰和铁王冠......
    """
    baradDur = BaradDur("巴拉督尔", description, greeting)
    # 戈埚洛斯平原
    description = """
    戈埚洛斯平原是魔多西北部的一片巨大荒漠。平原上布满了矿井和熔炉，用于锻造魔多军队的武器和盔甲，而周围则近乎四面环山，实乃要地之中的要地。
    它的北面和西面分别是埃瑞德砾苏伊山脉和埃斐尔度阿斯山脉，这两座峻岭又各自延伸出一道支脉，围住了平原的东面和南面，只留有一个开往努尔恩地区的裂口。
    """
    plateauOfGorgoth = Space("戈埚洛斯平原", description, constants.RegionType.MORDOR,
                             battleProbability=constants.SpaceSpawnProb.plateauOfGorgoth,
                             battleBonusDifficulty=constants.SpaceBonusDiff.plateauOfGorgoth, uniquePlace=baradDur)

    # 莱本宁 - 佩拉基尔
    # 旅店
    description = "刚铎沿海地区最好的海景度假胜地！"
    greeting = "“嘿哥们儿！欢迎来到阳光之家！”"
    sunnysideInn = Inn("阳光之家", description, greeting, 5)
    # 商店
    description = "海滩配件和用具。"
    greeting = "“嘿，怎么了，兄弟？”"
    palmTreeHut = Shop("棕榈之家", description, greeting, constants.RegionType.GONDOR, 6, 14)
    # 广场
    description = "三级浪！"
    greeting = "“兄弟，你看到那些海浪了吗？”"
    talk = {
        "刚铎人一": "兄弟，我们去海滩吧！",
        "刚铎人二": "兄弟！让我们冷静一会儿......",
        "刚铎人三": "兄弟！我听说今天晚些时候会有一个聚会。",
        "刚铎女人一": "不好意思，我有男朋友了....",
        "刚铎女人二": "嘿！待会你想做些什么？"
    }
    beach = Square("佩拉基尔海滩", description, greeting, talk, items.unique_items.beachItems)
    # 城市
    description = """
    佩拉基尔是位于安都因河口三角洲上游的一座城市，它是刚铎王国最古老和最重要的港口之一。
    佩拉基尔港始建于第二纪元2350年，它是忠贞派的努门诺尔人在中洲建立的最主要的海港之一。
    """
    greeting = "在刚铎港口城市佩拉基尔享受轻松的假期吧。"
    pelargir = City("佩拉基尔", description, greeting, [sunnysideInn, palmTreeHut, beach])
    # 莱本宁
    description = """
    莱本宁是刚铎王国的南方封地之一，它位于白色山脉以南，夹在吉尔莱恩河与安都因河之间。
    它的别名是五河之地，因为埃茹伊河、西瑞斯河、色尔尼河、吉尔莱恩河与凯洛斯河均流经该封邑境内。
    """
    lossamarch = Space("莱本宁", description, constants.RegionType.GONDOR,
                       battleProbability=constants.SpaceSpawnProb.lossamarch,
                       battleBonusDifficulty=constants.SpaceBonusDiff.lossamarch, city=pelargir)

    # 伊希利恩
    description = """
    伊希利恩意为月亮之地，是刚铎王国历史最为悠久、地位最为重要的封邑之一。
    它西临安都因大河，东面埃斐尔度阿斯山脉，北至死亡沼泽，南达波罗斯河，土地面积较大，地形整体十分狭长。
    """
    ithilien = Space("伊希利恩", description, constants.RegionType.GONDOR,
                     battleProbability=constants.SpaceSpawnProb.ithilien,
                     battleBonusDifficulty=constants.SpaceBonusDiff.ithilien)

    # 连接东西走向的所有地区
    shire.createExit("east", oldForest, outgoingOnly=False)
    weatherHills.createExit("east", trollshaws, outgoingOnly=False)
    trollshaws.createExit("east", mistyMountainsNorth, outgoingOnly=False)
    mistyMountainsNorth.createExit("east", highPass, outgoingOnly=False)
    barrowDowns.createExit("east", bruinen, outgoingOnly=False)
    swanfleet.createExit("east", mistyMountainsSouth, outgoingOnly=False)
    fangorn.createExit("east", fieldOfCelebrant, outgoingOnly=False)
    fangorn.createExit("east", theWold, outgoingOnly=False)
    westfold.createExit("east", westemnet, outgoingOnly=False)
    westemnet.createExit("east", eastemnet, outgoingOnly=False)
    eastemnet.createExit("east", emynMuil, outgoingOnly=False)
    eastfold.createExit("east", nindalf, outgoingOnly=False)
    nindalf.createExit("east", deadMarshes, outgoingOnly=False)
    anorien.createExit("east", anduin, outgoingOnly=False)
    anduin.createExit("east", ephelDuath, outgoingOnly=False)
    lossamarch.createExit("east", ithilien, outgoingOnly=False)
    orodruin.createExit("east", plateauOfGorgoth, outgoingOnly=False)

    # 连接南北走向的所有地区
    barrowDowns.createExit("south", oldForest, outgoingOnly=False)
    weatherHills.createExit("south", barrowDowns, outgoingOnly=False)
    trollshaws.createExit("south", bruinen, outgoingOnly=False)
    bruinen.createExit("south", mitheithel, outgoingOnly=False)
    mirkwood.createExit("south", southernMirkwood, outgoingOnly=False)
    southernMirkwood.createExit("south", lorien, outgoingOnly=False)
    mitheithel.createExit("south", swanfleet, outgoingOnly=False)
    swanfleet.createExit("south", dunland, outgoingOnly=False)
    dunland.createExit("south", calenardhon, outgoingOnly=False)
    lorien.createExit("south", fieldOfCelebrant, outgoingOnly=False)
    fieldOfCelebrant.createExit("south", theWold, outgoingOnly=False)
    fangorn.createExit("south", westemnet, outgoingOnly=False)
    theWold.createExit("south", eastemnet, outgoingOnly=False)
    westemnet.createExit("south", eastfold, outgoingOnly=False)
    eastemnet.createExit("south", nindalf, outgoingOnly=False)
    nindalf.createExit("south", cairAndros, outgoingOnly=False)
    emynMuil.createExit("south", deadMarshes, outgoingOnly=False)
    cairAndros.createExit("south", anduin, outgoingOnly=False)
    cirithUngol.createExit("south", ephelDuath, outgoingOnly=False)
    anorien.createExit("south", lossamarch, outgoingOnly=False)
    anduin.createExit("south", ithilien, outgoingOnly=False)

    # 通过独特地点连接的两地
    goblinTown.receiveSpaces(highPass, mirkwood)
    moria.receiveSpaces(mistyMountainsSouth, lorien)
    isenguard.receiveSpaces(calenardhon, westfold)
    blackGate.receiveSpaces(deadMarshes, udun)
    isenmouthe.receiveSpaces(udun, plateauOfGorgoth)
    minasMorgul.receiveSpaces(ephelDuath, plateauOfGorgoth)
    towerOfCirithUngol.receiveSpaces(cirithUngol, plateauOfGorgoth)

    # 创建包含所有地区的列表
    spaces = [shire, oldForest, weatherHills, trollshaws, mistyMountainsNorth,
              highPass, mirkwood, southernMirkwood, bruinen, mitheithel, swanfleet,
              dunland, mistyMountainsSouth, lorien, fangorn, fieldOfCelebrant,
              calenardhon, westfold, westemnet, eastemnet, emynMuil, eastfold, nindalf,
              deadMarshes, udun, cairAndros, orodruin, anorien, anduin, ephelDuath,
              cirithUngol, plateauOfGorgoth, lossamarch, ithilien]

    # 初始化随机向某些地区撒落独特物品
    for space in range(constants.SPACES_WITH_UNIQUE_ITEMS):
        if items.unique_items.lowLevelFindableUniques:
            # 确定撒落哪个独特物品
            item = random.choice(items.unique_items.lowLevelFindableUniques)
            items.unique_items.lowLevelFindableUniques.remove(item)
            # 确定撒落在哪个地区
            space = random.choice(spaces)
            # 将物品添加到该地区
            space.addItem(item)

    # 初始化随机向某些地区撒落精灵三戒（也可能未撒落任何一枚）
    # 确定要撒落的戒指
    chosenRings = []
    for ring in items.unique_items.elvenRings:
        if random.random() < constants.ELVEN_RING_PROB:
            chosenRings.append(ring)

    # 将戒指添加到随机地区
    for ring in chosenRings:
        space = random.choice(spaces)
        space.addItem(ring)

    return spaces


def getStartingInventory():
    """
    生成玩家的初始库存。

    @return:   库存的列表。
    """
    startingInventory = items.unique_items.startingInventory

    return startingInventory


def getPlayer(world, startingInventory):
    """
    创建玩家并给玩家起始装备。

    @return:     初始化完成的玩家对象
    """
    player = Player("独角螃蟹", world)

    for item in startingInventory:
        player.addToInventory(item)
    for item in startingInventory:
        player.equip(item)

    return player


def getCommandList(player):
    """
    生成游戏中使用的命令列表。

    @return:   用于存储游戏的命令的commandWords对象
    """
    # 创建commandWords对象
    commandWords = CommandWords()

    # 命令
    checkEquipmentCmd = CheckEquipmentCommand("equipment", "查看当前装备", player)
    commandWords.addCommand("equipment", checkEquipmentCmd)

    checkInventoryCmd = CheckInventoryCommand("inventory", "查看当前库存", player)
    commandWords.addCommand("inventory", checkInventoryCmd)

    checkMoneyCmd = CheckMoneyCommand("money", "查看金钱数量", player)
    commandWords.addCommand("money", checkMoneyCmd)

    checkStatsCmd = CheckStatsCommand("stats", "查看当前状态", player)
    commandWords.addCommand("stats", checkStatsCmd)

    descCmd = DescribeCommand("describe", "查看当前地区", player)
    commandWords.addCommand("describe", descCmd)

    dropCmd = DropCommand("drop", "丢弃物品", player)
    commandWords.addCommand("drop", dropCmd)

    eastCmd = EastCommand("east", "向东旅行", player)
    commandWords.addCommand("east", eastCmd)

    enterCmd = EnterCommand("enter", "进入地点", player)
    commandWords.addCommand("enter", enterCmd)

    equipCmd = EquipCommand("equip", "装备物品", player)
    commandWords.addCommand("equip", equipCmd)

    helpCmd = HelpCommand("help", "命令帮助", commandWords)
    commandWords.addCommand("help", helpCmd)

    mapCmd = MapCommand("map", "查看地图", player)
    commandWords.addCommand("map", mapCmd)

    northCmd = NorthCommand("north", "向北旅行", player)
    commandWords.addCommand("north", northCmd)

    pickupCmd = PickUpCommand("pick up", "拾取物品", player)
    commandWords.addCommand("pick up", pickupCmd)

    quitCmd = QuitCommand("quit", "退出游戏")
    commandWords.addCommand("quit", quitCmd)

    southCmd = SouthCommand("south", "向南旅行", player)
    commandWords.addCommand("south", southCmd)

    unequipCmd = UnequipCommand("unequip", "卸下装备", player)
    commandWords.addCommand("unequip", unequipCmd)

    usePotionCmd = UsePotionCommand("use potion", "使用药水", player)
    commandWords.addCommand("use potion", usePotionCmd)

    westCmd = WestCommand("west", "向西旅行", player)
    commandWords.addCommand("west", westCmd)

    return commandWords
