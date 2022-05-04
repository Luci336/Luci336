screen status01():
    hbox xalign 0.97 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_relations.webp" hover "icons_update/icon_relations_hover.webp" action [Show("statusscreen"), Hide("status01")]
    hbox xalign 0.91 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_map.webp" hover "icons_update/icon_map_hover.webp" action [Show("mapscreen"), Hide("status01")]
    hbox xalign 0.85 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_quest.webp" hover "icons_update/icon_quest_hover.webp" action [Show("questscreen"), Hide("status01")]
    hbox xalign 0.79 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_bag.webp" hover "icons_update/icon_bag_hover.webp" action [Show("inventoryscreen"), Hide("status01")]


    hbox xalign 0.02 yalign 0.99:
        imagebutton:
            idle "icons_update/icon_money.webp" hover "icons_update/icon_money.webp"
    hbox xalign 0.10 yalign 0.967:
        text _("$[money]") outlines [ (absolute(2), "#000", absolute(0), absolute(1))] font "Timeless.ttf" color "#FFF"

    hbox xalign 0.99 yalign 0.99:
        if (timeofday == 0):
            imagebutton:
                idle "icons_update/icon_morning.webp" hover "icons_update/icon_fastforward.webp" action If((disabled == False and timeofday != 5), Jump("fftrigger"))
        if (timeofday == 1):
            imagebutton:
                idle "icons_update/icon_noon.webp" hover "icons_update/icon_fastforward.webp" action If((disabled == False and timeofday != 5), Jump("fftrigger"))
        if (timeofday == 2):
            imagebutton:
                idle "icons_update/icon_afternoon.webp" hover "icons_update/icon_fastforward.webp" action If((disabled == False and timeofday != 5), Jump("fftrigger"))
        if (timeofday == 3):
            imagebutton:
                idle "icons_update/icon_evening.webp" hover "icons_update/icon_fastforward.webp" action If((disabled == False and timeofday != 5), Jump("fftrigger"))
        if (timeofday == 4):
            imagebutton:
                idle "icons_update/icon_night.webp" hover "icons_update/icon_fastforward.webp" action If((disabled == False and timeofday != 5), Jump("fftrigger"))
        if (timeofday == 5):
            imagebutton:
                idle "icons_update/icon_midnight.webp" hover "icons_update/icon_fastforward.webp"


    vbox xpos 0.9 ypos 0.910:
        text "{size=30}[dayinweek]" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] font "Timeless.ttf" color "#FFF"
        if (timeofday == 0):
            text "{size=30}Morning" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] font "Timeless.ttf" color "#FFF"
        if (timeofday == 1):
            text "{size=30}Noon" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] font "Timeless.ttf" color "#FFF"
        if (timeofday == 2):
            text "{size=30}Afternoon" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] font "Timeless.ttf" color "#FFF"
        if (timeofday == 3):
            text "{size=30}Evening" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] font "Timeless.ttf" color "#FFF"
        if (timeofday == 4):
            text "{size=30}Night" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] font "Timeless.ttf" color "#FFF"
        if (timeofday == 5):
            text "{size=30}Midnight" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] font "Timeless.ttf" color "#FFF"









screen storescreen():
    hbox xalign 0.02 yalign 0.99:
        imagebutton:
            idle "icons_update/icon_money.webp" hover "icons_update/icon_money.webp"
    hbox xalign 0.10 yalign 0.967:
        text _("$[money]") outlines [ (absolute(2), "#000", absolute(0), absolute(1))] font "Timeless.ttf" color "#FFF"

screen statusscreen():
    modal True
    hbox xalign 0.5 yalign 0.8:
        imagebutton:
            idle "screens_update/blank_screen.webp"
    hbox xalign 0.5 yalign 0.13:
        text "{size=200}Relationships" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] color "#C21807" font "BrushScriptRomanItalic.ttf" xalign 0.5
    hbox xalign 0.97 yalign 0.03 spacing 15:
        imagebutton:
            idle "icons_update/icon_relations.webp" hover "icons_update/icon_relations_hover.webp" action [Show("status01"), Hide("statusscreen")]
    hbox xalign 0.91 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_map.webp" hover "icons_update/icon_map_hover.webp" action [Show("mapscreen"), Hide("statusscreen")]
    hbox xalign 0.85 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_quest.webp" hover "icons_update/icon_quest_hover.webp" action [Show("questscreen"), Hide("statusscreen")]
    hbox xalign 0.79 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_bag.webp" hover "icons_update/icon_bag_hover.webp" action [Show("inventoryscreen"), Hide("statusscreen")]






    hbox xalign 0.5 yalign 0.35 spacing 15:
        imagebutton:
            idle "screens_update/card_este_01.webp" hover "screens_update/card_este_02.webp" action [Hide("statusscreen"), Show("estescreen")]
        imagebutton:
            idle "screens_update/card_silv_01.webp" hover "screens_update/card_silv_02.webp" action [Hide("statusscreen"), Show("silvscreen")]
        if (persistent.lock or azulmet):
            imagebutton:
                idle "screens_update/card_azul_01.webp" hover "screens_update/card_azul_02.webp" action [Hide("statusscreen"), Show("azulscreen")]
        if (persistent.lock or seremet):
            imagebutton:
                idle "screens_update/card_sere_01.webp" hover "screens_update/card_sere_02.webp" action [Hide("statusscreen"), Show("serescreen")]
        if (persistent.lock or laurmet):
            imagebutton:
                idle "screens_update/card_laur_01.webp" hover "screens_update/card_laur_02.webp" action [Hide("statusscreen"), Show("laurscreen")]
        if (persistent.lock or ferrmet):
            imagebutton:
                idle "screens_update/card_ferr_01.webp" hover "screens_update/card_ferr_02.webp" action [Hide("statusscreen"), Show("ferrscreen")]
        if (persistent.lock or makomet):
            imagebutton:
                idle "screens_update/card_mako_01.webp" hover "screens_update/card_mako_02.webp" action [Hide("statusscreen"), Show("makoscreen")]
        if (persistent.lock or celemet):
            imagebutton:
                idle "screens_update/card_cele_01.webp" hover "screens_update/card_cele_02.webp" action [Hide("statusscreen"), Show("celescreen")]
        if (altimet):
            imagebutton:
                idle "screens_update/card_alti_01.webp" hover "screens_update/card_alti_02.webp" action [Hide("statusscreen"), Show("altiscreen")]

    hbox xalign 0.5 yalign 0.65 spacing 15:



        if (altimet):
            imagebutton:
                idle "screens_update/card_alti_01.webp" hover "screens_update/card_alti_02.webp" action [Hide("statusscreen"), Show("altiscreen")]
        if (viermet):
            imagebutton:
                idle "screens_update/card_vier_01.webp" hover "screens_update/card_vier_02.webp" action [Hide("statusscreen"), Show("vierscreen")]
        if (kanamet):
            imagebutton:
                idle "screens_update/card_kana_01.webp" hover "screens_update/card_kana_02.webp" action [Hide("statusscreen"), Show("kanascreen")]
        if (ritamet):
            imagebutton:
                idle "screens_update/card_rita_01.webp" hover "screens_update/card_rita_02.webp" action [Hide("statusscreen"), Show("ritascreen")]



        if (magimet):
            imagebutton:
                idle "screens_update/card_magi_01.webp" hover "screens_update/card_magi_02.webp" action [Hide("statusscreen"), Show("magiscreen")]



        if (culamet):
            imagebutton:
                idle "screens_update/card_cula_01.webp" hover "screens_update/card_cula_02.webp" action [Hide("statusscreen"), Show("culascreen")]














































screen estescreen():
    modal True
    hbox xalign 0.97 yalign 0.03 spacing 15:
        imagebutton:
            idle "icons_update/icon_relations.webp" hover "icons_update/icon_relations_hover.webp" action [Show("statusscreen"), Hide("estescreen")]
    hbox xalign 0.91 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_map.webp" hover "icons_update/icon_map_hover.webp" action [Show("mapscreen"), Hide("estescreen")]
    hbox xalign 0.85 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_quest.webp" hover "icons_update/icon_quest_hover.webp" action [Show("questscreen"), Hide("estescreen")]
    hbox xalign 0.79 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_bag.webp" hover "icons_update/icon_bag_hover.webp" action [Show("status01"), Hide("estescreen")]

    add "images/screens_update/char_screen.webp" xalign 0.5 yalign 0.8
    add "images/screens_update/screen_este.webp" at left_to_right

    vbox xalign 0.5 yalign 0.17:
        text "{size=128}Estelle" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] color "#a79ba6" font "BubblegumSans.ttf" xalign 0.5
        text "[bl]{size=48}The Little [sil!c]" xalign 0.5
        text "[bl]{size=30}Age: 18" xalign 0.5
        text "[bl]{size=30}Affection: [esteaff]" xalign 0.5
        text "[bl]{size=30}Likes: Magic, Candy, Manga" xalign 0.5
        text "[bl]{size=30}Dislikes: People talking back to her" xalign 0.5
    hbox xalign 0.73 yalign 0.17:
        if (persistent.lock or estebought == True):
            imagebutton:
                idle "gallery/estebought_icon.webp" hover "gallery/estebought_icon_hover.webp" action Replay("estebought", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"
    hbox xalign 0.84 yalign 0.17:
        if (persistent.lock or esteevents >= 3):
            imagebutton:
                idle "gallery/este01_03_icon.webp" hover "gallery/este01_03_icon_hover.webp" action Replay("este01_03", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"
    hbox xalign 0.95 yalign 0.17:
        if (persistent.lock or esteevents >= 6):
            imagebutton:
                idle "gallery/este02_03_icon.webp" hover "gallery/este02_03_icon_hover.webp" action Replay("este02_03", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"
    hbox xalign 0.73 yalign 0.28:
        if (persistent.lock or esteevents >= 9):
            imagebutton:
                idle "gallery/este03_03_icon.webp" hover "gallery/este03_03_icon_hover.webp" action Replay("este03_03", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"
















screen silvscreen():
    modal True
    hbox xalign 0.97 yalign 0.03 spacing 15:
        imagebutton:
            idle "icons_update/icon_relations.webp" hover "icons_update/icon_relations_hover.webp" action [Show("statusscreen"), Hide("silvscreen")]
    hbox xalign 0.91 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_map.webp" hover "icons_update/icon_map_hover.webp" action [Show("mapscreen"), Hide("silvscreen")]
    hbox xalign 0.85 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_quest.webp" hover "icons_update/icon_quest_hover.webp" action [Show("questscreen"), Hide("silvscreen")]
    hbox xalign 0.79 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_bag.webp" hover "icons_update/icon_bag_hover.webp" action [Show("status01"), Hide("silvscreen")]

    add "images/screens_update/char_screen.webp" xalign 0.5 yalign 0.8
    add "images/screens_update/screen_silv.webp" at left_to_right

    vbox xalign 0.5 yalign 0.17:
        text "{size=128}Silvia" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] color "#af96a0" font "BubblegumSans.ttf" xalign 0.5
        text "[bl]{size=48}The Loving [mil!c]" xalign 0.5
        text "[bl]{size=30}Age: 39" xalign 0.5
        text "[bl]{size=30}Affection: [silvaff]" xalign 0.5
        text "[bl]{size=30}Likes: A lovey-dovey household" xalign 0.5
        text "[bl]{size=30}Dislikes: A dirty household" xalign 0.5

    hbox xalign 0.73 yalign 0.17:
        if (persistent.lock or silvbought == True):
            imagebutton:
                idle "gallery/prologue_11_icon.webp" hover "gallery/prologue_11_icon_hover.webp" action Replay("prologue_11", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"
    hbox xalign 0.84 yalign 0.17:
        if (persistent.lock or silvevents >= 3):
            imagebutton:
                idle "gallery/silv01_03_icon.webp" hover "gallery/silv01_03_icon_hover.webp" action Replay("silv01_03", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"
    hbox xalign 0.95 yalign 0.17:
        if (persistent.lock or silvevents >= 5):
            imagebutton:
                idle "gallery/silv02_02_icon.webp" hover "gallery/silv02_02_icon_hover.webp" action Replay("silv02_02", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"








screen azulscreen():
    modal True
    hbox xalign 0.97 yalign 0.03 spacing 15:
        imagebutton:
            idle "icons_update/icon_relations.webp" hover "icons_update/icon_relations_hover.webp" action [Show("statusscreen"), Hide("azulscreen")]
    hbox xalign 0.91 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_map.webp" hover "icons_update/icon_map_hover.webp" action [Show("mapscreen"), Hide("azulscreen")]
    hbox xalign 0.85 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_quest.webp" hover "icons_update/icon_quest_hover.webp" action [Show("questscreen"), Hide("azulscreen")]
    hbox xalign 0.79 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_bag.webp" hover "icons_update/icon_bag_hover.webp" action [Show("status01"), Hide("azulscreen")]

    add "images/screens_update/char_screen.webp" xalign 0.5 yalign 0.8
    add "images/screens_update/screen_azul.webp" at left_to_right

    vbox xalign 0.5 yalign 0.17:
        text "{size=128}Azula" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] color "#8dc0f2" font "BubblegumSans.ttf" xalign 0.5
        text "[bl]{size=48}The Valla Goddess" xalign 0.5
        text "[bl]{size=30}Age: ??" xalign 0.5
        text "[bl]{size=30}Affection: [azulaff]" xalign 0.5
        text "[bl]{size=30}Likes: Humans, Sweets, Television" xalign 0.5
        text "[bl]{size=30}Dislikes: Non-sugary foods" xalign 0.5

    hbox xalign 0.73 yalign 0.17:
        if (persistent.lock or azulevents >= 2):
            imagebutton:
                idle "gallery/azul01_02_icon.webp" hover "gallery/azul01_02_icon_hover.webp" action Replay("azul01_02", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"
    hbox xalign 0.84 yalign 0.17:
        if (persistent.lock or azulbought):
            imagebutton:
                idle "gallery/mainquest_13_icon.webp" hover "gallery/mainquest_13_icon_hover.webp" action Replay("mainquest_13", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"








screen serescreen():
    modal True
    hbox xalign 0.97 yalign 0.03 spacing 15:
        imagebutton:
            idle "icons_update/icon_relations.webp" hover "icons_update/icon_relations_hover.webp" action [Show("statusscreen"), Hide("serescreen")]
    hbox xalign 0.91 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_map.webp" hover "icons_update/icon_map_hover.webp" action [Show("mapscreen"), Hide("serescreen")]
    hbox xalign 0.85 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_quest.webp" hover "icons_update/icon_quest_hover.webp" action [Show("questscreen"), Hide("serescreen")]
    hbox xalign 0.79 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_bag.webp" hover "icons_update/icon_bag_hover.webp" action [Show("status01"), Hide("serescreen")]

    add "images/screens_update/char_screen.webp" xalign 0.5 yalign 0.8
    add "images/screens_update/screen_sere.webp" at left_to_right

    vbox xalign 0.5 yalign 0.17:
        text "{size=128}Serena" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] color "#e09b57" font "BubblegumSans.ttf" xalign 0.5
        text "[bl]{size=48}The Childhood Friend" xalign 0.5
        text "[bl]{size=30}Age: 22" xalign 0.5
        text "[bl]{size=30}Affection: [sereaff]" xalign 0.5
        text "[bl]{size=30}Likes: Hard work, Fitness, Money" xalign 0.5
        text "[bl]{size=30}Dislikes: Gaining weight, Being wasteful" xalign 0.5
    hbox xalign 0.73 yalign 0.17:
        if (persistent.lock or sereevents >= 2):
            imagebutton:
                idle "gallery/sere01_02_icon.webp" hover "gallery/sere01_02_icon_hover.webp" action Replay("sere01_02", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"
    hbox xalign 0.84 yalign 0.17:
        if (persistent.lock or sereevents >= 7):
            imagebutton:
                idle "gallery/sere03_01_icon.webp" hover "gallery/sere03_01_icon_hover.webp" action Replay("sere03_01", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"
    hbox xalign 0.95 yalign 0.17:
        if (persistent.lock or serebought == True):
            imagebutton:
                idle "gallery/serebought_icon.webp" hover "gallery/serebought_icon_hover.webp" action Replay("serebought", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"





























screen laurscreen():
    modal True
    hbox xalign 0.97 yalign 0.03 spacing 15:
        imagebutton:
            idle "icons_update/icon_relations.webp" hover "icons_update/icon_relations_hover.webp" action [Show("statusscreen"), Hide("laurscreen")]
    hbox xalign 0.91 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_map.webp" hover "icons_update/icon_map_hover.webp" action [Show("mapscreen"), Hide("laurscreen")]
    hbox xalign 0.85 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_quest.webp" hover "icons_update/icon_quest_hover.webp" action [Show("questscreen"), Hide("laurscreen")]
    hbox xalign 0.79 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_bag.webp" hover "icons_update/icon_bag_hover.webp" action [Show("status01"), Hide("laurscreen")]

    add "images/screens_update/char_screen.webp" xalign 0.5 yalign 0.8
    add "images/screens_update/screen_laur.webp" at left_to_right

    vbox xalign 0.5 yalign 0.17:
        text "{size=128}Laureate" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] color "#f2d6ab" font "BubblegumSans.ttf" xalign 0.5
        text "[bl]{size=48}The Princess of Scarlet" xalign 0.5
        text "[bl]{size=30}Age: 19" xalign 0.5
        text "[bl]{size=30}Affection: [lauraff]" xalign 0.5
        text "[bl]{size=30}Likes: Her citizens, Television" xalign 0.5
        text "[bl]{size=30}Dislikes: Bullies, Lewdness, Working" xalign 0.5
    hbox xalign 0.73 yalign 0.17:
        if (persistent.lock or laurevents >= 2):
            imagebutton:
                idle "gallery/laur01_02_icon.webp" hover "gallery/laur01_02_icon_hover.webp" action Replay("laur01_02", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"








screen ferrscreen():
    modal True
    hbox xalign 0.97 yalign 0.03 spacing 15:
        imagebutton:
            idle "icons_update/icon_relations.webp" hover "icons_update/icon_relations_hover.webp" action [Show("statusscreen"), Hide("ferrscreen")]
    hbox xalign 0.91 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_map.webp" hover "icons_update/icon_map_hover.webp" action [Show("mapscreen"), Hide("ferrscreen")]
    hbox xalign 0.85 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_quest.webp" hover "icons_update/icon_quest_hover.webp" action [Show("questscreen"), Hide("ferrscreen")]
    hbox xalign 0.79 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_bag.webp" hover "icons_update/icon_bag_hover.webp" action [Show("status01"), Hide("ferrscreen")]

    add "images/screens_update/char_screen.webp" xalign 0.5 yalign 0.8
    add "images/screens_update/screen_ferr.webp" at left_to_right

    vbox xalign 0.5 yalign 0.17:
        text "{size=128}Ferry" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] color "#336fca" font "BubblegumSans.ttf" xalign 0.5
        text "[bl]{size=48}The Combat Maid" xalign 0.5
        text "[bl]{size=30}Age: 28" xalign 0.5
        text "[bl]{size=30}Affection: [ferraff]" xalign 0.5
        text "[bl]{size=30}Likes: Attending to her Master" xalign 0.5
        text "[bl]{size=30}Dislikes: Laziness, Television, Wasting time" xalign 0.5
    hbox xalign 0.73 yalign 0.17:
        if (persistent.lock or ferrevents >= 1):
            imagebutton:
                idle "gallery/ferr01_01_icon.webp" hover "gallery/ferr01_01_icon_hover.webp" action Replay("ferr01_01", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"















screen altiscreen():
    modal True
    hbox xalign 0.97 yalign 0.03 spacing 15:
        imagebutton:
            idle "icons_update/icon_relations.webp" hover "icons_update/icon_relations_hover.webp" action [Show("statusscreen"), Hide("altiscreen")]
    hbox xalign 0.91 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_map.webp" hover "icons_update/icon_map_hover.webp" action [Show("mapscreen"), Hide("altiscreen")]
    hbox xalign 0.85 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_quest.webp" hover "icons_update/icon_quest_hover.webp" action [Show("questscreen"), Hide("altiscreen")]
    hbox xalign 0.79 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_bag.webp" hover "icons_update/icon_bag_hover.webp" action [Show("status01"), Hide("altiscreen")]

    add "images/screens_update/char_screen.webp" xalign 0.5 yalign 0.8
    add "images/screens_update/screen_alti.webp" at left_to_right

    vbox xalign 0.5 yalign 0.17:
        text "{size=128}Altina" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] color "#fbe2dc" font "BubblegumSans.ttf" xalign 0.5
        text "[bl]{size=48}The Sheepish Devout" xalign 0.5
        text "[bl]{size=30}Age: 20" xalign 0.5
        text "[bl]{size=30}Affection: [altiaff]" xalign 0.5
        text "[bl]{size=30}Likes: Cooking, Helping others, The Goddess" xalign 0.5
        text "[bl]{size=30}Dislikes: Scary people" xalign 0.5





























screen vierscreen():
    modal True
    hbox xalign 0.97 yalign 0.03 spacing 15:
        imagebutton:
            idle "icons_update/icon_relations.webp" hover "icons_update/icon_relations_hover.webp" action [Show("statusscreen"), Hide("vierscreen")]
    hbox xalign 0.91 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_map.webp" hover "icons_update/icon_map_hover.webp" action [Show("mapscreen"), Hide("vierscreen")]
    hbox xalign 0.85 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_quest.webp" hover "icons_update/icon_quest_hover.webp" action [Show("questscreen"), Hide("vierscreen")]
    hbox xalign 0.79 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_bag.webp" hover "icons_update/icon_bag_hover.webp" action [Show("status01"), Hide("vierscreen")]

    add "images/screens_update/char_screen.webp" xalign 0.5 yalign 0.8
    add "images/screens_update/screen_vier.webp" at left_to_right

    vbox xalign 0.5 yalign 0.17:
        text "{size=128}Viera" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] color "#cc8c77" font "BubblegumSans.ttf" xalign 0.5
        text "[bl]{size=48}The Street Fighter" xalign 0.5
        text "[bl]{size=30}Age: 21" xalign 0.5
        text "[bl]{size=30}Affection: [vieraff]" xalign 0.5
        text "[bl]{size=30}Likes: Fighting, Training, Cupcakes" xalign 0.5
        text "[bl]{size=30}Dislikes: Weaklings, Big breasts" xalign 0.5






















screen kanascreen():
    modal True
    hbox xalign 0.97 yalign 0.03 spacing 15:
        imagebutton:
            idle "icons_update/icon_relations.webp" hover "icons_update/icon_relations_hover.webp" action [Show("statusscreen"), Hide("kanascreen")]
    hbox xalign 0.91 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_map.webp" hover "icons_update/icon_map_hover.webp" action [Show("mapscreen"), Hide("kanascreen")]
    hbox xalign 0.85 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_quest.webp" hover "icons_update/icon_quest_hover.webp" action [Show("questscreen"), Hide("kanascreen")]
    hbox xalign 0.79 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_bag.webp" hover "icons_update/icon_bag_hover.webp" action [Show("status01"), Hide("kanascreen")]

    add "images/screens_update/char_screen.webp" xalign 0.5 yalign 0.8
    add "images/screens_update/screen_kana.webp" at left_to_right

    vbox xalign 0.5 yalign 0.17:
        text "{size=128}Kanae" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] color "#a26951" font "BubblegumSans.ttf" xalign 0.5
        text "[bl]{size=48}The Director of the Academy" xalign 0.5
        text "[bl]{size=30}Age: 32" xalign 0.5
        text "[bl]{size=30}Affection: [kanaaff]" xalign 0.5
        text "[bl]{size=30}Likes: Her students, Learning, Teaching" xalign 0.5
        text "[bl]{size=30}Dislikes: Her love life, Happy couples" xalign 0.5






















screen ritascreen():
    modal True
    hbox xalign 0.97 yalign 0.03 spacing 15:
        imagebutton:
            idle "icons_update/icon_relations.webp" hover "icons_update/icon_relations_hover.webp" action [Show("statusscreen"), Hide("ritascreen")]
    hbox xalign 0.91 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_map.webp" hover "icons_update/icon_map_hover.webp" action [Show("mapscreen"), Hide("ritascreen")]
    hbox xalign 0.85 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_quest.webp" hover "icons_update/icon_quest_hover.webp" action [Show("questscreen"), Hide("ritascreen")]
    hbox xalign 0.79 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_bag.webp" hover "icons_update/icon_bag_hover.webp" action [Show("status01"), Hide("ritascreen")]

    add "images/screens_update/char_screen.webp" xalign 0.5 yalign 0.8
    add "images/screens_update/screen_rita.webp" at left_to_right

    vbox xalign 0.5 yalign 0.17:
        text "{size=128}Rita" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] color "#8c1034" font "BubblegumSans.ttf" xalign 0.5
        text "[bl]{size=48}The Prodigal Mage" xalign 0.5
        text "[bl]{size=30}Age: 18" xalign 0.5
        text "[bl]{size=30}Affection: [ritaaff]" xalign 0.5
        text "[bl]{size=30}Likes: Burning, Fiery, Passion" xalign 0.5
        text "[bl]{size=30}Dislikes: Morons" xalign 0.5








screen makoscreen():
    modal True
    hbox xalign 0.97 yalign 0.03 spacing 15:
        imagebutton:
            idle "icons_update/icon_relations.webp" hover "icons_update/icon_relations_hover.webp" action [Show("statusscreen"), Hide("makoscreen")]
    hbox xalign 0.91 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_map.webp" hover "icons_update/icon_map_hover.webp" action [Show("mapscreen"), Hide("makoscreen")]
    hbox xalign 0.85 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_quest.webp" hover "icons_update/icon_quest_hover.webp" action [Show("questscreen"), Hide("makoscreen")]
    hbox xalign 0.79 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_bag.webp" hover "icons_update/icon_bag_hover.webp" action [Show("status01"), Hide("makoscreen")]

    add "images/screens_update/char_screen.webp" xalign 0.5 yalign 0.8
    add "images/screens_update/screen_mako.webp" at left_to_right

    vbox xalign 0.5 yalign 0.17:
        text "{size=128}Makoto" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] color "#c66551" font "BubblegumSans.ttf" xalign 0.5
        text "[bl]{size=48}Head of the Builder's Guild" xalign 0.5
        text "[bl]{size=30}Age: 22" xalign 0.5
        text "[bl]{size=30}Affection: [makoaff]" xalign 0.5
        text "[bl]{size=30}Likes: Building, Fixing things, Being on time" xalign 0.5
        text "[bl]{size=30}Dislikes: Laziness" xalign 0.5
    hbox xalign 0.73 yalign 0.17:
        if (persistent.lock or makoevents >= 2):
            imagebutton:
                idle "gallery/mako01_02_icon.webp" hover "gallery/mako01_02_icon_hover.webp" action Replay("mako01_02", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"
    hbox xalign 0.84 yalign 0.17:
        if (persistent.lock or makobought):
            imagebutton:
                idle "gallery/makobought_icon.webp" hover "gallery/makobought_icon_hover.webp" action Replay("makobought", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"








screen celescreen():
    modal True
    hbox xalign 0.97 yalign 0.03 spacing 15:
        imagebutton:
            idle "icons_update/icon_relations.webp" hover "icons_update/icon_relations_hover.webp" action [Show("statusscreen"), Hide("celescreen")]
    hbox xalign 0.91 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_map.webp" hover "icons_update/icon_map_hover.webp" action [Show("mapscreen"), Hide("celescreen")]
    hbox xalign 0.85 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_quest.webp" hover "icons_update/icon_quest_hover.webp" action [Show("questscreen"), Hide("celescreen")]
    hbox xalign 0.79 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_bag.webp" hover "icons_update/icon_bag_hover.webp" action [Show("status01"), Hide("celescreen")]

    add "images/screens_update/char_screen.webp" xalign 0.5 yalign 0.8
    add "images/screens_update/screen_cele.webp" at left_to_right

    vbox xalign 0.5 yalign 0.17:
        text "{size=128}Celestine" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] color "#f7c7b4" font "BubblegumSans.ttf" xalign 0.5
        text "[bl]{size=46}Friendly Neighborhood Swindler" xalign 0.5
        text "[bl]{size=30}Age: ??" xalign 0.5
        text "[bl]{size=30}Affection: [celeaff]" xalign 0.5
        text "[bl]{size=30}Likes: Money, Jewelry, Shiny Objects" xalign 0.5
        text "[bl]{size=30}Dislikes: Losing money, Humans" xalign 0.5
    hbox xalign 0.73 yalign 0.17:
        if (persistent.lock or celemet):
            imagebutton:
                idle "gallery/sere05_01_icon.webp" hover "gallery/sere05_01_icon_hover.webp" action Replay("sere05_01", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"
    hbox xalign 0.84 yalign 0.17:
        if (persistent.lock or celeevents >= 5):
            imagebutton:
                idle "gallery/cele01_05_icon.webp" hover "gallery/cele01_05_icon_hover.webp" action Replay("cele01_05", locked=False)
        else:
            imagebutton:
                idle "gallery/lock.webp"

screen magiscreen():
    modal True
    hbox xalign 0.97 yalign 0.03 spacing 15:
        imagebutton:
            idle "icons_update/icon_relations.webp" hover "icons_update/icon_relations_hover.webp" action [Show("statusscreen"), Hide("magiscreen")]
    hbox xalign 0.91 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_map.webp" hover "icons_update/icon_map_hover.webp" action [Show("mapscreen"), Hide("magiscreen")]
    hbox xalign 0.85 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_quest.webp" hover "icons_update/icon_quest_hover.webp" action [Show("questscreen"), Hide("magiscreen")]
    hbox xalign 0.79 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_bag.webp" hover "icons_update/icon_bag_hover.webp" action [Show("status01"), Hide("magiscreen")]

    add "images/screens_update/char_screen.webp" xalign 0.5 yalign 0.8
    add "images/screens_update/screen_magi.webp" at left_to_right

    vbox xalign 0.5 yalign 0.17:
        text "{size=128}Magilou" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] color "#cbccda" font "BubblegumSans.ttf" xalign 0.5
        text "[bl]{size=48}The Warden of the Prison" xalign 0.5
        text "[bl]{size=30}Age: 32" xalign 0.5
        text "[bl]{size=30}Affection: [magiaff]" xalign 0.5
        text "[bl]{size=30}Likes: Law, Order, Uniformity" xalign 0.5
        text "[bl]{size=30}Dislikes: Lawbreakers, Villains, Criminals" xalign 0.5

screen violscreen():
    modal True
    hbox xalign 0.97 yalign 0.03 spacing 15:
        imagebutton:
            idle "icons_update/icon_relations.webp" hover "icons_update/icon_relations_hover.webp" action [Show("statusscreen"), Hide("violscreen")]
    hbox xalign 0.91 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_map.webp" hover "icons_update/icon_map_hover.webp" action [Show("mapscreen"), Hide("violscreen")]
    hbox xalign 0.85 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_quest.webp" hover "icons_update/icon_quest_hover.webp" action [Show("questscreen"), Hide("violscreen")]
    hbox xalign 0.79 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_bag.webp" hover "icons_update/icon_bag_hover.webp" action [Show("status01"), Hide("violscreen")]

    add "images/screens_update/char_screen.webp" xalign 0.5 yalign 0.8
    add "images/screens_update/screen_viol.webp" at left_to_right

    vbox xalign 0.5 yalign 0.17:
        text "{size=128}Violetta" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] color "#7c7aa6" font "BubblegumSans.ttf" xalign 0.5
        text "[bl]{size=48}The Maid of Evergarden Cafe" xalign 0.5
        text "[bl]{size=30}Age: 28" xalign 0.5
        text "[bl]{size=30}Affection: [violaff]" xalign 0.5
        text "[bl]{size=30}Likes: Attending to her master" xalign 0.5
        text "[bl]{size=30}Dislikes: Disrespectful people" xalign 0.5






















screen culascreen():
    modal True
    hbox xalign 0.97 yalign 0.03 spacing 15:
        imagebutton:
            idle "icons_update/icon_relations.webp" hover "icons_update/icon_relations_hover.webp" action [Show("statusscreen"), Hide("culascreen")]
    hbox xalign 0.91 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_map.webp" hover "icons_update/icon_map_hover.webp" action [Show("mapscreen"), Hide("culascreen")]
    hbox xalign 0.85 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_quest.webp" hover "icons_update/icon_quest_hover.webp" action [Show("questscreen"), Hide("culascreen")]
    hbox xalign 0.79 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_bag.webp" hover "icons_update/icon_bag_hover.webp" action [Show("status01"), Hide("culascreen")]

    add "images/screens_update/char_screen.webp" xalign 0.5 yalign 0.8
    add "images/screens_update/screen_cula.webp" at left_to_right

    vbox xalign 0.5 yalign 0.17:
        text "{size=128}Cularia" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] color "#014c44" font "BubblegumSans.ttf" xalign 0.5
        text "[bl]{size=48}The Flower Girl" xalign 0.5
        text "[bl]{size=30}Age: " xalign 0.5
        text "[bl]{size=30}Affection: " xalign 0.5
        text "[bl]{size=30}Likes: Flowers" xalign 0.5
        text "[bl]{size=30}Dislikes: " xalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
