label missionstutorial:
    $ missions_tutorial = True
    mc "Hmm..."
    mc "These look like job requests sent from local businesses..."
    play sound "audio/ding.mp3" volume 3
    show screen tutorialscreen_07 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    pause

screen missionscreen:
    modal True
    hbox xalign 0.5 yalign 0.5:
        imagebutton:
            idle "screens_update/mission_screen.webp"
    hbox xalign 0.77 yalign 0.26:
        imagebutton:
            idle "icons_update/icon_close.webp" hover "icons_update/icon_close_hover.webp" action [Hide("missionscreen"), Jump("cityhalllabel_01")]
    hbox xalign 0.5 yalign 0.25:
        text "{size=100}Job Listings" outlines [ (absolute(3), "#000", absolute(0), absolute(1)) ] color "#FFF" font "Timeless.ttf"
    hbox xalign 0.5 yalign 0.50 spacing 15:
        if (missions_babysitter_enabled == True):
            imagebutton:
                idle "screens_missions/babysitter_icon.webp" hover "screens_missions/babysitter_icon_hover.webp" action [Hide("missionscreen"), Jump("babysitter_label")]
        if (missions_housekeeper_enabled == True):
            imagebutton:
                idle "screens_missions/housekeeper_icon.webp" hover "screens_missions/housekeeper_icon_hover.webp" action [Hide("missionscreen"), Jump("housekeeper_label")]
        if (missions_pizzagirl_enabled == True):
            imagebutton:
                idle "screens_missions/pizzagirl_icon.webp" hover "screens_missions/pizzagirl_icon_hover.webp" action [Hide("missionscreen"), Jump("pizzagirl_label")]
        if (missions_salesman_enabled == True):
            imagebutton:
                idle "screens_missions/salesman_icon.webp" hover "screens_missions/salesman_icon_hover.webp" action [Hide("missionscreen"), Jump("salesman_label")]
        if (missions_bodyguard_enabled == True):
            imagebutton:
                idle "screens_missions/bodyguard_icon.webp" hover "screens_missions/bodyguard_icon_hover.webp" action [Hide("missionscreen"), Jump("bodyguard_label")]
        if (missions_icecreamgirl_enabled == True):
            imagebutton:
                idle "screens_missions/icecreamgirl_icon.webp" hover "screens_missions/icecreamgirl_icon_hover.webp" action [Hide("missionscreen"), Jump("icecreamgirl_label")]
        if (missions_model_enabled == True):
            imagebutton:
                idle "screens_missions/model_icon.webp" hover "screens_missions/model_icon_hover.webp" action [Hide("missionscreen"), Jump("model_label")]



screen babysitter_screen:
    hbox xalign 0.5 yalign 0.5:
        imagebutton:
            idle "screens_update/mission_screen.webp"
    hbox xalign 0.5 yalign 0.25:
        text "{size=75}Babysitter" outlines [ (absolute(3), "#000", absolute(0), absolute(1)) ] color "#FFF" font "Timeless.ttf"
    add "screens_missions/babysitterscreen_icon.webp" at left_to_right_missions
    vbox xalign 0.5 yalign 0.45:
        text "{size=30}Looking for part-time babysitters!" style "questfont"
        text "{size=30}Applicant should be reliable and good with children." style "questfont"
        text "{size=30}Duties including assisting children with their homework," style "questfont"
        text "{size=30}transporting children to and from school, preparing healthy meals" style "questfont"
        text "{size=30}for little ones, and providing basic maintenance for household. " style "questfont"
    hbox xalign 0.5 yalign 0.65:
        text "{size=75}[oj]Price Rate: $[missions_babysitter_price]" style "questfont"

screen housekeeper_screen:
    hbox xalign 0.5 yalign 0.5:
        imagebutton:
            idle "screens_update/mission_screen.webp"
    hbox xalign 0.5 yalign 0.25:
        text "{size=75}Housekeeper" outlines [ (absolute(3), "#000", absolute(0), absolute(1)) ] color "#FFF" font "Timeless.ttf"
    add "screens_missions/housekeeperscreen_icon.webp" at left_to_right_missions
    vbox xalign 0.5 yalign 0.45:
        text "{size=30}Apartment complex in need of a housekeeper." style "questfont"
        text "{size=30}Applicant will be responsible for building's" style "questfont"
        text "{size=30}cleanliness, while providing tidy and sanitary" style "questfont"
        text "{size=30}amenities to guests and residents. Duties include" style "questfont"
        text "{size=30}cleaning floors, making beds, and dusting" style "questfont"
        text "{size=30}surfaces throughout a home or other building." style "questfont"
    hbox xalign 0.5 yalign 0.65:
        text "{size=75}[oj]Price Rate: $[missions_housekeeper_price]" style "questfont"

screen pizzagirl_screen:
    hbox xalign 0.5 yalign 0.5:
        imagebutton:
            idle "screens_update/mission_screen.webp"
    hbox xalign 0.5 yalign 0.25:
        text "{size=75}Pizza Girl" outlines [ (absolute(3), "#000", absolute(0), absolute(1)) ] color "#FFF" font "Timeless.ttf"
    add "screens_missions/pizzagirlscreen_icon.webp" at left_to_right_missions
    vbox xalign 0.5 yalign 0.45:
        text "{size=30}Maple's Grand Pizzeria is looking for pizza girls!" style "questfont"
        text "{size=30}Applicant must be responsible, punctual, and self-reliant." style "questfont"
        text "{size=30}Duties include transportation of hot items to" style "questfont"
        text "{size=30}desired locations within a certain time frame." style "questfont"
    hbox xalign 0.5 yalign 0.65:
        text "{size=75}[oj]Price Rate: $[missions_pizzagirl_price]" style "questfont"

screen salesman_screen:
    hbox xalign 0.5 yalign 0.5:
        imagebutton:
            idle "screens_update/mission_screen.webp"
    hbox xalign 0.5 yalign 0.25:
        text "{size=75}Salesman" outlines [ (absolute(3), "#000", absolute(0), absolute(1)) ] color "#FFF" font "Timeless.ttf"
    add "screens_missions/salesmanscreen_icon.webp" at left_to_right_missions
    vbox xalign 0.5 yalign 0.45:
        text "{size=30}Maplesoft Industries is in need of a door-to-door sales person." style "questfont"
        text "{size=30}Applicant will be responsible for selling Maple brand products," style "questfont"
        text "{size=30}merchandise, and services by setting up demonstrations door-to-door." style "questfont"
        text "{size=30}Applicant should be friendly, cordial, and sociable." style "questfont"
    hbox xalign 0.5 yalign 0.65:
        text "{size=75}[oj]Price Rate: $[missions_salesman_price]" style "questfont"

screen bodyguard_screen:
    hbox xalign 0.5 yalign 0.5:
        imagebutton:
            idle "screens_update/mission_screen.webp"
    hbox xalign 0.5 yalign 0.25:
        text "{size=75}Bodyguard" outlines [ (absolute(3), "#000", absolute(0), absolute(1)) ] color "#FFF" font "Timeless.ttf"
    add "screens_missions/bodyguardscreen_icon.webp" at left_to_right_missions
    vbox xalign 0.5 yalign 0.45:
        text "{size=30}Important Patrons are in need of hired help!" style "questfont"
        text "{size=30}Applicant should be physically intimidating" style "questfont"
        text "{size=30}with knowledge and experience in the combat arts." style "questfont"
        text "{size=30}Duties will include escorting clients across Scarlet" style "questfont"
        text "{size=30}while protecting him/her from harm." style "questfont"
    hbox xalign 0.5 yalign 0.65:
        text "{size=75}[oj]Price Rate: $[missions_bodyguard_price]" style "questfont"

screen icecreamgirl_screen:
    hbox xalign 0.5 yalign 0.5:
        imagebutton:
            idle "screens_update/mission_screen.webp"
    hbox xalign 0.5 yalign 0.25:
        text "{size=75}Ice Cream Girl" outlines [ (absolute(3), "#000", absolute(0), absolute(1)) ] color "#FFF" font "Timeless.ttf"
    add "screens_missions/icecreamgirlscreen_icon.webp" at left_to_right_missions
    vbox xalign 0.5 yalign 0.45:
        text "{size=30}Maple and Jerry's is looking for a part-time ice cream girl." style "questfont"
        text "{size=30}Applicant should be competent, friendly, and approachable." style "questfont"
        text "{size=30}Applicant will be required to greet customers, maintain" style "questfont"
        text "{size=30}dairy inventory, offer flavor suggestions, collect payment," style "questfont"
        text "{size=30}answer client questions, and adhere to health and safety guidelines." style "questfont"
    hbox xalign 0.5 yalign 0.65:
        text "{size=75}[oj]Price Rate: $[missions_icecreamgirl_price]" style "questfont"

screen model_screen:
    hbox xalign 0.5 yalign 0.5:
        imagebutton:
            idle "screens_update/mission_screen.webp"
    hbox xalign 0.5 yalign 0.25:
        text "{size=75}Model" outlines [ (absolute(3), "#000", absolute(0), absolute(1)) ] color "#FFF" font "Timeless.ttf"
    add "screens_missions/modelscreen_icon.webp" at left_to_right_missions
    vbox xalign 0.5 yalign 0.45:
        text "{size=30}Maple's Model Management (MMM) is seeking amateur" style "questfont"
        text "{size=30}models to promote, advertise, and showcase their" style "questfont"
        text "{size=30}clothing, footwear, and other inventory brands. Duties include" style "questfont"
        text "{size=30}participating in photoshoots, conventions, as well as" style "questfont"
        text "{size=30}posing for sculptors, artists, and painters. Applicant" style "questfont"
        text "{size=30}must be extremely confident in their body and meet" style "questfont"
        text "{size=30}height and weight guidelines." style "questfont"
    hbox xalign 0.5 yalign 0.65:
        text "{size=75}[oj]Price Rate: $[missions_model_price]" style "questfont"

label babysitter_label:
    hide screen status01
    show screen babysitter_screen

    mc "Should I assign someone to this job?"
    menu:
        "Silvia" if (silvbought == True and silv_is_dead == False):
            $ missions_babysitter_enabled = False
            $ silv_is_dead = True
            $ missions_babysitter = "silvia"
            play sound "audio/coins.mp3" volume 3
            show love_silv at up_happy
            "[yel]Silvia looks up to the task!"
            hide screen babysitter_screen
            hide love_silv at up_happy
            show screen missionscreen
        "Estelle" if (estebought == True and este_is_dead == False):
            $ missions_babysitter_enabled = False
            $ este_is_dead = True
            $ missions_babysitter = "estelle"
            play sound "audio/depress.mp3" volume 3
            show sad_este at up_happy
            "[yel]Estelle doesn't appear motivated to work..."
            hide screen babysitter_screen
            hide sad_este at up_happy
            show screen missionscreen
        "Makoto" if (makobought == True and mako_is_dead == False):
            $ missions_babysitter_enabled = False
            $ mako_is_dead = True
            $ missions_babysitter = "makoto"
            play sound "audio/coins.mp3" volume 3
            show love_mako at up_happy
            "[yel]Makoto is willing to put her building skills to the task..."
            hide screen babysitter_screen
            hide love_mako at up_happy
            show screen missionscreen
        "Serena" if (serebought == True and sere_is_dead == False):
            $ missions_babysitter_enabled = False
            $ sere_is_dead = True
            $ missions_babysitter = "serena"
            play sound "audio/coins.mp3" volume 3
            show love_sere at up_happy
            "[yel]Serena is willing to give it a shot..."
            hide screen babysitter_screen
            hide love_sere at up_happy
            show screen missionscreen
        "Nevermind..." if True:
            hide screen babysitter_screen
            show screen missionscreen
    while endgame != True:
        pause

label housekeeper_label:
    hide screen status01
    show screen housekeeper_screen

    mc "Should I assign someone to this job?"
    menu:
        "Silvia" if (silvbought == True and silv_is_dead == False):
            $ missions_housekeeper_enabled = False
            $ silv_is_dead = True
            $ missions_housekeeper = "silvia"
            play sound "audio/coins.mp3" volume 3
            show love_silv at up_happy
            "[yel]Silvia looks up to the task!"
            hide screen housekeeper_screen
            hide love_silv at up_happy
            show screen missionscreen
        "Estelle" if (estebought == True and este_is_dead == False):
            $ missions_housekeeper_enabled = False
            $ este_is_dead = True
            $ missions_housekeeper = "estelle"
            play sound "audio/depress.mp3" volume 3
            show sad_este at up_happy
            "[yel]Estelle doesn't appear motivated to work..."
            hide screen housekeeper_screen
            hide sad_este at up_happy
            show screen missionscreen
        "Makoto" if (makobought == True and mako_is_dead == False):
            $ missions_housekeeper_enabled = False
            $ mako_is_dead = True
            $ missions_housekeeper = "makoto"
            play sound "audio/coins.mp3" volume 3
            show love_mako at up_happy
            "[yel]Makoto is willing to put her building skills to the task..."
            hide screen housekeeper_screen
            hide love_mako at up_happy
            show screen missionscreen
        "Serena" if (serebought == True and sere_is_dead == False):
            $ missions_housekeeper_enabled = False
            $ sere_is_dead = True
            $ missions_housekeeper = "serena"
            play sound "audio/coins.mp3" volume 3
            show love_sere at up_happy
            "[yel]Serena looks up to the task!"
            hide screen housekeeper_screen
            hide love_sere at up_happy
            show screen missionscreen
        "Nevermind..." if True:
            hide screen housekeeper_screen
            show screen missionscreen
    while endgame != True:
        pause

label pizzagirl_label:
    hide screen status01
    show screen pizzagirl_screen

    mc "Should I assign someone to this job?"
    menu:
        "Silvia" if (silvbought == True and silv_is_dead == False):
            $ missions_pizzagirl_enabled = False
            $ silv_is_dead = True
            $ missions_pizzagirl = "silvia"
            play sound "audio/depress.mp3" volume 3
            show sad_silv at up_happy
            "[yel]Silvia doesn't seem confident about the job..."
            hide screen pizzagirl_screen
            hide sad_silv at up_happy
            show screen missionscreen
        "Estelle" if (estebought == True and este_is_dead == False):
            $ missions_pizzagirl_enabled = False
            $ este_is_dead = True
            $ missions_pizzagirl = "estelle"
            play sound "audio/depress.mp3" volume 3
            show sad_este at up_happy
            "[yel]Estelle doesn't appear motivated to work..."
            hide screen pizzagirl_screen
            hide sad_este at up_happy
            show screen missionscreen
        "Makoto" if (makobought == True and mako_is_dead == False):
            $ missions_pizzagirl_enabled = False
            $ mako_is_dead = True
            $ missions_pizzagirl = "makoto"
            play sound "audio/coins.mp3" volume 3
            show love_mako at up_happy
            "[yel]Makoto is willing to put her building skills to the task..."
            hide screen pizzagirl_screen
            hide love_mako at up_happy
            show screen missionscreen
        "Serena" if (serebought == True and sere_is_dead == False):
            $ missions_pizzagirl_enabled = False
            $ sere_is_dead = True
            $ missions_pizzagirl = "serena"
            play sound "audio/coins.mp3" volume 3
            show love_sere at up_happy
            "[yel]Serena is up to the task!"
            hide screen pizzagirl_screen
            hide love_sere at up_happy
            show screen missionscreen
        "Nevermind..." if True:
            hide screen pizzagirl_screen
            show screen missionscreen
    while endgame != True:
        pause

label salesman_label:
    hide screen status01
    show screen salesman_screen

    mc "Should I assign someone to this job?"
    menu:
        "Silvia" if (silvbought == True and silv_is_dead == False):
            $ missions_salesman_enabled = False
            $ silv_is_dead = True
            $ missions_salesman = "silvia"
            play sound "audio/depress.mp3" volume 3
            show sad_silv at up_happy
            "[yel]Silvia doesn't seem confident about the job..."
            hide screen salesman_screen
            hide sad_silv at up_happy
            show screen missionscreen
        "Estelle" if (estebought == True and este_is_dead == False):
            $ missions_salesman_enabled = False
            $ este_is_dead = True
            $ missions_salesman = "estelle"
            play sound "audio/depress.mp3" volume 3
            show sad_este at up_happy
            "[yel]Estelle doesn't appear motivated to work..."
            hide screen salesman_screen
            hide sad_este at up_happy
            show screen missionscreen
        "Makoto" if (makobought == True and mako_is_dead == False):
            $ missions_salesman_enabled = False
            $ mako_is_dead = True
            $ missions_salesman = "makoto"
            play sound "audio/coins.mp3" volume 3
            show love_mako at up_happy
            "[yel]Makoto is willing to put her building skills to the task..."
            hide screen salesman_screen
            hide love_mako at up_happy
            show screen missionscreen
        "Serena" if (serebought == True and sere_is_dead == False):
            $ missions_salesman_enabled = False
            $ sere_is_dead = True
            $ missions_salesman = "serena"
            play sound "audio/coins.mp3" volume 3
            show love_sere at up_happy
            "[yel]Serena looks up to the task!"
            hide screen salesman_screen
            hide love_sere at up_happy
            show screen missionscreen
        "Nevermind..." if True:
            hide screen salesman_screen
            show screen missionscreen
    while endgame != True:
        pause

label bodyguard_label:
    hide screen status01
    show screen bodyguard_screen

    mc "Should I assign someone to this job?"
    menu:
        "Silvia" if (silvbought == True and silv_is_dead == False):
            $ missions_bodyguard_enabled = False
            $ silv_is_dead = True
            $ missions_bodyguard = "silvia"
            play sound "audio/depress.mp3" volume 3
            show sad_silv at up_happy
            "[yel]Silvia thinks this is a terrible idea..."
            hide screen bodyguard_screen
            hide sad_silv at up_happy
            show screen missionscreen
        "Estelle" if (estebought == True and este_is_dead == False):
            $ missions_bodyguard_enabled = False
            $ este_is_dead = True
            $ missions_bodyguard = "estelle"
            play sound "audio/depress.mp3" volume 3
            show sad_este at up_happy
            "[yel]Estelle doesn't appear motivated to work..."
            hide screen bodyguard_screen
            hide sad_este at up_happy
            show screen missionscreen
        "Makoto" if (makobought == True and mako_is_dead == False):
            $ missions_bodyguard_enabled = False
            $ mako_is_dead = True
            $ missions_bodyguard = "makoto"
            play sound "audio/coins.mp3" volume 3
            show love_mako at up_happy
            "[yel]Makoto thinks Pandy might prove useful here..."
            hide screen bodyguard_screen
            hide love_mako at up_happy
            show screen missionscreen
        "Serena" if (serebought == True and sere_is_dead == False):
            $ missions_bodyguard_enabled = False
            $ sere_is_dead = True
            $ missions_bodyguard = "serena"
            play sound "audio/coins.mp3" volume 3
            show love_sere at up_happy
            "[yel]Serena thinks this is a terrible idea..."
            hide screen bodyguard_screen
            hide love_sere at up_happy
            show screen missionscreen
        "Nevermind..." if True:
            hide screen bodyguard_screen
            show screen missionscreen
    while endgame != True:
        pause

label icecreamgirl_label:
    hide screen status01
    show screen icecreamgirl_screen

    mc "Should I assign someone to this job?"
    menu:
        "Silvia" if (silvbought == True and silv_is_dead == False):
            $ missions_icecreamgirl_enabled = False
            $ silv_is_dead = True
            $ missions_icecreamgirl = "silvia"
            play sound "audio/depress.mp3" volume 3
            show sad_silv at up_happy
            "[yel]Silvia doesn't seem confident about the job..."
            hide screen icecreamgirl_screen
            hide sad_silv at up_happy
            show screen missionscreen
        "Estelle" if (estebought == True and este_is_dead == False):
            $ missions_icecreamgirl_enabled = False
            $ este_is_dead = True
            $ missions_icecreamgirl = "estelle"
            play sound "audio/depress.mp3" volume 3
            show sad_este at up_happy
            "[yel]Estelle doesn't appear motivated to work..."
            hide screen icecreamgirl_screen
            hide sad_este at up_happy
            show screen missionscreen
        "Makoto" if (makobought == True and mako_is_dead == False):
            $ missions_icecreamgirl_enabled = False
            $ mako_is_dead = True
            $ missions_icecreamgirl = "makoto"
            play sound "audio/coins.mp3" volume 3
            show love_mako at up_happy
            "[yel]Makoto is willing to put her building skills to the task..."
            hide screen icecreamgirl_screen
            hide love_mako at up_happy
            show screen missionscreen
        "Serena" if (serebought == True and sere_is_dead == False):
            $ missions_icecreamgirl_enabled = False
            $ sere_is_dead = True
            $ missions_icecreamgirl = "serena"
            play sound "audio/coins.mp3" volume 3
            show love_sere at up_happy
            "[yel]Serena is up to the task!"
            hide screen icecreamgirl_screen
            hide love_sere at up_happy
            show screen missionscreen
        "Nevermind..." if True:
            hide screen icecreamgirl_screen
            show screen missionscreen
    while endgame != True:
        pause

label model_label:
    hide screen status01
    show screen model_screen

    mc "Should I assign someone to this job?"
    menu:
        "Silvia" if (silvbought == True and silv_is_dead == False):
            $ missions_model_enabled = False
            $ silv_is_dead = True
            $ missions_model = "silvia"
            play sound "audio/depress.mp3" volume 3
            show sad_silv at up_happy
            "[yel]Silvia doesn't seem confident about the job..."
            hide screen model_screen
            hide sad_silv at up_happy
            show screen missionscreen
        "Estelle" if (estebought == True and este_is_dead == False):
            $ missions_model_enabled = False
            $ este_is_dead = True
            $ missions_model = "estelle"
            play sound "audio/coins.mp3" volume 3
            show love_este at up_happy
            "[yel]Estelle appears excited about the task!"
            hide screen model_screen
            hide love_este at up_happy
            show screen missionscreen
        "Makoto" if (makobought == True and mako_is_dead == False):
            $ missions_model_enabled = False
            $ mako_is_dead = True
            $ missions_model = "makoto"
            play sound "audio/coins.mp3" volume 3
            show love_mako at up_happy
            "[yel]Makoto thinks this is a horrible idea..."
            hide screen model_screen
            hide love_mako at up_happy
            show screen missionscreen
        "Serena" if (serebought == True and sere_is_dead == False):
            $ missions_model_enabled = False
            $ sere_is_dead = True
            $ missions_model = "serena"
            play sound "audio/coins.mp3" volume 3
            show love_sere at up_happy
            "[yel]Serena is willing to give it a shot..."
            hide screen model_screen
            hide love_sere at up_happy
            show screen missionscreen
        "Nevermind..." if True:
            hide screen model_screen
            show screen missionscreen
    while endgame != True:
        pause
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
