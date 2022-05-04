label sleeptrigger:

    if (disabled or mainquest < 9):
        "I can't sleep yet. There are things that I still have to do."
        jump mcroomlabel

    menu:
        "Should I go to sleep? [blu](Skips a day)" if True:
            hide screen status01
            scene whitescreen with dissolve
            call advanceday
            call respawn
            call charquest
            if (currentday02 == 0):
                scene whitescreen with dissolve
                call deathandtaxes

            jump mcroomlabel
        "Take a nap... [blu](Skips an hour)" if (timeofday != 5):
            $ timeofday += 1
            jump mcroomlabel
        "Stay up..." if True:
            pass

label mcroomlabel:
    $ outside = False
    $ location = "mcroom"

    call charevents

    if (timeofday >= 4):
        scene black with dissolve
        scene mcroom_night with dissolve
    elif True:
        scene black with dissolve
        scene mcroom_day with dissolve

    show screen status01
    call screen mcroom_screen

label hallwaylabel_01:
    $ outside = False
    $ location = "hallway_01"

    call charevents

    if (timeofday >= 4):
        scene black with dissolve
        scene hallway01_night with dissolve
    elif True:
        scene black with dissolve
        scene hallway01_day with dissolve

    show screen status01
    call screen hallway_screen_01

label hallwaylabel_02:
    $ outside = False
    $ location = "hallway_02"

    call charevents

    if (timeofday >= 4):
        scene black with dissolve
        scene hallway02_night with dissolve
    elif True:
        scene black with dissolve
        scene hallway02_day with dissolve

    show screen status01
    call screen hallway_screen_02

label esteroomlabel:
    $ outside = False
    $ location = "esteroom"

    call charevents

    if (timeofday == 5 and este_is_dead == False):
        scene black with dissolve
        scene esteroom_midnight with dissolve
    elif (timeofday >= 4):
        scene black with dissolve
        scene esteroom_night with dissolve
    elif True:
        scene black with dissolve
        scene esteroom_day with dissolve

    show screen status01
    call screen esteroom_screen

label silvroomlabel:
    $ outside = False
    $ location = "silvroom"

    call charevents

    if (timeofday == 5 and silv_is_dead == False):
        scene black with dissolve
        scene silvroom_midnight with dissolve
    elif (timeofday == 4):
        scene black with dissolve
        scene silvroom_night with dissolve
    elif True:
        scene black with dissolve
        scene silvroom_day with dissolve

    show screen status01
    call screen silvroom_screen

label azulroomlabel:
    $ outside = False
    $ location = "azulroom"

    call charevents

    if (azulbought == False):
        "There's nothing but junk inside this room..."
        jump hallwaylabel_02
    elif (timeofday == 5 and azul_is_dead == False):
        scene black with dissolve
        scene azulroom_midnight_01 with dissolve
    elif (timeofday == 5 and azul_is_dead):
        scene black with dissolve
        scene azulroom_midnight_02 with dissolve
    elif (timeofday >= 4):
        scene black with dissolve
        scene azulroom_night with dissolve
    elif True:
        scene black with dissolve
        scene azulroom_day with dissolve

    show screen status01
    call screen azulroom_screen

    jump hallwaylabel_02

label sereroomlabel:
    $ outside = False
    $ location = "sereroom"

    call charevents

    if (serebought and weekday == False and timeofday == 3 and voytime == False):
        hide screen status01
        scene black with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        $ voytime = True
        mc "..."
        mc "I hear rustling of clothing..."
        menu:
            "Take a peek..." if True:
                show voy_sere_01 with Dissolve(1)
                $ renpy.pause(1.5, hard=True)
                show voy_sere_02 with Dissolve(.5)
                $ renpy.pause(1.5, hard=True)
                show voy_sere_03 with Dissolve(.5)
                $ renpy.pause(1.5, hard=True)
                mc "..."
                jump hallwaylabel_02
            "Some other time..." if True:
                jump hallwaylabel_02

    if (serebought == False):
        "There's nothing but junk inside this room..."
        jump hallwaylabel_02
    elif (timeofday == 5 and sere_is_dead == False):
        scene black with dissolve
        scene sereroom_midnight_01 with dissolve
    elif (timeofday == 5 and sere_is_dead):
        scene black with dissolve
        scene sereroom_midnight_02 with dissolve
    elif (timeofday >= 4):
        scene black with dissolve
        scene sereroom_night with dissolve
    elif True:
        scene black with dissolve
        scene sereroom_day with dissolve

    show screen status01
    call screen sereroom_screen

    jump hallwaylabel_02

label bathroomlabel:
    $ outside = False
    $ location = "bathroom"

    call charevents





    if (mainquest >= 9 and timeofday == 0 and voytime == False):
        hide screen status01
        scene black with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        $ voytime = True
        mc "..."
        mc "I hear someone taking a shower..."
        menu:
            "Take a peek..." if True:
                call voylabel
                jump hallwaylabel_02
            "Some other time..." if True:
                jump hallwaylabel_02

    if (timeofday >= 4):
        scene black with dissolve
        scene bathroom_night with dissolve
    elif True:
        scene black with dissolve
        scene bathroom_day with dissolve

    show screen status01
    call screen bathroom_screen

label livingroomlabel:
    $ outside = False
    $ location = "livingroom"

    call charevents










    if (timeofday >= 4):
        scene black with dissolve
        scene livingroom_night with dissolve
    elif True:
        scene black with dissolve
        scene livingroom_day with dissolve

    show screen status01
    call screen livingroom_screen

label streetlabel_01:
    $ outside = True
    $ location = "street_01"

    call charevents

    if (timeofday >= 3):
        scene black with dissolve
        scene street01_night with dissolve
    elif True:
        scene black with dissolve
        scene street01_day with dissolve

    show screen status01
    call screen street_screen_01

label streetlabel_02:
    $ outside = True
    $ location = "street_02"

    call charevents

    if (timeofday >= 3):
        scene black with dissolve
        scene street02_night with dissolve
    elif True:
        scene black with dissolve
        scene street02_day with dissolve

    show screen status01
    call screen street_screen_02

label streetlabel_03:
    $ outside = True
    $ location = "street_03"

    call charevents

    if (timeofday >= 3):
        scene black with dissolve
        scene street03_night with dissolve
    elif True:
        scene black with dissolve
        scene street03_day with dissolve

    show screen status01
    call screen street_screen_03

label streetlabel_04:
    $ outside = True
    $ location = "street_04"

    call charevents

    if (timeofday >= 3):
        scene black with dissolve
        scene street04_night with dissolve
    elif True:
        scene black with dissolve
        scene street04_day with dissolve

    show screen status01
    call screen street_screen_04

label parklabel_01:
    $ outside = True
    $ location = "park_01"

    call charevents





    if (timeofday == 5):
        scene black with dissolve
        scene park01_night with dissolve
    elif (timeofday >= 3):
        scene black with dissolve
        scene park01_evening with dissolve
    elif True:
        scene black with dissolve
        scene park01_day with dissolve

    show screen status01
    call screen park_screen_01

label parklabel_02:
    $ outside = True
    $ location = "park_02"

    call charevents

    if (timeofday == 5):
        scene black with dissolve
        scene park02_night with dissolve
    elif (timeofday >= 3):
        scene black with dissolve
        scene park02_evening with dissolve
    elif True:
        scene black with dissolve
        scene park02_day with dissolve

    show screen status01
    call screen park_screen_02

label parklabel_03:
    $ outside = True
    $ location = "park_03"

    call charevents

    if (timeofday == 5):
        scene black with dissolve
        scene park03_night with dissolve
    elif (timeofday >= 3):
        scene black with dissolve
        scene park03_evening with dissolve
    elif True:
        scene black with dissolve
        scene park03_day with dissolve

    show screen status01
    call screen park_screen_03

label parklabel_04:
    $ outside = True
    $ location = "park_04"

    call charevents





    if (timeofday == 5):
        scene black with dissolve
        scene park04_night with dissolve
    elif (timeofday >= 3):
        scene black with dissolve
        scene park04_evening with dissolve
    elif True:
        scene black with dissolve
        scene park04_day with dissolve

    show screen status01
    call screen park_screen_04

label cityhalllabel_01:
    $ outside = True
    $ location = "cityhall_01"

    call charevents





    if (timeofday == 3):
        scene black with dissolve
        scene cityhall01_evening with dissolve
    elif (timeofday >= 4):
        scene black with dissolve
        scene cityhall01_night with dissolve
    elif True:
        scene black with dissolve
        scene cityhall01_day with dissolve

    show screen status01
    call screen cityhall_screen_01

label cityhalllabel_02:
    $ outside = True
    $ location = "cityhall_02"

    call charevents

    if (timeofday == 3):
        scene black with dissolve
        scene cityhall02_evening with dissolve
    elif (timeofday >= 4):
        scene black with dissolve
        scene cityhall02_night with dissolve
    elif True:
        scene black with dissolve
        scene cityhall02_day with dissolve

    show screen status01
    call screen cityhall_screen_02

label buildersguildlabel:
    $ outside = True
    $ location = "buildersguild"

    call charevents

    if (timeofday == 3):
        scene black with dissolve
        scene buildersguild_evening with dissolve
    elif (timeofday >= 4):
        scene black with dissolve
        scene buildersguild_night with dissolve
    elif True:
        scene black with dissolve
        scene buildersguild_morning with dissolve

    show screen status01
    call screen buildersguild_screen

label onsenlabel:
    $ outside = True
    $ location = "onsen_01"

    call charevents

    if (timeofday >= 3):
        scene black with dissolve
        scene onsen01_night with dissolve
    elif True:
        scene black with dissolve
        scene onsen01_morning with dissolve

    show screen status01
    call screen onsen_screen_01

label beachlabel_01:
    $ outside = True
    $ location = "beach_01"

    call charevents

    if (timeofday == 5):
        scene black with dissolve
        scene beach01_midnight with dissolve
    elif (timeofday >= 3):
        scene black with dissolve
        scene beach01_evening with dissolve
    elif True:
        scene black with dissolve
        scene beach01_morning with dissolve

    show screen status01
    call screen beach_screen_01

label beachlabel_02:
    $ outside = True
    $ location = "beach_02"

    call charevents

    if (timeofday == 5):
        scene black with dissolve
        scene beach02_midnight with dissolve
    elif (timeofday >= 3):
        scene black with dissolve
        scene beach02_evening with dissolve
    elif True:
        scene black with dissolve
        scene beach02_morning with dissolve

    show screen status01
    call screen beach_screen_02

label beachlabel_03:
    $ outside = True
    $ location = "beach_03"

    call charevents

    if (timeofday == 5):
        scene black with dissolve
        scene beach03_midnight with dissolve
    elif (timeofday >= 3):
        scene black with dissolve
        scene beach03_evening with dissolve
    elif True:
        scene black with dissolve
        scene beach03_morning with dissolve

    show screen status01
    call screen beach_screen_03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
