screen datingbeachscreen:
    modal True
    hbox xalign 0.5 yalign 0.5:
        imagebutton:
            idle "screens_update/dating_screen.webp"
    hbox xalign 0.90 yalign 0.22:
        imagebutton:
            idle "icons_update/icon_close.webp" hover "icons_update/icon_close_hover.webp" action [Hide("datingbeachscreen"), Hide("storescreen"), Jump("beachstand_adel_label")]
    hbox xalign 0.5 yalign 0.22:
        text "{size=85}A Date at the Beach" outlines [ (absolute(3), "#000", absolute(0), absolute(1)) ] color "#FFF" font "Timeless.ttf"


    hbox xalign 0.5 yalign 0.40 spacing 15:
        if (silvbought and silv_is_dead == False):
            imagebutton:
                idle "screens_update/card_silv_01.webp" hover "screens_update/card_silv_02.webp" action [Hide("datingbeachscreen"), Jump("dating_silv_01")]
        if (estebought and esteevents >= 5 and este_is_dead == False):
            imagebutton:
                idle "screens_update/card_este_01.webp" hover "screens_update/card_este_02.webp" action [Hide("datingbeachscreen"), Jump("dating_este_01")]
        if (serebought and sere_is_dead == False):
            imagebutton:
                idle "screens_update/card_sere_01.webp" hover "screens_update/card_sere_02.webp" action [Hide("datingbeachscreen"), Jump("dating_sere_01")]




screen dating_mood_bar_00:
    hbox xalign 0.02 yalign 0.02:
        imagebutton:
            idle "icons_update/dating_mood_00.webp"

screen dating_mood_bar_01:
    hbox xalign 0.02 yalign 0.02:
        imagebutton:
            idle "icons_update/dating_mood_01.webp"

screen dating_mood_bar_02:
    hbox xalign 0.02 yalign 0.02:
        imagebutton:
            idle "icons_update/dating_mood_02.webp"

screen dating_mood_bar_03:
    hbox xalign 0.02 yalign 0.02:
        imagebutton:
            idle "icons_update/dating_mood_03.webp"

screen dating_mood_bar_04:
    hbox xalign 0.02 yalign 0.02:
        imagebutton:
            idle "icons_update/dating_mood_04.webp"

screen dating_mood_bar_05:
    hbox xalign 0.02 yalign 0.02:
        imagebutton:
            idle "icons_update/dating_mood_05.webp"

label dating_mood_bar_label:
    if (dating_mood_pts <= 0):
        show screen dating_mood_bar_00
        hide screen dating_mood_bar_01
        hide screen dating_mood_bar_02
        hide screen dating_mood_bar_03
        hide screen dating_mood_bar_04
        hide screen dating_mood_bar_05
    elif (dating_mood_pts == 1):
        show screen dating_mood_bar_01
        hide screen dating_mood_bar_00
        hide screen dating_mood_bar_02
        hide screen dating_mood_bar_03
        hide screen dating_mood_bar_04
        hide screen dating_mood_bar_05
    elif (dating_mood_pts == 2):
        show screen dating_mood_bar_02
        hide screen dating_mood_bar_00
        hide screen dating_mood_bar_01
        hide screen dating_mood_bar_03
        hide screen dating_mood_bar_04
        hide screen dating_mood_bar_05
    elif (dating_mood_pts == 3):
        show screen dating_mood_bar_03
        hide screen dating_mood_bar_00
        hide screen dating_mood_bar_01
        hide screen dating_mood_bar_02
        hide screen dating_mood_bar_04
        hide screen dating_mood_bar_05
    elif (dating_mood_pts == 4):
        show screen dating_mood_bar_04
        hide screen dating_mood_bar_00
        hide screen dating_mood_bar_01
        hide screen dating_mood_bar_02
        hide screen dating_mood_bar_03
        hide screen dating_mood_bar_05
    elif (dating_mood_pts >= 5):
        show screen dating_mood_bar_05
        hide screen dating_mood_bar_00
        hide screen dating_mood_bar_01
        hide screen dating_mood_bar_02
        hide screen dating_mood_bar_03
        hide screen dating_mood_bar_04
    return

label dating_mood_bar_hide:
    hide screen dating_mood_bar_00
    hide screen dating_mood_bar_01
    hide screen dating_mood_bar_02
    hide screen dating_mood_bar_03
    hide screen dating_mood_bar_04
    hide screen dating_mood_bar_05
    return

label dating_mood_up:

    $ dating_mood_pts += 1
    play sound "audio/ding.mp3" volume 3

    return

label dating_mood_down:

    if dating_mood_pts > 0:
        $ dating_mood_pts -= 1
    play sound "audio/depress.mp3" volume 3
    return

label dating_silv_01:
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3
    $ timeofday = 4
    $ dating_mood_pts = 1
    $ money -= 2000
    play sound "audio/coins.mp3" volume 3
    show love_adel at up_happy
    "[yel]You paid Adeline $2,000!"
    hide screen storescreen
    $ renpy.pause(3, hard=True)
    show dating_story 001-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    show dating_story 001-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "The water sure is nice and warm..."
    show dating_story 001-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm..."
    mc "What's taking her so long?"
    mc "[mil!c] said that she was still changing, but..."
    show dating_story 001-04 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    silv "[mc], honey?"
    silv "H-How do I look? I know that it's not very appropriate for a woman my age..."
    play music "audio/adeline.mp3"
    scene black with dissolve
    $ renpy.movie_cutscene("images/videos/dating_silv_vid_01.webm", delay=None, loops=0, stop_music=False)
    show dating_story 001-05
    show screen dating_mood_bar_01 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "*GULP*"
    mc "W-Wow, [mil!c]... You look..."
    menu:
        "You look cute..." if True:
            $ renpy.fix_rollback()
            show dating_story 001-06 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Oh, [mc]..."
            silv "I know that you're trying to be nice, but this isn't cute at all..."
            show dating_story 001-07 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Cute is unicorns, teddy bears, and lovey-dovey..."
            show dating_story 001-08 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            mc "L-Lovey-dovey...!?"
            mc "Well, it does look good on you regardless..."
        "You look sexy..." if True:
            $ renpy.fix_rollback()
            show dating_story 001-09 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            silv "Eh...?"
            silv "W-What did you just call me?"
            show dating_story 001-10 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            mc "I said that you're sexy, [mil!c]."
            mc "Come closer... I want to get a better look at you."
            show dating_story 001-11 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "[mc], honey..."
            show dating_story 001-12 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "I'm your [mil]. You shouldn't be saying things like that..."
            show dating_story 001-11 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "...Not in public, at least."
            call dating_mood_up
            show aff_silv at up_happy
            "[yel]Silvia appears to be blushing..."
            hide aff_silv
        "Cover yourself up, woman!" if True:
            $ renpy.fix_rollback()
            show dating_story 001-13 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            silv "Eh!?"
            show dating_story 001-14 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "You heard me!"
            mc "What if someone sees you? I don't want other men staring at my [mil] like that!"
            show dating_story 001-15 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Ah, I suppose you're right..."
            silv "I'll try and remember not to wear something so revealing next time..."
            call dating_mood_down
            show sad_silv at up_happy
            "[yel]Silvia appears dejected..."
            hide sad_silv
    call dating_mood_bar_label
    show dating_story 001-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "That's enough standing for now, [mc]..."
    silv "Let's go over there and lay down."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show dating_story 001-17 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    silv "..."
    show dating_story 001-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "It was quite thoughtful of you to reserve the beach for the two of us, [mc]..."
    show dating_story 001-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "...though, I suppose you'd rather be here with a woman closer to your age."
    show dating_story 001-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    menu:
        "That's not true..." if True:
            $ renpy.fix_rollback()
            $ renpy.pause(.5, hard=True)
            mc "Don't think that way, [mil!c]."
            mc "If you keep worrying about your age, you'll never be able to have any fun."
            show dating_story 001-18 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Ah..."
            silv "That's surprisingly a mature answer from you, [mc]..."
            show dating_story 001-21 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Maybe you're right..."
            call dating_mood_up
            show aff_silv at up_happy
            "[yel]Silvia appears relieved..."
            hide aff_silv
        "Yeah, you were kind of the only one available..." if True:
            $ renpy.fix_rollback()
            show dating_story 001-19 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Oh..."
            silv "I see... I suppose I shouldn't have thought any differently..."
            show dating_story 001-22 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "I mean, you're a young man... and I'm..."
            call dating_mood_down
            show sad_silv at up_happy
            "[yel]Silvia heaves out a sigh..."
            hide sad_silv
        "It's normal for a man to want to spend time with their [mil]..." if True:
            $ renpy.fix_rollback()
            show dating_story 001-18 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Is that so?"
            silv "You're not embarrassed at all to be seen with me?"
            show dating_story 001-17 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Of course, not..."
            mc "I mean, you're my [mil]. No one's going to think you're my girlfriend or anything..."
            show dating_story 001-22 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Oh..."
            show dating_story 001-19 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Y-Yeah, I suppose you're right..."
            call dating_mood_down
            "[yel]Silvia looks disappointed..."
            hide sad_silv
    call dating_mood_bar_label
    show dating_story 001-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "..."
    show dating_story 001-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Speaking of which..."
    show dating_story 001-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "I'm sorry that I haven't been around much lately..."
    show dating_story 001-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "There's been so much work piling up, and I've been completely stressed out..."
    show dating_story 001-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu:
        "You work as a maid..." if True:
            $ renpy.fix_rollback()
            mc "Being a maid can't be easy..."
            mc "It must be tough having to clean up after people..."
            show dating_story 001-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Er..."
            silv "[mc], I believe that I've explained this to you already..."
            show dating_story 001-21 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Maids are the pinnacle of elite in Scarlet... You can't call yourself a full-fledge maid without proper credentials..."
            show dating_story 001-19 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "And unfortunately for me, I've flunked out of maid school many years ago."
            show dating_story 001-20 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Oh, right..."
        "You work as a prostitute..." if True:
            $ renpy.fix_rollback()
            mc "..."
            with vpunch
            mc "Y-You're a prostitute... right?"
            show dating_story 001-24 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            silv "Eh!?"
            silv "Y-You are way, way, {b}waaay{/b} off, [mc]!"
            call dating_mood_down
            show sad_silv at up_happy
            "[yel]Silvia is appalled..."
            hide sad_silv
        "You work as a housekeeper..." if True:
            $ renpy.fix_rollback()
            mc "Being a housekeeper can't be easy..."
            mc "It must be tough having to clean up after people..."
            show dating_story 001-21 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Hehe..."
            show dating_story 001-18 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "But I enjoy taking care of people..."
            show dating_story 001-21 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "And that includes taking care of you and Estelle."
            show dating_story 001-17 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            mc "And you do a very good job at it!"
            show dating_story 001-21 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Hehe..."
            silv "Thank you, honey."
            call dating_mood_up
            show aff_silv at up_happy
            "[yel]Silvia appears glad..."
            hide aff_silv
    call dating_mood_bar_label
    show dating_story 001-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hmm..."
    silv "[mc], this really won't be much of a vacation if you're just going to stare at me..."
    show dating_story 001-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "S-Sorry... You're just... so damn pretty."
    show dating_story 001-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hehe..."
    show dating_story 001-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Then how about you come closer?"
    show dating_story 001-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "No need to be shy, [mc]... Go ahead and rub lotion on my back."
    show dating_story 001-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu:
        "No thanks..." if True:
            $ renpy.fix_rollback()
            show dating_story 001-20 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "I'm good!"
            mc "I mean, it'd be weird for me to rub up my [mil], right?"
            show dating_story 001-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "[mc]..."
            silv "It's just lotion... I'd prefer not to get a tan..."
            show dating_story 001-22 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "And do you really want me to say it? My body isn't as nimble as it used to be... I can't reach the entirety of my back..."
            show dating_story 001-20 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "I-I see..."
            with vpunch
            mc "In that case, I'll be happy to help you!"
            call dating_mood_down
            show sad_silv at up_happy
            "[yel]Silvia is disappointed..."
            hide sad_silv
        "With pleasure..." if True:
            $ renpy.fix_rollback()
            show dating_story 001-28 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Of course, [mil!c]!"
            show dating_story 001-29 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Hehe..."



            hide aff_silv
    call dating_mood_bar_label
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show dating_story 001-30 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    mc "(Damn, she's so hot...)"
    mc "(Is it really okay to feel her up like this?)"
    show dating_story 001-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "..."
    show dating_story 001-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "What's taking so long, [mc]?"
    show dating_story 001-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh, right...!"
    show dating_story 001-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hold on..."
    silv "You can't do it with my bra like this, right?"
    show dating_story 001-34 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show dating_story 001-35 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show dating_story 001-36 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "*GULP*"
    mc "This is too much!"
    show dating_story 001-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "[mc]?"
    silv "I'm waiting..."
    show dating_story 001-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "R-Right!"
    show dating_story 001-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    show dating_silv_vid_02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Mmm..."
    silv "[mc], your hands feel good..."
    mc "Yeah, it does feel good..."
    mc "I mean, it {b}should{/b} feel good! We're at a beach!"
    silv "..."
    silv "Sometimes I feel like I'm at an impasse in my life..."
    silv "I'm also worried about Azula... She seems to be incredibly attached to you, [mc]..."
    silv "I pray that she doesn't have any ulterior motives for wanting to stay with us..."
    mc "..."
    menu:
        "She brings chaos to the house..." if True:
            $ renpy.fix_rollback()
            hide dating_silv_vid_02
            show dating_story 001-39 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "..."
            show dating_story 001-40 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "So you think the same, [mc]?"
            show dating_story 001-39 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Yeah..."
            mc "There's a lot of mystery surrounding her. That's for sure."
            show dating_story 001-41 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "...I see."
            call dating_mood_down
            show sad_silv at up_happy
            "[yel]Silvia appears worried..."
            hide sad_silv
        "She's harmless..." if True:
            $ renpy.fix_rollback()
            hide dating_silv_vid_02
            show dating_story 001-40 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "[mc]..."
            silv "I want to believe that, but you just never know..."
            show dating_story 001-41 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "I'm not even sure why I allowed her into the house in the first place..."
            show dating_story 001-39 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "She's harmless, [mil!c]..."
            mc "Azula might be a little odd, but that's because she's genuinely interested in the modern world..."
            show dating_story 001-40 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "[mc]..."
            show dating_story 001-39 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "...And don't worry."
            mc "I-If the time ever comes..."
            with vpunch
            mc "...I promise to {b}protect{/b} both you and Estelle from her!"
            show dating_story 001-42 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Hehe..."
            show dating_story 001-43 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Protecting us from an almighty being like her? I don't know..."
            show dating_story 001-42 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "But maybe you're right... Perhaps I'm worrying over nothing..."
            call dating_mood_up
            show aff_silv at up_happy
            "[yel]Silvia appears relieved..."
            hide aff_silv
        "She's a bad influence on Estelle..." if True:
            $ renpy.fix_rollback()
            hide dating_silv_vid_02
            show dating_story 001-39 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "..."
            show dating_story 001-40 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "You know what, I haven't even thought about that..."
            show dating_story 001-39 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Yeah..."
            mc "I'm a young man and she's always walking around in her underwear and not caring about how I might feel!"
            with vpunch
            mc "...N-Not that I'd feel anything if Estelle started walking around the house in her underwear, of course!"
            show dating_story 001-40 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Hmm..."
            show dating_story 001-41 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Those two don't get along very well. Whenever they are together, they're always arguing."
            show dating_story 001-40 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "But it's true that Azula is definitely making her presence known in the household."
    call dating_mood_bar_label
    show dating_story 001-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    show dating_silv_vid_02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "..."
    silv "[mc], can I ask you something?"
    mc "Of course."
    silv "Where do you see yourself in 5 years?"
    mc "Hmm..."
    mc "I don't know. I never really think about that type of stuff..."
    silv "I see..."
    silv "In 5 years, I see you and Estelle leaving the house..."
    silv "It's a fact of life for all young ones to leave their dens eventually, but I can't say I'm looking forward to being alone..."
    mc "..."
    menu:
        "That's just life..." if True:
            $ renpy.fix_rollback()
            hide dating_silv_vid_02
            show dating_story 001-40 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Yeah, I know..."
            show dating_story 001-41 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "But it's still an unsettling thought."
            show dating_story 001-39 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            mc "Everyone has to move forward. It can't be helped."
            show dating_story 001-41 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "...Right."
            call dating_mood_down
            show sad_silv at up_happy
            "[yel]Silvia appears depressed..."
            hide sad_silv
        "We'll still make time for you..." if True:
            $ renpy.fix_rollback()
            hide dating_silv_vid_02
            show dating_story 001-41 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Maybe you'll visit once every week..."
            show dating_story 001-40 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "But over time, that week becomes a month... and that month becomes a year..."
            show dating_story 001-41 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "What troubles me is the fact that I won't be able to see you every morning..."
            call dating_mood_down
            show sad_silv at up_happy
            "[yel]Silvia appears depressed..."
            hide sad_silv
        "I'll never leave you..." if True:
            $ renpy.fix_rollback()
            hide dating_silv_vid_02
            show dating_story 001-44 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Eh?"
            show dating_story 001-45 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "S-Stop joking, [mc]..."
            show dating_story 001-46 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "You wouldn't want to end up as one of those old men who live with their moms for the rest of their lives, right?"
            show dating_story 001-39 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            mc "So what if I do? You and Estelle are the most important people in my life."
            mc "I mean, I wouldn't have gone so far as to buy your Scarlet Contracts if I wanted to be away from you, right?"
            show dating_story 001-46 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "...Maybe."
            call dating_mood_up
            show aff_silv at up_happy
            "[yel]Silvia is blushing..."
            hide aff_silv
    call dating_mood_bar_label
    show dating_story 001-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    show dating_silv_vid_02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Oh, that reminds me..."
    silv "That girl next door, Serena-chan... How's she doing...?"
    mc "S-Serena!?"
    mc "I don't know... I don't see her as much as I used to..."
    silv "Hehe..."
    silv "The way you used to look at her was sooo adorable back then..."
    silv "Ah, if it's her, I don't mind if you two get married..."
    mc "..."
    menu:
        "S-She's just a friend!" if True:
            $ renpy.fix_rollback()
            hide dating_silv_vid_02
            show dating_story 001-47 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            with vpunch
            mc "S-She's just a friend!"
            mc "I-It's not like I've had a crush on her since the third grade or anything!"
            show dating_story 001-42 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Hehe..."
            silv "Being lovey-dovey with other girls is cute, too..."
            call dating_mood_up
            show aff_silv at up_happy
            "[yel]Silvia is smiling..."
            hide aff_silv
        "I don't care for her..." if True:
            $ renpy.fix_rollback()
            hide dating_silv_vid_02
            show dating_story 001-39 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "It's not like we talk to each other anymore..."
            mc "She just a neighbor to me at this point."
            show dating_story 001-40 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Hmm..."
            silv "Even if you're joking, that's still a cold-hearted thing to say, [mc]..."
            show dating_story 001-41 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Serena really cares about you, you know?"
            call dating_mood_down
            show sad_silv at up_happy
            "[yel]Silvia appears disappointed..."
            hide sad_silv
        "I never really noticed..." if True:
            $ renpy.fix_rollback()
            hide dating_silv_vid_02
            show dating_story 001-43 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Hehe..."
            silv "I think there are more girls who are interested in you than you think, [mc]."
            show dating_story 001-42 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "But if you get too greedy, you might end up breaking a few hearts, you know..."
            show dating_story 001-47 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "...If you say so."
    call dating_mood_bar_label
    show dating_story 001-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    show dating_silv_vid_02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hehe..."
    silv "Ah, I love that we're able to speak together like this, [mc]..."
    silv "Maybe we should have brought Estelle with us... I love it when you two are lovey-dovey..."
    mc "..."
    menu:
        "But I want to be lovey-dovey with you, too..." if True:
            $ renpy.fix_rollback()
            hide dating_silv_vid_02
            show dating_story 001-44 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            silv "Eh!?"
            silv "L-Lovey-dovey with me? As in... extra {b}lovey-lovey-dovey{/b}!?"
            show dating_story 001-47 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Yeah..."
            mc "You're special to me too, [mil!c]."
            show dating_story 001-45 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "[mc]..."
            silv "It's been a long time since someone wanted to be lovey-dovey with me..."
            call dating_mood_up
            show aff_silv at up_happy
            "[yel]Silvia is starry-eyed..."
            hide aff_silv
        "Bringing her would have made this trip more fun..." if True:
            $ renpy.fix_rollback()
            hide dating_silv_vid_02
            show dating_story 001-42 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Hehe..."
            show dating_story 001-43 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "I'm always so happy when the three of us are doing things together..."
            show dating_story 001-42 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Estelle would definitely make things more fun if she were around..."
        "Maybe I should have gathered {b}all{/b} of the girls instead..." if True:
            $ renpy.fix_rollback()
            hide dating_silv_vid_02
            show dating_story 001-44 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            silv "Eh?"
            show dating_story 001-39 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Yeah..."
            mc "The more the merrier, right? Isn't that what you always say in the house?"
            show dating_story 001-40 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "I-I guess so..."
            show dating_story 001-41 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "(But that'd mean less time for me...)"
            call dating_mood_down
            show sad_silv at up_happy
            "[yel]Silvia appears worried..."
            hide sad_silv
    call dating_mood_bar_label
    show dating_story 001-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "..."
    show dating_story 001-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "[mc], I think that's enough. I'm ready to get up now."
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    if (dating_mood_pts < 5):
        call dating_mood_bar_hide
        show dating_story 001-08 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        silv "..."
        show dating_story 001-06 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        silv "I had a fun time today, [mc]."
        show dating_story 001-07 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        silv "Thank you for bringing me here."
        show dating_story 001-08 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "No problem, [mil!c]."
        mc "I appreciate you taking the time to come."
        show dating_story 001-16 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        silv "I think it's about time I leave..."
        silv "There's still so much to do around the house."
        show dating_story 001-05-01 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        mc "..."
        mc "(That didn't go the way I wanted it to...)"
        scene black with Dissolve(1.5)
        $ renpy.pause(1.5, hard=True)
        play music "audio/days.mp3"
        $ renpy.pause(.5, hard=True)
        jump beachlabel_01
    elif True:
        call dating_mood_bar_hide
        show dating_story 001-08 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        silv "..."
        show dating_story 001-06 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        silv "That was fun, [mc]..."
        show dating_story 001-07 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        silv "But I think it's about time we return home."
        show dating_story 001-48 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        mc "..."
        show dating_story 001-49 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        silv "What's this?"
        silv "Why are you suddenly getting close to me, [mc]?"
        show dating_story 001-50 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "It's our own paradise here, [mil!c]..."
        mc "Why don't we spend a little more time being lovey-dovey..."
        show dating_story 001-51 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        silv "Lovey-dovey? With me?"
        show dating_story 001-52 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        silv "[mc], it's one thing to do it at home... it's another in public..."
        show dating_story 001-53 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        silv "Even in Scarlet, people frown upon {i}that{/i} sort of relationship."
        show dating_story 001-50 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "Don't worry. No one will ever know..."
        mc "There isn't anyone around except us... Adeline made sure of it..."
        show dating_story 001-52 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        silv "*Sigh*"
        silv "How did you end up becoming such a lecherous young man...?"
        show dating_story 001-50 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "I'm still growing, y'know?"
        mc "And right now, I need my milk..."
        show dating_story 001-54 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        show dating_story 001-55 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        silv "..."
        show dating_story 001-56 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        silv "Well, aren't you a greedy little boy..."
        $ renpy.pause(.5, hard=True)
        scene black with Dissolve(1.5)
        $ renpy.pause(1.5, hard=True)
        show dating_story 001-57 with Dissolve(1.5)
        $ renpy.pause(1.5, hard=True)
        show dating_story 001-58 with Dissolve(1.5)
        $ renpy.pause(1.5, hard=True)
        show dating_silv_vid_03 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        pause
        silv "There, there, [mc]..."
        silv "Press your lips against my bosom... Let all of your worries disappear..."
        mc "*SLURP* *SLURP*"
        mc "(Her tits are {b}delicious{/b}!!!)"
        mc "(Not only that, but there is a strange sense of familiarity about [mil!c]'s breasts...)"
        mc "(It felt as though I were satisfying a primitive need within me, as if suckling on her breasts was the most natural thing in the world...)"
        hide dating_silv_vid_03
        show dating_story 001-59 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        silv "Ah..."
        silv "[mc], you're sucking too hard..."
        show dating_story 001-60 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "Milk... *SLURP* ... Milk... *SLURP*"
        show dating_story 001-61 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        with vpunch
        mc "...MILKERS!!!"
        silv "Ahhhnnn...!!!"
        silv "Milk won't come out of them no matter how hard you try!!!"
        $ renpy.pause(1, hard=True)
        scene black with Dissolve(1.5)
        $ renpy.pause(1.5, hard=True)
        show dating_story 001-62 with Dissolve(1.5)
        $ renpy.pause(1.5, hard=True)
        silv "Geez, [mc]..."
        silv "You were sucking on me like you were a baby..."
        show dating_story 001-63 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        silv "Well, I suppose that should satisfy you for now..."
        show dating_story 001-64 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "..."
        mc "What do you mean?"
        mc "How can I be satisfied after just that?"
        show dating_story 001-63 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        silv "Eh?"
        silv "What do you mean?"
        show dating_story 001-65 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        with vpunch
        mc "Here..."
        mc "See for yourself."
        show dating_story 001-66 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        silv "*GULP*"
        silv "Y-Young cock..."
        $ renpy.pause(.5, hard=True)
        scene black with Dissolve(1.5)
        $ renpy.pause(1.5, hard=True)
        show dating_story 001-67 with Dissolve(1.5)
        $ renpy.pause(1.5, hard=True)
        show dating_silv_vid_04 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        pause
        mc "Oh god..."
        mc "It slid in perfectly..."
        silv "Ahn... Ahn..."
        silv "[mc], it feels so good..."
        mc "You're so wet..."
        mc "You've been really lonely, haven't you [mil!c]?"
        silv "Eh?"
        silv "O-Of course not..."
        silv "A woman my age doesn't need sex to be happy..."
        silv "The only thing I need in my life is a lovey-dovey household..."
        hide dating_silv_vid_04
        show dating_story 001-68 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        mc "A lovey-dovey household?"
        mc "There's other kinds of lovey-dovey, you know?"
        mc "...like this!"
        show dating_story 001-69 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        with vpunch
        silv "Ahnn...!!!"
        show dating_silv_vid_05 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        pause
        silv "Ahnnn!!! Ahnnn!!!"
        silv "[mc]!!! You're being too rough...!!!"
        mc "How is it?"
        mc "How is lovey-dovey sex?"
        silv "AHNNN... AHNNN..."
        silv "I... LOVE... LOVEY-DOVEY!!!"
        scene whitescreen with Dissolve(1)
        $ renpy.pause(1, hard=True)
        show dating_story 001-69 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        with vpunch
        $ renpy.pause(1, hard=True)
        with vpunch
        silv "Young cock... really is the BEST...!!!"
        $ renpy.pause(1, hard=True)
        scene black with Dissolve(1.5)
        $ renpy.pause(1.5, hard=True)
        play music "audio/days.mp3"
        $ renpy.pause(.5, hard=True)
        jump beachlabel_01
    return

label dating_este_01:
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3
    $ timeofday = 4
    $ dating_mood_pts = 1
    $ money -= 2000
    play sound "audio/coins.mp3" volume 3
    show love_adel at up_happy
    "[yel]You paid Adeline $2,000!"
    hide screen storescreen
    $ renpy.pause(3, hard=True)
    show dating_story 002-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    show dating_story 002-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Goddamnit, Estelle..."
    mc "Why do I have to do this for you?"
    show dating_story 002-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hehe..."
    este "You promised to be my cameraman and help me with my [oj]Tik Tok{/color} video, remember?"
    show dating_story 002-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah, yeah, yeah..."
    mc "Let's just get this over with already..."
    $ renpy.pause(.5, hard=True)
    play music "audio/adeline.mp3"
    scene black with dissolve
    $ renpy.movie_cutscene("images/videos/dating_este_vid_01.webm", delay=None, loops=0, stop_music=False)
    show dating_story 002-05
    show screen dating_mood_bar_01 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "..."
    show dating_story 002-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hehehe..."
    show dating_story 002-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Did you make sure to get my good side?"
    show dating_story 002-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Sure, sure..."
    mc "Are we done with the recording now?"
    mc "I don't want to spend the entire afternoon on this..."
    show dating_story 002-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Uh-huh..."
    show dating_story 002-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Thanks a bunch, [mc]..."
    show dating_story 002-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "When I become famous on [oj]Tik Tok{/color}, I'll be sure to acknowledge you."
    show dating_story 002-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "People won't think you're a loser anymore once they realize you're associated with someone as popular as me!"
    show dating_story 002-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Gee, thanks a lot, Estelle..."
    show dating_story 002-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "..."
    show dating_story 002-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "W-Well?"
    este "Don't just stand there gawking... How do I look?"
    show dating_story 002-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu:
        "Y-You look cute..." if True:
            $ renpy.fix_rollback()
            show dating_story 002-11 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Are you stupid or something...?"
            show dating_story 002-12 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Huh?"
            show dating_story 002-06 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Obviously I'm the cutest girl you know, [mc]..."
            show dating_story 002-08 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "It's a miracle that a loser like you is even allowed under the same roof as me!"
            show dating_story 002-05 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "You little..."
            call dating_mood_up
            show aff_este at up_happy
            "[yel]Estelle is giggling..."
            hide aff_este
        "You're really *GULP* {b}sexy{/b}..." if True:
            $ renpy.fix_rollback()
            show dating_story 002-11 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Hey!"
            este "You're thinking about lewd things again, aren't you!?"
            show dating_story 002-13 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            with vpunch
            este "Creep! Pervert! Hentai!"
            show dating_story 002-12 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            call dating_mood_down
            show sad_este at up_happy
            "[yel]Estelle thinks you're scum..."
            hide sad_este
        "Cover yourself up little lady!" if True:
            $ renpy.fix_rollback()
            show dating_story 002-13 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            este "Hey, jerk!"
            este "Don't you dare tell me what to do!"
            show dating_story 002-12 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Oi, oi..."
            mc "I don't like the idea of my [sil] strutting around in public half-naked like this!"
            mc "Much less the skin you show off on your [oj]Tik Tok{/color}!"
            show dating_story 002-11 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Screw you, [mc]!"
            este "You're not the boss of me!"
            show dating_story 002-12 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "You little..."
            call dating_mood_down
            show sad_este at up_happy
            "[yel]Estelle is glaring at you..."
            hide sad_este
    call dating_mood_bar_label
    show dating_story 002-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hehe..."
    show dating_story 002-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Come on! Let's play in the water, [mc]!"
    show dating_story 002-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "It's about time we have some {b}real{/b} fun!"
    show dating_story 002-16 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "*Sigh*"
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show dating_story 002-17 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    mc "I cannot believe you brought that here..."
    show dating_story 002-18 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "Hehe..."
    show dating_story 002-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Why not? We're at the beach, right?"
    show dating_story 002-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show dating_story 002-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Speaking of which..."
    show dating_story 002-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "How come there isn't anyone around except us?"
    show dating_story 002-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu:
        "If it's just us, we can do lewd things together..." if True:
            $ renpy.fix_rollback()
            show dating_story 002-24 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            with vpunch
            este "Creep! Pervert! Hentai!"
            show dating_story 002-25 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "I-If you try anything on me, I'll make sure you regret it!"
            show dating_story 002-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            with vpunch
            mc "Y-You're right! I was only joking!"
            mc "I mean, what kind of sicko would think that way about their own [sil]!"
            mc "Ha ha ha ha ha..."
            show dating_story 002-22 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "[mc]..."
            este "You really will go straight to {b}HELL{/b} if you continue acting like a [sil]-con pervert..."
            show dating_story 002-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            call dating_mood_down
            show sad_este at up_happy
            "[yel]Estelle thinks you belong in jail..."
            hide sad_este
        "I wanted to be alone with you..." if True:
            $ renpy.fix_rollback()
            show dating_story 002-21 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Eh!?"
            show dating_story 002-22 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "So let me get this straight, you purposely arranged this trip {b}knowing{/b} that we'd be alone..."
            show dating_story 002-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Well, yeah..."
            mc "I thought it'd be nice if the two of us spent some quality..."
            show dating_story 002-24 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            with vpunch
            este "Creep! Pervert! Hentai!"
            show dating_story 002-25 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "You're thinking of something pervy to try on me, aren't you!"
            show dating_story 002-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            call dating_mood_down
            show sad_este at up_happy
            "[yel]Estelle looks disappointed in you..."
            hide sad_este
        "The beach is closed to the public..." if True:
            $ renpy.fix_rollback()
            show dating_story 002-22 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "You're kidding, right?"
            show dating_story 002-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Nope..."
            mc "I had to make a reservation in order for us to be here today."
            show dating_story 002-25 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "That's the most evil thing I've ever heard!"
            show dating_story 002-21 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "The beach used to be free and open to everyone...!"
            show dating_story 002-22 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "...but now they're charging people to use it!?"
            show dating_story 002-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Yup, I think you're right..."
            mc "Whoever owns this beach must be pure evil."
            show dating_story 002-22 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Wait a second..."
            show dating_story 002-26 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "D-Doesn't that mean we have the beach all to ourselves..."
            show dating_story 002-27 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            call dating_mood_up
            show aff_este at up_happy
            "[yel]Estelle is blushing..."
            hide aff_este
    call dating_mood_bar_label
    show dating_story 002-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hehe... I love Mr. Sharky..."
    show dating_story 002-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Don't worry, I'll let you ride him after I'm done, [mc]."
    show dating_story 002-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I'm not riding that thing."
    show dating_story 002-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Eh?"
    este "Why not? You used to love Mr. Sharky too, didn't you?"
    show dating_story 002-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah, I did..."
    mc "But that was back when I was a kid..."
    show dating_story 002-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "W-What are you trying to say!?"
    show dating_story 002-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu:
        "I'm going to throw Mr. Sharky in the bin..." if True:
            $ renpy.fix_rollback()
            show dating_story 002-28 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Eh!?"
            este "W-Why would you do that?"
            show dating_story 002-29 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            show dating_story 002-21 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "[mc], that's so cruel..."
            este "Are you trying to purposely ruin my childhood?"
            call dating_mood_down
            show sad_este at up_happy
            "[yel]Estelle appears upset..."
            hide sad_este
        "There's no way I'm riding Mr. Sharky..." if True:
            $ renpy.fix_rollback()
            show dating_story 002-21 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Geez, [mc]..."
            show dating_story 002-22 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Stop being a spoil sport..."
            show dating_story 002-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            mc "If someone sees me on that thing, I'll be humiliated for the rest of my life."
            show dating_story 002-28 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Hmph..."
            este "As if being seen with you isn't already humiliating enough!"
            call dating_mood_down
            show sad_este at up_happy
            "[yel]Estelle looks disappointed..."
            hide sad_este
        "Mr. Sharky is for babies..." if True:
            $ renpy.fix_rollback()
            show dating_story 002-28 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Hey!"
            este "Are you trying to imply that I'm a child!?"
            show dating_story 002-29 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Uh, yes?"
            mc "Mr. Sharky is designed and marketed toward little children..."
            mc "For you to be riding one at your age speaks volumes of your maturity."
            show dating_story 002-24 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            with vpunch
            este "That's not true!"
            show dating_story 002-25 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "You take that back! Mr. Sharky isn't for babies!"
            show dating_story 002-29 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Is so!"
            show dating_story 002-28 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Is not!"
            show dating_story 002-29 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Is so!"
            show dating_story 002-28 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Is so!"
            show dating_story 002-29 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Is not!"
            show dating_story 002-18 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Hehe..."
            show dating_story 002-20 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "...Wait a second."
            show dating_story 002-19 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Gotcha, [mc]!"
            call dating_mood_up
            show aff_este at up_happy
            "[yel]Estelle appears to be having fun..."
            hide aff_este
    call dating_mood_bar_label
    show dating_story 002-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Let's change the damn subject already..."
    show dating_story 002-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Sure!"
    show dating_story 002-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "What do you want to talk about?"
    show dating_story 002-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm..."
    mc "It's your first year at Scarlet Magic Academy, right?"
    mc "How is it? Is it as fancy and elite as everyone says?"
    show dating_story 002-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "T-The Magic A-Academy...!?"
    show dating_story 002-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Y-Yeah... E-Everything is f-fine, I think...?"
    este "What would you like to know...?"
    show dating_story 002-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu:
        "Is the food any good?" if True:
            $ renpy.fix_rollback()
            show dating_story 002-18 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Oh, yes!"
            show dating_story 002-19 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "A school as prestigious and important as Scarlet Magic Academy deserves only the finest chefs and ingredients!"
            show dating_story 002-33 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "The meals are great! And I look forward to lunch every day!"
            show dating_story 002-20 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Oh, that's good to hear..."
            show dating_story 002-18 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Hehe..."
            show dating_story 002-34 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Of course, I'll never share any with you, [mc]."
            show dating_story 002-35 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "You little..."
            call dating_mood_up
            show aff_este at up_happy
            "[yel]Estelle appears smug..."
            hide aff_este
        "Meet any new friends at the academy?" if True:
            $ renpy.fix_rollback()
            show dating_story 002-22 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Hey..."
            este "Why would you want to know about that?"
            show dating_story 002-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Huh?"
            mc "What's wrong with me wanting to..."
            show dating_story 002-24 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            with vpunch
            este "Creep! Pervert! Hentai!"
            show dating_story 002-25 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "You're trying to use me to flirt with {b}other{/b} girls, aren't you!?."
            show dating_story 002-29 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            with vpunch
            mc "Me!? Flirt!? No way...!"
            show dating_story 002-25 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Don't try and lie to me!"
            show dating_story 002-28 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "I see how you've been surrounding yourself with other girls lately!"
            show dating_story 002-30 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "And t-that means less time with me!"
            show dating_story 002-29 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            call dating_mood_down
            show sad_este at up_happy
            "[yel]Estelle squints her eyes at you..."
            hide sad_este
        "How are your grades?" if True:
            $ renpy.fix_rollback()
            show dating_story 002-21 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            este "What?"
            show dating_story 002-31 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "W-Why do you need to know that?"
            show dating_story 002-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Huh?"
            mc "Isn't it normal to want to know how you're doing in your classes?"
            show dating_story 002-22 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Y-Yeah, but..."
            show dating_story 002-36 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Hmph! It's a private matter, okay!?"
            show dating_story 002-29 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Really..."
            show dating_story 002-28 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Of course!"
            show dating_story 002-36 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "You can't go around asking a girl something as personal as her grades!"
            show dating_story 002-25 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "It's just wrong! No, it's {b}shameless{/b}!"
            show dating_story 002-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            call dating_mood_down
            show sad_este at up_happy
            "[yel]Estelle wants to change the subject..."
            hide sad_este
    call dating_mood_bar_label
    show dating_story 002-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "..."
    show dating_story 002-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hey, [mc]..."
    show dating_story 002-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Have you noticed that [mil!c] seems more exhausted than usual?"
    show dating_story 002-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "You know, like after she comes home from work?"
    show dating_story 002-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "You don't think she's, y'know, seeing {b}someone{/b}, do you?"
    show dating_story 002-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu:
        "She seems as bubbly as usual..." if True:
            $ renpy.fix_rollback()
            show dating_story 002-21 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Geez, [mc]... How dense can you be...?"
            show dating_story 002-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "What do you mean?"
            mc "Doesn't she always seem like her usual joyful self?"
            show dating_story 002-37 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "*Sigh*"
            show dating_story 002-38 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "You really are clueless..."
            show dating_story 002-39 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "You know nothing about a maiden's heart..."
            call dating_mood_down
            show sad_este at up_happy
            "[yel]Estelle is frowning..."
            hide sad_este
        "I think she's more mentally exhausted..." if True:
            $ renpy.fix_rollback()
            show dating_story 002-22 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Eh?"
            este "What do you mean?"
            show dating_story 002-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Well, a lot has happened recently, hasn't it?"
            mc "And she does so much for us..."
            show dating_story 002-21 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Y-Yeah..."
            este "I guess you're right..."
            show dating_story 002-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Also..."
            mc "I can't put my finger on it, but it feels like she's hiding something from us..."
            show dating_story 002-30 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "You think so?"
            show dating_story 002-22 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Actually, she does seem a bit different ever since the household got bigger..."
            call dating_mood_up
            show aff_este at up_happy
            "[yel]Estelle agrees with you..."
            hide aff_este
        "Yeah, you could do more to help her, y'know?" if True:
            $ renpy.fix_rollback()
            show dating_story 002-25 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Like you're one to talk!"
            show dating_story 002-29 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Huh?"
            mc "What're you talking about!? I do help out around the house!"
            show dating_story 002-36 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Yeah, right!"
            show dating_story 002-28 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "I never see you do any chores or anything!"
            show dating_story 002-25 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "You don't even clean up after your own meals!"
            show dating_story 002-29 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Oi, oi..."
            mc "You don't either..."
            call dating_mood_down
            show sad_este at up_happy
            "[yel]Estelle is glaring at you..."
            hide sad_este
    call dating_mood_bar_label
    show dating_story 002-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "..."
    show dating_story 002-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Okay, that's enough!"
    show dating_story 002-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "I'm ready to sail off into the sunset and leave Scarlet behind!"
    show dating_story 002-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "...and guess what? I've decided that you're coming with me for the ride!"
    show dating_story 002-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Huh?"
    mc "What are you on about now?"
    show dating_story 002-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "I'm saying that we're going to ride to the other side of the beach and embark on a grand adventure...!"
    show dating_story 002-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "So hurry up and hop on board with Mr. Sharky and me!"
    show dating_story 002-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "There's no one else around, so your fragile ego won't be harmed in the process."
    show dating_story 002-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show dating_story 002-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Come on! Don't be such a spoil sport!"
    show dating_story 002-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Get on! I'll be heroine of this story, and you get to be my trusty sidekick!"
    show dating_story 002-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    menu:
        "Fine, I'll ride with you..." if True:
            $ renpy.fix_rollback()
            show dating_story 002-18 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Hah!"
            show dating_story 002-34 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "So you've finally decided to see it my way, huh!?"
            show dating_story 002-35 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Not really."
            mc "You're just so adamant on riding Mr. Sharky that I can't leave you hanging."
            show dating_story 002-18 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Hehe..."
            show dating_story 002-33 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Thank you, [mc]..."
            call dating_mood_up
            show aff_este at up_happy
            "[yel]Estelle appears enthusiastic..."
            hide aff_este
        "Fine, I'll ride... but only if I get to be the {b}hero{/b}..." if True:
            $ renpy.fix_rollback()
            show dating_story 002-24 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            with vpunch
            este "No way!"
            show dating_story 002-25 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "I'm the hero, not you!"
            show dating_story 002-29 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Are you kidding me?"
            mc "I should be the hero of this story, Estelle..."
            mc "I am, after all, older than you."
            show dating_story 002-36 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "So what if you are?"
            show dating_story 002-28 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "This story only needs one heroine and it's me!"
            show dating_story 002-29 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "*Sigh*"
            mc "You're having way too much fun with this..."
            call dating_mood_down
            show sad_este at up_happy
            "[yel]Estelle {i}really{/i} wants to be the hero..."
            hide sad_este
        "I'm still not riding that thing." if True:
            $ renpy.fix_rollback()
            show dating_story 002-30 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "...and why not?"
            show dating_story 002-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            mc "Do you know how silly I'll look riding that thing with you?"
            mc "Besides, it's not meant to hold two fully grown people."
            show dating_story 002-22 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Geez, [mc]..."
            este "You do realize that there's no one at the beach except us, right?"
            show dating_story 002-21 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Is your fragile ego really that important here?"
            show dating_story 002-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            call dating_mood_down
            show sad_este at up_happy
            "[yel]Estelle is upset with you..."
            hide sad_este
    call dating_mood_bar_label
    show dating_story 002-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "..."
    show dating_story 002-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Now get on top of Mr. Sharky, my trusty sidekick!"
    show dating_story 002-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Let us brave the cruel waters and sail off into the boundless sea!"
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show dating_story 002-40 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    este "..."
    show dating_story 002-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hehe..."
    este "Isn't this fun or what!?"
    show dating_story 002-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Why do I have to sit in the back?"
    show dating_story 002-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "I thought we already went over this..."
    show dating_story 002-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Heroines sit in the front. Side characters sit in the back. That's the rules."
    show dating_story 002-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Ugh..."
    mc "I'm the main character... not you..."
    show dating_story 002-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Now are you ready to set sail?"
    show dating_story 002-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Onward to adventure! The legendary treasure known only as the 'Two Piece' shall be ours!"
    show dating_story 002-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show dating_story 002-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "(If she's going to start moving, I should probably hold on tight...)"
    menu:
        "Hold on to her waist..." if True:
            $ renpy.fix_rollback()
            show dating_story 002-47 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            show dating_story 002-48 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            este "..."
            show dating_story 002-49 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "(Huh?)"
            mc "(Why isn't she saying anything?)"
            show dating_story 002-50 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "H-Hey, [mc]?"
            show dating_story 002-51 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "What is it now?"
            mc "Don't tell me you're going to call me a creep, a hentai, and a pervert for holding your waist..."
            show dating_story 002-50 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "No, it's not that..."
            este "I'm just wondering... is it me or are we sinking...?"
            scene black
            $ renpy.movie_cutscene("images/videos/dating_este_vid_02.webm", delay=None, loops=0, stop_music=False)
            play sound "audio/splash.mp3" volume 3
            scene black with Dissolve(1.5)
            $ renpy.pause(1.5, hard=True)
            "As predicted, Mr. Sharky couldn't handle our combined weight..."
            "Estelle and I swam back to shore shortly afterward..."
            call dating_mood_up
            show aff_este at up_happy
            "[yel]Estelle looks like she had fun..."
            hide aff_este
        "Hold on to her chest..." if True:
            $ renpy.fix_rollback()
            mc "..."
            show dating_story 002-40 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "(Fuck it...)"
            mc "(If she's going to make me tag along, I'm going to make things uncomfortable for her...)"
            show dating_story 002-52 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            este "..."
            show dating_story 002-55 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "(Huh?)"
            mc "(Why isn't there a reaction from her?)"
            mc "(Is she so distracted on her {i}adventure{/i} that she doesn't notice my hands on her tits?)"
            show dating_story 002-53 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "H-Hey, [mc]? What's going on?"
            show dating_story 002-54 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            with vpunch
            mc "N-Nothing at all!"
            mc "Definitely not trying to take advantage of the situation and feel you up!"
            show dating_story 002-50 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "[mc]..."
            este "Is it me or are we sinking...?"
            scene black
            $ renpy.movie_cutscene("images/videos/dating_este_vid_02.webm", delay=None, loops=0, stop_music=False)
            play sound "audio/splash.mp3" volume 3
            scene black with Dissolve(1.5)
            $ renpy.pause(1.5, hard=True)
            "As predicted, Mr. Sharky couldn't handle our combined weight..."
            "Estelle and I swam back to shore shortly afterward..."
            call dating_mood_up
            show aff_este at up_happy
            "[yel]Estelle looks like she had fun..."
            hide aff_este
        "Don't hold her at all..." if True:
            $ renpy.fix_rollback()
            show dating_story 002-43 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "You ready, [mc]?"
            show dating_story 002-42 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Yeah, yeah, yeah... Hurry up already..."
            show dating_story 002-45 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            este "Here we go then! Onward toward our grand adventure!"
            show dating_story 002-56 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            with vpunch
            mc "W-Whoa!!!"
            show dating_story 002-57 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            play sound "audio/splash.mp3" volume 3
            "*SPLASH*"
            scene black with Dissolve(1.5)
            $ renpy.pause(1.5, hard=True)
            "Your embarassing flop caused Estelle to forget about riding with Mr. Sharky..."
            "The two of you swam back to shore in shame..."
            call dating_mood_down
            show sad_este at up_happy
            "[yel]Estelle appears embarrassed for you..."
            hide sad_este
    call dating_mood_bar_label
    $ renpy.pause(3, hard=True)
    show dating_story 002-58 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    este "..."
    mc "..."
    show dating_story 002-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Well, that was a complete waste of time..."
    show dating_story 002-60 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Y-Yeah, you were right..."
    show dating_story 002-61 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "I just wanted to go on an amazing adventure with you..."
    $ renpy.pause(.5, hard=True)
    show dating_story 002-62 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    with vpunch
    mc "(W-What...!?)"
    mc "(Her pussy is showing!)"
    $ renpy.pause(.5, hard=True)
    show dating_story 002-63 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "[mc]?"
    este "W-Why are you staring at me like that...?"
    show dating_story 002-64 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "N-No reason!"
    show dating_story 002-66 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hey, I know that look..."
    show dating_story 002-65 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "You're thinking of something lewd again, aren't you?"
    show dating_story 002-67 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "A-Absolutely not!"
    show dating_story 002-68 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hmm..."
    este "Is there a crab next to me or something...?"
    show dating_story 002-69 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    este "...!?"
    mc "..."
    show dating_story 002-70 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Estelle, relax..."
    mc "I-It's perfectly normal for a man to see his [sil]'s pussy...!"
    show dating_story 002-71 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "KYAAAAAAHHH!!!"
    este "CREEP!!! PERVERT!!! HENTAI!!!"
    $ renpy.pause(1, hard=True)
    if (dating_mood_pts < 5):
        call dating_mood_bar_hide
        scene black with Dissolve(1.5)
        $ renpy.pause(1.5, hard=True)
        "Estelle rose to her feet and ran all the way home with tears in her eyes..."
        "As for me, I was stuck spending the rest of the afternoon at the beach by myself..."
        "This definitely didn't go the way I wanted it to..."
        $ renpy.pause(1.5, hard=True)
        play music "audio/days.mp3"
        $ renpy.pause(.5, hard=True)
        jump beachlabel_01
    elif True:
        call dating_mood_bar_hide
        show dating_story 002-72 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        mc "C-Chill out, Estelle! It was an accident!"
        mc "And besides! You're acting as though this was my fault!"
        show dating_story 002-73 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "Y-You saw it..."
        show dating_story 002-74 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "You saw my special spot... the place only my husband is allowed to see..."
        show dating_story 002-75 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "Now I can't get married anymore..."
        show dating_story 002-72 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        with vpunch
        mc "*GULP*"
        mc "H-Hey, Estelle! Relax!"
        mc "It's normal that we see each other naked every once in a while!"
        show dating_story 002-76 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "R-Really?"
        este "That's supposed to be normal?"
        show dating_story 002-77 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "..."
        mc "(Estelle can be surprisingly gullible...)"
        mc "(I guess that just means she trusts me...)"
        este "..."
        show dating_story 002-78 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "You're lying, aren't you?"
        show dating_story 002-77 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        with vpunch
        mc "N-Not at all!"
        mc "If we live under the same roof, we're bound to see each other naked by accident, right!?"
        mc "That's just a fact of life!"
        show dating_story 002-78 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "I see..."
        show dating_story 002-76 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "In that case..."
        show dating_story 002-79 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "I want to see {b}your{/b} special spot, too!"
        show dating_story 002-80 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "..."
        with vpunch
        mc "M-My special spot!?"
        show dating_story 002-79 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "Uh-huh..."
        show dating_story 002-81 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "You know? That disgusting thing you showed me before?"
        show dating_story 002-80 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "..."
        mc "Why do you want to see it...?"
        show dating_story 002-78 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "Er..."
        este "Don't get me wrong! I'm not interested in it or anything!"
        show dating_story 002-76 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "It's just for educational purposes, you dummy! Not like I care if it's yours or some random guy's penis on the street!"
        show dating_story 002-77 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "..."
        mc "Fuck it, I'll show you then..."
        show dating_story 002-82 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        with vpunch
        este "Eh?"
        este "It's already this big?"
        show dating_story 002-83 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "Well, yeah..."
        mc "Seeing your pussy made it hard like this..."
        show dating_story 002-84 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "Wow..."
        este "So you do think of me like that, huh?"
        show dating_story 002-83 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "..."
        show dating_story 002-85 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "Alright, then..."
        show dating_story 002-86 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "Hurry up and make the white stuff come out..."
        show dating_story 002-87 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "..."
        mc "We talked about this, remember?"
        mc "I'm going to need proper stimulation for that to happen..."
        show dating_story 002-88 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "Oh, yeah...!"
        show dating_story 002-89 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        este "I should touch it like this then, right?"
        show dating_story 002-90 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        show dating_este_vid_03
        pause
        mc "*GULP*"
        mc "(Her fingers are soft and slender...!)"
        este "How is it, [mc]?"
        este "Does it feel good?"
        mc "Y-Yeah..."
        mc "You've improved from before..."
        hide dating_este_vid_03
        show dating_story 002-91 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "Hey, Estelle?"
        mc "Can I try something else on you?"
        show dating_story 002-92 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "Eh?"
        este "T-This isn't enough?"
        show dating_story 002-91 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "No, no, it feels good..."
        mc "It's just that... I want to make you feel good, too..."
        show dating_story 002-93 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "I-I don't understand..."
        show dating_story 002-91 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "..."
        mc "Turn around for me..."
        show dating_story 002-92 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "Why...?"
        show dating_story 002-91 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "Because you have a cute little ass..."
        mc "...and I want to see it."
        show dating_story 002-94 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        este "Like this?"
        show dating_story 002-95 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "..."
        mc "Estelle, you're cute when you're actually doing what you're told..."
        show dating_story 002-96 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "S-Shut up!"
        show dating_story 002-95 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "..."
        mc "I'm going to take off your bottom, okay?"
        show dating_story 002-96 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        with vpunch
        este "Eh?"
        este "N-No way!"
        show dating_story 002-95 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "Come on, Estelle..."
        mc "Don't you remember what we discussed...? I showed you my special spot, so you should show me yours..."
        show dating_story 002-97 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "..."
        show dating_story 002-94 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "Just don't put it {i}inside{/i} me, okay?"
        show dating_story 002-96 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "I'm not ready for that yet..."
        $ renpy.pause(.5, hard=True)
        show dating_story 002-98 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        este "..."
        show dating_story 002-99 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        mc "Mmm..."
        mc "You really do have a cute little ass, Estelle..."
        show dating_story 002-100 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        este "Um..."
        este "What are you going to do now?"
        show dating_story 002-99 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "Let me see..."
        mc "How about this?"
        show dating_story 002-101 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        with vpunch
        este "Ah...!"
        este "I-I told you not to put it in...!"
        show dating_story 002-102 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "Calm down..."
        mc "It's just my fingers..."
        show dating_este_vid_04
        pause
        mc "..."
        mc "(Her pussy walls are so tight...)"
        mc "(Estelle is clearly a virgin... I can feel her getting wet from my touch...)"
        este "[mc]..."
        este "W-What's going on? I feel weird..."
        mc "Haven't you ever masturbated before, Estelle?"
        mc "I'm finger fucking your pussy right now..."
        este "Ahn... it doesn't usually feel this good when I do it alone..."
        mc "Here, how about this?"
        hide dating_este_vid_04
        show dating_story 002-103 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        with vpunch
        este "Ahn...!"
        show dating_story 002-104 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        show dating_este_vid_05
        pause
        mc "..."
        mc "How often do you masturbate, Estelle?"
        este "N-None of... ahn... your business!"
        mc "Tell me!"
        este "N-Never...!"
        mc "I want to know how often my [sil] masturbates!"
        este "[mc]... S-Stop it..."
        mc "Yes?"
        este "Something's... ahn... coming out...!"
        scene whitescreen with Dissolve(1)
        $ renpy.pause(1, hard=True)
        show dating_story 002-105 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        with vpunch
        $ renpy.pause(1, hard=True)
        with vpunch
        este "NOOO!!!"
        $ renpy.pause(1, hard=True)
        show dating_story 002-106 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        mc "..."
        $ renpy.pause(1, hard=True)
        scene black with Dissolve(1.5)
        $ renpy.pause(3, hard=True)
        play music "audio/days.mp3"
        $ renpy.pause(.5, hard=True)
        jump beachlabel_01
    return


label dating_sere_01:
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3
    $ timeofday = 4
    $ dating_mood_pts = 1
    $ money -= 2000
    play sound "audio/coins.mp3" volume 3
    show love_adel at up_happy
    "[yel]You paid Adeline $2,000!"
    hide screen storescreen
    $ renpy.pause(3, hard=True)
    show dating_story 003-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    show dating_story 003-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I can't believe Serena agreed to come here with me..."
    show dating_story 003-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I'm so damn nervous... What should I do? What should I say?"
    show dating_story 003-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "No wait..."
    mc "This might be my only chance to ever see her in a bikini... I can't screw this up..."
    show dating_story 003-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "[mc]?"
    sere "I'm ready for you..."
    play music "audio/adeline.mp3"
    scene black with dissolve
    $ renpy.movie_cutscene("images/videos/dating_sere_vid_01.webm", delay=None, loops=0, stop_music=False)
    show dating_story 003-06
    show screen dating_mood_bar_01 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "W-Whoa..."
    show dating_story 003-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Heh..."
    sere "It's been a while since I came to the beach..."
    show dating_story 003-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Be honest, [mc]... How do I look?"
    show dating_story 003-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    menu:
        "You lookin' {b}cute{/b}..." if True:
            $ renpy.fix_rollback()
            show dating_story 003-10 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "'Cute'...?"
            show dating_story 003-11 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Y-Yeah..."
            mc "Is there something wrong with that?"
            show dating_story 003-12 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Nah..."
            sere "I was just hoping you'd say something else..."
            show dating_story 003-13 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "(I knew I should have splurged on something {b}sexier{/b}...)"
            sere "(He probably called me cute because of the design...)"
            call dating_mood_down
            show sad_sere at up_happy
            "[yel]Serena appears somewhat disappointed..."
            hide sad_sere
        "You lookin' {b}sexy{/b}..." if True:
            $ renpy.fix_rollback()
            show dating_story 003-14 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            sere "Eh?"
            sere "W-What did you just say?"
            show dating_story 003-15 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            with vpunch
            mc "I-I meant to say that you look {b}pretty{/b}!"
            show dating_story 003-16 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Ah, [mc]..."
            show dating_story 003-17 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "You're unexpectedly bold today..."
            call dating_mood_up
            show aff_sere at up_happy
            "[yel]Serena appears to have heard your original comment..."
            hide aff_sere
        "You lookin' {b}thicc{/b}..." if True:
            $ renpy.fix_rollback()
            show dating_story 003-14 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            sere "Eh?"
            sere "I-I'm {i}thicc{/i}!?"
            show dating_story 003-18 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "As in, big...!? Fat...!? Obese...!?"
            show dating_story 003-19 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Oh no... I knew I should have worn a one-piece instead..."
            show dating_story 003-20 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            with vpunch
            mc "I meant that in a good way!"
            mc "Thicc girls are trending nowadays! Everyone wants a little meat on their girls, y'know?"
            call dating_mood_down
            show sad_sere at up_happy
            "[yel]Serena doesn't seem to be listening..."
            hide sad_sere
    call dating_mood_bar_label
    show dating_story 003-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    show dating_story 003-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Maybe I should change into something else..."
    show dating_story 003-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "You know, something more {i}appropriate{/i}..."
    show dating_story 003-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "What's wrong with what you have on now?"
    show dating_story 003-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Er..."
    sere "It's a little too {i}tight{/i}... I haven't worn this bikini since high school..."
    show dating_story 003-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "(S-She's grabbing her tit...)"
    menu:
        "It brings out your curves..." if True:
            $ renpy.fix_rollback()
            show dating_story 003-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Eh?"
            sere "Are you saying that I'm fat...?"
            show dating_story 003-24 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Stop it, Serena..."
            mc "You have an amazing figure. You need to stop being self-conscious about your body..."
            mc "I'm going to love you no matter how you look."
            show dating_story 003-09 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "..."
            mc "And besides..."
            mc "I like a little meat on my girls..."
            mc "More pushin' in the cushion... If you know what I mean..."
            show dating_story 003-16 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Oh, [mc]..."
            show dating_story 003-17 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "If you like it, then I guess it doesn't matter..."
            call dating_mood_up
            show aff_sere at up_happy
            "[yel]Serena appreciates your assertiveness..."
            hide aff_sere
        "It suits you..." if True:
            $ renpy.fix_rollback()
            show dating_story 003-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Er..."
            sere "What do you mean by that...?"
            show dating_story 003-22 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "W-Well..."
            mc "It looks good on you, you know? I wouldn't change anything..."
            show dating_story 003-10 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "[mc], you're just trying to be nice..."
            show dating_story 003-12 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "The problem is that it's too tight... My chest feels like it's going to pop out..."
            call dating_mood_down
            show sad_sere at up_happy
            "[yel]Serena doesn't think you're being honest..."
            hide sad_sere
        "Should I help buy you something?" if True:
            $ renpy.fix_rollback()
            show dating_story 003-14 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            sere "Eh!?"
            sere "You mean you'd actually want to go shopping with me!?"
            show dating_story 003-15 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Yeah, why not?"
            mc "I'd love to see you try on different bikinis for me."
            show dating_story 003-16 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Oh, [mc]... You're so bold..."
            show dating_story 003-13 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "..."
            show dating_story 003-12 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "W-Wait, you can't..."
            show dating_story 003-19 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "B-Because if you came with me, you'd be able to see my {i}sizes{/i}."
            call dating_mood_down
            show sad_sere at up_happy
            "[yel]Serena is embarrassed..."
            hide sad_sere
    call dating_mood_bar_label
    show dating_story 003-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Alright, let's get moving..."
    mc "There's something I've prepared just for you..."
    show dating_story 003-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Sure thing, [mc]!"
    show dating_story 003-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Let's see what you have in store for me."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show dating_story 003-26 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    sere "..."
    show dating_story 003-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "D-Did you really bring food to the beach?"
    show dating_story 003-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Y-Yeah..."
    mc "I figured that since this is a, uh, d-date... we'd do some cute couple things together..."
    show dating_story 003-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "...Right."
    sere "So did you think of this idea yourself or was it something you found on the MagiNet?"
    show dating_story 003-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "The MagiNet..."
    show dating_story 003-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Of course..."
    show dating_story 003-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "W-We can do something else if you'd like! I'm up for anything!"
    show dating_story 003-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "No, no... I appreciate the thought, but..."
    show dating_story 003-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I'm on a diet... And I've already eaten before I got here..."
    show dating_story 003-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show dating_story 003-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "*Sniff* *Sniff*"
    sere "H-Hold on a second..."
    show dating_story 003-32 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    sere "Do I smell cheeseburgers?"
    show dating_story 003-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Y-Yeah..."
    mc "I know how much you like them so I got a few from JYP burger..."
    show dating_story 003-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Ah..."
    with vpunch
    sere "A big... meaty... juicy..."
    show dating_story 003-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "...mouthwatering cheeseburger sounds delicious..."
    show dating_story 003-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Uh..."
    mc "A-Are you alright, Serena?"
    show dating_story 003-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    sere "Ah..."
    show dating_story 003-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "R-Right... I can't eat them... they're really fattening..."
    sere "And I've been trying to watch my weight recently..."
    show dating_story 003-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(She looks like she really wants the burgers...)"
    mc "(How can I get her to eat them without having her feel guilty?)"
    menu:
        "We can take a walk around the beach instead..." if True:
            $ renpy.fix_rollback()
            show dating_story 003-37 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Eh?"
            sere "But what about the food?"
            show dating_story 003-40 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Well..."
            mc "They'll still be here when we get back, right?"
            show dating_story 003-38 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Yes, but then they'll be cold and soggy by then..."
            show dating_story 003-37 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Or maybe the bugs will get to them before we do!"
            show dating_story 003-38 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Hmm..."
            show dating_story 003-41 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Okay, I guess it can't be helped!"
            show dating_story 003-42 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "We have to eat them {i}now{/i}!"
            call dating_mood_up
            show aff_sere at up_happy
            "[yel]Serena is finding an excuse to gorge..."
            hide aff_sere
        "They're 'lean' burgers..." if True:
            $ renpy.fix_rollback()
            show dating_story 003-37 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "A-Are you being serious?"
            show dating_story 003-38 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Wait, aren't these just cheeseburgers from JYP Burger?"
            sere "When has their fast food ever been '{i}lean{/i}'...?"
            show dating_story 003-40 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            mc "A-Actually, I have no idea if they're lean or not..."
            mc "I just blurted what was on my mind..."
            show dating_story 003-37 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Geez, [mc]..."
            sere "Don't say stuff just to try and make me feel better..."
            show dating_story 003-38 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "I'll eat them, but only because I don't want to be wasteful..."
            call dating_mood_down
            show sad_sere at up_happy
            "[yel]Serena is disappointed in you..."
            hide sad_sere
        "I spent a pretty penny on them..." if True:
            $ renpy.fix_rollback()
            show dating_story 003-37 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "R-Really?"
            show dating_story 003-38 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Er, wait..."
            sere "Aren't these just cheeseburgers from JYP Burger?"
            show dating_story 003-40 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            with vpunch
            mc "W-Well, yes... Yes, they are..."
            mc "It can still be pricey if you buy a lot though, right?"
            show dating_story 003-37 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Geez, [mc]..."
            sere "Don't say stuff just to try and make me feel better..."
            show dating_story 003-38 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "I'll eat them, but only because I don't want to be wasteful..."
            call dating_mood_down
            show sad_sere at up_happy
            "[yel]Serena is depressed about eating..."
            hide sad_sere
    $ renpy.pause(.5, hard=True)
    call dating_mood_bar_label
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show dating_story 003-43 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    sere "..."
    show dating_story 003-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "They're delicious, [mc]..."
    show dating_story 003-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Thanks for making this trip perfect!"
    show dating_story 003-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "No problem..."
    show dating_story 003-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Speaking of which..."
    sere "I heard that this place is now closed to the public..."
    show dating_story 003-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "...all because someone wanted the beach to themselves?"
    show dating_story 003-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah..."
    mc "Those rumors are true..."
    show dating_story 003-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Geez, how selfish..."
    show dating_story 003-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "How are we even allowed here in the first place?"
    show dating_story 003-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu:
        "I know people... {i}Powerful{/i} people..." if True:
            $ renpy.fix_rollback()
            show dating_story 003-45 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Wow, [mc]... Color me impressed!"
            show dating_story 003-46 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Yep, I have all sorts of connections!"
            mc "Princess Laureate, Azula, and Makoto, to name a few..."
            show dating_story 003-47 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Eh?"
            sere "Hold on... Most of those names sound {i}girlish{/i}..."
            show dating_story 003-49 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            mc "Now that you think about it, a lot of my friends {i}are{/i} girls..."
            show dating_story 003-48 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Geez, [mc]..."
            sere "You big dummy..."
            call dating_mood_down
            show sad_sere at up_happy
            "[yel]Serena is worried about these {i}powerful girls{/i} you know..."
            hide sad_sere
        "I had to make a reservation..." if True:
            $ renpy.fix_rollback()
            show dating_story 003-47 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Er..."
            sere "That wasn't {i}expensive{/i} was it?"
            show dating_story 003-49 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Just a little..."
            mc "But it's worth the money if we can have the beach all to ourselves..."
            show dating_story 003-50 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "[mc], what a waste of money..."
            show dating_story 003-48 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "We could have just went to the park or something instead..."
            call dating_mood_down
            show sad_sere at up_happy
            "[yel]Serena is worried about your reckless spending..."
            hide sad_sere
        "We snuck in here illegally..." if True:
            $ renpy.fix_rollback()
            show dating_story 003-47 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "R-Really?"
            show dating_story 003-49 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            show dating_story 003-51 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Ah, [mc]..."
            show dating_story 003-52 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "When did you become so {i}daring{/i}?"
            call dating_mood_up
            show aff_sere at up_happy
            "[yel]Serena admires your rebellious spirit..."
            hide aff_sere
    call dating_mood_bar_label
    show dating_story 003-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    show dating_story 003-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "So [mc]..."
    show dating_story 003-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Do tell me more about these other girls you've been occupying yourself with lately..."
    show dating_story 003-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Huh?"
    show dating_story 003-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Don't try and deny it..."
    show dating_story 003-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I'm just wondering what you're relationship status is with them..."
    show dating_story 003-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Not that I care or anything..."
    show dating_story 003-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu:
        "They're just friends..." if True:
            $ renpy.fix_rollback()
            show dating_story 003-49 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "..."
            mc "..."
            mc "W-What's wrong?"
            show dating_story 003-50 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Nothing..."
            show dating_story 003-55 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "(If I don't act more aggressive, I might lose [mc] to these {i}friends{/i} of his...)"
            call dating_mood_down
            show sad_sere at up_happy
            "[yel]Serena senses a rivalry brewing..."
        "They're just friends... with {i}benefits{/i}..." if True:
            $ renpy.fix_rollback()
            show dating_story 003-57 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Eh?"
            sere "[mc], do you even know what that means?"
            show dating_story 003-49 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "...?"
            mc "All my friends help me out in some way or another..."
            mc "That includes you too, right Serena?"
            show dating_story 003-56 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "..."
            show dating_story 003-45 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Heh..."
            show dating_story 003-44 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "For you to say that so casually, it must be the truth!"
            call dating_mood_up
            show aff_sere at up_happy
            "[yel]Your comment went surprisingly well..."
            hide aff_sere
        "They're acquaintances..." if True:
            $ renpy.fix_rollback()
            show dating_story 003-49 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "..."
            mc "..."
            mc "Is something the matter?"
            show dating_story 003-50 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "No, not really..."
            show dating_story 003-55 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "(If I don't act more aggressive, I might lose [mc] to these {i}acquaintances{/i} of his...)"
            call dating_mood_down
            show sad_sere at up_happy
            "[yel]Serena senses a rivalry brewing..."
            hide sad_sere
    call dating_mood_bar_label
    show dating_story 003-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    show dating_story 003-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hey, [mc]..."
    show dating_story 003-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I don't know how to say this, but..."
    show dating_story 003-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Estelle's been telling me some things... {i}disturbing{/i} things, about you..."
    show dating_story 003-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "What's she on about this time?"
    show dating_story 003-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Er..."
    show dating_story 003-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Something about a {b}secret hentai collection{/b} you keep hidden in your room?"
    show dating_story 003-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Specifically, hentai involving {i}[sil]s{/i}?"
    show dating_story 003-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu:
        "... ... ..." if True:
            $ renpy.fix_rollback()
            show dating_story 003-48 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "So you don't deny it, huh?"
            show dating_story 003-49 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            mc "I have no control over how my penis gets hard."
            mc "Even if it's considered wrong by society's standards, the most important part of a fetish is not acting upon it, right?"
            show dating_story 003-47 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Well..."
            show dating_story 003-50 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "That's true, I suppose..."
            call dating_mood_up
            show aff_sere at up_happy
            "[yel]Serena appreciates your honest answer..."
            hide aff_sere
        "Estelle's lying!" if True:
            $ renpy.fix_rollback()
            show dating_story 003-47 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Er..."
            sere "Estelle actually showed me some of it..."
            show dating_story 003-56 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            mc "Goddamnit, Estelle..."
            call dating_mood_down
            show sad_sere at up_happy
            "[yel]Serena is disappointed in you..."
            hide sad_sere
        "Estelle is trying to sabotage me!" if True:
            $ renpy.fix_rollback()
            show dating_story 003-53 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Hmm..."
            show dating_story 003-54 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            with vpunch
            mc "I-I definitely don't know how that little [sil] hentai got there!"
            show dating_story 003-47 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Er..."
            sere "So you {i}have{/i} looked through them, huh?"
            show dating_story 003-48 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Some of the pages were also really {i}crinkled{/i} and {i}dry{/i}..."
            show dating_story 003-56 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            call dating_mood_down
            show sad_sere at up_happy
            "[yel]Serena questions your moral integrity..."
            hide sad_sere
    call dating_mood_bar_label
    show dating_story 003-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    show dating_story 003-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Still..."
    show dating_story 003-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "That type of fetish is a bit too much..."
    show dating_story 003-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Little [sil] hentai, really?"
    show dating_story 003-56 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh god..."
    show dating_story 003-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "[mc]..."
    show dating_story 003-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "You really will go to {b}HELL{/b} if you think of Estelle as anything more than a [sil]..."
    show dating_story 003-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "I-It's just fantasy, Serena! Not like I'd do it in real life!"
    show dating_story 003-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Fair enough..."
    show dating_story 003-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I can understand looking at anime girls, but you should at least watch {i}normal{/i} hentai..."
    show dating_story 003-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "...otherwise, you might end up with a weird fetish like armpits or feet or something."
    show dating_story 003-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(Too late...)"
    show dating_story 003-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hehe..."
    sere "Maybe you should watch hentai with cute plotlines..."
    show dating_story 003-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "...you know, like the ones where the two childhood friends get together?"
    show dating_story 003-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I don't know much about hentai but I'm sure they're the best kinds!"
    show dating_story 003-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu:
        "We should watch hentai together..." if True:
            $ renpy.fix_rollback()
            show dating_story 003-57 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            sere "Eh?"
            show dating_story 003-48 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "N-No way! That's so weird!"
            show dating_story 003-49 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Why not, Serena?"
            mc "Cute couple goals involve watching quality hentai together right?"
            show dating_story 003-51 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Oh, [mc]..."
            show dating_story 003-52 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "You're so naughty..."
            call dating_mood_up
            show aff_sere at up_happy
            "[yel]Serena might be down to watch hentai..."
            hide aff_sere
        "There's no such thing as hentai with cute plotlines..." if True:
            $ renpy.fix_rollback()
            show dating_story 003-53 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Really now..."
            show dating_story 003-58 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "To be honest, I don't know much about hentai..."
            show dating_story 003-60 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            mc "Yeah!"
            mc "Hentai is all about getting off! If clothes aren't off within the first 5 minutes, it's not real hentai!"
            show dating_story 003-58 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Mhmm.."
            show dating_story 003-59 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Clearly, you're a hentai connoisseur if you're willing to speak about it in front of a girl..."
            call dating_mood_down
            show sad_sere at up_happy
            "[yel]Serena wishes you had more {i}normal{/i} hobbies..."
            hide sad_sere
        "I'm far too cultured to enjoy the simplicity of vanilla hentai..." if True:
            $ renpy.fix_rollback()
            show dating_story 003-60 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "..."
            mc "..."
            show dating_story 003-59 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "[mc], I think you need to go outside more often..."
            call dating_mood_down
            show sad_sere at up_happy
            "[yel]Serena is disturbed by your choice of interests..."
            hide sad_sere
    call dating_mood_bar_label
    show dating_story 003-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    show dating_story 003-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hey, [mc]... I'm thirsty..."
    show dating_story 003-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Got anything to drink in there?"
    show dating_story 003-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Yeah, there should be water in the basket."
    mc "I'm pretty parched myself... Mind handing me a bottle, too?"
    show dating_story 003-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Sure..."
    sere "You really thought of everything, [mc]!"
    show dating_story 003-61 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mc "(Heh... I'm a genius...)"
    mc "(Serena's walking right into my trap...)"
    show dating_story 003-62 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hey, [mc]?"
    show dating_story 003-63 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "There was only {i}one{/i} water bottle..."
    show dating_story 003-64 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Is that right? Looks like I really screwed this one up!"
    show dating_story 003-65 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I guess we're going to have to {b}share{/b} that one bottle!"
    show dating_story 003-66 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Oh..."
    show dating_story 003-65 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "How about we do this?"
    show dating_story 003-64 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You drink the first half of the bottle! Then I'll drink the second half!"
    show dating_story 003-67 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Really?"
    show dating_story 003-68 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "That's courteous of you, [mc]! Thanks a bunch!"
    show dating_story 003-70 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mc "(Perfect! {b}Indirect kiss{/b}, here I come!)"
    show dating_story 003-69 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "*GLUG* *GLUG* *GLUG*"
    mc "(That's right, Serena...)"
    mc "(Press those succulent lips of yours all over that water bottle...)"
    mc "(Soon, I'll be sipping out of that same bottle... Hehe...)"
    show dating_story 003-71 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "*GLUG* *GLUG* *GLUG* *GLUG*"
    mc "..."
    show dating_story 003-72 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "H-Hey, Serena... Don't forget to save some for me..."
    show dating_story 003-73 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Eh...?"
    show dating_story 003-74 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Ah, how refreshing..."
    show dating_story 003-75 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Thanks again for letting me go first, [mc]."
    show dating_story 003-76 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Y-Yeah, no problem..."
    show dating_story 003-77 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    mc "...?"
    show dating_story 003-78 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "So what are you waiting for?"
    mc "Pass the water bottle to me..."
    show dating_story 003-79 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I'm sorry, [mc]..."
    show dating_story 003-80 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "But I drank it all by accident."
    show dating_story 003-81 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "What!?"
    show dating_story 003-79 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "P-Please don't be mad..."
    show dating_story 003-80 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I'll make it up to you somehow..."
    show dating_story 003-82 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(Shit! What do I do now!? I really wanted that indirect kiss from Serena!)"
    show dating_story 003-83 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    sere "(Oh, no! I ruined everything... [mc] looks so disappointed... What should I do?)"
    show dating_story 003-84 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Er..."
    sere "I-I'll go ahead and bin this and..."
    show dating_story 003-85 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "H-Hold on a second!"
    mc "Maybe there's a few drips left in the bottle! Even a little bit will be enough to quench my thirst!"
    show dating_story 003-86 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Y-Yeah, so hand the bottle over to me!"
    show dating_story 003-87 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(This is the only way I'll get that {b}indirect kiss{/b} from her... I can't afford to let this chance slip away!)"
    sere "..."
    show dating_story 003-88 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "(Now I feel {i}really{/i} bad...)"
    sere "([mc] is going to act like a gentlemen because he doesn't want to hurt my feelings...)"
    sere "(I'm horrible... I'm always messing things up and needing him to help me...)"
    show dating_story 003-89 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "[mc], you don't have to be nice to me..."
    show dating_story 003-90 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "This is my fault, so I'll go ahead and bin the bottle..."
    show dating_story 003-91 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "N-No, that's alright!"
    mc "Give me the bottle and I'll trash it for you!"
    show dating_story 003-92 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    sere "Eh?"
    sere "I said I'll do it! It's only fair!"
    show dating_story 003-93 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "No, no, no! I must insist!"
    mc "Hand that bottle over, Serena!"
    show dating_story 003-94 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    sere "No way, [mc]! I'll do it myself!"
    show dating_story 003-95 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    sere "Kyaaah!!!"
    show dating_story 003-96 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play sound "audio/fall.mp3" volume 3
    with vpunch
    mc "Are you alright, Serena?"
    sere "Ugh..."
    show dating_story 003-97 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Y-Yeah, I'm fine..."
    sere "Good thing there's sand to break my fall..."
    show dating_story 003-98 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    sere "EEEHHH!?"
    show dating_story 003-97 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...?"
    mc "W-What's wrong?"
    show dating_story 003-100 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Y-Your {b}thing{/b}..."
    mc "..."
    show dating_story 003-99 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "OH FUCK!!!"
    mc "(I must have gotten hard from imagining Serena's indirect kiss!!!)"
    $ renpy.pause(1, hard=True)
    if (dating_mood_pts < 5):
        call dating_mood_bar_hide
        scene black with Dissolve(1.5)
        $ renpy.pause(1.5, hard=True)
        "Serena took off without another word..."
        "My plan had backfired, and I spent the rest of the afternoon at the beach by myself..."
        "This definitely didn't end the way I wanted it to..."
        $ renpy.pause(1.5, hard=True)
        play music "audio/days.mp3"
        $ renpy.pause(.5, hard=True)
        jump beachlabel_01
    elif True:
        call dating_mood_bar_hide
        show dating_story 003-101 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        mc "..."
        mc "I'm sorry you had to see that, Serena..."
        show dating_story 003-102 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        sere "[mc], you don't have to be sorry..."
        show dating_story 003-103 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        sere "Seeing your dick like that when you're alone with me can only mean one thing..."
        show dating_story 003-104 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "...Serena?"
        show dating_story 003-105 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        sere "Well, don't just stand there..."
        show dating_story 003-103 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        sere "Hurry up and take it out, [mc]..."
        show dating_story 003-106 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        sere "I'm your {i}girlfriend{/i}, so I have to take care of that for you, right?"
        $ renpy.pause(.5, hard=True)
        scene black with Dissolve(1.5)
        $ renpy.pause(3, hard=True)
        show dating_story 003-107 with Dissolve(1.5)
        $ renpy.pause(1.5, hard=True)
        sere "..."
        show dating_story 003-108 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        sere "You're really packing a monster down there, [mc]..."
        show dating_story 003-109 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "..."
        mc "Thanks..."
        show dating_story 003-110 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        sere "Now then..."
        sere "Let's see if it feels as hard as it looks..."
        show dating_story 003-111 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        show dating_sere_vid_02
        pause
        sere "Oh wow, [mc]..."
        sere "I can feel it throbbing in my hand..."
        sere "You must be really pent-up, huh?"
        mc "Ugh... Serena..."
        mc "Your fingers feel so good..."
        sere "Hehe..."
        sere "I'm glad that you're enjoying yourself..."
        sere "But it looks like I'm still {i}thirsty{/i} after all..."
        hide dating_sere_vid_02
        show dating_story 003-112 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        with vpunch
        mc "W-Whoa...!"
        show dating_sere_vid_03
        pause
        mc "Oh god..."
        mc "You're sucking my dick!"
        sere "Howsh... ish... thish?"
        mc "F-Fuck..."
        mc "Every time you speak... your tongue just..."
        sere "Mmm... Ish tha goosh...?"
        mc "Goddamnit... {i}YES{/i}!!!"
        mc "(She isn't just sucking my dick... She's using her tongue as well...)"
        mc "(Serena really {i}is{/i} thirsty!)"
        sere "Mmm... Mmm..."
        mc "I can't hold it in any longer..."
        mc "Let go of my dick or else I'm going to...!!!"
        scene whitescreen with Dissolve(1.5)
        $ renpy.pause(1.5, hard=True)
        show dating_story 003-113 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        with vpunch
        sere "Eh!?"
        show dating_story 003-114 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        with vpunch
        $ renpy.pause(1, hard=True)
        with vpunch
        mc "AAARRRGGG...!!!"
        $ renpy.pause(1, hard=True)
        show dating_story 003-115 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        mc "S-Shit!"
        mc "I didn't mean to cum in your mouth like that!"
        show dating_story 003-118 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        with vpunch
        sere "*GULP*"
        mc "!?"
        mc "Did you just...?"
        show dating_story 003-116 with Dissolve(1)
        $ renpy.pause(1, hard=True)
        sere "Mmm... Thick and delicious..."
        show dating_story 003-117 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        sere "Thank you for the meal..."
        $ renpy.pause(1, hard=True)
        scene black with Dissolve(1.5)
        $ renpy.pause(3, hard=True)
        play music "audio/days.mp3"
        $ renpy.pause(.5, hard=True)
        jump beachlabel_01
    return

label dating_mako_01:
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3
    $ timeofday = 4
    $ dating_mood_pts = 1
    $ money -= 2000
    play sound "audio/coins.mp3" volume 3
    show love_adel at up_happy
    "[yel]You paid Adeline $2,000!"
    hide screen storescreen
    $ renpy.pause(3, hard=True)
    show dating_story 004-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    show dating_story 004-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Makoto said that she'd have something special to show me today, but..."
    show dating_story 004-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Could it be what I think it is...?"
    show dating_story 004-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "'Kay, I'm ready, [mc]..."
    mako "You can turn around now."
    play music "audio/adeline.mp3"
    scene black with dissolve
    $ renpy.movie_cutscene("images/videos/dating_mako_vid_01.webm", delay=None, loops=0, stop_music=False)
    show dating_story 004-05
    show screen dating_mood_bar_01 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Makoto..."
    show dating_story 004-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "S-Sorry..."
    mako "You were expecting a swimsuit, weren't you?"
    show dating_story 004-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Well..."
    mc "When you said you had something special for our date... I thought you meant a swimsuit..."
    show dating_story 004-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Ah, right..."
    mako "The truth is, I picked one up before we got here, but I just felt weird in it..."
    show dating_story 004-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I don't think I'm ready for one just yet..."
    show dating_story 004-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu:
        "You look {b}cute{/b} the way you are..." if True:
            show dating_story 004-09 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            mako "Eh!?"
            show dating_story 004-10 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "...Something wrong?"
            show dating_story 004-13 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "Y-Yes!"
            mako "You're the worst! You're obviously making fun of me, [mc]!"
            call dating_mood_down
            show sad_mako at up_happy
            "[yel]Makoto doesn't think you're being serious..."
            hide sad_mako
        "You look {b}sexy{/b} the way you are..." if True:
            show dating_story 004-09 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            mako "Eh!?"
            show dating_story 004-10 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "...Something wrong?"
            show dating_story 004-13 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "Y-Yes!"
            mako "You're the worst! You're obviously making fun of me, [mc]!"
            call dating_mood_down
            show sad_mako at up_happy
            "[yel]Makoto feels self-conscious..."
            hide sad_mako
        "You better change into that swimsuit right now!" if True:
            show dating_story 004-09 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            mako "W-What!?"
            show dating_story 004-10 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            mc "This is a good opportunity to try it on..."
            mc "There's no one around to see you in it except me..."
            show dating_story 004-11 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "Hmm... I guess that's true..."
            call dating_mood_up
            show aff_mako at up_happy
            "[yel]Makoto is thinking about your comment..."
            hide aff_mako
    call dating_mood_bar_label
    show dating_story 004-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "..."
    show dating_story 004-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I'm sorry by the way..."
    show dating_story 004-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "For what?"
    show dating_story 004-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Well, you had to spend a ton of money to reserve the beach for us, right?"
    show dating_story 004-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "If this place were still mine, we'd be able to come and go as we please..."
    show dating_story 004-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(Makoto looks upset, I should try and cheer her up...)"
    menu:
        "I'm going to buy the beach back for you someday!" if True:
            show dating_story 004-07 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "..."
            mc "...I'm being serious!"
            show dating_story 004-08 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "Don't bother..."
            mako "There's no way she'll sell the place... It has too much historical value for her to give away..."
            show dating_story 004-15 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "I'll never have this beach again... It's just something I'll have to live with..."
            call dating_mood_down
            show sad_mako at up_happy
            "[yel]Makoto appears somewhat regretful..."
            hide sad_mako
        "That just makes it more special..." if True:
            show dating_story 004-14 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "It's because of the beach that we're together, Makoto."
            mc "So don't be so negative about it! This place is special to the both of us!"
            show dating_story 004-15 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "Geez, [mc]... Where have I heard that line before?"
            show dating_story 004-14 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Well, it's true!"
            show dating_story 004-15 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "[mc]..."
            show dating_story 004-16 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "Y-Yeah, I guess you're right."
            call dating_mood_up
            show aff_mako at up_happy
            "[yel]Makoto appreciates your optimism..."
            hide aff_mako
        "But then we wouldn't be alone..." if True:
            show dating_story 004-06 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "What do you mean?"
            show dating_story 004-07 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Well, the beach was open to the public before, right?"
            mc "It's thanks to whoever bought the place that we have the place for ourselves."
            show dating_story 004-06 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "[mc], if I owned the beach..."
            mako "Wouldn't that mean I could close it down for the two of us whenever I wanted to?"
            show dating_story 004-07 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "T-True..."
            call dating_mood_down
            show sad_mako at up_happy
            "[yel]Makoto doesn't seem impressed by your answer..."
            hide sad_mako
    call dating_mood_bar_label
    show dating_story 004-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Hey, that's enough moping..."
    mc "How about a walk around the beach? It might be refreshing..."
    show dating_story 004-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "S-Sure..."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show dating_story 004-17 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    mc "We walked a really long way..."
    show dating_story 004-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Hehe... Yeah..."
    show dating_story 004-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Thanks for bringing me here, [mc]... You were right, this was a good idea."
    show dating_story 004-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Did you come here often?"
    mc "You know, since your family owned the beach..."
    show dating_story 004-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Can't say that I did..."
    show dating_story 004-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I was always busy with building growing up, as is the custom with everyone in my family..."
    show dating_story 004-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh, right..."
    mc "Your clan is very important to you... You're from the..."
    menu:
        "Kagawa Family..." if True:
            show dating_story 004-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "Really, [mc]?"
            mako "How'd you get that one wrong..."
            call dating_mood_down
            show sad_mako at up_happy
            "[yel]Makoto is disappointed in you..."
            hide sad_mako
        "Kamata Family..." if True:
            show dating_story 004-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "Really, [mc]?"
            mako "How'd you get that one wrong..."
            call dating_mood_down
            show sad_mako at up_happy
            "[yel]Makoto is disappointed in you..."
            hide sad_mako
        "Komagata Family..." if True:
            show dating_story 004-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "Really, [mc]?"
            mako "How'd you get that one wrong..."
            call dating_mood_down
            show sad_mako at up_happy
            "[yel]Makoto is disappointed in you..."
            hide sad_mako
        "Komatsu Family..." if True:
            show dating_story 004-18 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "Hehe... Right!"
            mako "I'm so glad you remembered!"
            show dating_story 004-17 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "See? I do know things about you!"
            call dating_mood_up
            show aff_mako at up_happy
            "[yel]Makoto looks happy..."
            hide aff_mako
        "Komoda Family..." if True:
            show dating_story 004-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "Really, [mc]?"
            mako "How'd you get that one wrong..."
            call dating_mood_down
            show sad_mako at up_happy
            "[yel]Makoto is disappointed in you..."
            hide sad_mako
        "Komuro Family..." if True:
            show dating_story 004-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "Really, [mc]?"
            mako "How'd you get that one wrong..."
            call dating_mood_down
            show sad_mako at up_happy
            "[yel]Makoto is disappointed in you..."
            hide sad_mako
    call dating_mood_bar_label
    show dating_story 004-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "..."
    show dating_story 004-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "But yeah, building is very important in the Komatsu Clan..."
    show dating_story 004-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Everyone in the family is an expert at making stuff! I was even given a hammer and a block set on my very first birthday!"
    show dating_story 004-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm..."
    mc "I know that you're the heir to the Builders Guild, but is there anyone else in your family?"
    show dating_story 004-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Well, I have extended family, of course..."
    show dating_story 004-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Before my father passed, many of them were affiliated with the Builders Guild in some way..."
    show dating_story 004-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "But after I took ownership, everyone left to start their own businesses away from the Builders Guild."
    show dating_story 004-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu:
        "We'll just start our own family!" if True:
            show dating_story 004-28 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            mako "Eh!?"
            show dating_story 004-22 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "You heard me!"
            mc "We'll have our own paradise where all of our little ones are skilled builders!"
            mc "Think about how much we'd save in labor costs!"
            show dating_story 004-24 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "Hehe..."
            mako "I don't know if you're joking or not but that sounds... {i}interesting{/i}..."
            call dating_mood_up
            show aff_mako at up_happy
            "[yel]Makoto is giggling..."
            hide aff_mako
        "Maybe you should try and get in touch with some of them..." if True:
            show dating_story 004-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "Hmm... That's a thought..."
            mako "To be honest, I do see them every once in a while..."
            show dating_story 004-27 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            mc "Is something wrong?"
            show dating_story 004-29 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "Well..."
            mako "If they left the Builders Guild after I took over, that must mean they don't like me very much, right?"
            call dating_mood_down
            show sad_mako at up_happy
            "[yel]Makoto appears conflicted..."
            hide sad_mako
        "I'd love to meet other members of your family..." if True:
            show dating_story 004-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "Hmm... That's a thought..."
            mako "To be honest, I do see them every once in a while..."
            show dating_story 004-27 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            mc "Is something wrong?"
            show dating_story 004-29 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "Well..."
            mako "If they left the Builders Guild after I took over, that must mean they don't like me very much, right?"
            call dating_mood_down
            show sad_mako at up_happy
            "[yel]Makoto appears conflicted..."
            hide sad_mako
    call dating_mood_bar_label
    show dating_story 004-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "..."
    show dating_story 004-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Hey, [mc]..."
    show dating_story 004-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah?"
    show dating_story 004-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "There's something I've been wanting to do since you invited me here..."
    show dating_story 004-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I hope you don't mind..."
    show dating_story 004-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Of course I won't..."
    mc "What did you want to do?"
    show dating_story 004-30 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mako "Hehe..."
    show dating_story 004-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu:
        "You want to dig for buried treasure..." if True:
            show dating_story 004-32 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "Treasure...?"
            mako "Don't be ridiculous, [mc]... That's for little kids..."
            show dating_story 004-33 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Really..."
            call dating_mood_down
            show sad_mako at up_happy
            "[yel]Makoto questions your maturity..."
            hide sad_mako
        "You want to bury me in the sand..." if True:
            show dating_story 004-32 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "Treasure...?"
            mako "Don't be ridiculous, [mc]... That's for little kids..."
            show dating_story 004-33 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Really..."
            call dating_mood_down
            show sad_mako at up_happy
            "[yel]Makoto questions your maturity..."
            hide sad_mako
        "You want to build a sand castle..." if True:
            show dating_story 004-32 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "Hey, how'd you guess that!?"
            show dating_story 004-33 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Well, I know you like building things..."
            mc "...But isn't stuff like that for little kids?"
            show dating_story 004-34 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mako "Ehehehe..."
            call dating_mood_up
            show aff_mako at up_happy
            "[yel]Makoto is pleased you know her so well..."
    call dating_mood_bar_label
    show dating_story 004-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I've always wanted to try making a sand castle..."
    mako "What do you think? A great idea, right?"
    show dating_story 004-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Er... Sure. It might be fun."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)


    mako "..."
    mako "Castles are so cool, [mc]..."
    mako "I want to build one for myself someday..."

    mc "Sheesh..."
    mc "Even now, you're thinking about building stuff, huh?"

    mako "Hehe..."
    mako "What do you think? How'd you like to be the king of a castle I built?"

    mc "..."

    menu:
        "Only if you're my queen..." if True:
            pass
        "" if True:
            pass





    sere "*GULP*"
    mc "!?"
    mc "Did you just...?"
    show dating_story 003-116 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "Mmm... Thick and delicious..."
    show dating_story 003-117 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Thank you for the meal..."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    play music "audio/days.mp3"
    $ renpy.pause(.5, hard=True)
    jump beachlabel_01
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
