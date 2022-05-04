screen mapscreen():
    modal True



    hbox xalign 0.5 yalign 0.8:
        imagebutton:
            idle "screens_update/blank_screen.webp"
    hbox xalign 0.97 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_relations.webp" hover "icons_update/icon_relations_hover.webp" action [Show("statusscreen"), Hide("mapscreen")]
    hbox xalign 0.91 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_map.webp" hover "icons_update/icon_map_hover.webp" action [Show("status01"), Hide("mapscreen")]
    hbox xalign 0.85 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_quest.webp" hover "icons_update/icon_quest_hover.webp" action [Show("questscreen"), Hide("mapscreen")]
    hbox xalign 0.79 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_bag.webp" hover "icons_update/icon_bag_hover.webp" action [Show("inventoryscreen"), Hide("mapscreen")]

    if (disabled == True):
        hbox xalign 0.5 yalign 0.5:
            text "{size=100}Map temporarily unavailable" outlines [ (absolute(3), "#000", absolute(0), absolute(1)) ] color "#FFF" font "Timeless.ttf"
    else:
        hbox xalign 0.5 yalign 0.05:
            text "{size=150}Map" outlines [ (absolute(3), "#000", absolute(0), absolute(1)) ] color "#FFF" font "Timeless.ttf"
        imagebutton:
            idle "screens_map/mcroom_map.webp" hover "screens_map/mcroom_map_hover.webp" action [Hide("mapscreen"), Jump("mcroomlabel")] xalign 0.08 yalign 0.25
        imagebutton:
            idle "screens_map/street_map.webp" hover "screens_map/street_map_hover.webp" action [Hide("mapscreen"), Jump("streetlabel_01")] xalign 0.36 yalign 0.25
        imagebutton:
            idle "screens_map/park_map.webp" hover "screens_map/park_map_hover.webp" action [Hide("mapscreen"), Jump("parklabel_04")] xalign 0.64 yalign 0.25
        if (mainquest >= 8):
            imagebutton:
                idle "screens_map/cityhall_map.webp" hover "screens_map/cityhall_map_hover.webp" action [Hide("mapscreen"), Jump("cityhalllabel_01")] xalign 0.92 yalign 0.25
        if (makomet == True):
            imagebutton:
                idle "screens_map/buildersguild_map.webp" hover "screens_map/buildersguild_map_hover.webp" action [Hide("mapscreen"), Jump("buildersguildlabel")] xalign 0.08 yalign 0.42
        if (makoevents >= 2):
            imagebutton:
                idle "screens_map/onsen_map.webp" hover "screens_map/onsen_map_hover.webp" action [Hide("mapscreen"), Jump("onsenlabel")] xalign 0.36 yalign 0.42
        if (makoevents >= 4):
            imagebutton:
                idle "screens_map/beach_map.webp" hover "screens_map/beach_map_hover.webp" action [Hide("mapscreen"), Jump("beachlabel_01")] xalign 0.64 yalign 0.42







    if (disabled == False):

        hbox xpos 0.08 ypos 0.30:
            if (silv_is_dead == False and mainquest >= 9 and (timeofday == 2 or timeofday == 3 or timeofday == 4)):
                if (weekday == False and timeofday == 3 and este_is_dead == True):
                    pass
                else:
                    imagebutton:
                        idle "icons_quest/map_silv.webp"
            if (este_is_dead == False and mainquest >= 9 and (timeofday == 2 or timeofday == 3 or timeofday == 4)):
                if (weekday == False and timeofday == 3 and silv_is_dead == True):
                    pass
                else:
                    imagebutton:
                        idle "icons_quest/map_este.webp"
            if (sere_is_dead == False and serebought):
                if (timeofday == 4):
                    imagebutton:
                        idle "icons_quest/map_sere.webp"









        hbox xpos 0.30 ypos 0.30:
            if (sere_is_dead == False and seremet and mainquest >= 9):
                if (timeofday == 0 or timeofday == 1 or timeofday == 2):
                    imagebutton:
                        idle "icons_quest/map_sere.webp"
                if (timeofday == 3 and timeofday == 3 and weekday == False):
                    imagebutton:
                        idle "icons_quest/map_sere.webp"
            if (cula_is_dead == False and flowergirlmet):
                if (timeofday == 3 or timeofday == 4):
                    imagebutton:
                        idle "icons_quest/map_cula.webp"
            if (silv_is_dead == False and weekday == False):
                if (timeofday == 0):
                    imagebutton:
                        idle "icons_quest/map_silv.webp"
            if (cele_is_dead == False and celemet):
                if (timeofday == 3 or timeofday == 4):
                    imagebutton:
                        idle "icons_quest/map_cele.webp"


        hbox xpos 0.52 ypos 0.30:
            if (azul_is_dead == False and azulmet and mainquest >= 9):
                if (timeofday == 0 or timeofday == 1):
                    imagebutton:
                        idle "icons_quest/map_azul.webp"

            if (ferr_is_dead == False and laurevents >= 3):
                if (timeofday == 3 or timeofday == 4):
                    imagebutton:
                        idle "icons_quest/map_ferr.webp"


        hbox xpos 0.74 ypos 0.30:
            if (laur_is_dead == False and laurmet and mainquest >= 9):
                if (timeofday == 3 or timeofday == 4):
                    imagebutton:
                        idle "icons_quest/map_laur.webp"

            if (ferr_is_dead == False and laurevents >= 3):
                if (timeofday == 2):
                    imagebutton:
                        idle "icons_quest/map_ferr.webp"


        hbox xpos 0.08 ypos 0.45:
            if (mako_is_dead == False and makomet):
                if (timeofday == 1 or timeofday == 2):
                    imagebutton:
                        idle "icons_quest/map_mako.webp"


        hbox xpos 0.52 ypos 0.45:
            if (adel_is_dead == False and adelmet):
                if (timeofday < 3):
                    imagebutton:
                        idle "icons_quest/map_adel.webp"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
