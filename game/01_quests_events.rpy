label charquest:


    if (silvaff == 5 and silvevents == 0 and silvquest == False):
        $ silvquest = True
        play sound "audio/coins.mp3" volume 3
        show love_silv at up_happy_02
        "[oj]Silvia wants to speak with you!\nCheck your {b}Quest Log!"
    if (silvaff == 10 and silvevents == 3 and silvquest == False):
        $ silvquest = True
        play sound "audio/coins.mp3" volume 3
        show love_silv at up_happy_02
        "[oj]Silvia wants to speak with you!\nCheck your {b}Quest Log!"


    if (esteaff == 4 and esteevents == 0 and estequest == False):
        $ estequest = True
        play sound "audio/coins.mp3" volume 3
        show love_este at up_happy_02
        "[oj]Estelle wants to speak with you!\nCheck your {b}Quest Log!"
    if (esteaff == 8 and esteevents == 3 and estequest == False):
        $ estequest = True
        play sound "audio/coins.mp3" volume 3
        show love_este at up_happy_02
        "[oj]Estelle wants to speak with you!\nCheck your {b}Quest Log!"
    if (esteaff == 13 and esteevents == 6 and estequest == False):
        $ estequest = True
        play sound "audio/coins.mp3" volume 3
        show love_este at up_happy_02
        "[oj]Estelle wants to speak with you!\nCheck your {b}Quest Log!"


    if (azulaff == 4 and azulevents == 0 and azulquest == False):
        $ azulquest = True
        play sound "audio/coins.mp3" volume 3
        show love_azul at up_happy_02
        "[oj]Azula wants to speak with you!\nCheck your {b}Quest Log!"
    if (azulaff == 9 and azulevents == 2 and azulquest == False):
        $ azulquest = True
        play sound "audio/coins.mp3" volume 3
        show love_azul at up_happy_02
        "[oj]Azula wants to speak with you!\nCheck your {b}Quest Log!"


    if (sereaff == 5 and sereevents == 0 and serequest == False):
        $ serequest = True
        play sound "audio/coins.mp3" volume 3
        show love_sere at up_happy_02
        "[oj]Serena wants to speak with you!\nCheck your {b}Quest Log!"
    if (sereaff == 9 and sereevents == 2 and serequest == False):
        $ serequest = True
        play sound "audio/coins.mp3" volume 3
        show love_sere at up_happy_02
        "[oj]Serena wants to speak with you!\nCheck your {b}Quest Log!"
    if (sereaff == 14 and sereevents == 5 and serequest == False):
        $ serequest = True
        play sound "audio/coins.mp3" volume 3
        show love_sere at up_happy_02
        "[oj]Serena wants to speak with you!\nCheck your {b}Quest Log!"
    if (sereaff == 19 and sereevents == 9 and serequest == False):
        $ serequest = True
        play sound "audio/coins.mp3" volume 3
        show love_sere at up_happy_02
        "[oj]Serena wants to speak with you!\nCheck your {b}Quest Log!"


    if (lauraff == 4 and laurevents == 0 and laurquest == False):
        $ laurquest = True
        play sound "audio/coins.mp3" volume 3
        show love_laur at up_happy_02
        "[oj]Laureate wants to speak with you!\nCheck your {b}Quest Log!"


    if (makoaff == 4 and makoevents == 0 and makoquest == False):
        $ makoquest = True
        play sound "audio/coins.mp3" volume 3
        show love_mako at up_happy_02
        "[oj]Makoto wants to speak with you!\nCheck your {b}Quest Log!"
    if (makoaff == 8 and makoevents == 2 and makoquest == False):
        $ makoquest = True
        play sound "audio/coins.mp3" volume 3
        show love_mako at up_happy_02
        "[oj]Makoto wants to speak with you!\nCheck your {b}Quest Log!"


    if (ferraff == 5 and ferrevents == 0 and ferrquest == False):
        $ ferrquest = True
        play sound "audio/coins.mp3" volume 3
        show love_ferr at up_happy_02
        "[oj]Ferry wants to speak with you!\nCheck your {b}Quest Log!"


    if (celeaff == 3 and celeevents == 0 and celequest == False):
        $ celequest = True
        play sound "audio/coins.mp3" volume 3
        show love_cele at up_happy_02
        "[oj]Celestia wants to speak with you!\nCheck your {b}Quest Log!"
    if (celeaff == 6 and celeevents == 5 and celequest == False):
        $ celequest = True
        play sound "audio/coins.mp3" volume 3
        show love_cele at up_happy_02
        "[oj]Celestia wants to speak with you!\nCheck your {b}Quest Log!"

    return

label charevents:


    if (celemet):
        $ fortune_luck += 0.05
        if (fortune_pot <= 30000):
            $ fortune_pot += renpy.random.randint(1,3)


    if (location == "livingroom" and mainquest == 1):
        $ mainquest += 1
        jump prologue_03
    if (location == "bathroom" and mainquest == 0):
        $ mainquest += 1
        jump prologue_02
    if (location == "silvroom" and mainquest == 2):
        $ mainquest += 1
        jump prologue_04
    if (location == "silvroom" and mainquest == 3):
        mc "*Gulp*"
        mc "[mil!c] is still changing in there..."
        mc "She said to wait for her in the living room..."
        jump hallwaylabel_01
    if (location == "livingroom" and mainquest == 3):
        $ mainquest += 1
        $ timeofday += 1
        jump prologue_05
    if (location == "street_01" and mainquest < 4):
        "I can't leave the house yet. There are things that I still need to do."
        jump livingroomlabel
    if (location == "street_01" and mainquest == 4):
        $ mainquest += 1
        jump prologue_06
    if (location == "park_01" and mainquest == 5):
        $ mainquest += 1
        jump prologue_07
    if (location == "park_04" and mainquest == 6):
        $ mainquest += 1
        jump prologue_08
    if (location == "street_01" and mainquest == 7):
        $ mainquest += 1
        jump prologue_09
    if (location == "cityhall_01" and mainquest == 8):
        $ mainquest += 1
        jump prologue_10
    if (location == "livingroom" and mainquest == 9 and azulevents == 4 and sidequest >= 5 and timeofday < 5 and estebought):
        $ mainquest += 1
        $ timeofday += 1
        $ makomet = True
        jump mainquest_10
    if ((location == "cityhall_01_laurtv" or location == "cityhall_02_laurphone") and mainquest == 10):
        $ mainquest += 1
        jump mainquest_11
    if ((location == "buildersguild_makotired" or location == "buildersguild_makosword") and mainquest == 11):
        $ mainquest += 1
        jump mainquest_12

    if ((location == "cityhall_01" or location == "cityhall_02") and mainquest == 13 and makoevents >= 6 and (timeofday == 3 or timeofday == 4)):
        $ mainquest += 1
        $ timeofday = 5
        jump mainquest_14



    if (cula_is_dead == False):
        if (location == "street_02_cula" and mainquest >= 9 and (timeofday == 3 or timeofday == 4) and flowergirlmet == False):
            $ flowergirlmet = True
            jump cula00


    if (silv_is_dead == False):
        if (location == "livingroom" and silvaff == 5 and silvevents == 0 and timeofday == 3 and silvquest == True):
            $ silvevents += 1
            jump silv01_01
        if (location == "street_02_cula" and silvaff == 5 and silvevents == 1 and (timeofday == 3 or timeofday == 4) and silvquest == True):
            $ silvevents += 1
            jump silv01_02
        if (location == "silvroom" and silvaff == 5 and silvevents == 2 and timeofday == 3 and silvquest == True and inventory_magicflower > 0):
            $ silvquest = False
            $ silvevents += 1
            $ sidequest += 1
            $ timeofday += 1
            $ inventory_magicflower -= 1
            jump silv01_03

        if (location == "livingroom" and silvaff == 10 and silvevents == 3 and timeofday == 3 and silvquest == True):
            $ silvevents += 1
            $ timeofday += 1
            jump silv02_01
        if (location == "livingroom" and silvaff == 10 and silvevents == 4 and timeofday == 0 and silvquest == True):
            $ silvquest = False
            $ silvevents += 1
            $ sidequest += 1
            $ timeofday += 1
            jump silv02_02



    if (este_is_dead == False):
        if (location == "mcroom" and esteaff == 4 and esteevents == 0 and timeofday == 3 and estequest == True and sere_is_dead == False):
            $ esteevents += 1
            jump este01_01
        if (location == "livingroom" and esteaff == 4 and esteevents == 1 and timeofday == 3 and estequest == True):
            $ esteevents += 1
            jump este01_02
        if (location == "park_03" and esteaff == 4 and esteevents == 2 and timeofday == 3 and estequest == True):
            $ estequest = False
            $ esteevents += 1
            $ sidequest += 1
            $ timeofday += 1
            jump este01_03
        if (location == "livingroom" and esteaff == 8 and esteevents == 3 and timeofday == 3 and estequest == True):
            $ esteevents += 1
            jump este02_01
        if (location == "street_01_sere" and esteaff == 8 and esteevents == 4 and estequest == True):
            $ esteevents += 1
            jump este02_02
        if (location == "esteroom" and esteaff == 8 and esteevents == 5 and timeofday == 2 and estequest == True):
            $ estequest = False
            $ esteevents += 1
            $ sidequest += 1
            $ timeofday += 1
            jump este02_03

        if (location == "livingroom" and esteaff == 13 and esteevents == 6 and timeofday == 0 and estequest == True):
            $ esteevents += 1
            jump este03_01
        if (location == "cityhall_01" and esteaff == 13 and esteevents == 7 and timeofday == 0 and estequest == True):
            $ esteevents += 1
            $ timeofday += 1
            jump este03_02
        if (location == "mcroom" and esteaff == 13 and esteevents == 8 and timeofday == 1 and estequest == True):
            $ estequest = False
            $ esteevents += 1
            $ sidequest += 1
            $ timeofday = 4
            jump este03_03


    if (azul_is_dead == False):
        if (location == "livingroom" and azulaff == 4 and azulevents == 0 and timeofday == 0 and azulquest == True):
            $ azulevents += 1
            jump azul01_01
        if (location == "park_04" and azulaff == 4 and azulevents == 1 and timeofday == 0 and azulquest == True):
            $ azulquest = False
            $ azulevents += 1
            $ sidequest += 1
            $ timeofday += 2
            jump azul01_02

        if (location == "park_04" and azulaff == 9 and azulevents == 2 and timeofday == 0 and azulquest == True):
            $ azulevents += 1
            $ timeofday += 1
            jump azul01_03
        if (location == "hallway_01" and azulaff == 9 and azulevents == 3 and timeofday == 5 and azulquest == True):
            $ azulquest = False
            $ azulevents += 1
            $ sidequest += 1
            jump azul01_04


    if (sere_is_dead == False):
        if (location == "livingroom" and sereaff == 5 and sereevents == 0 and timeofday == 3 and serequest == True):
            $ sereevents += 1
            jump sere01_01
        if (location == "street_01_sere" and sereaff == 5 and sereevents == 1 and timeofday == 0 and serequest == True):
            $ serequest = False
            $ sereevents += 1
            $ sidequest += 1
            $ timeofday = 4
            jump sere01_02

        if (location == "street_01" and sereaff == 9 and sereevents == 2 and timeofday == 0 and serequest == True):
            $ sereevents += 1
            jump sere02_01
        if (location == "livingroom_silvkitchen" and sereaff == 9 and sereevents == 3 and timeofday == 2 and serequest == True):
            $ sereevents += 1
            jump sere02_02
        if (location == "street_01" and sereaff == 9 and sereevents == 4 and timeofday == 2 and serequest == True):
            $ serequest = False
            $ sereevents += 1
            $ sidequest += 1
            $ timeofday = 4
            $ violmet = True
            jump sere02_03

        if (location == "street_01" and sereaff == 14 and sereevents == 5 and timeofday == 0 and serequest == True):
            $ sereevents += 1
            jump sere03_01
        if (location == "mcroom" and sereaff == 14 and sereevents == 6 and timeofday == 4 and serequest == True):
            $ serequest = False
            $ sereevents += 1
            $ sidequest += 1
            $ timeofday += 1
            jump sere03_02


        if (location == "street_01_sere" and sereaff == 14 and sereevents == 7 and timeofday == 2):
            $ sereevents += 1
            $ timeofday = 4
            jump sere04_01
        if (location == "livingroom" and sereaff == 14 and sereevents == 8 and timeofday == 4):
            $ sereevents += 1
            $ timeofday = 5
            jump sere04_02


        if (location == "livingroom" and sereaff == 19 and sereevents == 9 and timeofday == 0 and weekday and serequest == True):
            $ sereevents += 1
            $ timeofday += 1
            jump sere05_01
        if (location == "street_04" and sereaff == 19 and sereevents == 10 and timeofday == 4 and serequest == True):
            $ serequest = False
            $ sereevents += 1
            $ sidequest += 1
            $ timeofday = 4
            $ celemet = True
            jump sere05_02



    if (laur_is_dead == False):
        if (location == "livingroom" and lauraff == 4 and laurevents == 0 and timeofday == 0 and laurquest):
            $ laurevents += 1
            jump laur01_01
        if (location == "cityhall_01" and lauraff == 4 and laurevents == 1 and timeofday == 5 and laurquest):
            $ laurevents += 1
            jump laur01_02
        if (location == "park_01" and lauraff == 4 and laurevents == 2 and (timeofday == 3 or timeofday == 4) and laurquest):
            $ laurquest = False
            $ laurevents += 1
            $ sidequest += 1
            $ timeofday = 5
            jump laur01_03


    if (mako_is_dead == False):
        if (location == "livingroom" and makoaff == 4 and makoevents == 0 and timeofday == 4 and makoquest):
            $ makoevents += 1
            jump mako01_01
        if (location == "street_01" and makoaff == 4 and makoevents == 1 and timeofday == 3 and makoquest):
            $ makoquest = False
            $ makoevents += 1
            $ sidequest += 1
            jump mako01_02

        if (location == "livingroom" and makoaff == 8 and makoevents == 2 and timeofday == 0 and makoquest):
            $ makoevents += 1
            jump mako02_01
        if (location == "street_01_sere" and makoaff == 8 and makoevents == 3 and makoquest):
            $ makoevents += 1
            $ timeofday += 1
            jump mako02_02
        if (location == "beach_01" and makoaff == 8 and makoevents == 4 and timeofday == 1 and makoquest):
            $ makoevents += 1
            jump mako02_03
        if (location == "beach_03" and makoaff == 8 and makoevents == 5 and timeofday == 1 and makoquest):
            $ makoquest = False
            $ makoevents += 1
            $ sidequest += 1
            $ timeofday += 1
            jump mako02_04


    if (ferr_is_dead == False):
        if (location == "park_02" and ferraff == 5 and ferrevents == 0 and timeofday == 3 and ferrquest):
            $ ferrquest = False
            $ ferrevents += 1
            $ sidequest += 1
            $ timeofday = 5
            jump ferr01_01


    if (cele_is_dead == False):
        if (location == "street_04_cele" and celeaff == 3 and celeevents == 0 and timeofday == 4 and celequest):
            $ celeevents += 1
            $ timeofday = 5
            jump cele01_01
        if (location == "street_04" and celeaff == 3 and celeevents == 3 and timeofday == 5 and celequest):
            $ celeevents += 1
            jump cele01_04
        if (location == "park_04" and celeaff == 3 and celeevents == 4 and timeofday == 5 and celequest):
            $ celequest = False
            $ celeevents += 1
            $ sidequest += 1
            jump cele01_05

        if (location == "street_04" and celeaff == 6 and celeevents == 5 and timeofday == 4 and celequest):
            $ celeevents += 1
            $ timeofday = 5
            jump cele02_01
        if (location == "cityhall_01" and celeaff == 6 and celeevents == 6 and timeofday == 5 and celequest):
            $ celeevents += 1
            jump cele02_02
        if (location == "street_04" and celeaff == 6 and celeevents == 7 and timeofday == 5 and celequest):
            $ celequest = False
            $ celeevents += 1
            $ sidequest += 1
            jump cele02_03



    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
