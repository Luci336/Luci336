screen mcroom_screen:
    if (timeofday >= 4):
        imagebutton:
            focus_mask True
            idle "screens_update_02/mcroom_door_night.webp" hover "screens_update_02/mcroom_door_hover.webp" action Hide("mcroom_screen"), Jump("hallwaylabel_01")
        imagebutton:
            focus_mask True
            idle "screens_update_02/mcroom_bed_night.webp" hover "screens_update_02/mcroom_bed_hover.webp" action Hide("mcroom_screen"), Call("sleeptrigger")
        imagebutton:
            focus_mask True
            idle "screens_update_02/mcroom_comp_night.webp" hover "screens_update_02/mcroom_comp_night_hover.webp" action Hide("mcroom_screen"), Show("pcscreen")
    else:
        imagebutton:
            focus_mask True
            idle "screens_update_02/mcroom_door.webp" hover "screens_update_02/mcroom_door_hover.webp" action Hide("mcroom_screen"), Jump("hallwaylabel_01")
        imagebutton:
            focus_mask True
            idle "screens_update_02/mcroom_bed.webp" hover "screens_update_02/mcroom_bed_hover.webp" action Hide("mcroom_screen"), Call("sleeptrigger")
        imagebutton:
            focus_mask True
            idle "screens_update_02/mcroom_comp_day.webp" hover "screens_update_02/mcroom_comp_day_hover.webp" action Hide("mcroom_screen"), Show("pcscreen")






screen hallway_screen_01:
    if timeofday >= 4:
        imagebutton:
            focus_mask True
            idle "screens_update_02/hallway01_silvdoor_night.webp" hover "screens_update_02/hallway01_silvdoor_hover.webp" action Hide("hallway_screen_01"), Jump("silvroomlabel")
        imagebutton:
            focus_mask True
            idle "screens_update_02/hallway01_estedoor_night.webp" hover "screens_update_02/hallway01_estedoor_hover.webp" action Hide("hallway_screen_01"), Jump("esteroomlabel")
    else:
        imagebutton:
            focus_mask True
            idle "screens_update_02/hallway01_silvdoor.webp" hover "screens_update_02/hallway01_silvdoor_hover.webp" action Hide("hallway_screen_01"), Jump("silvroomlabel")
        imagebutton:
            focus_mask True
            idle "screens_update_02/hallway01_estedoor.webp" hover "screens_update_02/hallway01_estedoor_hover.webp" action Hide("hallway_screen_01"), Jump("esteroomlabel")

    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowdown.webp" hover "screens_update_02/arrowdown_hover.webp" action Hide("hallway_screen_01"), Jump("mcroomlabel")
    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowleft.webp" hover "screens_update_02/arrowleft_hover.webp" action Hide("hallway_screen_01"), Jump("hallwaylabel_02")
    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowright.webp" hover "screens_update_02/arrowright_hover.webp" action Hide("hallway_screen_01"), Jump("livingroomlabel")

screen hallway_screen_02:
    if timeofday >= 4:
        imagebutton:
            focus_mask True
            idle "screens_update_02/hallway02_bathdoor_night.webp" hover "screens_update_02/hallway02_bathdoor_hover.webp" action Hide("hallway_screen_02"), Jump("bathroomlabel")
        imagebutton:
            focus_mask True
            idle "screens_update_02/hallway02_seredoor_night.webp" hover "screens_update_02/hallway02_seredoor_hover.webp" action Hide("hallway_screen_02"), Jump("sereroomlabel")
        imagebutton:
            focus_mask True
            idle "screens_update_02/hallway02_azuldoor_night.webp" hover "screens_update_02/hallway02_azuldoor_hover.webp" action Hide("hallway_screen_02"), Jump("azulroomlabel")
    else:
        imagebutton:
            focus_mask True
            idle "screens_update_02/hallway02_bathdoor_day.webp" hover "screens_update_02/hallway02_bathdoor_hover.webp" action Hide("hallway_screen_02"), Jump("bathroomlabel")
        imagebutton:
            focus_mask True
            idle "screens_update_02/hallway02_seredoor_day.webp" hover "screens_update_02/hallway02_seredoor_hover.webp" action Hide("hallway_screen_02"), Jump("sereroomlabel")
        imagebutton:
            focus_mask True
            idle "screens_update_02/hallway02_azuldoor_day.webp" hover "screens_update_02/hallway02_azuldoor_hover.webp" action Hide("hallway_screen_02"), Jump("azulroomlabel")

    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowright.webp" hover "screens_update_02/arrowright_hover.webp" action Hide("hallway_screen_02"), Jump("hallwaylabel_01")



screen esteroom_screen:
    if (este_is_dead == False and estequest == False and mainquest >= 9):
        if (timeofday == 2 and weekday):
            imagebutton:
                focus_mask True
                idle "screens_update_02/esteroom_study.webp" hover "screens_update_02/esteroom_study_hover.webp" action Hide("esteroom_screen"), Jump("esteroom_estestudy_label")
        if (timeofday == 2 and weekday == False):
            imagebutton:
                focus_mask True
                idle "screens_update_02/esteroom_stretch.webp" hover "screens_update_02/esteroom_stretch_hover.webp" action Hide("esteroom_screen"), Jump("esteroom_estestretch_label")
        if (timeofday == 4):
            imagebutton:
                focus_mask True
                idle "screens_update_02/esteroom_estenight.webp" hover "screens_update_02/esteroom_estenight_hover.webp" action Hide("esteroom_screen"), Jump("esteroom_estenight_label")

    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowdown.webp" hover "screens_update_02/arrowdown_hover.webp" action Hide("hallway_screen_01"), Jump("hallwaylabel_01")

screen silvroom_screen:
    if (silv_is_dead == False and silvquest == False and mainquest >= 9):
        if (timeofday == 3 and weekday):
            imagebutton:
                focus_mask True
                idle "screens_update_02/silvroom_closet.webp" hover "screens_update_02/silvroom_closet_hover.webp" action Hide("silvroom_screen"), Jump("silvroom_silvclean_label")
        if (timeofday == 4):
            imagebutton:
                focus_mask True
                idle "screens_update_02/silvroom_silvsleep.webp" hover "screens_update_02/silvroom_silvsleep_hover.webp" action Hide("silvroom_screen"), Jump("silvroom_silvsleep_label")
    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowdown.webp" hover "screens_update_02/arrowdown_hover.webp" action Hide("hallway_screen_01"), Jump("hallwaylabel_01")

screen azulroom_screen:





    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowdown.webp" hover "screens_update_02/arrowdown_hover.webp" action Hide("hallway_screen_02"), Jump("hallwaylabel_02")

screen sereroom_screen:
    if (sere_is_dead == False and serebought):
        if (timeofday == 4):
            imagebutton:
                focus_mask True
                idle "screens_update_02/sereroom_serehair.webp" hover "screens_update_02/sereroom_serehair_hover.webp" action Hide("sereroom_screen"), Jump("sereroom_serehair_label")
    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowdown.webp" hover "screens_update_02/arrowdown_hover.webp" action Hide("hallway_screen_02"), Jump("hallwaylabel_02")


screen bathroom_screen:
    if timeofday >= 4:
        imagebutton:
            focus_mask True
            idle "screens_update_02/bathroom_door_night.webp" hover "screens_update_02/bathroom_door_hover.webp" action Hide("bathroom_screen"), Jump("hallwaylabel_02")
    else:
        imagebutton:
            focus_mask True
            idle "screens_update_02/bathroom_door_day.webp" hover "screens_update_02/bathroom_door_hover.webp" action Hide("bathroom_screen"), Jump("hallwaylabel_02")

screen livingroom_screen:
    if (silv_is_dead == False and silvquest == False and mainquest >= 9):
        if (timeofday == 2):
            imagebutton:
                focus_mask True
                idle "screens_update_02/livingroom_silvkitchen.webp" hover "screens_update_02/livingroom_silvkitchen_hover.webp" action Hide("livingroom_screen"), Jump("livingroom_silvkitchen_label")
    if (silv_is_dead == False and silvquest == False and este_is_dead == False and estequest == False and timeofday == 3 and weekday == False):
        imagebutton:
            focus_mask True
            idle "screens_update_02/livingroom_dinner.webp" hover "screens_update_02/livingroom_dinner_hover.webp" action Hide("livingroom_screen"), Jump("livingroom_dinner_label")

    if (este_is_dead == False and estequest == False and mainquest >= 9):
        if (timeofday == 3 and weekday):
            imagebutton:
                focus_mask True
                idle "screens_update_02/livingroom_estetv.webp" hover "screens_update_02/livingroom_estetv_hover.webp" action Hide("livingroom_screen"), Jump("livingroom_estetv_label")
    if (azul_is_dead == False and azulbought):
        if (timeofday == 3 and weekday):
            imagebutton:
                focus_mask True
                idle "screens_update_02/livingroom_azulcake.webp" hover "screens_update_02/livingroom_azulcake_hover.webp"
        if (timeofday == 4 and weekday == False):
            imagebutton:
                focus_mask True
                idle "screens_update_02/livingroom_azultv.webp" hover "screens_update_02/livingroom_azultv_hover.webp"
    if (sere_is_dead == False and serebought):
        if (timeofday == 3 and weekday):
            imagebutton:
                focus_mask True
                idle "screens_update_02/livingroom_sereeat.webp" hover "screens_update_02/livingroom_sereeat_hover.webp"
    if (timeofday >= 4):
        imagebutton:
            focus_mask True
            idle "screens_update_02/livingroom_door_night.webp" hover "screens_update_02/livingroom_door_hover.webp" action Hide("livingroom_screen"), Jump("streetlabel_01")
    else:
        imagebutton:
            focus_mask True
            idle "screens_update_02/livingroom_door_day.webp" hover "screens_update_02/livingroom_door_hover.webp" action Hide("livingroom_screen"), Jump("streetlabel_01")
    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowdown.webp" hover "screens_update_02/arrowdown_hover.webp" action Hide("hallway_screen_01"), Jump("hallwaylabel_01")
    hbox xalign 0.02 yalign 0.99:
        imagebutton:
            idle "icons_update/icon_money.webp" hover "icons_update/icon_money.webp"
    hbox xalign 0.10 yalign 0.967:
        text _("$[money]") outlines [ (absolute(2), "#000", absolute(0), absolute(1))] font "Timeless.ttf" color "#FFF"

screen street_screen_01:
    if (sere_is_dead == False and timeofday <= 2):
        imagebutton:
            focus_mask True
            idle "screens_update_02/street01_seredoor.webp" hover "screens_update_02/street01_seredoor_hover.webp" action Hide("street_screen_01"), Jump("street01_serestore_label")
    if (sere_is_dead == False and timeofday == 3 and weekday == False):
        imagebutton:
            focus_mask True
            idle "screens_update_02/street01_serewalk.webp" hover "screens_update_02/street01_serewalk_hover.webp" action Hide("street_screen_01"), Jump("street01_serewalk_label")
    if (silv_is_dead == False and silvquest == False and timeofday == 0 and weekday == False):
        imagebutton:
            focus_mask True
            idle "screens_update_02/street01_silvwalk.webp" hover "screens_update_02/street01_silvwalk_hover.webp" action Hide("street_screen_01"), Jump("street01_silvwalk_label")

    if (celeevents == 2 and celetreasure == 1 and timeofday == 5):
        imagebutton:
            focus_mask True
            idle "screens_update_03/street01_trashcan.webp" hover "screens_update_03/street01_trashcan_hover.webp" action Hide("street_screen_01"), Jump("cele01_03")
    if (celeevents > 4):
        imagebutton:
            focus_mask True
            idle "screens_update_03/street01_trashcan.webp" hover "screens_update_03/street01_trashcan_hover.webp" action Hide("street_screen_01"), Jump("street01_trashcan_label")

    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowleft.webp" hover "screens_update_02/arrowleft_hover.webp" action Hide("street_screen_01"), Jump("streetlabel_02")
    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowright.webp" hover "screens_update_02/arrowright_hover.webp" action Hide("street_screen_01"), Jump("streetlabel_03")
    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowdown.webp" hover "screens_update_02/arrowdown_hover.webp" action Hide("street_screen_01"), Jump("livingroomlabel")

screen street_screen_02:
    if (cula_is_dead == False and mainquest >= 9 and timeofday >= 3 and timeofday != 5):
        imagebutton:
            focus_mask True
            idle "screens_update_02/street02_cula.webp" hover "screens_update_02/street02_cula_hover.webp" action Hide("street_screen_02"), Jump("street02_culatalk_label")

    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowup.webp" hover "screens_update_02/arrowup_hover.webp" action Hide("street_screen_02"), Jump("parklabel_01")
    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowdown.webp" hover "screens_update_02/arrowdown_hover.webp" action Hide("street_screen_02"), Jump("streetlabel_01")

screen street_screen_03:
    if (viol_is_dead == False and timeofday < 3):
        imagebutton:
            focus_mask True
            idle "screens_update_02/street03_violdoor_01.webp" hover "screens_update_02/street03_violdoor_01_hover.webp" action Hide("street_screen_03"), Jump("street03_violdoorday_label")
    if (viol_is_dead == False and timeofday >= 3):
        imagebutton:
            focus_mask True
            idle "screens_update_02/street03_violdoor_02.webp" hover "screens_update_02/street03_violdoor_02_hover.webp" action Hide("street_screen_03"), Jump("street03_violdoornight_label")





    if (celeevents > 4):
        imagebutton:
            focus_mask True
            idle "screens_update_03/street03_trashcan.webp" hover "screens_update_03/street03_trashcan_hover.webp" action Hide("street_screen_03"), Jump("street03_trashcan_label")

    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowleft.webp" hover "screens_update_02/arrowleft_hover.webp" action Hide("street_screen_03"), Jump("streetlabel_04")
    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowdown.webp" hover "screens_update_02/arrowdown_hover.webp" action Hide("street_screen_03"), Jump("streetlabel_01")

screen street_screen_04:
    if (cele_is_dead == False and celemet):
        if (timeofday == 3 or timeofday == 4):
            imagebutton:
                focus_mask True
                idle "screens_update_02/street04_celelean.webp" hover "screens_update_02/street04_celelean_hover.webp" action Hide("park_screen_04"), Jump("street04_celelean_label")

    if (celeevents == 1 and celetreasure == 0 and timeofday == 5):
        imagebutton:
            focus_mask True
            idle "screens_update_03/street04_trashcan.webp" hover "screens_update_03/street04_trashcan_hover.webp" action Hide("street_screen_03"), Jump("cele01_02")

    if (celeevents > 4):
        imagebutton:
            focus_mask True
            idle "screens_update_03/street04_trashcan.webp" hover "screens_update_03/street04_trashcan_hover.webp" action Hide("street_screen_04"), Jump("street04_trashcan_label")

    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowdown.webp" hover "screens_update_02/arrowdown_hover.webp" action Hide("street_screen_03"), Jump("streetlabel_03")

screen park_screen_01:
    if (park01_flower_01 == True and flowers_r < 75 and flowers_sr < 30 and flowers_ssr < 15 and flowers_ssg < 5):
        imagebutton:
            focus_mask True
            idle "screens_update_03/park01_flower_01.webp" hover "screens_update_03/park01_flower_01_hover.webp" action SetVariable("park01_flower_01", False), Jump("flowerpicking")
    if (park01_flower_02 == True and flowers_r < 75 and flowers_sr < 30 and flowers_ssr < 15 and flowers_ssg < 5):
        imagebutton:
            focus_mask True
            idle "screens_update_03/park01_flower_02.webp" hover "screens_update_03/park01_flower_02_hover.webp" action SetVariable("park01_flower_02", False), Jump("flowerpicking")
    if (park01_flower_03 == True and flowers_r < 75 and flowers_sr < 30 and flowers_ssr < 15 and flowers_ssg < 5):
        imagebutton:
            focus_mask True
            idle "screens_update_03/park01_flower_03.webp" hover "screens_update_03/park01_flower_03_hover.webp" action SetVariable("park01_flower_03", False), Jump("flowerpicking")

    if (ferr_is_dead == False and laurevents >= 3):
        if (timeofday == 4):
            imagebutton:
                focus_mask True
                idle "screens_update_02/park01_ferrrock.webp" hover "screens_update_02/park01_ferrrock_hover.webp" action Hide("park_screen_01"), Jump("park01_ferrrock_label")

    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowleft.webp" hover "screens_update_02/arrowleft_hover.webp" action Hide("park_screen_01"), Jump("parklabel_02")
    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowright.webp" hover "screens_update_02/arrowright_hover.webp" action Hide("park_screen_01"), Jump("parklabel_03")
    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowdown.webp" hover "screens_update_02/arrowdown_hover.webp" action Hide("park_screen_01"), Jump("streetlabel_02")

screen park_screen_02:
    if (park02_flower_01 == True and flowers_r < 75 and flowers_sr < 30 and flowers_ssr < 15 and flowers_ssg < 5):
        imagebutton:
            focus_mask True
            idle "screens_update_03/park02_flower_01.webp" hover "screens_update_03/park02_flower_01_hover.webp" action SetVariable("park02_flower_01", False), Jump("flowerpicking")
    if (park02_flower_02 == True and flowers_r < 75 and flowers_sr < 30 and flowers_ssr < 15 and flowers_ssg < 5):
        imagebutton:
            focus_mask True
            idle "screens_update_03/park02_flower_02.webp" hover "screens_update_03/park02_flower_02_hover.webp" action SetVariable("park02_flower_02", False), Jump("flowerpicking")
    if (park02_flower_03 == True and flowers_r < 75 and flowers_sr < 30 and flowers_ssr < 15 and flowers_ssg < 5):
        imagebutton:
            focus_mask True
            idle "screens_update_03/park02_flower_03.webp" hover "screens_update_03/park02_flower_03_hover.webp" action SetVariable("park02_flower_03", False), Jump("flowerpicking")

    if (azul_is_dead == False and mainquest >= 9):
        if (timeofday == 1):
            imagebutton:
                focus_mask True
                idle "screens_update_02/park02_azulfly.webp" hover "screens_update_02/park02_azulfly_hover.webp" action Hide("park_screen_02"), Jump("park02_azulfly_label")

    if (ferr_is_dead == False and laurevents >= 3):
        if (timeofday == 3):
            imagebutton:
                focus_mask True
                idle "screens_update_02/park02_ferrstretch.webp" hover "screens_update_02/park02_ferrstretch_hover.webp" action Hide("park_screen_02"), Jump("park02_ferrstretch_label")

    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowleft.webp" hover "screens_update_02/arrowleft_hover.webp" action Hide("park_screen_02"), Jump("parklabel_04")
    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowright.webp" hover "screens_update_02/arrowright_hover.webp" action Hide("park_screen_02"), Jump("parklabel_01")

screen park_screen_03:
    if (park03_flower_01 == True and flowers_r < 75 and flowers_sr < 30 and flowers_ssr < 15 and flowers_ssg < 5):
        imagebutton:
            focus_mask True
            idle "screens_update_03/park03_flower_01.webp" hover "screens_update_03/park03_flower_01_hover.webp" action SetVariable("park03_flower_01", False), Jump("flowerpicking")
    if (park03_flower_02 == True and flowers_r < 75 and flowers_sr < 30 and flowers_ssr < 15 and flowers_ssg < 5):
        imagebutton:
            focus_mask True
            idle "screens_update_03/park03_flower_02.webp" hover "screens_update_03/park03_flower_02_hover.webp" action SetVariable("park03_flower_02", False), Jump("flowerpicking")
    if (park03_flower_03 == True and flowers_r < 75 and flowers_sr < 30 and flowers_ssr < 15 and flowers_ssg < 5):
        imagebutton:
            focus_mask True
            idle "screens_update_03/park03_flower_03.webp" hover "screens_update_03/park03_flower_03_hover.webp" action SetVariable("park03_flower_03", False), Jump("flowerpicking")

    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowleft.webp" hover "screens_update_02/arrowleft_hover.webp" action Hide("park_screen_03"), Jump("parklabel_01")

screen park_screen_04:
    if (azul_is_dead == False and mainquest >= 9):
        if (timeofday == 0):
            imagebutton:
                focus_mask True
                idle "screens_update_02/park04_azulrock.webp" hover "screens_update_02/park04_azulrock_hover.webp" action Hide("park_screen_04"), Jump("park04_azulrock_label")
    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowright.webp" hover "screens_update_02/arrowright_hover.webp" action Hide("park_screen_04"), Jump("parklabel_02")

screen cityhall_screen_01:
    if (ferr_is_dead == False and mainquest >= 9):




        if (timeofday == 2):
            imagebutton:
                focus_mask True
                idle "screens_update_02/cityhall01_ferrsit.webp" hover "screens_update_02/cityhall01_ferrsit_hover.webp" action Hide("cityhall_screen_01"), Jump("cityhall01_ferrsit_label")
    if (laur_is_dead == False and mainquest >= 9):
        if (timeofday == 3):
            imagebutton:
                focus_mask True
                idle "screens_update_02/cityhall01_laurtv.webp" hover "screens_update_02/cityhall01_laurtv_hover.webp" action Hide("cityhall_screen_01"), Jump("cityhall01_laurtv_label")
            imagebutton:
                focus_mask True
                idle "screens_update_02/cityhall01_maotv.webp" hover "screens_update_02/cityhall01_maotv_hover.webp" action Hide("cityhall_screen_01"), Jump("cityhall01_maotv_label")
    if (silvbought == True):
        if ((timeofday == 0 or timeofday == 1) and missions_tutorial == False):
            imagebutton:
                focus_mask True
                idle "screens_update_02/cityhall01_missions.webp" hover "screens_update_02/cityhall01_missions_hover.webp" action Hide("cityhall_screen_01"), Jump("missionstutorial")
        elif (timeofday == 0 or timeofday == 1):
            imagebutton:
                focus_mask True
                idle "screens_update_02/cityhall01_missions.webp" hover "screens_update_02/cityhall01_missions_hover.webp" action Hide("cityhall_screen_01"), Hide("status01"), Show("missionscreen")

    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowup.webp" hover "screens_update_02/arrowup_hover.webp" action Hide("cityhall_screen_01"), Jump("cityhalllabel_02")

screen cityhall_screen_02:
    if (laur_is_dead == False and mainquest >= 9):
        if (timeofday <= 2):
            imagebutton:
                focus_mask True
                idle "screens_update_02/cityhall02_laursleep.webp" hover "screens_update_02/cityhall02_laursleep_hover.webp" action Hide("cityhall_screen_02"), Jump("cityhall02_laursleep_label")
        if (timeofday == 4):
            imagebutton:
                focus_mask True
                idle "screens_update_02/cityhall02_laurphone.webp" hover "screens_update_02/cityhall02_laurphone_hover.webp" action Hide("cityhall_screen_02"), Jump("cityhall02_laurphone_label")





    imagebutton:
        focus_mask True
        idle "screens_update_02/arrowdown.webp" hover "screens_update_02/arrowdown_hover.webp" action Hide("cityhall_screen_02"), Jump("cityhalllabel_01")

screen buildersguild_screen:
    if (mako_is_dead == False):
        if (timeofday == 1):
            imagebutton:
                focus_mask True
                idle "screens_update_02/buildersguild_makotired.webp" hover "screens_update_02/buildersguild_makotired_hover.webp" action Hide("buildersguild_screen"), Jump("buildersguild_makotired_label")
        if (timeofday == 2):
            imagebutton:
                focus_mask True
                idle "screens_update_02/buildersguild_makosword.webp" hover "screens_update_02/buildersguild_makosword_hover.webp" action Hide("buildersguild_screen"), Jump("buildersguild_makosword_label")

screen onsen_screen_01:
    if (mainquest >= 9999999):
        if (timeofday == 1):
            imagebutton:
                focus_mask True
                idle "screens_update_02/buildersguild_makotired.webp" hover "screens_update_02/buildersguild_makotired_hover.webp" action Hide("buildersguild_screen"), Jump("buildersguild_makotired_label")

screen beach_screen_01:
    if (adel_is_dead == False and makoevents < 6 and timeofday <= 2):
        imagebutton:
            focus_mask True
            idle "screens_update_02/beach01_standempty_day.webp" hover "screens_update_02/beach01_standempty_day_hover.webp" action Hide("beach_screen_01"), Jump("beachstandempty_label")
    if (adel_is_dead == False and makoevents >= 6 and timeofday <= 2):
        imagebutton:
            focus_mask True
            idle "screens_update_02/beach01_standadel_day.webp" hover "screens_update_02/beach01_standadel_day_hover.webp" action Hide("beach_screen_01"), Jump("beachstand_adel_label")
    if (makoevents <= 5):
        imagebutton:
            focus_mask True
            idle "screens_update_02/arrowright.webp" hover "screens_update_02/arrowright_hover.webp" action Hide("beach_screen_01"), Jump("beachlabel_02")

screen beach_screen_02:
    if (makoevents <= 5):
        imagebutton:
            focus_mask True
            idle "screens_update_02/arrowleft.webp" hover "screens_update_02/arrowleft_hover.webp" action Hide("beach_screen_02"), Jump("beachlabel_01")
        imagebutton:
            focus_mask True
            idle "screens_update_02/arrowdown.webp" hover "screens_update_02/arrowdown_hover.webp" action Hide("beach_screen_02"), Jump("beachlabel_03")

screen beach_screen_03:
    if (makoevents <= 5):
        imagebutton:
            focus_mask True
            idle "screens_update_02/arrowleft.webp" hover "screens_update_02/arrowleft_hover.webp" action Hide("beach_screen_03"), Jump("beachlabel_02")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
