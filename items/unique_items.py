#!/usr/bin/python

from items.item import Item
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from items.charm import Charm
import constants

"""
以下是游戏中的一些独特物品。例如：“至尊戒”"
"""
# 剧情物品
# 初始库存
staff = Weapon("短杖", "隐藏着锋利的刀口", 4, 2, 2)
leatherCloak = Armor("皮斗篷", "旅行外衣", 3, 8, 1)
theOneRing = Item("至尊戒", "非常重要", 6, 540)
vodka = Potion("伏特加", "有益健康", 1, 4, 4)
startingInventory = [staff, leatherCloak, theOneRing, vodka]

# 霍比屯广场
walkingCane = Item("手杖", "帮助作用值得怀疑", 2, 2)
tea = Potion("茶", "令人愉快的茶点", 1, 1, 4)
newspaper = Item("夏尔报", "主要是小报……关于霍比特人", 0, 0)
hobbitonSquareItems = {"纳夫特尔·图克": walkingCane, "阿马兰斯·白兰地鹿": [tea, newspaper]}

# 埃尔隆德议会
legolasHair = Item("莱戈拉斯的头发", "用于制造", 0, 12)
mithrilVest = Armor("秘银衫", "来自比尔博的礼物", 1, 102, 4)
anduril = Weapon("安督利尔 — 西方之焰", "曾经破碎的剑，现已重铸", 2, 114, 22)
councilOfElrondItems = {"埃尔隆德": anduril, "莱戈拉斯": legolasHair, "比尔博": mithrilVest}

# 坑洞
water = Potion("清水", "可使人清醒", 1, 4, 8)
elvenRum = Potion("精灵朗姆酒", "对所有其他种族有毒", 1, 6, -5)
thePitItems = {"库茹芬": water, "戴隆": elvenRum}

# 精灵王的宝座
sweetNewElvenWare = Armor("华丽的精灵甲", "来自黑森林的最新款式", 4, 52, 3)
elvenkingsThroneItems = {"贝烈格·库沙理安": sweetNewElvenWare}

# 跃马客栈
tea = Potion("茶", "杜多留下的", 1, 3, 1)
bulletin = Item("告示", "有关黑骑手的详细目击情况", 0, 0)
prancingPonyItems = {"哈里·金银花": bulletin, "杜多·巴金斯": tea}

# 加拉德瑞尔之镜
elvenCloak = Armor("精灵斗篷", "加拉德瑞尔的礼物", 4, 62, 3)
phialOfGaladriel = Item("加拉德瑞尔的水晶瓶", "“愿它在黑暗中成为你的光”", 1, 92)
galadrielsMirrorItems = {"加拉德瑞尔": [elvenCloak, phialOfGaladriel]}

# 海尔姆深谷广场
vodka = Potion("洛汗伏特加", "驭马者的毒药", 1, 12, 32)
vodka2 = Potion("生命之水", "廉价的伏特加", 1, 10, 24)
helmsDeepCommonsItems = {"埃肯布兰德": vodka, "老甘姆林": vodka2}

# 埃多拉斯广场
tea = Potion("茶", "用于分享故事", 1, 16, 46)
tea2 = Potion("茶", "秘密配方", 1, 14, 42)
newspaper = Item("剪报", "主要用于回忆过去", 1, 0)
edorasCommonsItems = {"海尔姆游击手": tea, "弗雷亚拉夫": tea2, "布里塔": newspaper}

# 奥德堡广场
russianTea = Potion("下午茶", "酒精含量仅为 30%（按体积计）", 1, 8, 28)
freePizza = Potion("免费披萨饼", "跟墓碑一样硬", 1, 16, 52)
chineseHandouts = Item("中文讲义", "语句欠佳", 14, 42)
auburnSquareCommons = {"德米特里": russianTea, "吉姆": freePizza, "克里斯": chineseHandouts}

# Market Square
fruitSamples = Potion("Fruit Samples", "Meagerly", 2, 18, 30)
foodHoards = Potion("Spare Food Hoards", "Generously given", 4, 42, 85)
negativeThinking = Charm("Negative Thinking", "Not something you want",
                         35, 0, -15, -2, -40)
marketSquareItems = {"Calmacil": fruitSamples, "Atanatar": foodHoards,
                     "Castamir": negativeThinking}

# Tower of Echelion
palatir = Item("Palatir", "For seeing mysteries", 6, 112)
windbeam = Charm("Windbeam", "Strengthens the hearts of men", 4, 116, 14, 1, 36)
executorSword = Weapon("Executor Sword", "A gift from Prince Imrahil",
                       12, 112, 26)
towerOfEchelionItems = {"Denethor": [palatir, windbeam],
                        "Prince Imrahil": executorSword}

# Beach
draagz = Item("Draagz", "Bad for health", 2, 76)
vodka = Potion("Vodka", "From the Gondorian heartland", 1, 52, 48)
flowersAndTrinkets = Charm("Flowers And Trinkets", "Mental health bonuses",
                           5, 72, 6, 0, 18)
beachItems = {"Gondorian bro #3": [draagz, vodka],
              "Gondorian bro #2": flowersAndTrinkets}

# 精灵三戒
narya = Charm("纳雅", "火之戒，精灵三戒之一", 0, 270, 100, 0, 0)
nenya = Charm("能雅", "水之戒，精灵三戒之一", 0, 280, 0, 0, 500)
vilya = Charm("维雅", "气之戒，精灵三戒之一", 0, 265, 0, 15, 0)
elvenRings = [narya, nenya, vilya]

# 商店武器
# 伊利雅德的商店
walkingStick = Weapon("短杖", "既能拄着旅行又能当作武器", 2, 4, 1)
gardenShovel = Weapon("花园铲", "我们能找到的最好的武器之一...", 3, 5, 2)
gardenSythe = Weapon("花园篱", "这也能用？太吓人了", 3, 7, 4)
shortSword = Weapon("短剑", "霍比特人标配", 3, 8, 5)
hobbitElite = Weapon("精英霍比特人战斗装备", "其实就是些石子", 2, 12, 6)

eriadorWeaponsDist = {
    walkingStick: [0, 2],
    gardenShovel: [0, 2],
    gardenSythe: [1, 4],
    shortSword: [2, 6],
    hobbitElite: [4, 20]
}

# 洛汗的商店
ironSword = Weapon("Iron Sword", "Strange markings", 6, 18, 12)
mediumSword = Weapon("Medium Sword", "Battle tested", 8, 26, 14)
rohirricBow = Weapon("Rohirric Bow", "Historic embroidery", 10, 30, 16)
battleMace = Weapon("Battle Mace", "Classic for knights", 8, 42, 20)
battleLance = Weapon("Battle Lance", "Knight esesential", 14, 62, 26)

rohanWeaponsDist = {
    ironSword: [0, 8],
    mediumSword: [6, 10],
    rohirricBow: [7, 10],
    battleMace: [8, 12],
    battleLance: [10, 20],
}

# 罗马尼安的商店
elvenTrainerBow = Weapon("精灵训练弓", "给精灵小孩用的", 6, 16, 8)
elvenBlade = Weapon("精灵刃", "雪白而发亮", 5, 24, 12)
elvenBow = Weapon("精灵弓", "精灵标配", 6, 35, 16)
doubleBlades = Weapon("精灵双刃", "挥舞如风", 6, 42, 18)
eliteElvenSword = Weapon("精英精灵刃", "拥有强大而神奇的特性", 8, 118, 32)
eliteElvenBow = Weapon("精英精灵长弓", "由瑁珑树制成", 8, 112, 40)

rhovanionWeaponsDist = {
    elvenTrainerBow: [0, 8],
    elvenBlade: [6, 10],
    elvenBow: [7, 10],
    doubleBlades: [8, 12],
    eliteElvenSword: [12, 20],
    eliteElvenBow: [12, 20],
}

# 刚铎的商店
soldiersSword = Weapon("Soldier's Sword", "Standard grade", 8, 30, 16)
longSword = Weapon("Long Sword", "A Gondorian blade", 12, 52, 20)
compoundBow = Weapon("Compound Bow", "Extreme range", 12, 56, 22)
eliteLongSword = Weapon("Elite Long Sword", "A Numernorian blade", 10, 112, 25)
gondorianLongbow = Weapon("Gondorian Longbow", "Extreme range", 14, 102, 30)

gondorWeaponsDist = {
    soldiersSword: [0, 12],
    longSword: [12, 15],
    compoundBow: [13, 16],
    eliteLongSword: [16, 20],
    gondorianLongbow: [16, 20],
}

# 商店盔甲
# 伊利雅德的商店
farmerShawl = Armor("农夫的披肩", "防晒用", 4, 8, 1)
travelCloak = Armor("旅行披风", "一条黑暗的裹尸布", 3, 12, 1)
leatherCloak = Armor("皮斗篷", "穿起来真的很窒闷", 5, 14, 2)

eriadorArmorDist = {
    farmerShawl: [0, 2],
    travelCloak: [2, 4],
    leatherCloak: [4, 20]
}

# 洛汗的商店
leatherArmor = Armor("Leather Armor", "Light and lithe", 6, 18, 2)
chainmail = Armor("Chainmail", "Took an incredibly long time to make", 10, 24, 4)
suitOfArmor = Armor("Suit of Armor", "To become a knight in shining armor",
                    25, 85, 6)
rohirricBreastplate = Armor("Rohirric Breastplate", "Aged with dignity",
                            16, 74, 5)

rohanArmorDist = {
    leatherArmor: [0, 7],
    chainmail: [8, 12],
    suitOfArmor: [10, 14],
    rohirricBreastplate: [12, 20]
}

# 罗马尼安的商店
workersGear = Armor("精灵服", "精灵们平时穿的衣服", 6, 14, 2)
elvenWare = Armor("精灵甲", "轻盈而又经得起时间考验", 4, 40, 3)
eliteElvenWare = Armor("精英精灵甲", "被报以巨额溢价", 4, 152, 5)
velvetSuit = Armor("天鹅绒服", "性感的着装", 6, 262, 8)

rhovanionArmorDist = {
    workersGear: [0, 6],
    elvenWare: [6, 10],
    eliteElvenWare: [9, 15],
    velvetSuit: [12, 20]
}

# 刚铎的商店
standardSoldiersArmor = Armor("Standard Soldier's Armor", "Sells for a reason",
                              12, 56, 3)
platemail = Armor("Platemail", "Can take a wallop", 18, 84, 4)
magneticArmor = Armor("Magnetic Armor", "Repels attacks", 16, 124, 5)
eliteGondorianArmor = Armor("Elite Gondorian Armor", "Elite Platemail",
                            18, 142, 6)

gondorArmorDist = {
    standardSoldiersArmor: [0, 12],
    platemail: [12, 16],
    magneticArmor: [16, 20],
    eliteGondorianArmor: [17, 20]
}

# 商店药水
# 伊利雅德的商店
hobbitTea = Potion("霍比特茶", "主要是月桂叶", 1, 4, 4)
shireWater = Potion("夏尔水", "产自白兰地河", 1, 6, 6)
shireWater2 = Potion("夏尔水", "产自夏尔伯恩", 1, 8, 10)

eriadorPotionDist = {
    hobbitTea: [0, 2],
    shireWater: [2, 4],
    shireWater2: [2, 20]
}

# 洛汗的商店
adornWater = Potion("Adorn Water", "From the Adorn River", 1, 14, 22)
rohirricTea = Potion("Rohirric Tea", "Calming effects", 1, 24, 30)
fangornWater = Potion("Entwash Water", "Extreme restorative properties", 1, 48, 64)

rohanPotionDist = {
    adornWater: [0, 6],
    rohirricTea: [6, 10],
    fangornWater: [10, 20]
}

# 罗马尼安的商店
elvenTea = Potion("精灵茶", "具有神奇的作用", 1, 18, 16)
mirkwoodWater = Potion("精灵水", "来自迷雾山脉", 1, 24, 24)
magicalElixir = Potion("魔法药剂", "散发着奇特的光芒", 2, 60, 50)

rhovanionPotionDist = {
    elvenTea: [0, 10],
    mirkwoodWater: [8, 12],
    magicalElixir: [12, 20]
}

# 刚铎的商店
anduinWater = Potion("Anduin Water", "All the way from the Anduin River", 1, 52, 72)
snowmelt = Potion("Snowmelt", "From the White Mountains", 1, 64, 82)
advancedElixir = Potion("Advanced Elixir", "From the Houses of Healing", 2, 102, 152)

gondorPotionDist = {
    anduinWater: [0, 12],
    snowmelt: [10, 15],
    advancedElixir: [14, 20]
}

# 商店武器总分布
shopWeaponDist = {
    constants.RegionType.ERIADOR: eriadorWeaponsDist,
    constants.RegionType.RHOVANION: rhovanionWeaponsDist,
    constants.RegionType.ROHAN: rohanWeaponsDist,
    constants.RegionType.GONDOR: gondorWeaponsDist}

# 商店盔甲总分布
shopArmorDist = {
    constants.RegionType.ERIADOR: eriadorArmorDist,
    constants.RegionType.RHOVANION: rhovanionArmorDist,
    constants.RegionType.ROHAN: rohanArmorDist,
    constants.RegionType.GONDOR: gondorArmorDist}

# 商店药水总分布
shopPotionDist = {
    constants.RegionType.ERIADOR: eriadorPotionDist,
    constants.RegionType.RHOVANION: rhovanionPotionDist,
    constants.RegionType.ROHAN: rohanPotionDist,
    constants.RegionType.GONDOR: gondorPotionDist}

# 独特武器
guthwine = Weapon("古斯威奈", "伊奥梅尔的佩剑。赃物", 8, 142, 22)
herugrim = Weapon("赫鲁格林", "希奥顿的佩剑。会引起负面的关注", 8, 136, 26)
orchrist = Weapon("奥克锐斯特", "辛达语：兽咬剑", 15, 160, 24)

# 独特盔甲
tarhelmCrown = Armor("塔因头盔", "来自暗黑破坏神中的崔斯特瑞姆", 6, 86, 3)
snowclash = Armor("雪之冲突 — 战场腰带", "来自暗黑破坏神中的崔斯特瑞姆", 5, 92, 4)
razortail = Armor("剃刀之尾 — 鲨皮腰带", "来自暗黑破坏神中的崔斯特瑞姆", 8, 102, 4)
nightsmoke = Armor("夜烟 — 扣带", "来自暗黑破坏神中的崔斯特瑞姆", 4, 114, 5)
peasantCrown = Armor("粗野之冠 — 战帽", "来自暗黑破坏神中的崔斯特瑞姆", 4, 85, 4)
crownOfThieves = Armor("盗贼皇冠", "来自暗黑破坏神中的崔斯特瑞姆", 5, 76, 3)

# 精英级独特武器
glamdring = Weapon("格拉姆德凛", "西部语：击敌锤", 6, 162, 72)
anglachel = Weapon("安格拉赫尔", "烈星之铁", 6, 170, 76)
angrist = Weapon("安格锐斯特", "辛达语：劈铁者", 5, 174, 80)
anguirel = Weapon("安格微瑞尔", "永恒之铁", 6, 172, 82)
belthronding = Weapon("贝尔斯隆丁", "贝烈格·库沙理安所使用的弓", 5, 176, 76)
dramborleg = Weapon("德拉姆博烈格", "锋利的重击", 6, 160, 78)
scepterOfAnnuminas = Weapon("安努米那斯的权杖", "由阿尔诺诸王持有", 6, 232, 96)

# 精英级独特盔甲
helmOfHador = Armor("哈多头盔", "哈多家族的族长所佩戴的头盔", 5, 140, 12)
harlequinCrestShako = Armor("谐角之冠军帽", "来自暗黑破坏神中的崔斯特瑞姆", 6, 162, 10)
templarsMight = Armor("神圣盔甲", "来自暗黑破坏神中的崔斯特瑞姆", 6, 152, 12)
tyraelsMight = Armor("泰瑞尔的力量", "来自暗黑破坏神中的崔斯特瑞姆", 6, 170, 14)

# 精英级独特宝物
aeglos = Weapon("艾格洛斯", "埃睿尼安·吉尔-加拉德所挥舞的长矛", 6, 220, 152)
ananruth = Weapon("阿兰如斯", "辛达语：王者之怒", 5, 242, 146)
ringil = Weapon("凛吉尔", "冰冷的火花", 8, 248, 156)
grond = Weapon("格龙得", "黑暗魔君魔苟斯所使用的巨锤", 30, 653, 340)
crownOfElendil = Armor("埃兰迪尔王冠", "刚铎国王所佩戴的辉煌王冠", 6, 220, 16)
ironCrown = Armor("铁王冠", "魔苟斯为自己铸造的王冠，其上镶嵌着三颗精灵宝钻", 10, 316, 22)

lowLevelFindableUniques = [guthwine, herugrim, orchrist, tarhelmCrown, snowclash, razortail, nightsmoke, peasantCrown,
                           crownOfThieves]

highLevelFindableUniques = [glamdring, anglachel, angrist, anguirel, belthronding, dramborleg, scepterOfAnnuminas,
                            helmOfHador, harlequinCrestShako, templarsMight, tyraelsMight]

eliteLevelFindableUniques = [aeglos, ananruth, ringil, grond, crownOfElendil, ironCrown]
