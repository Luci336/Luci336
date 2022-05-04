transform left_to_right:
    xalign 0.0 yalign 0.0
    linear 0.3 xalign 0.04

transform up_happy:
    xalign .95 yalign 1.1
    linear 1.5 yalign 0.95

transform up_happy_02:
    xalign .05 yalign 1.1
    linear 1.5 yalign 0.95

transform left_to_right_missions:
    xalign 0.0 yalign 0.35
    linear 0.3 xalign 0.18

transform right_to_left_fortune:
    xalign 0.7 yalign 0.5
    linear 0.3 xalign 0.5

label splashscreen:
    scene black with dissolve
    show warningscreen with Dissolve(.7)
    $ renpy.pause(1.5, hard=True)
    pause
    show whitescreen with Dissolve(.7)
    return



image silv01_03_01 = Movie(play="images/videos/silv01_03_01.webm", pos=(0,0), anchor=(0,0))
image silv02_02_01 = Movie(play="images/videos/silv02_02_01.webm", pos=(0,0), anchor=(0,0))
image silv02_02_02 = Movie(play="images/videos/silv02_02_02.webm", pos=(0,0), anchor=(0,0))
image silv02_02_03 = Movie(play="images/videos/silv02_02_03.webm", pos=(0,0), anchor=(0,0))
image silv02_02_04 = Movie(play="images/videos/silv02_02_04.webm", pos=(0,0), anchor=(0,0))

image estebought_02 = Movie(play="images/videos/estebought_02.webm", pos=(0,0), anchor=(0,0))
image este02_03_01 = Movie(play="images/videos/este02_03_01.webm", pos=(0,0), anchor=(0,0))

image este03_03_01 = Movie(play="images/videos/este03_03_01.webm", pos=(0,0), anchor=(0,0))
image este03_03_03 = Movie(play="images/videos/este03_03_03.webm", pos=(0,0), anchor=(0,0))

image azul01_02_01 = Movie(play="images/videos/azul01_02_01.webm", pos=(0,0), anchor=(0,0))
image azul01_02_02 = Movie(play="images/videos/azul01_02_02.webm", pos=(0,0), anchor=(0,0))

image sere01_02_01 = Movie(play="images/videos/sere01_02_01.webm", pos=(0,0), anchor=(0,0))
image sere03_01_01 = Movie(play="images/videos/sere03_01_01.webm", pos=(0,0), anchor=(0,0))

image mako01_02_01 = Movie(play="images/videos/mako01_02_01.webm", pos=(0,0), anchor=(0,0))
image mako01_02_02 = Movie(play="images/videos/mako01_02_02.webm", pos=(0,0), anchor=(0,0))

image mainquest_13_01 = Movie(play="images/videos/mainquest_13_01.webm", pos=(0,0), anchor=(0,0))
image mainquest_13_02 = Movie(play="images/videos/mainquest_13_02.webm", pos=(0,0), anchor=(0,0))
image mainquest_13_03 = Movie(play="images/videos/mainquest_13_03.webm", pos=(0,0), anchor=(0,0))
image mainquest_13_04 = Movie(play="images/videos/mainquest_13_04.webm", pos=(0,0), anchor=(0,0))
image mainquest_13_05 = Movie(play="images/videos/mainquest_13_05.webm", pos=(0,0), anchor=(0,0))

image ferr01_01_01 = Movie(play="images/videos/ferr01_01_01.webm", pos=(0,0), anchor=(0,0))

image makobought_01 = Movie(play="images/videos/makobought_01.webm", pos=(0,0), anchor=(0,0))
image makobought_02 = Movie(play="images/videos/makobought_02.webm", pos=(0,0), anchor=(0,0))
image makobought_03 = Movie(play="images/videos/makobought_03.webm", pos=(0,0), anchor=(0,0))

image serebought_01 = Movie(play="images/videos/serebought_01.webm", pos=(0,0), anchor=(0,0))
image serebought_02 = Movie(play="images/videos/serebought_02.webm", pos=(0,0), anchor=(0,0))
image serebought_03 = Movie(play="images/videos/serebought_03.webm", pos=(0,0), anchor=(0,0))
image serebought_04 = Movie(play="images/videos/serebought_04.webm", pos=(0,0), anchor=(0,0))
image serebought_05 = Movie(play="images/videos/serebought_05.webm", pos=(0,0), anchor=(0,0))
image serebought_06 = Movie(play="images/videos/serebought_06.webm", pos=(0,0), anchor=(0,0))

image cele01_05_01 = Movie(play="images/videos/cele01_05_01.webm", pos=(0,0), anchor=(0,0))



image beachstand_adel_vid = Movie(play="images/screens_talk/adeltalk/beachstand_adel_vid.webm", pos=(0,0), anchor=(0,0))

image street03_violdoorday_vid = Movie(play="images/screens_talk/violtalk/street03_violdoorday_vid.webm", pos=(0,0), anchor=(0,0))
image street03_violdoornight_vid = Movie(play="images/screens_talk/violtalk/street03_violdoornight_vid.webm", pos=(0,0), anchor=(0,0))

image street04_celelean_vid = Movie(play="images/screens_talk/celetalk/street04_celelean_vid.webm", pos=(0,0), anchor=(0,0))

image voy_silv_01 = Movie(play="images/videos/voy_silv_01.webm", pos=(0,0), anchor=(0,0))
image voy_este_01 = Movie(play="images/videos/voy_este_01.webm", pos=(0,0), anchor=(0,0))

image street01_serestore_vid = Movie(play="images/screens_talk/seretalk/street01_serestore_vid.webm", pos=(0,0), anchor=(0,0))
image street01_serewalk_vid = Movie(play="images/screens_talk/seretalk/street01_serewalk_vid.webm", pos=(0,0), anchor=(0,0))
image sereroom_serehair_vid = Movie(play="images/screens_talk/seretalk/sereroom_serehair_vid.webm", pos=(0,0), anchor=(0,0))

image cityhall01_laurtv_vid = Movie(play="images/screens_talk/laurtalk/cityhall01_laurtv_vid.webm", pos=(0,0), anchor=(0,0))
image cityhall02_laurphone_vid = Movie(play="images/screens_talk/laurtalk/cityhall02_laurphone_vid.webm", pos=(0,0), anchor=(0,0))

image street02_cula_vid = Movie(play="images/screens_talk/culatalk/street02_cula_vid.webm", pos=(0,0), anchor=(0,0))

image cityhall02_ferrsit_vid = Movie(play="images/screens_talk/ferrtalk/cityhall02_ferrsit_vid.webm", pos=(0,0), anchor=(0,0))
image cityhall01_ferrlean_vid = Movie(play="images/screens_talk/ferrtalk/cityhall01_ferrlean_vid.webm", pos=(0,0), anchor=(0,0))
image cityhall01_ferrsit_vid = Movie(play="images/screens_talk/ferrtalk/cityhall01_ferrsit_vid.webm", pos=(0,0), anchor=(0,0))
image park02_ferrstretch_vid = Movie(play="images/screens_talk/ferrtalk/park02_ferrstretch_vid.webm", pos=(0,0), anchor=(0,0))
image park01_ferrrock_vid = Movie(play="images/screens_talk/ferrtalk/park01_ferrrock_vid.webm", pos=(0,0), anchor=(0,0))

image esteroom_estestudy_vid = Movie(play="images/screens_talk/estetalk/esteroom_estestudy_vid.webm", pos=(0,0), anchor=(0,0))
image livingroom_estetv_vid = Movie(play="images/screens_talk/estetalk/livingroom_estetv_vid.webm", pos=(0,0), anchor=(0,0))
image esteroom_estestretch_vid = Movie(play="images/screens_talk/estetalk/esteroom_estestretch_vid.webm", pos=(0,0), anchor=(0,0))
image esteroom_estenight_vid = Movie(play="images/screens_talk/estetalk/esteroom_estenight_vid.webm", pos=(0,0), anchor=(0,0))

image silvroom_silvclean_vid = Movie(play="images/screens_talk/silvtalk/silvroom_silvclean_vid.webm", pos=(0,0), anchor=(0,0))
image livingroom_silvkitchen_vid = Movie(play="images/screens_talk/silvtalk/livingroom_silvkitchen_vid.webm", pos=(0,0), anchor=(0,0))
image silvroom_silvsleep_vid = Movie(play="images/screens_talk/silvtalk/silvroom_silvsleep_vid.webm", pos=(0,0), anchor=(0,0))
image street01_silvwalk_vid = Movie(play="images/screens_talk/silvtalk/street01_silvwalk_vid.webm", pos=(0,0), anchor=(0,0))

image park04_azulrock_vid = Movie(play="images/screens_talk/azultalk/park04_azulrock_vid.webm", pos=(0,0), anchor=(0,0))
image park02_azulfly_vid = Movie(play="images/screens_talk/azultalk/park02_azulfly_vid.webm", pos=(0,0), anchor=(0,0))

image buildersguild_makotired_vid = Movie(play="images/screens_talk/makotalk/buildersguild_makotired_vid.webm", pos=(0,0), anchor=(0,0))
image buildersguild_makosword_vid = Movie(play="images/screens_talk/makotalk/buildersguild_makosword_vid.webm", pos=(0,0), anchor=(0,0))

image prologue_11_01 = Movie(play="images/videos/prologue_11_01.webm", pos=(0,0), anchor=(0,0))
image prologue_11_02 = Movie(play="images/videos/prologue_11_02.webm", pos=(0,0), anchor=(0,0))

image mainquest_10_01 = Movie(play="images/videos/mainquest_10_01.webm", pos=(0,0), anchor=(0,0))



image dating_silv_vid_02 = Movie(play="images/videos/dating_silv_vid_02.webm", pos=(0,0), anchor=(0,0))
image dating_silv_vid_03 = Movie(play="images/videos/dating_silv_vid_03.webm", pos=(0,0), anchor=(0,0))
image dating_silv_vid_04 = Movie(play="images/videos/dating_silv_vid_04.webm", pos=(0,0), anchor=(0,0))
image dating_silv_vid_05 = Movie(play="images/videos/dating_silv_vid_05.webm", pos=(0,0), anchor=(0,0))

image dating_este_vid_03 = Movie(play="images/videos/dating_este_vid_03.webm", pos=(0,0), anchor=(0,0))
image dating_este_vid_04 = Movie(play="images/videos/dating_este_vid_04.webm", pos=(0,0), anchor=(0,0))
image dating_este_vid_05 = Movie(play="images/videos/dating_este_vid_05.webm", pos=(0,0), anchor=(0,0))

image dating_sere_vid_02 = Movie(play="images/videos/dating_sere_vid_02.webm", pos=(0,0), anchor=(0,0))
image dating_sere_vid_03 = Movie(play="images/videos/dating_sere_vid_03.webm", pos=(0,0), anchor=(0,0))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
