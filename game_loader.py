#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

from space import Space
from player import Player
from cities.city import City
from cities.inn import Inn
from cities.square import Square
from cities.shop import Shop
from unique_place import UniquePlace
from items.item import Item
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
import items.unique_items
from commands.command_words import CommandWords
from commands.help_command import HelpCommand
from commands.quit_command import QuitCommand
from commands.describe_command import DescribeCommand
from commands.drop_command import DropCommand
from commands.enter_command import EnterCommand
from commands.pick_up_command import PickUpCommand
from commands.equip_command import EquipCommand
from commands.unequip_command import UnequipCommand
from commands.use_potion_command import UsePotionCommand
from commands.check_inventory_command import CheckInventoryCommand
from commands.check_equipment_command import CheckEquipmentCommand
from commands.check_money_command import CheckMoneyCommand
from commands.check_stats_command import CheckStatsCommand
from commands.map_command import MapCommand
from commands.north_command import NorthCommand
from commands.south_command import SouthCommand
from commands.east_command import EastCommand
from commands.west_command import WestCommand
from unique_places.tom_bombadil_house import TomBombadilHouse
from unique_places.weathertop import Weathertop
from unique_places.isenguard import Isenguard
from unique_places.tharbad import Tharbad
from unique_places.argonath import Argonath
from unique_places.ost_in_edhil import OstInEdhil
from unique_places.goblin_town import GoblinTown
from unique_places.minas_morgul import MinasMorgul
from unique_places.black_gate import BlackGate
from unique_places.isenmouthe import Isenmouthe
from unique_places.barad_dur import BaradDur
from unique_places.dol_guldur import DolGuldur
from unique_places.tower_of_cirith_ungol import TowerOfCirithUngol
from unique_places.moria import Moria
from unique_places.derningle import Derningle
import constants


def getWorld():
    """
    创造中土。中土由一系列相连的地区组成。地区中可能有城市和独特地点。城市中可能有旅馆、广场和商店。

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
    greeting = "\"你听说过这个消息吗？\""
    hobbiton = City("霍比屯", description, greeting, [sallyInn, sallyShop, hobbitonSquare])
    # 夏尔
    description = """
    夏尔分为北、南、东、西四个区；它的首府是位于西区的白岗上的大洞镇。大洞镇市长是夏尔的霍比特人当中唯一真正的官员。
    夏尔主要依赖农业，其土地非常适合耕种。它的主要产物之一是烟斗草，其特别适合在远南部的温暖地区种植。
    """
    shire = Space("夏尔", description, constants.RegionType.ERIADOR, battleProbability=constants.SpaceSpawnProb.shire,
                  city=hobbiton)

    # 老林子 - 汤姆·邦巴迪尔的家
    # 独特地点
    description = "一所居住在柳条河山谷的神秘而强大的存在的房子。"
    greeting = """
    \"老汤姆·邦巴迪尔是个快乐的人；
    他的夹克是亮蓝色的，他的靴子是黄色的。\"
    """
    tomBombadil = TomBombadilHouse("汤姆·邦巴迪尔的家", description, greeting)
    # 老林子
    description = """
    老林子是中洲为数不多的原始森林之一，在第二纪元之前覆盖了伊利雅德的大部分地区。
    众所周知，老林子因霍比屯居民对其边界的焚毁而变得不欢迎外界之人并经常捉弄游客。
    """
    oldForest = Space("老林子", description, constants.RegionType.ERIADOR,
                      battleProbability=constants.SpaceSpawnProb.oldForest, uniquePlace=tomBombadil)

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
                         battleProbability=constants.SpaceSpawnProb.weatherHills, uniquePlace=weathertop)

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
                                battleProbability=constants.SpaceSpawnProb.mistyMountainsNorth, city=rivendell)

    # 高隘口 - 半兽人镇
    # 独特地点
    description = """
    半兽人镇是迷雾山脉中部山腹内的一座半兽人据点，一个被称作半兽人王的巨型半兽人统治着此地。
    所谓半兽人镇，实际上是一系列错综复杂的洞窟和隧道系统，它们遍布于迷雾山脉的山腹之内，咕噜所待过的洞穴就位于其中深处。
    """
    greeting = "\"是潜伏过去还是直接攻入？\""
    goblinTown = GoblinTown("半兽人镇", description, greeting)
    # 高隘口
    description = """
    高隘口是少数几处可供跨越迷雾山脉的隘口之一，位于幽谷以东。
    它的范围向西止于幽谷，从那里东大道向上蜿蜒入山，途中经过半兽人镇。

    ***通过半兽人镇可以向南进入黑森林***
    """
    highPass = Space("高隘口", description, constants.RegionType.HIGH_PASS,
                     battleProbability=constants.SpaceSpawnProb.highPass, uniquePlace=goblinTown)

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
    description = "\"瑟兰杜伊的酒宴！\""
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
    greeting = "\"是什么让你觉得你属于这里？\""
    talk = {
        "瑟兰杜伊": "哼！我是统治黑森林王国的精灵王！",
        "安格罗德": "这里的人对你几乎咬牙切齿，具体的原因你问问就知道了。",
        "阿瑞蒂尔": "哼！人类！",
        "阿尔巩": "哼！你不知道你身上的精灵甲已经落伍了吗？",
        "贝烈格·库沙理安": "哼！你应该穿上更好的精灵甲！"
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
    黑森林在辛达语中被称为\"大恐怖之林\"，它是罗瓦尼安的一大片森林，其原名为大绿林；
    第三纪元末年，因为邪恶力量的入侵，大绿林才被人们称为黑森林。索隆战败后，这里又被重新命名为绿叶森林。
    """
    mirkwood = Space("黑森林", description, constants.RegionType.RHOVANION,
                     battleProbability=constants.SpaceSpawnProb.mirkwood, city=elvenkingsHalls)

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
    greeting = "\"你们好，我是旅馆老板琳达。\""
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
    greeting = "\"戒灵一直在夜间造访这附近！\""
    bree = City("布理", description, greeting, [lindasInn, hanksBattleGear, prancingPony])
    # 古冢岗-布理
    description = """
    古冢岗是坐落于夏尔东部的连绵矮山丘，在老林子的北部，布理村庄的西南部。
    山脉中的许多丘陵巨石遍布，坟冢到处可见，这也是其名由来。
    """
    barrowDowns = Space("古冢岗-布理", description, constants.RegionType.BARROW_DOWNS,
                        battleProbability=constants.SpaceSpawnProb.barrowDowns, city=bree)

    # 布茹伊能河
    description = """
    布茹伊能河，又名响水河，是东伊利雅德的一条河流。
    它发源于迷雾山脉西麓，最终汇入米斯艾塞尔河，其南翼流经埃尔隆德建立的避难所幽谷。
    """
    bruinen = Space("布茹伊能河", description, constants.RegionType.ERIADOR,
                    battleProbability=constants.SpaceSpawnProb.bruinen)

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
                    battleProbability=constants.SpaceSpawnProb.dunland)

    # 迷雾山脉南部
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

    ***通过墨瑞亚可以向东进入罗瑞恩***
    """
    mistyMountainsSouth = Space("迷雾山脉南部", description, constants.RegionType.MORIA, uniquePlace=moria)

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
    """
    lorien = Space("罗瑞恩", description, constants.RegionType.RHOVANION,
                   battleProbability=constants.SpaceSpawnProb.lorien, city=carasGaladhon)

    # 范贡森林 - 秘林谷
    # 独特地点
    description = "此处是恩特们举行会议的地点"
    greeting = "\"欢迎来到恩特大会！不必那么着急。\""
    derningle = Derningle("秘林谷", description, greeting)
    # 范贡森林
    description = """
    范贡森林是一片深邃而黑暗的林地，位于迷雾山脉南部的下方，该山脉的东侧。
    在洛汗，这片森林借用了老恩特范贡的名字，被洛汗人民称为“恩特森林”。
    """
    fangorn = Space("范贡森林", description, constants.RegionType.ROHAN,
                    battleProbability=constants.SpaceSpawnProb.fangorn, uniquePlace=derningle)

    # 北高原
    description = """
    北高原是洛汗的最北部，也是人口最少的地区，位于范贡森林和安都因河之间，军事划分上属于东马克。
    此地适宜放牧，多风，但十分荒凉，很少有人居住。近年来，由于奥克的频繁出没，这里已经不再安全。
    """
    theWold = Space("北高原", description, constants.RegionType.MORDOR,
                    battleProbability=constants.SpaceSpawnProb.theWold)

    # 凯勒布兰特原野
    description = """
    凯勒布兰特原野是凯勒布兰特河与利姆清河之间的大片土地，位于洛丝罗瑞恩的东南部。
    第三纪元2510年，洛汗人奋起援助刚铎的凯勒布兰特原野之战在这里发生。
    """
    fieldOfCelebrant = Space("凯勒布兰特原野", description, constants.RegionType.MORDOR,
                             battleProbability=constants.SpaceSpawnProb.fieldOfCelebrant)

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

    # Westfold - Helm's Deep
    # Inn
    description = "Where people go to sober up."
    greeting = "No one is there to greet you."
    sobrietyRoom = Inn("Sobriety Room", description, greeting, 0)
    # Shop
    description = "The Armory [read: booze shop]."
    greeting = "We got every poison under the sun...."
    theArmory = Shop("The Armory", description, greeting,
                     constants.RegionType.ROHAN, 8, 6)
    # Square
    description = "Mass drunkenness."
    greeting = "Everyone is passed out."
    talk = {
        "Erkenbrand": "Ughhhhhhh....",
        "Gambling the Old": "Merrrrrrrrrrrrr...."
    }
    helmsDeepCommons = Square("Helms Deep Commons", description, greeting,
                              talk, items.unique_items.helmsDeepCommonsItems)
    # City
    description = """Helm's Deep is a large valley gorge in northwestern Ered 
    Nimrais below the Thrihyrne. It consists of a massive defensive system 
    called the Hornburg.
    """
    greeting = "\"Welcome to Helm's Deep! WHOOO!!! PARTY!\""
    helmsDeep = City("Helm's Deep", description, greeting,
                     [sobrietyRoom, theArmory, helmsDeepCommons])
    # Westfold
    description = """The Westfold is the western part of Rohan, close to the 
    White Mountains and situated between the river Isen and the Folde. The 
    North-South Road runs through the Westfold from the Fords of Isen to 
    Edoras. Its strongpoint is Helm's Deep.
    """
    westfold = Space("Westfold", description, constants.RegionType.ROHAN,
                     battleProbability=constants.SpaceSpawnProb.westfold,
                     battleBonusDifficulty=constants.SpaceBonusDiff.westfold,
                     city=helmsDeep)

    # Westemnet
    description = """The Eastemnet is part of Rohan. It is an area of wide, 
    grassy plains east of the Entwash River.
    """
    westemnet = Space("West Emmet", description, constants.RegionType.ROHAN,
                      battleProbability=constants.SpaceSpawnProb.westemnet,
                      battleBonusDifficulty=constants.SpaceBonusDiff.westemnet)

    # Eastemnet
    description = """The Eastemnet is part of Rohan. It contains wide, grassy 
    plains and is east of the Entwash and west of the Great River, Anduin.
    """
    eastemnet = Space("East Emmet", description, constants.RegionType.ROHAN,
                      battleProbability=constants.SpaceSpawnProb.eastemnet)

    # Emyn Muil
    description = """Emyn Muil is a range of hills south of the Brown Lands 
    and north of Nindalf. The Anduin cuts through these hills and pools in Nen 
    Hithoel.
    """
    emynMuil = Space("Emyn Muil", description, constants.RegionType.MORDOR,
                     battleProbability=constants.SpaceSpawnProb.emynMuil)

    # Eastfold - Edoras
    # Inn
    description = "A quaint inn settled on an open plain."
    greeting = "\"Travelers! We'd be glad to have you for the night.\""
    sunsetVillage = Inn("Prairie View", description, greeting, 5)
    # Shop
    description = "Crafts and various collectibles."
    greeting = "We have items dating back from T.A. 1497!"
    twiceRemembered = Shop("Twice Remembered", description, greeting,
                           constants.RegionType.ROHAN, 10, 8)
    # Square
    description = "A country square full of mostly older folk."
    greeting = "\"We love our lands.\""
    talk = {
        "Helm Gammerhand": "I wish you the best on your journey.",
        "Brytta Leofa": "I have several daughters your age.",
        "Morwen Steelsheen": ("I would love to teach you blacksmithing if you have"
                              " the time."),
        "Frealaf Hildeson": ("Mostly older folks here. My kids are off to work in"
                             " the city.")
    }
    edorasCommons = Square("Edoras Commons", description, greeting, talk,
                           items.unique_items.edorasCommonsItems)
    # City
    description = """Rohan's first capital was at Aldburg until Eorl the 
    Young's son Brego built Edoras. It is Rohan's only real city and holds the 
    Golden Hall of Meduseld.
    """
    greeting = "\"Welcome to Edoras!\""
    edoras = City("Edoras", description, greeting, [sunsetVillage,
                                                    twiceRemembered, edorasCommons])
    # Eastfold - Aldburg
    # Inn
    description = "Innkeeper is a man by the name of Seth."
    greeting = "\"We'd be glad to have you for the night.\""
    sethsHostel = Inn("Seth's Hostel", description, greeting, 5)
    # Shop
    description = "Other items too."
    greeting = "\"Would you like some samples?\""
    milesCookieFactory = Shop("Miles' Cookie Factory", description, greeting,
                              constants.RegionType.ROHAN, 10, 12)
    # Square
    description = "Many interesting discussions."
    greeting = "\"I wonder how this works...?\""
    talk = {
        "Dmitriy": "Dante.",
        "Jim \"The Dear Ladd\" Jr.": "Let's fobrinicate the fobazz!",
        "Chris": "I am from China."
    }
    auburnSquare = Square("Auburn Square Commons", description, greeting,
                          talk, items.unique_items.auburnSquareCommons)
    # City
    description = """Aldburg was built by Eorl in the region known as the 
    Folde, east of Edoras. The Kings of Rohan moved to Edoras after Brego, son 
    of Eorl, completed the Golden Hall.
    """
    greeting = "\"Welcome to Aldburg!\""
    aldburg = City("Aldburg", description, greeting, [sethsHostel,
                                                      milesCookieFactory, auburnSquare])
    # Eastfold
    description = """Eastfold is a part of the realm of Rohan. Bounded by the 
    Mering Stream and Snowbourn River, it contains the cities of Aldburg and 
    Edoras.
    """
    eastfold = Space("Eastfold", description, constants.RegionType.ROHAN,
                     battleProbability=constants.SpaceSpawnProb.eastfold,
                     city=[edoras, aldburg])

    # Nindalf
    description = """The swamps of Nindalf or Wetwang lie to the south of Emyn 
    Muil and east of the Great River Anduin and are fed by the great inland 
    delta of Entwash. The Dead Marshes lie further east and are an extension 
    of Nindalf.
    """
    nindalf = Space("Nimdalf", description, constants.RegionType.MORDOR,
                    battleProbability=constants.SpaceSpawnProb.nindalf)

    # Dead Marshes - Black Gate
    # Unique Place
    description = """The Black Gate of Mordor is a gate built by Sauron to 
    prevent invasion through the Pass of Cirith Gorgor, the gap between the 
    Ered Lithui and the Ephel Duath.
    """
    greetings = "\"One does not simply walk into Mordor.\""
    blackGate = BlackGate("Black Gate", description, greetings)
    # Dead Marshes
    description = """The Dead Marshes are an area of swampland east of the
    Dagorlad plain. It is the site of the ancient Battle of Dagorlad.
    
    ***Udun is accessible to the east through The Black Gate***
    """
    deadMarshes = Space("Dead Marshes", description,
                        constants.RegionType.MORDOR,
                        uniquePlace=blackGate)

    # Valley of Udun - Isenmouthe
    # Unique Place
    description = """Isenmouthe or Carach Angren is a pass in the northeastern 
    part of Mordor and guards the southern end of the valley, Udun.
    
    The pass is heavily guarded with fortresses and watchtowers.
    """
    greetings = "\"One does not simply walk into Mordor part II.\""
    isenmouthe = Isenmouthe("Isenmouthe", description, greetings)
    # Valley of Udun
    description = """Udun is a depressed valley in northwestern Mordor. It 
    lies between Cirith Gorgor and Isenmouthe and is traversed by large armies 
    of Sauron in times of war.
    
    ***Plateau of Gorgoth is accessible to the south through Isenmouthe***
    """
    udun = Space("Udun", description, constants.RegionType.MORDOR,
                 battleProbability=constants.SpaceSpawnProb.udun,
                 battleBonusDifficulty=constants.SpaceBonusDiff.udun,
                 uniquePlace=isenmouthe)

    # Cair Andros
    description = """Cair Andros, meaning "Ship of the Long-Foam," is an
    island in the river Anduin, resting nearly forty miles to the north of 
    Osgiliath. It is of paramount importance to Gondor because it prevents the 
    enemy from crossing the river and entering into Anorien.
    """
    cairAndros = Space("Cair Andros", description,
                       constants.RegionType.GONDOR,
                       battleProbability=constants.SpaceSpawnProb.cairAndros,
                       battleBonusDifficulty=constants.SpaceBonusDiff.cairAndros)

    # 欧洛都因（末日山）
    description = "末日山，也被称为欧洛都因或阿蒙阿马斯，是魔多的火山，至尊戒是在这里锻造的。这是唯一可以摧毁至尊戒的地方。"
    orodruin = Space("欧洛都因", description, constants.RegionType.MORDOR,
                     battleProbability=constants.SpaceSpawnProb.orodruin,
                     battleBonusDifficulty=constants.SpaceBonusDiff.orodruin)

    # Anorien - Minas Tirith
    # Inn
    description = "Where elite Gondorian healers do their work."
    greeting = "\"Welcome to the Houses of Healing. What can I do for you?\""
    housesOfHealing = Inn("Houses of Healing", description, greeting, 5)
    # Shop
    description = "An elite armory, used by the best Gondorian troops."
    greeting = "Welcome to the Smithy of Kings! We have legendary blades...."
    smithyOfKings = Shop("Smithy of Kings", description, greeting,
                         constants.RegionType.GONDOR, 14, 14)
    # Square
    description = "Minas Tirith commons."
    greeting = "Tension greets you as you enter Minas Tirith Commons."
    talk = {
        "Calmacil": "Would you like to buy some fruit?",
        "Castamir": "Everyone is afraid....",
        "Ciryandil": "Orcish raids have been increasing in the outlying lands....",
        "Minalcar": "I wonder what we can do with Mordor....",
        "Narmacil": "I wonder if the king will return",
        "Tarondor": "I hope Rohan will bring aid....",
        "Atanatar": "Word has it that Mordor is preparing to attack...."
    }
    marketSquare = Square("Market Square", description, greeting, talk,
                          items.unique_items.marketSquareItems)
    # Square
    description = "Site of Gondorian royalty."
    greeting = "Denethor would like to see you...."
    talk = {
        "Denethor": "You are the true king of Gondor.",
        "Faramir": "The lands recently stolen by Sauron should be retaken....",
        "Boromir": "Nice ring. Give it to me!",
        "Prince Imrahil": "Sauron plans on moving soon....",
        "Swan Knight": "Here is a gift to help you fight!"
    }
    towerOfEcthelion = Square("Tower of Ecthelion", description, greeting,
                              talk, items.unique_items.towerOfEchelionItems)
    # City
    description = """Minas Tirith is a city of Gondor originally called Minas 
    Anor. From T.A. 1640 onwards it became the capital of the South-kingdom 
    and the seat of its Kings and ruling Stewards.
    """
    greeting = "\"Welcome to the last stronghold of the West, Minas Tirith.\""
    minasTirith = City("Minas Tirith", description, greeting,
                       [housesOfHealing, marketSquare, towerOfEcthelion, smithyOfKings])
    # Anorien
    description = """Anorien is the fiefdom of Gondor containing Minas Tirith, 
    the capital of Gondor. Originally known as Minas Anor, it replaced 
    Osgiliath as capital of Gondor as Osgiliath was lost to Sauron.
    """
    anorien = Space("Anorien", description, constants.RegionType.GONDOR,
                    battleProbability=constants.SpaceSpawnProb.anorien,
                    city=minasTirith)

    # Anduin - Argonath
    # Unique Place
    description = "Great for dates."
    greeting = ("\"Welcome to Argonath! Stay within the designated areas and"
                " listen to your guide.\"")
    argonath = Argonath("Argonath", description, greeting)
    # Anduin - Osgiliath
    # Inn
    description = "A place to rest in the midst of battle."
    greeting = "\"Your cot is on the top left.\""
    soldierBarracks = Inn("Soldier Barracks", description, greeting, 5)
    # Shop
    description = "Rapidly depleting inventories."
    greeting = "What would you like? We are low on everything...."
    osgiliathArmory = Shop("Osgiliath Armory", description, greeting,
                           constants.RegionType.GONDOR, 4, 12)
    # Square
    description = "Once a glorious square in the capital of Gondor."
    greeting = "You find the square in ruins and deserted."
    talk = {}
    osgiliathCommons = Square("Osgiliath Commons", description, greeting,
                              talk)
    # City
    description = """Osgiliath was the ancient capital of the Kingdom of 
    Gondor. Depopulated during the Third Age, it gradually fell into ruin. 
    Osgiliath has strategic importance as a crossing point over the Anduin.
    """
    greeting = "\"Be on your guard. We are constantly under attack.\""
    osgiliath = City("Osgiliath", description, greeting, [soldierBarracks,
                                                          osgiliathArmory, osgiliathCommons])
    # Anduin
    description = """Anduin is a river that crosses most of Middle-Earth east
    of the Misty Mountains. Passing through many lands, it has many names:
    Langflood by the ancestors of the Rohirrim, the Great River of Wilderland 
    in the Westron of Rivendell and the Shire, and simply the Great River in 
    Gondor.
    """
    anduin = Space("Anduin", description, constants.RegionType.GONDOR,
                   battleProbability=constants.SpaceSpawnProb.anduin,
                   battleBonusDifficulty=constants.SpaceBonusDiff.anduin,
                   city=osgiliath, uniquePlace=argonath)

    # Ephel Duath - Minas Morgul
    # Unique Place
    description = """Minas Morgul is a fortress-city in Mordor. Originally 
    created as a Gondorian outpost and the sister city of Minas Anor, Minas 
    Ithil safeguarded the eastern borders of the Kingdom of Gondor and its 
    capital from the forces of Mordor during the early part of the Third Age.

    Minas Morgul is home to the Nazgul.
    """
    greeting = "\"One does not simply walk into Mordor.\""
    minasMorgul = MinasMorgul("Minas Morgul", description, greeting)
    # Ephel Duath
    description = """The Ephel Dúath, or the Mountains of Shadow, is a range of
    mountains that guards Mordor's western and southern borders.
    
    ***Plateau of Gorgoth is accessible to the east through Minas Morgul***
    """
    ephelDuath = Space("Ephel Duath", description,
                       constants.RegionType.MORDOR,
                       battleProbability=constants.SpaceSpawnProb.ephelDuath,
                       battleBonusDifficulty=constants.SpaceBonusDiff.ephelDuath,
                       uniquePlace=minasMorgul)

    # Cirith Ungol - Tower of Cirith Ungol
    # Unique Place
    description = """Gondor occupied the fortress until T.A. 1636 when the
    Great Plague killed large parts of Gondor's population. After the plague,
    Gondor never again manned the Tower of Cirith Ungol and evil was allowed
    to return to Mordor. Similar fates suffered the mountain fortress of 
    Durthang in northwestern Mordor and the Towers of the Teeth at Morannon.
    """
    greeting = "\"May it be a light to you in dark places.\""
    towerOfCirithUngol = TowerOfCirithUngol("Tower of Cirith Ungol",
                                            description, greeting)
    # Cirith Ungol
    description = """Cirith Ungol is the pass through the western mountains of
    Mordor and the only way towards the land from the west. It is guarded by 
    the Tower of Cirith Ungol, built by the Men of Gondor after the War of the 
    Last Alliance of Elves and Men.
    
    ***Plateau of Gorgoth is accessible to the east through Tower of Cirith Ungol***
    """
    cirithUngol = Space("Cirith Ungol", description,
                        constants.RegionType.MORDOR,
                        battleProbability=constants.SpaceSpawnProb.cirithUngol,
                        battleBonusDifficulty=constants.SpaceBonusDiff.cirithUngol,
                        uniquePlace=towerOfCirithUngol)

    # Plateau of Gorgoth - Barad Dur
    # Unique Place
    description = """Barad-dur is the Dark Lord Sauron's sanctuary fortress in 
    Mordor and serves as his base of operations. Over 1400 meters high and 
    held together by dark magic, it is the largest fortress in Middle-earth.
    """
    greeting = """\"Rising black, blacker and darker than the vast shades amid 
    which it stood, the cruel pinnacles and iron crown of the topmost tower of 
    Barad-dur....\""""
    baradDur = BaradDur("Barad Dur", description, greeting)
    # Plateau of Gorgoth
    description = """Plateau of Gorgoroth is a region in the northwestern 
    region of Mordor. Gorgoroth is the location of the mines and forges which 
    supply Mordor's armies with weapons and armor.
    """
    plateauOfGorgoth = Space("Plateau of Gorgoth", description,
                             constants.RegionType.MORDOR,
                             battleProbability=constants.SpaceSpawnProb.plateauOfGorgoth,
                             battleBonusDifficulty=constants.SpaceBonusDiff.plateauOfGorgoth,
                             uniquePlace=baradDur)

    # Lossamarch - Pelargir
    # Inn
    description = "Beach resort along one of Gondor's finest coasts!"
    greeting = "\"Hey bro! Welcome to Sunnyside Inn!\""
    sunnysideInn = Inn("Sunnyside Inn", description, greeting, 5)
    # Shop
    description = "Beach accessories and paraphernalia."
    greeting = "\"Hey what's up, bro?\""
    palmTreeHut = Shop("Palm Tree Hut", description, greeting,
                       constants.RegionType.GONDOR, 6, 14)
    # Square
    description = "Class-three waves!"
    greeting = "\"Bro, did you see those waves?\""
    talk = {
        "Gondorian bro #1": "Bro, let's hit the beach!",
        "Gondorian bro #2": "Bro! Let's just chill for awhile....",
        "Gondorian bro #3": ("Bro! I hear there's going to be a party later"
                             " tonight."),
        "Gondorian chick #1": "Bro, I have a boyfriend....",
        "Gondorian chick #2": "Bro, what are you doing later?"
    }
    beach = Square("Pelargir Beach", description, greeting, talk,
                   items.unique_items.beachItems)
    # City
    description = """One of the oldest cities in Middle Earth, Pelargir served
    as chief haven of the faithful as Numenorians migrated to Middle Earth to
    escape persecution. In later years, Pelargir served as chief port of 
    Gondor.
    """
    greeting = "Enjoy a relaxing stay at Pelargir, port city of Gondor."
    pelargir = City("Pelargir", description, greeting, [sunnysideInn,
                                                        palmTreeHut, beach])
    # Lossamarch
    description = """Lossarnach is a region and fiefdom in Southern Gondor. 
    Known as the Vale of Flowers, it is a fertile region lying south of the 
    White Mountains.
    """
    lossamarch = Space("Lossamarch", description, constants.RegionType.GONDOR,
                       battleProbability=constants.SpaceSpawnProb.lossamarch,
                       city=pelargir)

    # Ithilien
    description = """Ithilien is the fiefdom of Gondor bordering Mordor from 
    the southwest.
    """
    ithilien = Space("Ithilien", description, constants.RegionType.GONDOR,
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
