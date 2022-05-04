
label endless:
    while endgame != True:
        pause
    return

label fftrigger:

    if (mainquest >= 9 and disabled == False):
        if (timeofday < 5):
            $ timeofday += 1
    elif True:
        "Skipping time is temporarily unavailable."

    if (location == "mcroom"):
        jump mcroomlabel
    elif (location == "hallway_01"):
        jump hallwaylabel_01
    elif (location == "hallway_02"):
        jump hallwaylabel_02
    elif (location == "esteroom"):
        jump esteroomlabel
    elif (location == "silvroom"):
        jump silvroomlabel
    elif (location == "azulroom"):
        jump azulroomlabel
    elif (location == "sereroom"):
        jump sereroomlabel
    elif (location == "bathroom"):
        jump bathroomlabel
    elif (location == "livingroom"):
        jump livingroomlabel
    elif (location == "street_01"):
        jump streetlabel_01
    elif (location == "street_02"):
        jump streetlabel_02
    elif (location == "street_03"):
        jump streetlabel_03
    elif (location == "street_04"):
        jump streetlabel_04
    elif (location == "park_01"):
        jump parklabel_01
    elif (location == "park_02"):
        jump parklabel_02
    elif (location == "park_03"):
        jump parklabel_03
    elif (location == "park_04"):
        jump parklabel_04
    elif (location == "cityhall_01"):
        jump cityhalllabel_01
    elif (location == "cityhall_02"):
        jump cityhalllabel_02
    elif (location == "buildersguild"):
        jump buildersguildlabel
    elif (location == "onsen_01"):
        jump onsenlabel
    elif (location == "beach_01"):
        jump beachlabel_01
    elif (location == "beach_02"):
        jump beachlabel_02
    elif (location == "beach_03"):
        jump beachlabel_03
    elif True:
        "Error code: fftrigger 01_chat"
        return



label livingroom_dinner_label:
    hide screen status01
    show livingroom_dinner 01 with dissolve

    menu:
        "Have dinner together... [red](+Affection)" if True:
            $ timeofday += 1
            scene black with dissolve
            show livingroom_dinner 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            "[yel]You spent some time with the household."
            show livingroom_dinner 03 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            call charaff ("silvia")
            if (estebought == True):
                call charaff ("estelle")
            jump livingroomlabel
        "Leave..." if True:
            show livingroom_dinner 04 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Maybe next time..."
            jump livingroomlabel



label esteroom_estestudy_label:
    $ location = "esteroom_estestudy"
    hide screen status01
    call charevents

    scene esteroom_estestudy 01 with dissolve
    show esteroom_estestudy_vid

    menu:
        "Talk..." if True:
            mc "So Estelle..."
            mc "Looks like you're studying, huh?"
            hide esteroom_estestudy_vid
            show esteroom_estestudy 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Of course!"
            este "I'm a student for the esteemed Scarlet Magic Academy, after all!"
            show esteroom_estestudy 03 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "But more importantly..."
            este "What are you doing inside my room, pervert?"
            jump esteroom_estestudy_label
        "Spend time together... [red](+Affection)" if (disabled == False):
            menu:
                "Help with homework..." if True:
                    $ timeofday += 1
                    scene black with dissolve
                    show esteroom_estestudy 05 with dissolve
                    "[yel]You spent some time with Estelle."
                    show esteroom_estestudy 06 with dissolve
                "Request a handjob..." if esteevents >= 6:
                    $ timeofday += 1
                    scene black with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    show este02_03_01 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    pause
                    "[yel]You spent some time with Estelle."
                "Leave..." if True:
                    jump esteroomlabel
            call charaff ("estelle")
            jump esteroomlabel
        "Give gift... [red](+Affection)" if (inventory_tutorial and givegift == False and disabled == False):
            call chargift ("estelle")
            hide esteroom_estestudy_vid
            show esteroom_estestudy 02 with dissolve
            este "Hehe..."
            este "Thanks, [mc]!"
            jump esteroomlabel
        "Leave..." if True:







            jump esteroomlabel

label esteroom_estestretch_label:
    $ location = "esteroom_estestretch"
    hide screen status01
    call charevents

    scene esteroom_estestretch 01 with dissolve
    show esteroom_estestretch_vid

    menu:
        "Talk..." if True:
            hide esteroom_estestretch_vid
            show esteroom_estestretch 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Oh, Estelle..."
            mc "Did I catch you at a bad time?"
            show esteroom_estestretch 03 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Eh?"
            este "What do you want, [mc]?"
            show esteroom_estestretch 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Nothing, really..."
            mc "I just didn't expect to see you working out..."
            show esteroom_estestretch 04 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Hehe..."
            este "A mage must not only have a strong mind, but a strong body too!"
            jump esteroom_estestretch_label
        "Help exercise... [red](+Affection)" if (estebought == True and disabled == False):
            $ timeofday += 1
            scene black with dissolve
            show esteroom_estestretch 05 with dissolve
            "[yel]You spent some time with Estelle."
            show esteroom_estestretch 06 with dissolve
            call charaff ("estelle")
            jump esteroomlabel
        "Give gift... [red](+Affection)" if (inventory_tutorial and givegift == False and disabled == False):
            call chargift ("estelle")
            hide esteroom_estestretch_vid
            show esteroom_estestretch 04 with dissolve
            este "Hehe..."
            este "Thanks, [mc]!"
            jump esteroomlabel
        "Leave..." if True:






            jump esteroomlabel

label livingroom_estetv_label:
    $ location = "livingroom_estetv"
    hide screen status01
    call charevents

    scene livingroom_estetv 01 with dissolve
    show livingroom_estetv_vid

    menu:
        "Talk..." if True:
            mc "Hey, Estelle..."
            mc "Didn't we used to always watch TV together?"
            hide livingroom_estetv_vid
            show livingroom_estetv 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Of course!"
            este "Remember when we got hold of those scary movies when [mil!c] left us home alone?"
            show livingroom_estetv 01 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Oh yeah..."
            mc "You used to close your eyes and squeeze my arm whenever the scary stuff happened."
            show livingroom_estetv 03 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Er..."
            este "I-I don't remember that part..."
            jump livingroom_estetv_label
        "Watch TV together... [red](+Affection)" if (estebought == True and disabled == False):
            $ timeofday += 1
            scene black with dissolve
            show livingroom_estetv 05 with dissolve
            "[yel]You spent some time with Estelle."
            show livingroom_estetv 06 with dissolve
            call charaff ("estelle")
            jump livingroomlabel
        "Give gift... [red](+Affection)" if (estebought == True and inventory_tutorial and givegift == False and disabled == False):
            call chargift ("estelle")
            hide livingroom_estetv_vid
            show livingroom_estetv 04 with dissolve
            este "Ah, for me?"
            este "Much appreciated, [mc]!"
            jump livingroomlabel
        "Leave..." if True:






            jump livingroomlabel

label esteroom_estenight_label:
    $ location = "esteroom_estenight"
    hide screen status01
    call charevents

    scene esteroom_estenight 01 with dissolve
    show esteroom_estenight_vid

    menu:
        "Talk..." if True:
            mc "Hey, Estelle..."
            mc "Getting ready for bed?"
            hide esteroom_estenight_vid
            show esteroom_estenight 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Uh-huh..."
            este "Unlike you, I have to get up early in the morning."
            show esteroom_estenight 01 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Sure..."
            mc "Good night, Estelle."
            jump esteroom_estenight_label
        "Sleep together... [red](+Affection)" if (disabled == False):
            hide esteroom_estenight_vid
            show esteroom_estenight 03 with dissolve
            este "Eh!?"
            este "N-No way..."
            este "We can't do that unless we're m-married..."
            play sound "audio/depress.mp3" volume 3
            show sad_este at up_happy
            "[yel]Estelle isn't willing to share her bed..."
            jump esteroomlabel
        "Leave..." if True:
            jump esteroomlabel



label silvroom_silvclean_label:
    $ location = "silvroom_silvclean"
    hide screen status01
    call charevents

    scene silvroom_silvclean 01 with dissolve
    show silvroom_silvclean_vid

    menu:
        "Talk..." if True:
            mc "Hey, [mil!c]..."
            mc "What are you up to?"
            hide silvroom_silvclean_vid
            show silvroom_silvclean 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Oh, I'm just tidying up my room..."
            silv "Since I'm a [yel]homemaker{/color}, I just can't stand it when a house is unclean..."
            jump silvroom_silvclean_label
        "Spend time together... [red](+Affection)" if (disabled == False):
            $ timeofday += 1
            scene black with dissolve
            show silvroom_silvclean 04 with dissolve
            "[yel]You spent some time helping Silvia."
            show silvroom_silvclean 05 with dissolve
            call charaff ("silvia")
            jump silvroomlabel
        "Give gift... [red](+Affection)" if (inventory_tutorial and givegift == False and disabled == False):
            call chargift ("silvia")
            hide silvroom_silvclean_vid
            show silvroom_silvclean 03-2 with dissolve
            silv "Oh my..."
            silv "Thank you, [mc]!"
            jump silvroomlabel
        "Leave..." if True:





            jump silvroomlabel

label livingroom_silvkitchen_label:
    $ location = "livingroom_silvkitchen"
    hide screen status01
    call charevents

    scene livingroom_silvkitchen 01 with dissolve
    show livingroom_silvkitchen_vid

    menu:
        "Talk..." if True:
            hide livingroom_silvkitchen_vid
            show livingroom_silvkitchen 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "How are you, [mc]?"
            silv "What would you like for dinner tonight?"
            show livingroom_silvkitchen 01 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Anything's fine..."
            mc "Thank you, [mil!c]."
            jump livingroom_silvkitchen_label
        "Spend time together... [red](+Affection)" if (disabled == False):
            menu:
                "Help with dinner..." if True:
                    $ timeofday += 1
                    scene black with dissolve
                    show livingroom_silvkitchen 04 with dissolve
                    "[yel]You spent some time helping Silvia."
                    show livingroom_silvkitchen 05 with dissolve
                "Rub her ass..." if silvevents >= 5:
                    $ timeofday += 1
                    scene black with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    show silv02_02_02 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    pause
                    "[yel]You spent some time with Silvia."
                "Request doggystyle sex..." if silvevents >= 5:
                    $ timeofday += 1
                    scene black with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    show silv02_02_03 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    pause
                    show silv02_02_04 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    pause
                    "[yel]You spent some time with Silvia."
                "Leave..." if True:
                    jump livingroomlabel
            call charaff ("silvia")
            jump livingroomlabel
        "Give gift... [red](+Affection)" if (inventory_tutorial and givegift == False and disabled == False):
            call chargift ("silvia")
            hide livingroom_silvkitchen_vid
            show livingroom_silvkitchen 03 with dissolve
            silv "Oh, [mc]! I love it!"
            jump livingroomlabel
        "Leave..." if True:





            jump livingroomlabel

label silvroom_silvsleep_label:
    $ location = "silvroom_silvsleep"
    hide screen status01
    call charevents

    scene silvroom_silvsleep 01 with dissolve
    show silvroom_silvsleep_vid

    menu:
        "Talk..." if True:
            hide silvroom_silvsleep_vid
            show silvroom_silvsleep 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "[mc], you've been up all day..."
            silv "Shouldn't you get ready for bed?"
            show silvroom_silvsleep 01 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "I will soon..."
            show silvroom_silvsleep 03 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Well, I'm beat..."
            if (weekday):
                silv "I have to get up early for work tomorrow..."
            elif True:
                silv "I have to get up early to go to the market tomorrow..."
            jump silvroom_silvsleep_label
        "Spend time together... [red](+Affection)" if (disabled == False):
            menu:
                "Sleep together... [blu](Skips to next day)" if True:
                    hide silvroom_silvsleep_vid
                    show silvroom_silvsleep 04 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    call charaff ("silvia")
                    call advanceday
                    call respawn
                    call charquest
                    if (currentday02 == 0):
                        scene whitescreen with dissolve
                        call deathandtaxes

                    jump silvroomlabel
                "Request a handjob..." if silvbought:
                    $ timeofday += 1
                    scene black with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    show prologue_11_01 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    pause
                    show prologue_11_02 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    pause
                    "[yel]You spent some time with Silvia."
                "Leave..." if True:
                    jump silvroomlabel
            call charaff ("silvia")
            jump silvroomlabel
        "Leave..." if True:





            jump silvroomlabel

label street01_silvwalk_label:
    $ location = "street_01_silv"
    hide screen status01
    call charevents

    scene street01_silvwalk 01 with dissolve
    show street01_silvwalk_vid

    menu:
        "Talk..." if True:
            mc "Hey there, [mil!c]."
            mc "Coming home from the market?"
            hide street01_silvwalk_vid
            show street01_silvwalk 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Yes, sweetheart..."
            silv "I like going in the morning because the fruits are vegetables are at their freshest!"
            jump street01_silvwalk_label
        "Help with groceries... [red](+Affection)" if (disabled == False):
            $ timeofday += 1
            scene black with dissolve
            show street01_silvwalk 04 with dissolve
            "[yel]You spent some time with Silvia."
            show street01_silvwalk 05 with dissolve
            call charaff ("silvia")
            jump streetlabel_01
        "Give gift... [red](+Affection)" if (inventory_tutorial and givegift == False and disabled == False):
            call chargift ("silvia")
            hide street01_silvwalk_vid
            show street01_silvwalk 03 with dissolve
            silv "Oh?"
            silv "Thank you, [mc]."
            jump streetlabel_01
        "Leave..." if True:





            jump streetlabel_01



label street01_serestore_label:
    $ location = "street_01_sere"
    hide screen status01
    call charevents

    show screen storescreen

    scene street01_serestore 01 with dissolve
    show street01_serestore_vid

    menu:
        "Talk..." if True:
            hide screen storescreen
            mc "Hey there, Serena..."
            mc "How's the store doing?"
            hide street01_serestore_vid
            show street01_serestore 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Hiya, [mc]!"
            sere "It's usually slow, but..."
            sere "...during the [yel]afternoon{/color}, business really picks up!"
            jump street01_serestore_label
        "Work at store... [red](+Affection)" if (mainquest >= 9 and serework == False and disabled == False):
            if (timeofday == 2):
                $ timeofday += 1
                call charwork ("serena")
                call charaff ("serena")
                hide screen storescreen
                jump streetlabel_01
            elif True:
                menu:
                    "How long should I work for?"
                    "Part-time..." if True:
                        call charwork ("serena")
                        call charaff ("serena")
                        $ timeofday += 1
                        hide screen storescreen
                        jump streetlabel_01
                    "Full-time..." if (timeofday < 2):
                        call charwork ("serena_fulltime")
                        call charaff ("serena")
                        $ timeofday += 2
                        hide screen storescreen
                        jump streetlabel_01
                    "Overtime..." if (timeofday == 0):
                        call charwork ("serena_overtime")
                        call charaff ("serena")
                        $ timeofday += 4
                        hide screen storescreen
                        jump streetlabel_01
                    "Leave..." if True:
                        hide screen storescreen
                        jump streetlabel_01
        "Leave..." if True:
            hide screen storescreen





            jump streetlabel_01

label street01_serewalk_label:
    $ location = "street_01_serewalk"
    hide screen status01
    call charevents

    scene street01_serewalk 01 with dissolve
    show street01_serewalk_vid

    menu:
        "Talk..." if True:
            mc "All done for today, Serena?"
            hide street01_serewalk_vid
            show street01_serewalk 03 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "That's right..."
            show street01_serewalk 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "I just got finished and I'm heading home."
            show street01_serewalk 01 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Hmm..."
            mc "Just be careful, okay? It can be dangerous at night..."
            show street01_serewalk 03 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Ah, don't worry..."
            show street01_serewalk 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "I can take care of myself. I carry around mace and I'm not afraid to use it..."
            show street01_serewalk 01 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            show street01_serewalk 04 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            sere "W-Wait a second..."
            show street01_serewalk 05 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "On second thought, maybe you're right..."
            show street01_serewalk 06 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "I'd feel much safer if there was a big, strong man who could walk me home every night..."
            jump street01_serewalk_label
        "Walk home together... [red](+Affection)" if (disabled == False):
            $ timeofday += 1
            scene black with dissolve
            show street01_serewalk 07 with dissolve
            "[yel]You spent some time with Serena."
            show street01_serewalk 08 with dissolve
            call charaff ("serena")
            jump streetlabel_01
        "Leave..." if True:
            jump streetlabel_01

    label sereroom_serehair_label:
        $ location = "sereroom_serehair"
        hide screen status01
        call charevents

        scene sereroom_serehair 01 with dissolve
        show sereroom_serehair_vid

        menu:
            "Talk..." if True:
                hide sereroom_serehair_vid
                show sereroom_serehair 02 with Dissolve(.5)
                $ renpy.pause(.5, hard=True)
                mc "Hey there, Serena..."
                mc "About time for bed?"
                show sereroom_serehair 03 with Dissolve(.5)
                $ renpy.pause(.5, hard=True)
                sere "Uh-huh..."
                sere "It was already a long day at work..."
                show sereroom_serehair 02 with Dissolve(.5)
                $ renpy.pause(.5, hard=True)
                mc "..."
                mc "Do you want some company?"
                show sereroom_serehair 04 with Dissolve(.5)
                $ renpy.pause(.5, hard=True)
                sere "Oh, [mc]..."
                jump sereroom_serehair_label
            "Spend time together... [red](+Affection)" if (disabled == False):
                menu:
                    "Sleep together... [blu](Skips to next day)" if True:
                        $ timeofday += 1
                        scene black with Dissolve(.5)
                        $ renpy.pause(.5, hard=True)
                        show sereroom_sleep with Dissolve(.5)
                        $ renpy.pause(.5, hard=True)
                        "[yel]You spent some time with Serena."
                        call advanceday
                        call respawn
                        call charquest
                        if (currentday02 == 0):
                            scene whitescreen with dissolve
                            call deathandtaxes
                    "Request to eat pussy..." if True:

                        $ timeofday += 1
                        scene black with Dissolve(.5)
                        $ renpy.pause(.5, hard=True)
                        show serebought_01 with Dissolve(.5)
                        $ renpy.pause(.5, hard=True)
                        pause
                        show serebought_02 with Dissolve(.5)
                        $ renpy.pause(.5, hard=True)
                        pause
                        show serebought_03 with Dissolve(.5)
                        $ renpy.pause(.5, hard=True)
                        pause
                        "[yel]You spent some time with Serena."
                    "Request a handjob..." if True:
                        $ timeofday += 1
                        scene black with Dissolve(.5)
                        $ renpy.pause(.5, hard=True)
                        show serebought_04 with Dissolve(.5)
                        $ renpy.pause(.5, hard=True)
                        pause
                        "[yel]You spent some time with Serena."
                    "Request to have sex..." if True:
                        $ timeofday += 1
                        scene black with Dissolve(.5)
                        $ renpy.pause(.5, hard=True)
                        show serebought_05 with Dissolve(.5)
                        $ renpy.pause(.5, hard=True)
                        pause
                        show serebought_06 with Dissolve(.5)
                        $ renpy.pause(.5, hard=True)
                        pause
                        "[yel]You spent some time with Serena."
                    "Leave..." if True:
                        jump sereroomlabel
                call charaff ("serena")
                jump sereroomlabel
            "Leave..." if True:
                jump sereroomlabel



label park04_azulrock_label:
    $ location = "park_04_azul"
    hide screen status01
    call charevents

    scene park04_azulrock 01 with dissolve
    show park04_azulrock_vid

    menu:
        "Talk..." if True:
            mc "Good morning, Azula."
            mc "Er, why are you laying on that rock..."
            hide park04_azulrock_vid
            show park04_azulrock 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            azul "Hehe..."
            azul "This lake has always been one of my favorite hotspots in Scarlet..."
            azul "I'm so happy that it's still around after all these years..."
            show park04_azulrock 01 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Hmm..."
            mc "How old are you exactly, Azula?"
            show park04_azulrock 03 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            azul "Er..."
            azul "I'll let the theorycrafters figure that one out..."
            jump park04_azulrock_label
        "Spend time together... [red](+Affection)" if (disabled == False):
            menu:
                "Provide essence..." if True:
                    $ timeofday += 1
                    scene black with dissolve
                    show park04_azulrock 04 with dissolve
                    "[yel]You spent some time with Azula."
                    show park04_azulrock 05 with dissolve
                "Request blowjob..." if azulevents >= 3:
                    $ timeofday += 1
                    scene black with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    show azul01_02_01 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    pause
                    show azul01_02_02 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    pause
                    "[yel]You spent some time with Azula."
                "Leave..." if True:
                    jump parklabel_04
            call charaff ("azula")
            jump parklabel_04
        "Give gift... [red](+Affection)" if (inventory_tutorial and givegift == False and disabled == False):
            call chargift ("azula")
            hide park04_azulrock_vid
            show park04_azulrock 02 with dissolve
            azul "Hehe..."
            azul "It's great, [mc]! Thank you!"
            jump parklabel_04
        "Leave..." if True:
            jump parklabel_04

label park02_azulfly_label:
    $ location = "park_02_azulfly"
    hide screen status01
    call charevents

    scene park02_azulfly 01 with dissolve
    show park02_azulfly_vid

    menu:
        "Talk..." if True:
            hide park02_azulfly_vid
            show park02_azulfly 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Amazing, Azula..."
            mc "How are you able to do that?"
            show park02_azulfly 03 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            azul "Ah, [mc]..."
            azul "Perhaps it's because this creature views me as {i}harmless{/i}."
            show park02_azulfly 04 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            azul "Hehe, I'm not surprised..."
            azul "As the Goddess of this land, I have a great respect for nature."
            jump park02_azulfly_label
        "Spend time together... [red](+Affection)" if (disabled == False):
            $ timeofday += 1
            scene black with dissolve
            show park02_azulfly 05 with dissolve
            "[yel]You spent some time with Azula."
            show park02_azulfly 06 with dissolve
            call charaff ("azula")
            jump parklabel_02
        "Give gift... [red](+Affection)" if (inventory_tutorial and givegift == False and disabled == False):
            call chargift ("azula")
            hide park02_azulfly_vid
            show park02_azulfly 03 with dissolve
            azul "As expected of my male companion!"
            azul "Thank you, [mc]."
            jump parklabel_02
        "Leave..." if True:
            jump parklabel_02



label street02_culatalk_label:
    $ location = "street_02_cula"
    hide screen status01
    call charevents
    show screen storescreen
    show screen flower_rates_screen

    scene street02_cula 01 with dissolve
    show street02_cula_vid

    menu:
        "Talk..." if True:
            hide screen storescreen
            hide screen flower_rates_screen
            hide street02_cula_vid
            show street02_cula 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mvcula "I'm not much of a talker..."
            mvcula "Unless it's business related, please refrain from asking personal questions."
            mvcula "I'm just an NPC character and I'll never win a [oj]Patreon Poll{/color}, so what's the point of getting close to me?"
            show street02_cula 01 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "S-Sure..."
            jump street02_culatalk_label
        "Purchase Magical Flower... [blu]$[magicflower_price]" if ((inventory_magicflower < 3) and silvevents >= 1):
            hide screen storescreen
            hide screen flower_rates_screen
            if (magicflower_price > money):
                hide street02_cula_vid
                show street02_cula 02 with dissolve
                mvcula "You don't have enough money..."
                jump street02_culatalk_label
            elif True:
                hide screen storescreen
                hide screen flower_rates_screen
                hide street02_cula_vid
                show street02_cula 03 with dissolve
                mvcula "Make sure you give this flower to someone special to you."
                play sound "audio/coins.mp3" volume 3
                show love_cula at up_happy
                "[yel]You paid $[magicflower_price] to Flower Girl!"
                $ money -= magicflower_price
                $ inventory_magicflower += 1
                jump street02_culatalk_label
        "Sell Rare Flowers..." if flowers_r > 0:
            hide screen storescreen
            hide screen flower_rates_screen
            hide street02_cula_vid
            show street02_cula 03 with dissolve
            $ flowers_total = flowers_r * flower_prices_r
            mvcula "Will you take [yel]$[flowers_total]{/color} for your [yel][flowers_r] Rare Flowers{/color}?"
            show street02_cula 01 with dissolve
            menu:
                "Deal!" if True:
                    play sound "audio/coins.mp3" volume 3
                    show love_cula at up_happy
                    "[yel]You gained $[flowers_total]!!!"
                    $ money += flowers_total
                    $ flowers_r = 0
                    jump street02_culatalk_label
                "No deal!" if True:
                    jump street02_culatalk_label
        "Sell SR Flowers..." if flowers_sr > 0:
            hide screen storescreen
            hide screen flower_rates_screen
            hide street02_cula_vid
            show street02_cula 03 with dissolve
            $ flowers_total = flowers_sr * flower_prices_sr
            mvcula "Will you take [yel]$[flowers_total]{/color} for your [yel][flowers_sr] SR Flowers{/color}?"
            show street02_cula 01 with dissolve
            menu:
                "Deal!" if True:
                    play sound "audio/coins.mp3" volume 3
                    show love_cula at up_happy
                    "[yel]You gained $[flowers_total]!!!"
                    $ money += flowers_total
                    $ flowers_sr = 0
                    jump street02_culatalk_label
                "No deal!" if True:
                    jump street02_culatalk_label
        "Sell SSR Flowers..." if flowers_ssr > 0:
            hide screen storescreen
            hide screen flower_rates_screen
            hide street02_cula_vid
            show street02_cula 03 with dissolve
            $ flowers_total = flowers_ssr * flower_prices_ssr
            mvcula "Will you take [yel]$[flowers_total]{/color} for your [yel][flowers_ssr] SSR Flowers{/color}?"
            show street02_cula 01 with dissolve
            menu:
                "Deal!" if True:
                    play sound "audio/coins.mp3" volume 3
                    show love_cula at up_happy
                    "[yel]You gained $[flowers_total]!!!"
                    $ money += flowers_total
                    $ flowers_ssr = 0
                    jump street02_culatalk_label
                "No deal!" if True:
                    jump street02_culatalk_label
        "Sell SSG Flowers..." if flowers_ssg > 0:
            hide screen storescreen
            hide screen flower_rates_screen
            hide street02_cula_vid
            show street02_cula 03 with dissolve
            $ flowers_total = flowers_ssg * flower_prices_ssg
            mvcula "Will you take [yel]$[flowers_total]{/color} for your [yel][flowers_ssg] SSGSS Flowers{/color}?"
            show street02_cula 01 with dissolve
            menu:
                "Deal!" if True:
                    play sound "audio/coins.mp3" volume 3
                    show love_cula at up_happy
                    "[yel]You gained $[flowers_total]!!!"
                    $ money += flowers_total
                    $ flowers_ssg = 0
                    jump street02_culatalk_label
                "No deal!" if True:
                    jump street02_culatalk_label
        "Leave..." if True:
            hide screen storescreen
            hide screen flower_rates_screen





            jump streetlabel_02
    pause



label cityhall02_laursleep_label:
    $ location = "cityhall_02_laursleep"
    hide screen status01
    call charevents

    scene cityhall02_laursleep 01 with dissolve

    menu:
        "Wake up..." if True:
            if (timeofday == 0):
                mc "Princess..."
                mc "Shouldn't you be up by now?"
                show cityhall02_laursleep 02 with Dissolve(.5)
                $ renpy.pause(.5, hard=True)
                laur "Ah..."
                laur "I love you..."
                laur "...{i}Mao Mao{/i}."
                laur "Once we take down those Sky Pirates our reputation will soar..."
                laur "...and I'll be that much closer to becoming the legend I'm destined to be!"
                laur "Hehe..."
                show cityhall02_laursleep 01 with Dissolve(.5)
                $ renpy.pause(.5, hard=True)
                mc "..."
                jump cityhall02_laursleep_label
            if (timeofday == 1):
                mc "Princess..."
                mc "Why are you still sleeping..."
                show cityhall02_laursleep 02 with Dissolve(.5)
                $ renpy.pause(.5, hard=True)
                laur "Hehe..."
                laur "After years of dedicated searching, we finally discovered the long-lost Pure Heart Valley..."
                laur "Once the legendary prize of the legendary Pure Heart Valley is mine, I will become a truly legendary princess..."
                show cityhall02_laursleep 01 with Dissolve(.5)
                $ renpy.pause(.5, hard=True)
                mc "..."
                jump cityhall02_laursleep_label
            if (timeofday == 2):
                mc "Princess..."
                mc "How are you still not up yet?"
                show cityhall02_laursleep 03 with Dissolve(.5)
                $ renpy.pause(.5, hard=True)
                laur "..."
                laur "This is all my fault..."
                laur "None of this would have happened if I only acted sooner..."
                show cityhall02_laursleep 01 with Dissolve(.5)
                $ renpy.pause(.5, hard=True)
                mc "..."
                jump cityhall02_laursleep_label
        "Leave..." if True:
            if (timeofday == 2):
                mc "Sleep well, Princess."
                show cityhall02_laursleep 03 with Dissolve(.5)
                $ renpy.pause(.5, hard=True)
                laur "..."
                laur "Did I... make the wrong choice?"
                jump cityhalllabel_02
            elif (timeofday == 1):
                mc "Sleep well, Princess."
                show cityhall02_laursleep 02 with Dissolve(.5)
                $ renpy.pause(.5, hard=True)
                laur "Hehe..."
                laur "You remind me of me, and I'm pretty incredible..."
                jump cityhalllabel_02
            elif True:
                mc "Sleep well, Princess."
                show cityhall02_laursleep 02 with Dissolve(.5)
                $ renpy.pause(.5, hard=True)
                laur "Hehe..."
                laur "Another flawless victory where I did everything right..."
                jump cityhalllabel_02

label cityhall01_laurtv_label:
    $ location = "cityhall_01_laurtv"
    hide screen status01
    call charevents

    scene cityhall01_laurtv 01 with dissolve
    show cityhall01_laurtv_vid

    menu:
        "Talk..." if True:
            mc "Hey there, Princess."
            mc "Er, shouldn't you be working instead of watching videos?"
            hide cityhall01_laurtv_vid
            show cityhall01_laurtv 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            laur "Eh?"
            laur "I am working... I'm, uh, multi-tasking..."
            show cityhall01_laurtv 03 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            laur "And Mao Mao is very important to the people of Scarlet (probably)..."
            laur "Hehe..."
            show cityhall01_laurtv 01 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            jump cityhall01_laurtv_label
        "Watch Mao Mao together... [red](+Affection)" if (disabled == False):
            $ timeofday += 1
            call charwork ("laureate_01")
            call charaff ("laureate")
            jump cityhalllabel_01
        "Make a purchase..." if (disabled == False):







            call buylabel
            jump cityhalllabel_01
        "Leave..." if True:





            jump cityhalllabel_01

label cityhall01_maotv_label:
    hide screen status01

    show cityhall01_maotv 01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "What is this show?"
    show cityhall01_maotv 02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Ah, it's my favorite cartoon..."
    laur "'Mao Mao: Heroes of Pure Heart'..."
    show cityhall01_maotv 03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "It's a great show that inspires leadership, altriusm, and friendship."
    show cityhall01_maotv 02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Want to watch it with me?"
    mc "..."
    mc "Maybe some other time..."
    jump cityhalllabel_01

label cityhall02_laurphone_label:
    $ location = "cityhall_02_laurphone"
    hide screen status01
    call charevents

    scene cityhall02_laurphone 01 with dissolve
    show cityhall02_laurphone_vid

    menu:
        "Talk..." if True:
            mc "Good evening, Princess."
            mc "Uh, what are you doing with your phone?"
            hide cityhall02_laurphone_vid
            show cityhall02_laurphone 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            laur "Hehe..."
            laur "Just checking out [oj]Scarlet Law's Patreon{/color}..."
            laur "Did you know that they have official NSFW pics there?"
            show cityhall02_laurphone 03 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Yeah, everyone knows that..."
            mc "But isn't it a little bit too expensive?"
            show cityhall02_laurphone 04 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            laur "Eh?"
            laur "N-Nudes aren't cheap, you know?"
            jump cityhall02_laurphone_label
        "Spend time together... [red](+Affection)" if (disabled == False):
            $ timeofday += 1
            call charwork ("laureate_02")
            call charaff ("laureate")
            jump cityhalllabel_02
        "Make a purchase..." if (disabled == False):







            call buylabel
            jump cityhalllabel_02
        "Leave..." if True:







            jump cityhalllabel_02



label cityhall02_ferrsit_label:
    $ location = "cityhall_02_ferrsit"
    hide screen status01
    call charevents

    scene cityhall02_ferrsit 01 with dissolve
    show cityhall02_ferrsit_vid

    menu:
        "Talk..." if True:
            mc "Good morning, Ferry."
            mc "What are you up to?"
            hide cityhall02_ferrsit_vid
            show cityhall02_ferrsit 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            ferr "My duty is to safeguard the princess."
            ferr "...that includes while she's asleep."
            show cityhall02_ferrsit 01 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "I see..."
            mc "Isn't that a little..."
            show cityhall02_ferrsit 03 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            ferr "Those are my orders."
            ferr "And I shall carry them out without fail."
            jump cityhall02_ferrsit_label
        "Stand watch together... [red](Not available)" if (disabled == False):
            jump cityhalllabel_02
        "Leave..." if True:





            jump cityhalllabel_02

label cityhall01_ferrsit_label:
    $ location = "cityhall_01_ferrsit"
    hide screen status01
    call charevents

    scene cityhall01_ferrsit 01 with dissolve
    show cityhall01_ferrsit_vid

    menu:
        "Talk..." if True:
            mc "Hey there, Ferry."
            mc "What are you up to?"
            hide cityhall01_ferrsit_vid
            show cityhall01_ferrsit 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            ferr "I'm currently making a mental note of the daily complaints filed in by the citizens of Scarlet..."
            ferr "I'll be sure to review them with Her Highness when she wakes up."
            show cityhall01_ferrsit 01 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Hmm..."
            mc "Isn't that something the princess should do on her own?"
            mc "More importantly, do you ever take a day off, Ferry?"
            show cityhall01_ferrsit 03 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            ferr "Yes, Her Highness allows me time to myself during the night."
            ferr "When that happens, I head over to the [yel]park{/color} to train my body so that I can better serve her."
            show cityhall01_ferrsit 01 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            jump cityhall01_ferrsit_label
        "Hang around... [red](+Affection)" if (disabled == False):
            $ timeofday += 1
            scene black with dissolve
            show cityhall01_ferrsit 04 with dissolve
            "[yel]You spent some time with Ferry."
            show cityhall01_ferrsit 05 with dissolve
            call charaff ("ferry")
            jump cityhalllabel_01
        "Leave..." if True:





            jump cityhalllabel_01

label cityhall01_ferrlean_label:
    $ location = "cityhall_01_ferrlean"
    hide screen status01
    call charevents

    scene cityhall01_ferrlean 01 with dissolve
    show cityhall01_ferrlean_vid

    menu:
        "Talk..." if True:
            mc "Er..."
            mc "Just standing around, Ferry?"
            hide cityhall01_ferrlean_vid
            show cityhall01_ferrlean 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            ferr "Yes, that is my job."
            ferr "I shall stand guard until Her Highness tells me otherwise."
            show cityhall01_ferrlean 01 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Yeah, that's fine, but..."
            mc "You don't have to take that literally, you know?"
            mc "I'm sure Laureate wouldn't mind if you turned on the television or something."
            show cityhall01_ferrlean 03 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            ferr "If Her Highness wanted the television on, she would have instructed me to do so."
            ferr "Until then, I shall remain on watch."
            show cityhall01_ferrlean 01 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            jump cityhall01_ferrlean_label
        "Hang around... [red](Not available)" if (disabled == False):
            jump cityhalllabel_01
        "Leave..." if True:





            jump cityhalllabel_01

label park02_ferrstretch_label:
    $ location = "park_02_ferrstretch"
    hide screen status01
    call charevents

    scene park02_ferrstretch 01 with dissolve
    show park02_ferrstretch_vid

    menu:
        "Talk..." if True:
            mc "Ferry, you're in such great shape..."
            mc "How did you manage to get so strong?"
            hide park02_ferrstretch_vid
            show park02_ferrstretch 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            ferr "It's very simple..."
            show park02_ferrstretch 04 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            ferr "My workout routine involves 100 push-ups, 100 sit-ups, 100 squats..."
            show park02_ferrstretch 03 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            ferr "...and, of course, running at least 6 miles a day around Scarlet."
            show park02_ferrstretch 01 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "I-I see..."
            show park02_ferrstretch 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            ferr "I'll be expecting the same from you eventually, [mc]."
            show park02_ferrstretch 03 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            ferr "With that kind of strength, you'll be able to protect Her Highness with just one punch."
            show park02_ferrstretch 01 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            jump park02_ferrstretch_label
        "Work out with Ferry... [red](+Affection)" if (disabled == False):
            $ timeofday += 1
            scene black with dissolve
            show park02_ferrstretch 05 with dissolve
            "[yel]You spent some time with Ferry."
            show park02_ferrstretch 06 with dissolve
            call charaff ("ferry")
            jump parklabel_02
        "Leave..." if True:







            jump parklabel_02

label park01_ferrrock_label:
    $ location = "park_01_ferrrock"
    hide screen status01
    call charevents

    scene park01_ferrrock 01 with dissolve
    show park01_ferrrock_vid

    menu:
        "Talk..." if True:
            mc "Er, Ferry..."
            mc "Aren't you ever... afraid of being out here all alone at night?"
            hide park01_ferrrock_vid
            show park01_ferrrock 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            ferr "Not particularly."
            ferr "This is the only time when I can train without being disturbed."
            show park01_ferrrock 03 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            ferr "...The rest of my day is spent with Her Highness."
            show park01_ferrrock 01 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Yeah, but..."
            mc "What if you run into some {i}unsavory{/i} types?"
            show park01_ferrrock 03 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            ferr "Hmph..."
            ferr "Any cur daring enough to test me is welcome to try."
            show park01_ferrrock 04 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            ferr "I would not be a maid if I were afraid to get my hands dirty."
            show park01_ferrrock 01 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            jump park01_ferrrock_label
        "Spend time with Ferry... [red](+Affection)" if (disabled == False):
            $ timeofday += 1
            scene black with dissolve
            show park01_ferrrock 05 with dissolve
            "[yel]You spent some time with Ferry."
            show park01_ferrrock 06 with dissolve
            call charaff ("ferry")
            jump parklabel_01
        "Leave..." if True:







            jump parklabel_01



label buildersguild_makotired_label:
    $ location = "buildersguild_makotired"
    hide screen status01
    call charevents

    scene buildersguild_makotired 01 with dissolve
    show buildersguild_makotired_vid

    menu:
        "Talk..." if True:
            mc "Hey, Makoto."
            mc "You look like you've worked up a sweat..."
            hide buildersguild_makotired_vid
            show buildersguild_makotired 04 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "Heh..."
            mako "Of course! A builder's work is never truly done!"
            show buildersguild_makotired 03 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "...for a Komatsu, I mean."
            jump buildersguild_makotired_label
        "Work at Builders Guild... [red](+Affection)" if (disabled == False):
            $ timeofday += 1
            call charwork ("makoto_01")
            call charaff ("makoto")

            jump buildersguildlabel
        "Request Services..." if (makoevents >= 2):
            call buildlabel
            jump buildersguildlabel
        "Leave..." if True:
            jump buildersguildlabel

label buildersguild_makosword_label:
    $ location = "buildersguild_makosword"
    hide screen status01
    call charevents

    scene buildersguild_makosword 01 with dissolve
    show buildersguild_makosword_vid

    menu:
        "Talk..." if True:
            hide buildersguild_makosword_vid
            show buildersguild_makosword 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Makoto..."
            mc "Do you actually {i}know{/i} how to use a sword?"
            show buildersguild_makosword 04 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "Nah, I don't..."
            mako "But my family has been making [yel]weapons{/color} for generations."
            show buildersguild_makosword 03 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "In fact, one of the guild's biggest contractors are the [yel]Holy Knights{/color}."
            mako "They seem to always be in need of weapons, for whatever reason..."
            jump buildersguild_makosword_label
        "Work at Builders Guild... [red](+Affection)" if (disabled == False):
            $ timeofday += 1
            call charwork ("makoto_01")
            call charaff ("makoto")

            jump buildersguildlabel
        "Request Services..." if (makoevents >= 2):
            call buildlabel
            jump buildersguildlabel
        "Leave..." if True:
            jump buildersguildlabel




label beachstandempty_label:
    $ location = "beachstand_empty"
    hide screen status01
    call charevents

    scene beachstand_empty with dissolve

    menu:
        "Leave..." if True:
            jump beachlabel_01

label beachstand_adel_label:
    $ location = "beachstand_adel"
    hide screen status01
    call charevents

    scene beachstand_adel 01 with dissolve


    menu:
        "Talk..." if True:

            show beachstand_adel 02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            adel "Good day to you, [mc]."
            adel "Welcome to Lady Maple's Beach Paradise..."
            scene beachstand_adel 01 with dissolve
            menu beachstand_adeltalk:
                "Why aren't you wearing a swimsuit?" if True:

                    show beachstand_adel 03 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    adel "I've been given express permission to maintain my maid uniform by my fair lady, Lady Maple..."
                    show beachstand_adel 04 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    adel "...so long as I'm within the confines of this booth, of course."
                    show beachstand_adel 05 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    adel "It suits me, yes? As a maid, I pride myself on dressing professionally."
                    show beachstand_adel 01 with dissolve

                    jump beachstand_adeltalk
                "Who is Lady Maple?" if True:

                    show beachstand_adel 06 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    with vpunch
                    adel "Know your place, human!!! How dare you ask such a blasphemous question!?"
                    show beachstand_adel 07 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    adel "Lady Maple is only the most important '{b}being{/b}' in Scarlet!"
                    show beachstand_adel 08 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    mc "..."
                    mc "(This maid is really devoted to her master...)"
                    show beachstand_adel 09 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    adel "Her title as [yel]Champion{/color} should already serve as a testament to her superiority over the commonfolk..."
                    show beachstand_adel 10 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    adel "She is magnificiently beautiful and intelligent, revered and awed by many, while also benevolent, thoughtful, and merciful..."
                    show beachstand_adel 11 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    mc "..."
                    show beachstand_adel 12 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    adel "Yes, yes, yes... Lady Maple is the epitome of perfection, the {b}ultimate being{/b} who will lead Scarlet into a new dawn..."
                    show beachstand_adel 14 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    mc "..."
                    show beachstand_adel 01 with dissolve

                    jump beachstand_adeltalk
                "Why isn't there anyone here at the beach?" if True:

                    show beachstand_adel 02 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    adel "The people currently occupying the beach represent the high class of society, whom even Lady Maple recognizes..."
                    show beachstand_adel 03 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    adel "In other words, {b}no one{/b}."
                    show beachstand_adel 01 with dissolve

                    jump beachstand_adeltalk
                "When will JYP ever make a scene for you?" if True:

                    show beachstand_adel 03 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    adel "Fufu~"
                    adel "So you have set your prying eyes upon me, as well?"
                    show beachstand_adel 10 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    adel "Unfortunately for you, my mind, body, and soul is reserved only for my master, Lady Maple..."
                    show beachstand_adel 09 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    adel "...in other words, I'm just a side character. Not like I'll ever win a poll or anything on the [oj]Patreon{/color}."
                    show beachstand_adel 11 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    mc "..."
                    show beachstand_adel 01 with dissolve

                    jump beachstand_adeltalk
                "Nevermind..." if True:
                    jump beachstand_adel_label
        "Reserve the beach for the day... [red]$2,000" if True:






            if (weekday):
                show beachstand_adel 02 with Dissolve(.5)
                $ renpy.pause(.5, hard=True)
                adel "Lady Maple will only allow commoners to make reservations during the [yel]weekends{/color}."
                show beachstand_adel 03 with Dissolve(.5)
                $ renpy.pause(.5, hard=True)
                adel "As a reminder, the cost will be [yel]$2,000{/color}... One grand for you and one grand for your partner..."
                jump beachstand_adel_label
            elif (weekday == False and money < 2000):
                show beachstand_adel 05 with Dissolve(.5)
                $ renpy.pause(.5, hard=True)
                adel "Unfortunately, you don't have enough money."
                adel "Now begone before I throw you out."
                jump beachstand_adel_label
            elif True:
                show beachstand_adel 03 with Dissolve(.5)
                $ renpy.pause(.5, hard=True)
                show screen storescreen
                adel "Very well..."
                adel "Who would you like to go with? Do not forget, the fee is [yel]$2,000."
                show beachstand_adel 01 with Dissolve(.5)
                $ renpy.pause(.5, hard=True)
                show screen datingbeachscreen with Dissolve(.5)
                $ renpy.pause(.5, hard=True)
                while endgame != True:
                    pause
        "Leave..." if True:
            jump beachlabel_01



label street03_violdoorday_label:
    $ location = "street03_violdoorday"
    hide screen status01
    call charevents

    scene street03_violdoorday 01 with dissolve
    show street03_violdoorday_vid with dissolve

    menu:
        "Talk..." if True:
            mc "..."
            if (violmet):
                mc "Violetta's fast asleep..."
                mc "I shouldn't bother her unless I really need something..."
            elif True:
                mc "Is she... sleeping?"
                mv "Zzz..."
            jump street03_violdoorday_label
        "Leave..." if True:
            jump streetlabel_03

label street03_violdoornight_label:
    $ location = "street03_violdoornight"
    hide screen status01
    call charevents

    scene street03_violdoornight 01 with dissolve
    show street03_violdoornight_vid with dissolve

    menu:
        "Talk..." if True:
            mc "..."
            if (violmet):
                mc "Violetta's fast asleep..."
                mc "I shouldn't bother her unless I really need something..."
            elif True:
                mc "Is she... sleeping?"
                mv "Zzz..."
            jump street03_violdoornight_label
        "Leave..." if True:
            jump streetlabel_03



label street04_celelean_label:
    $ location = "street_04_cele"
    hide screen status01
    call charevents

    show screen storescreen
    show screen fortunepotscreen

    $ junkvalue = int(20+(sidequest/2))

    scene street04_celelean 01 with dissolve
    show street04_celelean_vid

    menu:
        "Talk..." if True:
            hide screen storescreen
            hide screen fortunepotscreen
            menu:
                "About your sales..." if True:
                    mc "..."
                    mc "You do realize that no one is ever going to buy your goods this late at night..."
                    hide street04_celelean_vid
                    show street04_celelean 02 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    cele "I wouldn't be so sure..."
                    show street04_celelean 03 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    cele "There's always a dope or two who stop by at this hour."
                    show street04_celelean 04 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    cele "I mean, you're here after all, right?"
                    jump street04_celelean_label
                "What are Omikujis...?" if True:
                    hide street04_celelean_vid
                    show street04_celelean 03 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    cele "They are fortunes blessed by the Goddess herself!"
                    cele "Definitely not making that one up!"
                    show street04_celelean 01 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    mc "Uh-huh..."
                    show street04_celelean 04 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    cele "Hehe..."
                    cele "Each fortune you draw can potentially win you a prize..."
                    show street04_celelean 03 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    cele "Makes things a little more exciting, right?"
                    play sound "audio/ding.mp3" volume 2
                    show screen tutorialscreen_09 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    pause
                "What is the 'Golden Ticket'?" if True:
                    hide street04_celelean_vid
                    show street04_celelean 03 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    cele "It's this shiny piece of paper I found while I was dumpster diving!"
                    cele "Pretty cool, right?"
                    show street04_celelean 01 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    mc "Yes, but what does it do, exactly?"
                    mc "Like, is it worth getting?"
                    show street04_celelean 02 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    cele "Well, that depends..."
                    cele "You ever play for achievements in a video game?"
                    show street04_celelean 01 with Dissolve(.5)
                    $ renpy.pause(.5, hard=True)
                    mc "..."
                    jump street04_celelean_label
                "Leave..." if True:
                    jump street04_celelean_label
        "Work with Celestia... [red](+Affection)" if (celework == False):
            hide screen storescreen
            hide screen fortunepotscreen
            $ celework = True
            $ timeofday += 1
            call charwork ("celestia")
            call charaff ("celestia")

            jump streetlabel_04
        "Draw an Omikuji... [red](Daily Limit: [fortune_cap]/10) (Cost $25)" if True:
            if (fortune_cap == 10):
                hide screen storescreen
                hide screen fortunepotscreen
                hide street04_celelean_vid
                show street04_celelean 03 with Dissolve(.5)
                $ renpy.pause(.5, hard=True)
                cele "Sorry, but I'm out of fortunes~"
                show street04_celelean 04 with Dissolve(.5)
                $ renpy.pause(.5, hard=True)
                cele "Please come again next time~ Hehehe~"
                jump street04_celelean_label
            elif (money < 25):
                hide screen storescreen
                hide screen fortunepotscreen
                hide street04_celelean_vid
                show street04_celelean 03 with Dissolve(.5)
                $ renpy.pause(.5, hard=True)
                cele "Sorry, but you don't have enough money..."
                show street04_celelean 04 with Dissolve(.5)
                $ renpy.pause(.5, hard=True)
                cele "Remember to gamble responsibly!"
                jump street04_celelean_label
            elif True:
                $ money -= 25
                call fortunepicking
                jump street04_celelean_label
        "Sell your junk... [yel](Current: [junkinventory]) ($[junkvalue]/each)" if junkinventory:
            hide screen storescreen
            hide screen fortunepotscreen
            $ junktotal = junkvalue * junkinventory
            $ junkinventory = 0
            $ money += junktotal
            play sound "audio/coins.mp3" volume 3
            show love_cele at up_happy
            "[yel]You sold the junk you found to Celestia for $[junktotal]!!!"
            jump street04_celelean_label
        "Leave..." if True:
            hide screen storescreen
            hide screen fortunepotscreen
            jump streetlabel_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
