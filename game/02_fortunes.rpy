screen fortunepotscreen:
    hbox xalign 0.01 yalign 0.01:
        imagebutton:
            idle "screens_update/fortune_prizepot.webp"
    if (goldenticket):
        hbox xpos 0.08 ypos 0.07:
            text "{size=50}$[fortune_pot]" outlines [ (absolute(1), "#000", absolute(0), absolute(1)) ] color "#FFF" font "Timeless.ttf"
    else:
        hbox xpos 0.015 ypos 0.07:
            text "{size=38}Golden Ticket + $[fortune_pot]" outlines [ (absolute(1), "#000", absolute(0), absolute(1)) ] color "#FFF" font "Timeless.ttf"

label prize(fortune):

    $ prizesum = 0
    $ grandrng = 0
    if (fortune_pot <= 30000):
        $ fortune_pot += renpy.random.randint(1,50)

    if (fortune == "fortune_01"):
        $ grandrng = fortune_luck + renpy.random.randint(1,5000)
        if (grandrng >= 5000 and goldenticket == False):
            play sound "audio/flowers_ssr.mp3" volume 3
            "[yel]You won the GRAND PRIZE of $[fortune_pot]!!!"
            play sound "audio/flowers_ssr.mp3" volume 3
            "[yel]You also won a GOLDEN TICKET!!!"
            $ goldenticket = True
            $ money += fortune_pot
            $ fortune_pot = 10000
            $ fortune_luck = 0
            hide screen storescreen
            hide screen fortunepotscreen
            jump goldenticketwon
        elif (grandrng >= 5000 and goldenticket):
            play sound "audio/flowers_ssr.mp3" volume 3
            "[yel]You won the GRAND PRIZE of $[fortune_pot]!!!"
            $ money += fortune_pot
            $ fortune_pot = 10000
            $ fortune_luck = 0
        elif True:
            $ prizesum += renpy.random.randint(150,350)
            "[yel]You won a prize of $[prizesum]!"
            play sound "audio/flowers_r.mp3" volume 2
            "[oj]You feel luck surging through you..."
            $ money += prizesum

    elif (fortune == "fortune_02"):
        $ prizesum = renpy.random.randint(35,125)
        "[yel]You won a prize of $[prizesum]!"
        $ money += prizesum

    elif (fortune == "fortune_03"):
        $ prizesum = renpy.random.randint(10,40)
        "[yel]You won a minor prize of $[prizesum]!"
        $ money += prizesum

    elif (fortune == "fortune_04"):
        $ prizesum = renpy.random.randint(10,40)
        "[yel]You won a minor prize of $[prizesum]!"
        $ money += prizesum

    elif (fortune == "fortune_05"):
        $ prizesum = renpy.random.randint(10,25)
        "[yel]You won a minor prize of $[prizesum]!"
        $ money += prizesum

    return

label fortunepicking:


    $ fortune_cap += 1

    $ fortune_chance = ""
    $ fortune_chance = renpy.random.choice(['fortune_01', 'fortune_02', 'fortune_03', 'fortune_04', 'fortune_05', 'fortune_06', 'fortune_07', 'fortune_08', 'fortune_09'])

    if (fortune_chance == 'fortune_01'):
        $ fortune_luck += 1
        play sound "audio/flowers_ssr.mp3" volume 2
        show love_cele at up_happy
        show fortune_01 at right_to_left_fortune with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        "[yel]{i}Dai-kichi{/i}! You drew a great blessing!"
        call prize ("fortune_01")
    if (fortune_chance == 'fortune_02'):
        $ fortune_luck += 0.1
        play sound "audio/flowers_r.mp3" volume 2
        show love_cele at up_happy
        show fortune_02 at right_to_left_fortune with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        "[yel]{i}Chū-kichi{/i}! You drew a middle blessing!"
        call prize ("fortune_02")
    if (fortune_chance == 'fortune_03'):
        $ fortune_luck += 0.1
        play sound "audio/flowers_r.mp3" volume 2
        show love_cele at up_happy
        show fortune_03 at right_to_left_fortune with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        "[yel]{i}Shō-kichi{/i}! You drew a minor blessing!"
        call prize ("fortune_03")
    if (fortune_chance == 'fortune_04'):
        $ fortune_luck += 0.1
        play sound "audio/flowers_r.mp3" volume 2
        show love_cele at up_happy
        show fortune_04 at right_to_left_fortune with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        "[yel]{i}Han-Kichi{/i}! You drew a half blessing!"
        call prize ("fortune_04")
    if (fortune_chance == 'fortune_05'):
        $ fortune_luck += 0.1
        play sound "audio/flowers_r.mp3" volume 2
        show love_cele at up_happy
        show fortune_05 at right_to_left_fortune with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        "[yel]{i}Kichi{/i}! You drew a blessing!"
        call prize ("fortune_05")
    if (fortune_chance == 'fortune_06'):
        play sound "audio/depress.mp3" volume 3
        show sad_cele at up_happy
        show fortune_06 at right_to_left_fortune with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        "[yel]{i}Kyo{/i}! Uh-oh! You drew a curse!"
    if (fortune_chance == 'fortune_07'):
        play sound "audio/depress.mp3" volume 3
        show sad_cele at up_happy
        show fortune_07 at right_to_left_fortune with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        "[yel]{i}Han-Kyo{/i}! Uh-oh! You drew a half curse!"
    if (fortune_chance == 'fortune_08'):
        play sound "audio/depress.mp3" volume 3
        show sad_cele at up_happy
        show fortune_08 at right_to_left_fortune with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        "[yel]{i}Sho-Kyo{/i}! Uh-oh! You drew a minor curse!"
    if (fortune_chance == 'fortune_09'):
        $ fortune_luck -= 0.5
        play sound "audio/depress.mp3" volume 3
        show sad_cele at up_happy
        show fortune_09 at right_to_left_fortune with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        "[yel]{i}Dai-Kyo{/i}! Uh-oh! You drew a great curse!"
        play sound "audio/depress.mp3" volume 3
        "[oj]You feel terribly unlucky..."


    return


label goldenticketwon:
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 024-142 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/celestia.mp3"
    with vpunch
    cele "I-Impossible..."
    cele "I can't believe you actually won..."
    show story 024-155 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Heh..."
    mc "Don't underestimate me, Celestia! I can do anything if I put my mind to it!"
    show story 024-136 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Dang..."
    cele "Now I have to part with my favorite [yel]Golden Ticket{/color}..."
    show story 024-135 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "What the heck's so special about this!? There's nothing on it!"
    show story 024-138 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "You ever try finding all the Korok seeds in Zelda?"
    show story 024-156 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 024-137 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Sheesh..."
    cele "I really liked that thing, y'know!? I found it while I was dumpster diving!"
    show story 024-135 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Are you saying that this ticket actually has value?"
    show story 024-138 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Of course it has value..."
    show story 024-136 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Isn't it really pretty to look at?"
    show story 024-135 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    $ renpy.pause(1, hard=True)
    stop music fadeout 3.0
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump streetlabel_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
