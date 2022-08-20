#!/usr/bin/python

from monsters.barrow_wight import BarrowWight
from monsters.goblin import Goblin
from monsters.great_goblin import GreatGoblin
from monsters.king_of_the_barrows import KingOfTheBarrows
from monsters.nazgul import Nazgul
from monsters.nazgul_ii import Nazgul_II
from monsters.nazgul_iii import Nazgul_III
from monsters.troll import Troll
from monsters.warg_rider import WargRider
from monsters.uruk_hai import UrukHai
from monsters.uruk_hai_archer import UrukHaiArcher
from monsters.elite_uruk_hai import EliteUrukHai
from monsters.dunlending import Dunlending
from monsters.orc import Orc
from monsters.orc_archer import OrcArcher
from monsters.siege_works import SiegeWorks
from monsters.dragon_of_mordor import DragonOfMordor
from monsters.corsair_of_umbar import CorsairOfUmbar
from monsters.armored_mumakil import ArmoredMumakil
from monsters.black_numernorian import BlackNumernorian
from monsters.easterling_warrior import EasterlingWarrior
from monsters.sauroman import Sauroman
from monsters.mouth_of_sauron import MouthOfSauron
from monsters.witch_king import WitchKing
from monsters.shelob import Shelob
from monsters.balrog import Balrog
from monsters.orc_ii import Orc_II
from monsters.orc_archer_ii import OrcArcher_II
from monsters.troll_ii import Troll_II
from monsters.black_numernorian_ii import BlackNumernorian_II

"""
指环王中使用的常量。
"""
#游戏常量
COMMAND_PROMPT           = "> "
CURRENCY                 = "rubles"
SPACES_WITH_UNIQUE_ITEMS = 4
ELVEN_RING_PROB          = .3

#Player initialization
class PlayerInitialization(object):
    """
    Constants used in player initialization.
    """
    EXPERIENCE    = 0
    LEVEL         = 1
    MONEY         = 20
    MAX_HP        = 20
    ATTACK        = 5
    WEIGHT_LIMIT  = 15
    WEAPON_ATTACK = 0
    ARMOR_DEFENSE = 0
    CHARM_ATTACK  = 0
    CHARM_DEFENSE = 0
    CHARM_HP      = 0

#Character stats constants
HP_STAT           = 1.2
ATTACK_STAT       = 1.2
MAX_LEVEL         = 20
WEIGHT_LIMIT_STAT = 1.15

#Player levels
"""
Keys are player levels; values are the experience required to obtain its paired
level.
"""
LEVEL_EXP_REQUIREMENT = {1: 0, 2: 20, 3: 44, 4: 72, 5: 105, 6: 144, 7: 190, 
8: 245, 9: 311, 10: 390, 11: 484, 12: 596, 13: 730, 14:890 , 15: 1082, 
16: 1312, 17: 1588, 18: 1919, 19: 2316, 20: 2792}

#Item stat constants 
SELL_LOSS_PERCENTAGE = .5
WEAPON_COST          = 1
ARMOR_COST           = 2

#物品类型的列举
class ItemType(object):
    """
    物品类型。
    """
    GENERIC = 1 # 通用
    ARMOR   = 2 # 盔甲
    WEAPON  = 3 # 武器
    POTION  = 4 # 药水
    CHARM   = 5 # 饰品

#方向枚举
class Direction(object):
    """
    主要方向。
    """
    NORTH = 'north'
    SOUTH = 'south'
    EAST  = 'east'
    WEST  = 'west'

#地区类型的列举
class RegionType(object):
    """
    中土世界的地区类型。
    """
    ERIADOR       = 1 # 伊利雅德
    BARROW_DOWNS  = 2 # 古冢岗
    HIGH_PASS     = 3 # 高隘口
    ENEDWAITH     = 4 # 伊宁威治
    MORIA         = 5 # 墨瑞亚
    RHOVANION     = 6 # 罗马尼安
    ROHAN         = 7 # 洛汗
    GONDOR        = 8 # 刚铎
    MORDOR        = 8 # 魔多

#Region base spawn
class RegionBaseSpawn(object):
    """
    Regional base spawn per random battle for space in region.
    """
    ERIADOR       = 1
    BARROW_DOWNS  = 4
    HIGH_PASS     = 0
    ENEDWAITH     = 6
    MORIA         = 5
    RHOVANION     = 6
    ROHAN         = 6
    GONDOR        = 8
    MORDOR        = 8

#在地区中时发生随机战斗的概率
class SpaceSpawnProb(object):
    """用于存储地区发生随机战斗的概率。"""
    shire               = 0     # 夏尔
    oldForest           = .7    # 老林子
    weatherHills        = .75   # 风云丘陵
    trollshaws          = .85   # 食人妖森林
    mistyMountainsNorth = .85   # 迷雾山脉北部
    highPass            = 0     # 高隘口
    mirkwood            = .4    # 幽暗密林
    southernMirkwood    = .9    # 幽暗密林南部
    barrowDowns         = .85   # 古冢岗
    bruinen             = .75   # 布茹伊能河
    mitheithel          = .75   # 苍泉河
    swanfleet           = .75   # 天鹅泽
    dunland             = .85   # 黑蛮地
    mistyMountainsSouth = 0     # 迷雾山脉南部
    lorien              = .4    # 罗瑞恩
    fangorn             = .4    # 范贡森林
    theWold             = .4
    fieldOfCelebrant    = .25
    calenardhon         = .95
    westfold            = .85
    westemnet           = .8
    eastemnet           = .6
    emynMuil            = .4
    eastfold            = .5
    nindalf             = .8
    deadMarshes         = .5
    udun                = .95
    cairAndros          = .8
    orodruin            = .95   # 欧洛都因（末日火山）
    anorien             = .75
    anduin              = .85
    ephelDuath          = .9
    cirithUngol         = .9
    plateauOfGorgoth    = .95
    lossamarch          = .6
    ithilien            = .85

#地区的奖励难度
class SpaceBonusDiff(object):
    """用于存储地区的奖励难度。"""
    shire               = 0     # 夏尔
    oldForest           = 0     # 老林子
    weatherHills        = 0     # 风云丘陵
    trollshaws          = .2    # 食人妖森林
    mistyMountainsNorth = 0     # 迷雾山脉北部
    highPass            = 0     # 高隘口
    mirkwood            = 0     # 幽暗密林
    southernMirkwood    = .2    # 幽暗密林南部
    barrowDowns         = 0     # 古冢岗
    bruinen             = 0     # 布茹伊能河
    mitheithel          = .2    # 苍泉河
    swanfleet           = .2    # 天鹅泽
    dunland             = 0     # 黑蛮地
    mistyMountainsSouth = 0     # 迷雾山脉南部
    lorien              = 0     # 罗瑞恩
    fangorn             = 0     # 范贡森林
    theWold             = -.3
    fieldOfCelebrant    = -.3
    calenardhon         = .5
    westfold            = .3
    westemnet           = .15
    eastemnet           = 0
    emynMuil            = -.2
    eastfold            = 0
    nindalf             = -.2
    deadMarshes         = .2
    udun                = .3
    cairAndros          = .2
    orodruin            = .3    # 欧洛都因（末日火山）
    anorien             = .3
    anduin              = 0
    ephelDuath          = .2
    cirithUngol         = .2
    plateauOfGorgoth    = .2
    lossamarch          = 0
    ithilien            = .2

#怪物名称
class MonsterNames(object):
    """包含指环王中怪物的名称。"""
    BarrowWight         = "古冢尸妖"
    Goblin              = "半兽人"
    GreatGoblin         = "巨型半兽人"
    KingOfTheBarrows    = "尸妖王"
    Nazgul              = "戒灵"
    Nazgul_II           = "戒灵II"
    Nazgul_III          = "戒灵III"
    Troll               = "食人妖"
    WargRider           = "座狼骑手"
    UrukHai             = "乌鲁克族"
    UrukHaiArcher       = "乌鲁克族弓手"
    EliteUrukHai        = "乌鲁克族精英"
    Dunlending          = "黑蛮地人"
    Orc                 = "奥克"
    OrcArcher           = "奥克弓手"
    SiegeWorks          = "围城工事"
    DragonOfMordor      = "魔多龙"
    CorsairOfUmbar      = "昂巴海盗"
    ArmoredMumakil      = "披甲毛象"
    BlackNumernorian    = "黑努曼诺尔人"
    EasterlingWarrior   = "伊斯特林战士"
    Sauroman            = "反叛的萨鲁曼"
    MouthOfSauron       = "索隆之口"
    WitchKing           = "安格玛巫王"
    Shelob              = "尸罗"
    Balrog              = "炎魔"
    Orc_II              = "奥克II"
    OrcArcher_II        = "奥克弓手II"
    Troll_II            = "食人妖II"
    BlackNumernorian_II = "黑努曼诺尔人II"
    
#怪物的描述
class MonsterDescriptions(object):
    """包含指环王中怪物的描述。"""
    BarrowWight         = "一个悲伤的灵魂萦绕在此。"
    Goblin              = "\"把你所有的东西都给我！\""
    GreatGoblin         = "\"把你所有的东西都给我！！！\""
    KingOfTheBarrows    = "一个极强的恶灵。"
    Nazgul              = "\"AAAAEEEEEEEEEEE!!!\""
    Nazgul_II           = "戒灵之长。"
    Nazgul_III          = "现在有了龙坐骑！"
    Troll               = "\"我快活地走着。\""
    WargRider           = "喜欢骑…座狼。"
    UrukHai             = "\"你提起过兄弟我？\""
    UrukHaiArcher       = "拥有远程攻击的能力。"
    EliteUrukHai        = "卧推冠军。"
    Dunlending          = "中洲的原住民。。"
    Orc                 = "不大好。"
    OrcArcher           = "一个十足的混蛋。"
    SiegeWorks          = "在这种情况下完全没用。"
    DragonOfMordor      = "恶龙的远亲。"
    CorsairOfUmbar      = "基本上就是海盗。"
    ArmoredMumakil      = "载有弓箭手的装甲大象。"
    BlackNumernorian    = "极为强大的巫师。"
    EasterlingWarrior   = "来自中国。"
    Sauroman            = "白道会的首领。"
    MouthOfSauron       = "索隆的副手与特使。"
    WitchKing           = "索隆手下最恐怖的奴仆。"
    Shelob              = "乌苟立安特的最后一个子嗣。"
    Balrog              = "都林的祸根。"
    Orc_II              = "奥克之长。"
    OrcArcher_II        = "奥克弓手之长。"
    Troll_II            = "食人妖之长。"
    BlackNumernorian_II = "黑努曼诺尔人之长。"
    
#Monster attack strings
class MonsterAttackStrings(object):
    """
    Contains the attack strings of the monsters in LotR. For instance,
    "Goblin *sliced and diced* %s for %s damage!"
    """
    BarrowWight         = "sang a sad song"
    Goblin              = "slice and diced"
    GreatGoblin         = "slice and diced"
    KingOfTheBarrows    = "sang a symphony of sadness"
    Nazgul              = "slashed you with a Morgul knife"
    Nazgul_II           = "slashed you with Scythe of Sorrow"
    Nazgul_III          = "fire-breathing dragoned you"
    Troll               = "slamed you with fists of malice"
    WargRider           = "trampled around"
    UrukHai             = "tried to out lift you"
    UrukHaiArcher       = "tried to out lift you"
    EliteUrukHai        = "tried to out lift you"
    Dunlending          = "hacked and slashed"
    Orc                 = "hacked"
    OrcArcher           = "shot fiery darts"
    SiegeWorks          = "did nothing"
    DragonOfMordor      = "used hyperbeam"
    CorsairOfUmbar      = "slashed"
    ArmoredMumakil      = "got pissed and started trampling around"
    BlackNumernorian    = "summon spiritual darkness"
    EasterlingWarrior   = "tried to avenge his ancestors"
    Sauroman            = "cast elemental spells"
    MouthOfSauron       = "slashed you with an enchanted blade"
    WitchKing           = "performed black magic"
    Shelob              = "stung you"
    Balrog              = "scourged you with whips of fire"
    Orc_II              = "hacked"
    OrcArcher_II        = "shot fiery darts"
    Troll_II            = "slamed you with fists of malice"
    BlackNumernorian_II = "summon spiritual darkness"
    
class MonsterDeathStrings(object):
    """
    Contains the death strings of the monsters in LotR. These strings
    are displayed as player kills monster.
    """
    BarrowWight         = "\"Good. I am going back to sleep now.\""
    Goblin              = "\"I'm going back home now.\""
    GreatGoblin         = "\"I'm going back home now too.\""
    KingOfTheBarrows    = "\"I am going back to sleep now.\""
    Nazgul              = "\"AAAAEEEEEEEEEEE!!!\""
    Nazgul_II           = "\"...AAAAEEEEEEEEEEE!!!\""
    Nazgul_III          = "\"....\""
    Troll               = "\"Merrily I troll away.\""
    WargRider           = "[Whimpers] ...My warg...."
    UrukHai             = "Well, back to the gym I guess...."
    UrukHaiArcher       = "Leg lifts and suicides here I come...."
    EliteUrukHai        = "[Walks back to the locker room depressed.]"
    Dunlending          = "\"Why the heck am I even here?\""
    Orc                 = "Orc was cut in two!"
    OrcArcher           = "Orcish Archer was slain!"
    SiegeWorks          = "...."
    DragonOfMordor      = "Dragon of Mordor was knocked out!"
    CorsairOfUmbar      = "Corsair of Umbar went back home."
    ArmoredMumakil      = "Armored Mumakil is going home to Africa now."
    BlackNumernorian    = "[Black Numernorian returned to the shadows.]"
    EasterlingWarrior   = "Easterling Warrior went back to China."
    Sauroman            = "\"Wizards reincarnate you know....\""
    MouthOfSauron       = "\"Rides off to fight another day.\""
    WitchKing           = "\"Hmm....\""
    Shelob              = "[Shelob retreats into the shadows.]"
    Balrog              = "[The Balrog retreats into the shadows.']"
    Orc_II              = "Orc was cut in two!"
    OrcArcher_II        = "Orcish Archer was slain!"
    Troll_II            = "\"Merrily I troll away.\""
    BlackNumernorian_II = "[Black Numernorian returned to the shadows.]"
    
#Region monster distribution
"""
A dictionary of dictionaries where the higher-level keys are regions. 
The inner set contains the monster class-probability pairs that are 
used as probability distribution functions for monster spawn.

monster_factory's getMonsters() generates a random number between [0, 1). If 
the randomly generated number falls within the range of each class, a monster 
of that class is spawned.
"""
REGIONAL_MONSTER_DISTRIBUTION = {
    RegionType.ERIADOR:      {Nazgul: [0, 1]},
    RegionType.BARROW_DOWNS: {BarrowWight: [0, .9], 
                              KingOfTheBarrows: [.9, 1]},
    RegionType.HIGH_PASS:    {Goblin: [0, 1]},
    RegionType.ENEDWAITH:    {WargRider: [0, .3], 
                              Dunlending: [.3, .6], 
                              UrukHai: [.6, .8], 
                              UrukHaiArcher: [.8, .9], 
                              EliteUrukHai: [.9, 1]},
     RegionType.MORIA:       {Orc: [0, .7], 
                              OrcArcher: [.7, .925], 
                              Troll: [.925, .98], 
                              Balrog: [.98, 1]},
     RegionType.RHOVANION:   {Orc: [0, .5], 
                              OrcArcher: [.5, .7], 
                              Nazgul_II: [.7, .85], 
                              BlackNumernorian: [.85, 1]},
     RegionType.ROHAN:       {UrukHai: [0, .5], 
                              UrukHaiArcher: [.5, .7], 
                              EliteUrukHai: [.7, .8], 
                              WargRider: [.8, 1]},
     RegionType.GONDOR:      {Orc: [0, .45], 
                              OrcArcher: [.45, .6],
                              EasterlingWarrior: [.6, .65],
                              Troll: [.65, .75], 
                              Nazgul_II: [.75, .785], 
                              DragonOfMordor: [.785, .8], 
                              CorsairOfUmbar: [.8, .85], 
                              ArmoredMumakil: [.85, .9], 
                              SiegeWorks: [.9, .95], 
                              BlackNumernorian: [.95, 1]},
     RegionType.MORDOR:      {Orc_II: [0, .5], 
                              OrcArcher_II: [.5, .7], 
                              Troll_II: [.7, .8], 
                              Nazgul_III: [.8, .85], 
                              DragonOfMordor: [.85, .875], 
                              BlackNumernorian_II: [.875, .95], 
                              SiegeWorks: [.95, 1]}
     }

#怪物基础数据
"""
怪物基础数据是创建怪物时使用的唯一参数。
基础数据是一个有3个元素列表，分别表示：hp、攻击力和经验（按此顺序）。
"""
MONSTER_STATS = {BarrowWight:          [18, 2, 6],
                 Goblin:               [28, 5, 12],
                 GreatGoblin:          [72, 8, 42],
                 KingOfTheBarrows:     [72, 4, 32],
                 Nazgul:               [44, 3, 12],
                 Nazgul_II:            [82, 10, 52],
                 Nazgul_III:           [240, 48, 120],
                 Troll:                [86, 8, 36],
                 WargRider:            [32, 5, 14],
                 UrukHai:              [54, 5, 18],
                 UrukHaiArcher:        [32, 6, 16],
                 EliteUrukHai:         [72, 8, 28],
                 Dunlending:           [26, 5, 12],
                 Orc:                  [26, 5, 12],
                 OrcArcher:            [22, 7, 16],
                 SiegeWorks:           [220, 0, 52],
                 DragonOfMordor:       [300, 67, 176],
                 CorsairOfUmbar:       [76, 12, 48],
                 ArmoredMumakil:       [264, 42, 96],
                 BlackNumernorian:     [66, 12, 48],
                 EasterlingWarrior:    [74, 8, 30],
                 Sauroman:             [342, 52, 170],
                 MouthOfSauron:        [480, 72, 250],
                 WitchKing:            [600, 84, 320],
                 Shelob:               [450, 70, 140],
                 Balrog:               [1840, 162, 860],
                 Orc_II:               [72, 10, 35],
                 OrcArcher_II:         [66, 12, 40],
                 Troll_II:             [166, 16, 80],
                 BlackNumernorian_II:  [152, 24, 92]}
    
#Battle engine context
class BattleEngineContext(object):
    """
    Constants used for BattleEngine mode determination.
    """
    RANDOM = 1
    STORY  = 2

#Battle engine     
class ItemFind(object):
    """
    Constants used for determining whether player has found items as a result 
    of battle.
    """
    lowLevel   = [100, 5000, 300]
    highLevel  = [350, 5000, 600]
    eliteLevel = [500, 5000, 1000]
    
#Battle engine constants
class BattleEngine(object):
    """
    Constants for battle engine.
    """
    RUN_PROBABILITY_SUCCESS = 1
    STANDARD_DEVIATION      = 3
    MONEY_CONSTANT          = 3

#商店的生成概率常数
class ShopFactoryConstants(object):
    """
    商店物品类型生成中使用的常量。
    """
    WEAPON_UPPER_LIMIT = .25 # 商店刷武器的概率 25%
    ARMOR_UPPER_LIMIT  = .5 # 商店刷盔甲的概率 25%
    POTION_UPPER_LIMIT = .975 # 商店刷药水的概率 47.5%
    STANDARD_DEVIATION = 2.5 # 商品品质分布的标准差
    QUALITY_MINIMUM    = 0 # 商品品质的最低值
    QUALITY_MAXIMUM    = 20 # 商品品质的最高值
    UNIQUE_QUALITY_REQ = 10 # 会生成高于该品质物品的商店才会生成低级独特物品

#Unique Place constants
"""
Constants used for unique places.
"""
WEATHERTOP_BATTLE_PROB = .5
WEATHERTOP_WITCH_KING_PROB = .125
THARBAD_BATTLE_PROB = .2
THARBAD_ITEM_FIND_PROB = .5
ARGONATH_EXP_INCREASE = .1
DERINGLE_EXP_INCREASE = .05
GOBLIN_TOWN_EVASION_PROB = .4
DOL_GULDUR_WITCH_KING_PROB = .125
CIRITH_UNGOL_EVASION_PROB = .4
CIRITH_UNGOL_SHELOB_PROB = .4
MORIA_ITEM_FIND_PROB = .3
MORIA_LOW_RISK_UPPER_LIMIT = 1
MORIA_MED_RISK_UPPER_LIMIT = 3
MORIA_LOW_RISK_SNEAK_UPPER_LIMIT = .65
MORIA_LOW_RISK_NEUTRAL_UPPER_LIMIT = .9
MORIA_MED_RISK_SNEAK_UPPER_LIMIT = .3
MORIA_MED_RISK_NEUTRAL_UPPER_LIMIT = .7
MORIA_HIGH_RISK_NEUTRAL_UPPER_LIMIT = .2