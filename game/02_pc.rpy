screen pcscreen:
    modal True
    hbox xalign 0.5 yalign 0.5:
        imagebutton:
            idle "screens_update/mission_screen.webp"
    hbox xalign 0.77 yalign 0.26:
        imagebutton:
            idle "icons_update/icon_close.webp" hover "icons_update/icon_close_hover.webp" action [Hide("pcscreen"), Jump("mcroomlabel")]
    hbox xalign 0.5 yalign 0.25:
        text "{size=100}My Computer" outlines [ (absolute(3), "#000", absolute(0), absolute(1)) ] color "#FFF" font "Timeless.ttf"
    hbox xalign 0.5 yalign 0.45 spacing 15:
        imagebutton:
            idle "screens_pc/pc_oldscenes.webp" hover "screens_pc/pc_oldscenes_hover.webp" action [Hide("missionscreen"), Jump("pc_oldscenes_label")]
        imagebutton:
            idle "screens_pc/pc_fanart.webp" hover "screens_pc/pc_fanart_hover.webp" action [Hide("missionscreen"), Jump("pc_fanart_label")]
        if (esteevents >= 1):
            imagebutton:
                idle "screens_pc/pc_tiktok.webp" hover "screens_pc/pc_tiktok_hover.webp" action [Hide("missionscreen"), Jump("pc_tiktok_label")]




label pc_oldscenes_label:
    hide screen status01
    hide screen pcscreen
    show screen pc_oldscenes_screen
    while endgame != True:
        pause

label pc_tiktok_label:
    hide screen status01
    hide screen pcscreen
    $ renpy.run(OpenURL('https://www.tiktok.com/@estelleofscarlet'))
    show screen pcscreen
    while endgame != True:
        pause

label pc_fanart_label:
    hide screen status01
    hide screen pcscreen
    "This feature is currently unavailable."
    show screen pcscreen
    while endgame != True:
        pause

screen pc_oldscenes_screen:
    modal True
    hbox xalign 0.5 yalign 0.8:
        imagebutton:
            idle "screens_update/blank_screen.webp"
    hbox xalign 0.5 yalign 0.08:
        text "{size=100}Story Scenes" outlines [ (absolute(3), "#000", absolute(0), absolute(1)) ] color "#FFF" font "Timeless.ttf"
    hbox xalign 0.99 yalign 0.09:
        imagebutton:
            idle "icons_update/icon_close.webp" hover "icons_update/icon_close_hover.webp" action [Hide("pc_oldscenes_screen"), Jump("mcroomlabel")]



    hbox xalign 0.06 yalign 0.22:
        if (persistent.lock or mainquest >= 3):
            imagebutton:
                idle "gallery/prologue_04_icon.webp" hover "gallery/prologue_04_icon_hover.webp" action Replay("prologue_04", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"

    hbox xalign 0.17 yalign 0.22:
        if (persistent.lock or azulmet):
            imagebutton:
                idle "gallery/prologue_08_icon.webp" hover "gallery/prologue_08_icon_hover.webp" action Replay("prologue_08", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"

    hbox xalign 0.28 yalign 0.22:
        if (persistent.lock or mainquest >= 9):
            imagebutton:
                idle "gallery/prologue_10_icon.webp" hover "gallery/prologue_10_icon_hover.webp" action Replay("prologue_10", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"

    hbox xalign 0.39 yalign 0.22:
        if (persistent.lock or laurevents >= 3):
            imagebutton:
                idle "gallery/laur01_03_icon.webp" hover "gallery/laur01_03_icon_hover.webp" action Replay("laur01_03", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"

    hbox xalign 0.50 yalign 0.22:
        if (persistent.lock or makomet):
            imagebutton:
                idle "gallery/mainquest_10_icon.webp" hover "gallery/mainquest_10_icon_hover.webp" action Replay("mainquest_10", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"
    hbox xalign 0.61 yalign 0.22:
        if (persistent.lock or adelmet):
            imagebutton:
                idle "gallery/mako02_04_icon.webp" hover "gallery/mako02_04_icon_hover.webp" action Replay("mako02_04", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"
    hbox xalign 0.72 yalign 0.22:
        if (persistent.lock or sereevents >= 5):
            imagebutton:
                idle "gallery/sere02_01_icon.webp" hover "gallery/sere02_01_icon_hover.webp" action Replay("sere02_01", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"
    hbox xalign 0.83 yalign 0.22:
        if (persistent.lock or sereevents >= 5):
            imagebutton:
                idle "gallery/sere02_03_icon.webp" hover "gallery/sere02_03_icon_hover.webp" action Replay("sere02_03", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"
    hbox xalign 0.94 yalign 0.22:
        if (persistent.lock or sereevents >= 8):
            imagebutton:
                idle "gallery/sere03_02_icon.webp" hover "gallery/sere03_02_icon_hover.webp" action Replay("sere03_02", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"
    hbox xalign 0.06 yalign 0.33:
        if (persistent.lock or esteevents >= 9):
            imagebutton:
                idle "gallery/este03_02_icon.webp" hover "gallery/este03_02_icon_hover.webp" action Replay("este03_02", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"
    hbox xalign 0.17 yalign 0.33:
        if (persistent.lock or celeevents >= 8):
            imagebutton:
                idle "gallery/cele02_02_icon.webp" hover "gallery/cele02_02_icon_hover.webp" action Replay("cele02_02", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
