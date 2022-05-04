label charwork(char):
    if (char == "serena"):
        scene black with dissolve
        show street01_serestore 04 with dissolve
        "[yel]You spent some time with Serena."
        show street01_serestore 09 with dissolve
        if (timeofday == 2):
            $ workroll = renpy.random.randint(100,250) + (sidequest*2)
        elif True:
            $ workroll = renpy.random.randint(75,175) + (sidequest)
        $ money += workroll
        $ serework = True
        play sound "audio/coins.mp3" volume 3
        show love_sere at up_happy
        "[yel]You earned $[workroll]!"
        hide love_sere at up_happy
    if (char == "serena_fulltime"):
        scene black with dissolve
        show street01_serestore 04 with dissolve
        "[yel]You spent some time with Serena."
        show street01_serestore 09 with dissolve
        $ workroll = renpy.random.randint(200,350) + (sidequest*2)
        $ money += workroll
        $ serework = True
        play sound "audio/coins.mp3" volume 3
        show love_sere at up_happy
        "[yel]You earned $[workroll]!"
        hide love_sere at up_happy
    if (char == "serena_overtime"):
        scene black with dissolve
        show street01_serestore 04 with dissolve
        "[yel]You spent some time with Serena."
        show street01_serestore 09 with dissolve
        $ workroll = renpy.random.randint(300,500) + (sidequest*2)
        $ money += workroll
        $ serework = True
        play sound "audio/coins.mp3" volume 3
        show love_sere at up_happy
        "[yel]You earned $[workroll]!"
        hide love_sere at up_happy
    if (char == "laureate_01"):
        scene black with dissolve
        show cityhall01_laurtv 05 with dissolve
        "[yel]You spent some time with Laureate."
        show cityhall01_laurtv 06 with dissolve
        if (laurevents >= 2):
            $ workroll = renpy.random.randint(90,235) + (sidequest)
            $ money += workroll
            play sound "audio/coins.mp3" volume 3
            show love_laur at up_happy
            "[yel]You earned $[workroll]!"
    if (char == "laureate_02"):
        scene black with dissolve
        show cityhall02_laurphone 06 with dissolve
        "[yel]You spent some time with Laureate."
        show cityhall02_laurphone 07 with dissolve
        if (laurevents >= 2):
            $ workroll = renpy.random.randint(90,235) + (sidequest)
            $ money += workroll
            play sound "audio/coins.mp3" volume 3
            show love_laur at up_happy
            "[yel]You earned $[workroll]!"
    if (char == "makoto_01"):
        $ makorand = renpy.random.randint(1,11)
        scene black with dissolve
        if (makorand == 1):
            show buildersguild_makowork 01 with dissolve
            "[yel]You spent some time with Makoto."
            show buildersguild_makowork 02 with dissolve
        if (makorand == 2):
            show buildersguild_makowork 03 with dissolve
            "[yel]You spent some time with Makoto."
            show buildersguild_makowork 04 with dissolve
        if (makorand == 3):
            show buildersguild_makowork 05 with dissolve
            "[yel]You spent some time with Makoto."
            show buildersguild_makowork 06 with dissolve
        if (makorand == 4):
            show buildersguild_makowork 07 with dissolve
            "[yel]You spent some time with Makoto."
            show buildersguild_makowork 08 with dissolve
        if (makorand == 5):
            show buildersguild_makowork 09 with dissolve
            "[yel]You spent some time with Makoto."
            show buildersguild_makowork 10 with dissolve
        if (makorand == 6):
            show buildersguild_makowork 11 with dissolve
            "[yel]You spent some time with Makoto."
            show buildersguild_makowork 12 with dissolve
        if (makorand == 7):
            show buildersguild_makowork 13 with dissolve
            "[yel]You spent some time with Makoto."
            show buildersguild_makowork 14 with dissolve
        if (makorand == 8):
            show buildersguild_makowork 15 with dissolve
            "[yel]You spent some time with Makoto."
            show buildersguild_makowork 16 with dissolve
        if (makorand == 9):
            show buildersguild_makowork 17 with dissolve
            "[yel]You spent some time with Makoto."
            show buildersguild_makowork 18 with dissolve
        if (makorand == 10):
            show buildersguild_makowork 19 with dissolve
            "[yel]You spent some time with Makoto."
            show buildersguild_makowork 20 with dissolve
        if (makorand == 11):
            show buildersguild_makowork 21 with dissolve
            "[yel]You spent some time with Makoto."
            show buildersguild_makowork 22 with dissolve
        show buildersguild_makowork 50 with dissolve
        $ workroll = renpy.random.randint(100,225) + (sidequest)
        $ money += workroll
        play sound "audio/coins.mp3" volume 3
        show love_mako at up_happy
        "[yel]You earned $[workroll]!"
    if (char == "celestia"):
        scene black with dissolve
        show story 024-145 with dissolve
        "[yel]You spent some time with Celestia."
        show story 024-146 with dissolve
        $ workroll = renpy.random.randint(2,15) + (sidequest)
        $ money += workroll
        play sound "audio/coins.mp3" volume 3
        show love_cele at up_happy
        "[yel]You earned $[workroll]!"
    return

label charaff(char):
    if (char == "silvia"):
        if (silvevents == 0 and silvaff < 5):
            $ silvaff += 1
            play sound "audio/ding.mp3" volume 3
            show aff_silv at up_happy
            "[yel]Silvia Affection Up!"
        elif (silvevents == 3 and silvaff < 10):
            $ silvaff += 1
            play sound "audio/ding.mp3" volume 3
            show aff_silv at up_happy
            "[yel]Silvia Affection Up!"
        elif True:
            "[oj]Silvia's affection is already maxed..."

    if (char == "estelle"):
        if (esteevents == 0 and esteaff < 4):
            $ esteaff += 1
            play sound "audio/ding.mp3" volume 3
            show aff_este at up_happy
            "[yel]Estelle Affection Up!"
        elif (esteevents == 3 and esteaff < 8):
            $ esteaff += 1
            play sound "audio/ding.mp3" volume 3
            show aff_este at up_happy
            "[yel]Estelle Affection Up!"
        elif (esteevents == 6 and esteaff < 13 and serebought and makobought):
            $ esteaff += 1
            play sound "audio/ding.mp3" volume 3
            show aff_este at up_happy
            "[yel]Estelle Affection Up!"
        elif True:
            "[oj]Estelle's affection is already maxed..."

    if (char == "azula"):
        if (azulevents == 0 and azulaff < 4):
            $ azulaff += 1
            play sound "audio/ding.mp3" volume 3
            show aff_azul at up_happy
            "[yel]Azula Affection Up!"
        elif (azulevents == 2 and azulaff < 9):
            $ azulaff += 1
            play sound "audio/ding.mp3" volume 3
            show aff_azul at up_happy
            "[yel]Azula Affection Up!"
        elif True:
            "[oj]Azula's affection is already maxed..."

    if (char == "laureate"):
        if (laurevents == 0 and lauraff < 4):
            $ lauraff += 1
            play sound "audio/ding.mp3" volume 3
            show aff_laur at up_happy
            "[yel]Laureate Affection Up!"
        elif True:
            "[oj]Laureate's affection is already maxed..."

    if (char == "serena"):
        if (sereevents == 0 and sereaff < 5):
            $ sereaff += 1
            play sound "audio/ding.mp3" volume 3
            show aff_sere at up_happy
            "[yel]Serena Affection Up!"
        elif (sereevents == 2 and sereaff < 9):
            $ sereaff += 1
            play sound "audio/ding.mp3" volume 3
            show aff_sere at up_happy
            "[yel]Serena Affection Up!"
        elif (sereevents == 5 and sereaff < 14 and estebought):
            $ sereaff += 1
            play sound "audio/ding.mp3" volume 3
            show aff_sere at up_happy
            "[yel]Serena Affection Up!"
        elif (sereevents == 9 and sereaff < 19 and serebought and makobought):
            $ sereaff += 1
            play sound "audio/ding.mp3" volume 3
            show aff_sere at up_happy
            "[yel]Serena Affection Up!"
        elif True:
            "[oj]Serena's affection is already maxed..."

    if (char == "makoto"):
        if (mainquest >= 12):
            hide love_mako
            if (makoevents == 0 and makoaff < 4):
                $ makoaff += 1
                play sound "audio/ding.mp3" volume 3
                show aff_mako at up_happy
                "[yel]Makoto Affection Up!"
            elif (makoevents == 2 and makoaff < 8):
                $ makoaff += 1
                play sound "audio/ding.mp3" volume 3
                show aff_mako at up_happy
                "[yel]Makoto Affection Up!"
            elif True:
                "[oj]Makoto's affection is already maxed..."

    if (char == "ferry"):
        hide love_ferr
        if (ferrevents == 0 and ferraff < 5):
            $ ferraff += 1
            play sound "audio/ding.mp3" volume 3
            show aff_ferr at up_happy
            "[yel]Ferry Affection Up!"
        elif True:
            "[oj]Ferry's affection is already maxed..."

    if (char == "celestia"):
        hide love_cele
        if (celeevents == 0 and celeaff < 3):
            $ celeaff += 1
            play sound "audio/ding.mp3" volume 3
            show aff_cele at up_happy
            "[yel]Celestia's Affection Up!"
        elif (celeevents == 5 and celeaff < 6):
            $ celeaff += 1
            play sound "audio/ding.mp3" volume 3
            show aff_cele at up_happy
            "[yel]Celestia's Affection Up!"
        elif True:
            "[oj]Celestia's affection is already maxed..."
    return

label deathandtaxes:
    $ waifutax = 0
    if (silvbought == True):
        $ waifutax += renpy.random.randint(25,75)
    if (estebought == True):
        $ waifutax += renpy.random.randint(50,125)
    if (azulbought == True):
        $ waifutax += renpy.random.randint(25,75)
    if (serebought == True):
        $ waifutax += renpy.random.randint(25,75)
    if (makobought == True):
        $ waifutax += renpy.random.randint(25,75)

    $ waifutaxtotal += waifutax

    if (waifutax > money):
        scene black with Dissolve(3)
        $ renpy.pause(3, hard=True)
        stop music fadeout 3.0
        $ renpy.pause(1.5, hard=True)
        "You didn't have enough money to pay the mandatory [red]Waifu Tax..."
        "The girls you owned were taken, sold off and enslaved to pay your debts..."
        "Next time, pay attention to your finances."
        $ renpy.pause(1, hard=True)
        show gameover with Dissolve(3)
        $ renpy.pause(3, hard=True)
        play music "audio/sad.mp3"
        while endgame != True:
            pause
    elif True:
        $ money -= waifutax
        play sound "audio/coins.mp3" volume 3
        show love_laur at up_happy
        "[yel]You paid $[waifutax] in Waifu Tax and weekly fees for the girls."
    return

label voylabel:
    if (weekday):
        show voy_silv_01 with Dissolve(1.5)
        $ renpy.pause(1.5, hard=True)
        mc "..."
        "It looks like [mil!c] is showering before she leaves for work..."
        "I should probably leave before she catches me..."
    elif True:
        show voy_este_01 with Dissolve(1.5)
        $ renpy.pause(1.5, hard=True)
        mc "..."
        "It looks like Estelle is showering early in the morning..."
        "I should probably leave before she catches me..."
    return

label advanceday:
    if (currentday02 == 6):
        $ currentday02 = 0
        $ dayinweek = currentday[currentday02]
    elif True:
        $ currentday02 += 1
        $ dayinweek = currentday[currentday02]

    if (currentday02 == 0 or currentday02 == 6):
        $ weekday = False
    elif True:
        $ weekday = True
    $ daycounter += 1
    $ timeofday = 0

    $ voytime = False
    $ givegift = False
    $ serework = False
    $ celework = False

    $ fortune_cap = 0


    if (daycounter >= 30 and estebought == False):
        scene black with Dissolve(1.5)
        $ renpy.pause(1.5, hard=True)
        hide screen status01
        stop music fadeout 3.0
        "[yel]You failed to purchase Estelle's Scarlet contract before day 30."
        "[yel]Start from the very beginning, you evil cuck."
        scene gameover with Dissolve(1.5)
        play music "audio/sad.mp3"
        while endgame != True:
            pause
    return

label flowerpicking:
    hide screen status01

    if (flowers_tutorial == False):
        $ flowers_tutorial = True
        mc "Hmm..."
        mc "This flower looks unusual..."
        show screen tutorialscreen_05 with Dissolve(1.5)
        $ renpy.pause(1.5, hard=True)

    $ flower_rarity = 0
    $ flower_rarity = renpy.random.randint(1,100)

    if (flower_rarity <= 80):
        $ flowers_r += 1
        play sound "audio/flowers_r.mp3" volume 2
        show flowerpicking_r_icon at up_happy
        "You picked up a [yel]Rare Flower!"
    elif (flower_rarity <= 95):
        play sound "audio/flowers_sr.mp3" volume 2
        show flowerpicking_sr_icon at up_happy
        $ flowers_sr += 1
        "You picked up a [yel]SR Flower!"
    elif (flower_rarity <= 99):
        play sound "audio/flowers_ssr.mp3" volume 2
        show flowerpicking_ssr_icon at up_happy
        $ flowers_ssr += 1
        "You picked up a [yel]SSR Flower!"
    elif (flower_rarity == 100):
        play sound "audio/flowers_ssr.mp3" volume 3
        show flowerpicking_ssg_icon at up_happy
        $ flowers_ssg += 1
        "You picked up a [yel]SSGSS Flower!"

    if (location == "park_01"):
        jump parklabel_01
    if (location == "park_02"):
        jump parklabel_02
    if (location == "park_03"):
        jump parklabel_03

label respawn:

    $ junk_street01 = False
    $ junk_street03 = False
    $ junk_street04 = False

    $ flower_respawn = 0
    $ flower_respawn = renpy.random.randint(1,100)
    $ flower_prices_r = 0
    $ flower_prices_sr = 0
    $ flower_prices_ssr = 0
    $ flower_prices_ssg = 0

    $ flower_prices_r = renpy.random.randint(15,35)
    $ flower_prices_sr = renpy.random.randint(80,115)
    $ flower_prices_ssr = renpy.random.randint(400,560)
    $ flower_prices_ssg = renpy.random.randint(1500,2100)

    $ magicflower_price = 0
    $ magicflower_price = renpy.random.randint(100,500)


    if (flower_respawn <= 75):
        $ park01_flower_01 = True
    elif True:
        $ park01_flower_01 = False

    $ flower_respawn = renpy.random.randint(1,100)
    if (flower_respawn <= 75):
        $ park01_flower_02 = True
    elif True:
        $ park01_flower_02 = False

    $ flower_respawn = renpy.random.randint(1,100)
    if (flower_respawn <= 75):
        $ park01_flower_03 = True
    elif True:
        $ park01_flower_03 = False


    $ flower_respawn = renpy.random.randint(1,100)
    if (flower_respawn <= 75):
        $ park02_flower_01 = True
    elif True:
        $ park02_flower_01 = False

    $ flower_respawn = renpy.random.randint(1,100)
    if (flower_respawn <= 75):
        $ park02_flower_02 = True
    elif True:
        $ park02_flower_02 = False

    $ flower_respawn = renpy.random.randint(1,100)
    if (flower_respawn <= 75):
        $ park02_flower_03 = True
    elif True:
        $ park02_flower_03 = False


    $ flower_respawn = renpy.random.randint(1,100)
    if (flower_respawn <= 75):
        $ park03_flower_01 = True
    elif True:
        $ park03_flower_01 = False

    $ flower_respawn = renpy.random.randint(1,100)
    if (flower_respawn <= 75):
        $ park03_flower_02 = True
    elif True:
        $ park03_flower_02 = False

    $ flower_respawn = renpy.random.randint(1,100)
    if (flower_respawn <= 75):
        $ park03_flower_03 = True
    elif True:
        $ park03_flower_03 = False




    if (missions_babysitter == "silvia"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 5):
            play sound "audio/coins.mp3" volume 3
            show love_silv at up_happy
            $ silv_is_dead = False
            $ missions_babysitter = ""
            $ money += missions_babysitter_price
            "[yel]Silvia performed well at her job today!"
            "[yel]You made $[missions_babysitter_price]!"
            hide love_silv at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_silv at up_happy
            $ silv_is_dead = False
            $ missions_babysitter = ""
            "[yel]Silvia performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_silv at up_happy
    if (missions_babysitter == "estelle"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 90):
            play sound "audio/coins.mp3" volume 3
            show love_este at up_happy
            $ este_is_dead = False
            $ missions_babysitter = ""
            $ money += missions_babysitter_price
            "[yel]Estelle performed well at her job today!"
            "[yel]You made $[missions_babysitter_price]!"
            hide love_este at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_este at up_happy
            $ este_is_dead = False
            $ missions_babysitter = ""
            "[yel]Estelle performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_este at up_happy
    if (missions_babysitter == "makoto"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 40):
            play sound "audio/coins.mp3" volume 3
            show love_mako at up_happy
            $ mako_is_dead = False
            $ missions_babysitter = ""
            $ money += missions_babysitter_price
            "[yel]Makoto performed well at her job today!"
            "[yel]You made $[missions_babysitter_price]!"
            hide love_mako at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_mako at up_happy
            $ mako_is_dead = False
            $ missions_babysitter = ""
            "[yel]Makoto performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_mako at up_happy
    if (missions_babysitter == "serena"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 80):
            play sound "audio/coins.mp3" volume 3
            show love_sere at up_happy
            $ sere_is_dead = False
            $ missions_babysitter = ""
            $ money += missions_babysitter_price
            "[yel]Serena performed well at her job today!"
            "[yel]You made $[missions_babysitter_price]!"
            hide love_sere at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_sere at up_happy
            $ sere_is_dead = False
            $ missions_babysitter = ""
            "[yel]Serena performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_sere at up_happy


    if (missions_housekeeper == "silvia"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 5):
            play sound "audio/coins.mp3" volume 3
            show love_silv at up_happy
            $ silv_is_dead = False
            $ missions_housekeeper = ""
            $ money += missions_housekeeper_price
            "[yel]Silvia performed well at her job today!"
            "[yel]You made $[missions_housekeeper_price]!"
            hide love_silv at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_silv at up_happy
            $ silv_is_dead = False
            $ missions_housekeeper = ""
            "[yel]Silvia performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_silv at up_happy
    if (missions_housekeeper == "estelle"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 94):
            play sound "audio/coins.mp3" volume 3
            show love_este at up_happy
            $ este_is_dead = False
            $ missions_housekeeper = ""
            $ money += missions_housekeeper_price
            "[yel]Estelle performed well at her job today!"
            "[yel]You made $[missions_housekeeper_price]!"
            hide love_este at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_este at up_happy
            $ este_is_dead = False
            $ missions_housekeeper = ""
            "[yel]Estelle performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_este at up_happy
    if (missions_housekeeper == "makoto"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 40):
            play sound "audio/coins.mp3" volume 3
            show love_mako at up_happy
            $ mako_is_dead = False
            $ missions_housekeeper = ""
            $ money += missions_housekeeper_price
            "[yel]Makoto performed well at her job today!"
            "[yel]You made $[missions_housekeeper_price]!"
            hide love_mako at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_mako at up_happy
            $ mako_is_dead = False
            $ missions_housekeeper = ""
            "[yel]Makoto performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_mako at up_happy
    if (missions_housekeeper == "serena"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 80):
            play sound "audio/coins.mp3" volume 3
            show love_sere at up_happy
            $ sere_is_dead = False
            $ missions_housekeeper = ""
            $ money += missions_housekeeper_price
            "[yel]Serena performed well at her job today!"
            "[yel]You made $[missions_housekeeper_price]!"
            hide love_sere at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_sere at up_happy
            $ sere_is_dead = False
            $ missions_housekeeper = ""
            "[yel]Serena performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_sere at up_happy


    if (missions_pizzagirl == "silvia"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 85):
            play sound "audio/coins.mp3" volume 3
            show love_silv at up_happy
            $ silv_is_dead = False
            $ missions_pizzagirl = ""
            $ money += missions_pizzagirl_price
            "[yel]Silvia performed well at her job today!"
            "[yel]You made $[missions_pizzagirl_price]!"
            hide love_silv at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_silv at up_happy
            $ silv_is_dead = False
            $ missions_pizzagirl = ""
            "[yel]Silvia performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_silv at up_happy
    if (missions_pizzagirl == "estelle"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 90):
            play sound "audio/coins.mp3" volume 3
            show love_este at up_happy
            $ este_is_dead = False
            $ missions_pizzagirl = ""
            $ money += missions_pizzagirl_price
            "[yel]Estelle performed well at her job today!"
            "[yel]You made $[missions_pizzagirl_price]!"
            hide love_este at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_este at up_happy
            $ este_is_dead = False
            $ missions_pizzagirl = ""
            "[yel]Estelle performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_este at up_happy
    if (missions_pizzagirl == "makoto"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 40):
            play sound "audio/coins.mp3" volume 3
            show love_mako at up_happy
            $ mako_is_dead = False
            $ missions_pizzagirl = ""
            $ money += missions_pizzagirl_price
            "[yel]Makoto performed well at her job today!"
            "[yel]You made $[missions_pizzagirl_price]!"
            hide love_mako at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_mako at up_happy
            $ mako_is_dead = False
            $ missions_pizzagirl = ""
            "[yel]Makoto performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_mako at up_happy
    if (missions_pizzagirl == "serena"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 20):
            play sound "audio/coins.mp3" volume 3
            show love_sere at up_happy
            $ sere_is_dead = False
            $ missions_pizzagirl = ""
            $ money += missions_pizzagirl_price
            "[yel]Serena performed well at her job today!"
            "[yel]You made $[missions_pizzagirl_price]!"
            hide love_sere at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_sere at up_happy
            $ sere_is_dead = False
            $ missions_pizzagirl = ""
            "[yel]Serena performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_sere at up_happy


    if (missions_salesman == "silvia"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 85):
            play sound "audio/coins.mp3" volume 3
            show love_silv at up_happy
            $ silv_is_dead = False
            $ missions_salesman = ""
            $ money += missions_salesman_price
            "[yel]Silvia performed well at her job today!"
            "[yel]You made $[missions_salesman_price]!"
            hide love_silv at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_silv at up_happy
            $ silv_is_dead = False
            $ missions_salesman = ""
            "[yel]Silvia performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_silv at up_happy
    if (missions_salesman == "estelle"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 90):
            play sound "audio/coins.mp3" volume 3
            show love_este at up_happy
            $ este_is_dead = False
            $ missions_salesman = ""
            $ money += missions_salesman_price
            "[yel]Estelle performed well at her job today!"
            "[yel]You made $[missions_salesman_price]!"
            hide love_este at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_este at up_happy
            $ este_is_dead = False
            $ missions_salesman = ""
            "[yel]Estelle performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_este at up_happy
    if (missions_salesman == "makoto"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 40):
            play sound "audio/coins.mp3" volume 3
            show love_mako at up_happy
            $ mako_is_dead = False
            $ missions_salesman = ""
            $ money += missions_salesman_price
            "[yel]Makoto performed well at her job today!"
            "[yel]You made $[missions_salesman_price]!"
            hide love_mako at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_mako at up_happy
            $ mako_is_dead = False
            $ missions_salesman = ""
            "[yel]Makoto performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_mako at up_happy
    if (missions_salesman == "serena"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 20):
            play sound "audio/coins.mp3" volume 3
            show love_sere at up_happy
            $ sere_is_dead = False
            $ missions_salesman = ""
            $ money += missions_salesman_price
            "[yel]Serena performed well at her job today!"
            "[yel]You made $[missions_salesman_price]!"
            hide love_sere at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_sere at up_happy
            $ sere_is_dead = False
            $ missions_salesman = ""
            "[yel]Serena performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_sere at up_happy


    if (missions_bodyguard == "silvia"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 95):
            play sound "audio/coins.mp3" volume 3
            show love_silv at up_happy
            $ silv_is_dead = False
            $ missions_bodyguard = ""
            $ money += missions_bodyguard_price
            "[yel]Silvia performed well at her job today!"
            "[yel]You made $[missions_bodyguard_price]!"
            hide love_silv at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_silv at up_happy
            $ silv_is_dead = False
            $ missions_bodyguard = ""
            "[yel]Silvia performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_silv at up_happy
    if (missions_bodyguard == "estelle"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 90):
            play sound "audio/coins.mp3" volume 3
            show love_este at up_happy
            $ este_is_dead = False
            $ missions_bodyguard = ""
            $ money += missions_bodyguard_price
            "[yel]Estelle performed well at her job today!"
            "[yel]You made $[missions_bodyguard_price]!"
            hide love_este at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_este at up_happy
            $ este_is_dead = False
            $ missions_bodyguard = ""
            "[yel]Estelle performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_este at up_happy
    if (missions_bodyguard == "makoto"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 40):
            play sound "audio/coins.mp3" volume 3
            show love_mako at up_happy
            $ mako_is_dead = False
            $ missions_bodyguard = ""
            $ money += missions_bodyguard_price
            "[yel]Makoto performed well at her job today!"
            "[yel]You made $[missions_bodyguard_price]!"
            hide love_mako at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_mako at up_happy
            $ mako_is_dead = False
            $ missions_bodyguard = ""
            "[yel]Makoto performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_mako at up_happy
    if (missions_bodyguard == "serena"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 90):
            play sound "audio/coins.mp3" volume 3
            show love_sere at up_happy
            $ sere_is_dead = False
            $ missions_bodyguard = ""
            $ money += missions_bodyguard_price
            "[yel]Serena performed well at her job today!"
            "[yel]You made $[missions_bodyguard_price]!"
            hide love_sere at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_sere at up_happy
            $ sere_is_dead = False
            $ missions_bodyguard = ""
            "[yel]Serena performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_sere at up_happy


    if (missions_icecreamgirl == "silvia"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 85):
            play sound "audio/coins.mp3" volume 3
            show love_silv at up_happy
            $ silv_is_dead = False
            $ missions_icecreamgirl = ""
            $ money += missions_icecreamgirl_price
            "[yel]Silvia performed well at her job today!"
            "[yel]You made $[missions_icecreamgirl_price]!"
            hide love_silv at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_silv at up_happy
            $ silv_is_dead = False
            $ missions_icecreamgirl = ""
            "[yel]Silvia performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_silv at up_happy
    if (missions_icecreamgirl == "estelle"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 90):
            play sound "audio/coins.mp3" volume 3
            show love_este at up_happy
            $ este_is_dead = False
            $ missions_icecreamgirl = ""
            $ money += missions_icecreamgirl_price
            "[yel]Estelle performed well at her job today!"
            "[yel]You made $[missions_icecreamgirl_price]!"
            hide love_este at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_este at up_happy
            $ este_is_dead = False
            $ missions_icecreamgirl = ""
            "[yel]Estelle performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_este at up_happy
    if (missions_icecreamgirl == "makoto"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 40):
            play sound "audio/coins.mp3" volume 3
            show love_mako at up_happy
            $ mako_is_dead = False
            $ missions_icecreamgirl = ""
            $ money += missions_icecreamgirl_price
            "[yel]Makoto performed well at her job today!"
            "[yel]You made $[missions_icecreamgirl_price]!"
            hide love_mako at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_mako at up_happy
            $ mako_is_dead = False
            $ missions_icecreamgirl = ""
            "[yel]Makoto performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_mako at up_happy
    if (missions_icecreamgirl == "serena"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 20):
            play sound "audio/coins.mp3" volume 3
            show love_sere at up_happy
            $ sere_is_dead = False
            $ missions_icecreamgirl = ""
            $ money += missions_icecreamgirl_price
            "[yel]Serena performed well at her job today!"
            "[yel]You made $[missions_icecreamgirl_price]!"
            hide love_sere at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_sere at up_happy
            $ sere_is_dead = False
            $ missions_icecreamgirl = ""
            "[yel]Serena performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_sere at up_happy


    if (missions_model == "silvia"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 85):
            play sound "audio/coins.mp3" volume 3
            show love_silv at up_happy
            $ silv_is_dead = False
            $ missions_model = ""
            $ money += missions_model_price
            "[yel]Silvia performed well at her job today!"
            "[yel]You made $[missions_model_price]!"
            hide love_silv at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_silv at up_happy
            $ silv_is_dead = False
            $ missions_model = ""
            "[yel]Silvia performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_silv at up_happy
    if (missions_model == "estelle"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 10):
            play sound "audio/coins.mp3" volume 3
            show love_este at up_happy
            $ este_is_dead = False
            $ missions_model = ""
            $ money += missions_model_price
            "[yel]Estelle performed well at her job today!"
            "[yel]You made $[missions_model_price]!"
            hide love_este at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_este at up_happy
            $ este_is_dead = False
            $ missions_model = ""
            "[yel]Estelle performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_este at up_happy
    if (missions_model == "makoto"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 85):
            play sound "audio/coins.mp3" volume 3
            show love_mako at up_happy
            $ mako_is_dead = False
            $ missions_model = ""
            $ money += missions_model_price
            "[yel]Makoto performed surprisingly well today!"
            "[yel]You made $[missions_model_price]!"
            hide love_mako at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_mako at up_happy
            $ mako_is_dead = False
            $ missions_model = ""
            "[yel]Makoto performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_mako at up_happy
    if (missions_model == "serena"):
        $ mission_success_rate = renpy.random.randint(1,100)
        if (mission_success_rate > 85):
            play sound "audio/coins.mp3" volume 3
            show love_sere at up_happy
            $ sere_is_dead = False
            $ missions_model = ""
            $ money += missions_model_price
            "[yel]Serena performed well at her job today!"
            "[yel]You made $[missions_model_price]!"
            hide love_sere at up_happy
        elif True:
            play sound "audio/depress.mp3" volume 3
            show sad_sere at up_happy
            $ sere_is_dead = False
            $ missions_model = ""
            "[yel]Serena performed miserably at her job today..."
            "[yel]She didn't make any money from the job..."
            hide sad_sere at up_happy



    $ missions_cap = 0
    $ missions_randomize = 0

    $ missions_babysitter_enabled = False
    $ missions_housekeeper_enabled = False
    $ missions_pizzagirl_enabled = False
    $ missions_salesman_enabled = False
    $ missions_bodyguard_enabled = False
    $ missions_icecreamgirl_enabled = False
    $ missions_model_enabled = False

    $ missions_babysitter = ""
    $ missions_housekeeper = ""
    $ missions_pizzagirl = ""
    $ missions_salesman = ""
    $ missions_bodyguard = ""
    $ missions_icecreamgirl = ""
    $ missions_model = ""

    $ missions_babysitter_price = renpy.random.randint(50,350) + (sidequest)
    $ missions_housekeeper_price = renpy.random.randint(50,350) + (sidequest)
    $ missions_pizzagirl_price = renpy.random.randint(50,350) + (sidequest)
    $ missions_salesman_price = renpy.random.randint(50,350) + (sidequest)
    $ missions_bodyguard_price = renpy.random.randint(200,600) + (sidequest)
    $ missions_icecreamgirl_price = renpy.random.randint(50,350) + (sidequest)
    $ missions_model_price = renpy.random.randint(200,600) + (sidequest)

    while (missions_cap < 4):
        $ missions_randomize = renpy.random.randint(1,7)
        if (missions_randomize == 1):
            $ missions_babysitter_enabled = True
        elif (missions_randomize == 2):
            $ missions_housekeeper_enabled = True
        elif (missions_randomize == 3):
            $ missions_pizzagirl_enabled = True
        elif (missions_randomize == 4):
            $ missions_salesman_enabled = True
        elif (missions_randomize == 5):
            $ missions_bodyguard_enabled = True
        elif (missions_randomize == 6):
            $ missions_icecreamgirl_enabled = True
        elif (missions_randomize == 7):
            $ missions_model_enabled = True
        $ missions_cap += 1

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
