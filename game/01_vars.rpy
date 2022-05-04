define mc = Character("[mcname]", color="#FF0000")
define silv = Character("Silvia", color="af96a0")
define este = Character("Estelle", color="a79ba6")
define laur = Character("Laureate", color="f2d6ab")
define mv = Character("???", color="8dc0f2")
define azul = Character("Azula", color="8dc0f2")
define sere = Character("Serena", color="e09b57")
define ferr = Character("Ferry", color="336fca")
define alti = Character("Altina", color="fbe2dc")
define vier = Character("Viera", color="cc8c77")
define rita = Character("Rita", color="8c1034")
define kana = Character("Kanae", color="a26951")
define mako = Character("Makoto", color="c66551")
define cele = Character("Celestia", color="f7c7b4")
define viol = Character("Violetta", color="7c7aa6")
define magi = Character("Magilou", color="cbccda")

define tori = Character("Tori", color="d7868b")
define hana = Character("Hannah", color="ee822a")
define adel = Character("Adeline", color="c17cca")



define mvalti = Character("Pink Girl", color="ff7a99")
define mvvier = Character("Flat Girl", color="a16738")
define mvlaur = Character("Blonde-haired Girl", color="f2d6ab")
define mvcula = Character("Flower Girl", color="FFFFFF")

define mvmako = Character("Hammer Bro", color="c66551")
define mvtori = Character("Cheerful Girl", color="d7868b")
define mvhana = Character("Orange-haired Girl", color="ee822a")
define mvmizu = Character("Girl With Glasses", color="d2ab98")
define mvadel = Character("Mystery Maid", color="c17cca")
define mvcele = Character("Shady Fox Girl", color="f7c7b4")

define mv2 = Character("???", color="FFFFFF")
define pand = Character("Pandoria", color="FFFF00")
define aspi = Character("Aspio", color="FF8C00")
define gen1 = Character("Random Girl #1", color="FFFFFF")
define gen2 = Character("Random Girl #2", color="00ff00")
define gen3 = Character("Older Woman", color="FFFFFF")
define gen4 = Character("Nurse", color="FFFFFF")
define gen5 = Character("Overly-hype Fangirl", color="FFFF00")
define kid1 = Character("Random Child #1", color="FFFFFF")
define kid2 = Character("Random Child #2", color="FFFFFF")
define kid3 = Character("Red-haired Girl", color="FF3333")
define gen6 = Character("Well-dressed Man", color="FFFFFF")
define gen7 = Character("Random Guy #1", color="FFFFFF")
define gen10 = Character("Random Guy #2", color="C0C0C0")
define gen8 = Character("Tom", color="cc92fB")
define gen9 = Character("Bosco", color="9addfb")
define gen11 = Character("*Poor Voice Imitation*", color="FF0000")

define anno = Character("Announcer", color="FFFF00")
define magif = Character("Father", color="edb8bd")
define magiy = Character("Young Magilou", color="ADD8E6")
define magic = Character("Colette Mordio", color="FFFFFF")

define bl = "{color=#000}"
define red = "{color=#8C001A}"
define yel = "{color=#FFFF00}"
define font = "{font=gabriola.ttf}{size=70}"
define gre = "{color=#008000}"
define blu = "{color=#0000ff}"
define pur = "{color=#9932CC}"
define oj = "{color=#FFA500}"

style questfont is text:
    size 40
    font "footlight-mt-light.ttf"
    xalign 0.5
    yoffset 30
    color "#FFF" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ]

style flowerrates is text:
    font "footlight-mt-light.ttf"
    xalign 0.5
    yoffset 30
    color "#FFF" outlines [ (absolute(2), "#000", absolute(0), absolute(2)) ]

style invfont is text:
    size 40
    font "footlight-mt-light.ttf"
    xalign 0.5
    yoffset 30
    color "#000" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ]




























































default silvaff = 1
default esteaff = 0
default azulaff = 0
default sereaff = 1
default lauraff = 0
default ferraff = 0
default altiaff = 0
default vieraff = 0
default ritaaff = 0
default kanaaff = 0
default makoaff = 0
default celeaff = 0
default magiaff = 0
default violaff = 0

default culaaff = 0

define currentday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
define currentday02 = 0
default weekday = False
default endgame = False
default timeofday = 1
default daycounter = 1
default money = 10
default questcounter = 0
default outside = False
default voytime = False

default dayinweek = currentday[currentday02]

default location = ""
default indining = False
default inliving = False

default mainquest = 0
default sidequest = 0
default disabled = True

default azulmet = False
default seremet = False
default laurmet = False
default ferrmet = False
default altimet = False
default viermet = False
default ritamet = False
default kanamet = False
default makomet = False
default celemet = False
default magimet = False
default violmet = False

default adelmet = False
default culamet = False

default silvbought = False
default estebought = False
default azulbought = False
default serebought = False
default laurbought = False
default ferrbought = False
default altibought = False
default vierbought = False
default ritabought = False
default kanabought = False
default makobought = False
default celebought = False
default magibought = False
default violbought = False

default culabought = False

default silv_is_dead = True
default este_is_dead = True
default azul_is_dead = False
default sere_is_dead = False
default laur_is_dead = False
default ferr_is_dead = False
default alti_is_dead = False
default vier_is_dead = False
default rita_is_dead = False
default kana_is_dead = False
default mako_is_dead = False
default cele_is_dead = False
default magi_is_dead = False
default viol_is_dead = False

default cula_is_dead = False
default adel_is_dead = False

default silvevents = 0
default esteevents = 0
default azulevents = 0
default sereevents = 0
default laurevents = 0
default ferrevents = 0
default altievents = 0
default vierevents = 0
default ritaevents = 0
default kanaevents = 0
default makoevents = 0
default celeevents = 0
default magievents = 0
default violevents = 0

default culaevents = 0

default sideevents = 0
default sidequesttrigger = False

default silvquest = False
default estequest = False
default azulquest = False
default serequest = False
default laurquest = False
default makoquest = False
default ferrquest = False
default celequest = False

default silvwork = False
default estework = False
default azulwork = False
default serework = False
default laurwork = False
default ferrwork = False
default altiwork = False
default vierwork = False
default ritawork = False
default kanawork = False
default makowork = False
default celework = False
default magiwork = False
default violwork = False

default culawork = False

default silvtime = False
default estetime = False
default azultime = False
default seretime = False
default laurtime = False
default ferrtime = False
default altitime = False
default viertime = False
default ritatime = False
default kanatime = False
default makotime = False
default celetime = False
default magitime = False
default violtime = False

default culatime = False

default menuset = set()


default givegift = False
default flowers_tutorial = False
default flowergirlmet = False

default parfait_tutorial = False

default flowers_r = 0
default flowers_sr = 0
default flowers_ssr = 0
default flowers_ssg = 0

default park01_flower_01 = True
default park01_flower_02 = True
default park01_flower_03 = True

default park02_flower_01 = True
default park02_flower_02 = True
default park02_flower_03 = True

default park03_flower_01 = True
default park03_flower_02 = True
default park03_flower_03 = True

default inventory_tutorial = False
default inventory_book = 0
default inventory_magicflower = 0
default inventory_parfait = 0
default inventory_plushie = 0



default missions_tutorial = False

default missions_cap = 0
default missions_randomize = 0
default missions_babysitter = ""
default missions_housekeeper = ""
default missions_pizzagirl = ""
default missions_salesman = ""
default missions_bodyguard = ""
default missions_icecreamgirl = ""
default missions_model = ""

default missions_babysitter_enabled = False
default missions_housekeeper_enabled = False
default missions_pizzagirl_enabled = False
default missions_salesman_enabled = False
default missions_bodyguard_enabled = False
default missions_icecreamgirl_enabled = False
default missions_model_enabled = False

default missions_babysitter_price = 0
default missions_housekeeper_price = 0
default missions_pizzagirl_price = 0
default missions_salesman_price = 0
default missions_bodyguard_price = 0
default missions_icecreamgirl_price = 0
default missions_model_price = 0



default dating_mood_pts = 0



default waifutaxtotal = 0



default fortune_cap = 0
default fortune_luck = 0
default fortune_pot = 10000
default goldenticket = False
default goldenticketevents = 0

default celetreasure = 0
default junkinventory = 0
default junk_street01 = False
default junk_street03 = False
default junk_street04 = False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
