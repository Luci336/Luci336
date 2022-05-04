label buylabel:

    show screen storescreen

    menu:
        "Purchase Estelle's Scarlet Contract - [red]$5,000" if (estebought == False):
            if (money >= 5000):
                $ money -= 5000
                $ estebought = True

                jump estebought
            elif True:
                "I don't have enough money..."
                hide screen storescreen
                return

        "Purchase Serena's Scarlet Contract - [red]$10,000" if (serebought == False and sereevents == 9):
            if (money >= 10000):
                $ money -= 10000
                $ serebought = True
                jump serebought
            elif True:
                "I don't have enough money..."
                hide screen storescreen
                return

        "Purchase Makoto's Scarlet Contract - [red]$10,000" if (makobought == False and makoevents == 6 and mainquest == 14):
            if (money >= 10000):
                $ money -= 10000
                $ makobought = True
                jump makobought
            elif True:
                "I don't have enough money..."
                hide screen storescreen
                return
        "Nevermind..." if True:

            hide screen storescreen
            return

label buildlabel:

    show screen storescreen

    menu:
        "Repair room for Azula - [red]$1,000" if (azulbought == False):
            if (money >= 1000):
                hide screen storescreen
                $ money -= 1000
                $ azulbought = True
                $ mainquest += 1
                $ timeofday = 5
                jump mainquest_13
            elif True:
                "I don't have enough money..."
                hide screen storescreen
                return
        "Nevermind..." if True:
            hide screen storescreen
            return

label estebought:
    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "With [mil!c]'s savings combined with my own, I was able to pay off Estelle's Scarlet Contract..."
    play sound "audio/coins.mp3" volume 3
    show love_laur at up_happy
    "[yel]You paid $5,000 to Laureate!"
    hide screen storescreen
    $ renpy.pause(1, hard=True)
    show story 003-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/laureate02.mp3"
    laur "..."
    show story 003-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Whew..."
    laur "It took all day, but the papers are finally notarized."
    show story 003-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Congratulations, [mc], you are officially Estelle's owner."
    laur "Hehe... How exciting is that?"
    show story 003-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Thanks, Laureate."
    mc "I couldn't have done this without you."
    show story 003-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "No problem..."
    laur "To be honest, I'm delighted that someone local is using the Scarlet Law..."
    laur "Every contract bought really does help Scarlet's economy."
    laur "Also, please do not forget that your weekly [yel]'Waifu Tax'{/color} bill will be increased, probably by about double..."
    laur "...so make sure you have money before the end of the week."
    show story 003-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah..."
    mc "Say Laureate, don't you ever feel like the Scarlet Law is..."
    mc "...you know, {b}evil{/b}?"
    mc "It can't be right to buy and sell people like livestock..."
    show story 003-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "[mc], you have a lot to learn about {i}ruling{/i}."
    laur "There are some things in life that even a princess cannot control."
    laur "The Scarlet Laws were created by the {b}Goddess{/b} who ruled this land many years ago..."
    laur "And its {i}curse{/i} will surely ruin Scarlet if its laws are not enforced."
    laur "Despite what most of the commonfolk think, this law is out of my hands."
    show story 003-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Right..."
    mc "I should probably head home and tell Estelle the good news then."
    mc "Good night, Princess."
    show story 003-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "..."
    mc "Huh?"
    mc "What is it?"
    show story 003-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Nothing, really..."
    laur "You originally wanted to save both your [mil] and little [sil], right?"
    laur "But allow me to make a bold prediction..."
    laur "...something tells me that you won't stop with just those two."
    laur "Not that I mind, of course, since buying contracts is great for Scarlet."
    show story 003-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "You're a weird one, Princess."
    mc "I only bought their contracts because I wanted to help them."
    mc "...there's no reason for me to want more."
    show story 003-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Hehe..."
    laur "If you say so."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3.0
    show story 003-07 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    mc "Alright, I'm back home."
    mc "I hope Estelle didn't go to bed already..."
    show story 003-08 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Oh, there's Estelle..."
    mc "Looks like she's still watching TV."
    show story 003-09 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play music "audio/estelle.mp3"
    mc "..."
    mc "Estelle, we need to talk."
    este "..."
    mc "..."
    mc "Estelle?"
    show story 003-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Not right now, [mc]..."
    este "I really want to watch this..."
    show story 003-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Estelle, it's important."
    show story 003-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "Urgh..."
    este "Fine, what is it!"
    show story 003-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Here..."
    mc "Take a look at this..."
    show story 003-13 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "..."
    "I handed her the notarized slip of paper that Laureate gave me..."
    "Estelle takes a moment to read it over before her eyes go wide..."
    show story 003-14 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "I-Is this what I think it is..."
    show story 003-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah, Estelle..."
    mc "You're free now..."
    mc "Well, not totally free since you belong to me, but..."
    mc "I think you know what I mean."
    show story 003-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "[mc]!!!"
    este "Does that mean that I get to stay with you and [mil!c] in Scarlet!?"
    show story 003-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah..."
    show story 003-17 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "W-Whoa!!!"
    show story 003-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Thank you so much, [mc]!!!"
    show story 003-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "I love you! I love you! I love you!"
    show story 003-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Heh..."
    mc "Don't mention it, Estelle..."
    mc "You know I could never leave my sweet little [sil] behind."
    show story 003-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "..."
    show story 003-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "D-Did you just... call me {b}sweet{/b}?"
    show story 003-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Of course..."
    mc "I used to always call you my sweet baby [sil], didn't I?"
    show story 003-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Ah..."
    este "Yeah, you did..."
    este "But that was a long time ago..."
    este "I'm always calling you names and stuff..."
    este "...I'm anything {i}but{/i} sweet to you."
    show story 003-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Estelle..."
    mc "That's just part of your duties as my little [sil]."
    mc "You're always going to give me hell."
    mc "And you know what? I don't ever want you to change."
    mc "I want you to keep being you, Estelle... Because that's what I love about you."
    show story 003-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "L-Love...?"
    show story 003-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    stop music fadeout 3
    "Estelle had a dazed look on her face..."
    "It's at this point that I realize my hands were holding up my little [sil]'s fleshy bottom..."
    "Her lips puffered out... Her face lowered to mine..."
    $ renpy.movie_cutscene("images/videos/estebought_01.webm", delay=None, loops=0, stop_music=False)
    show story 003-23
    $ renpy.pause(1.5, hard=True)
    show story 003-24 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 003-25 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    este "Eh!?"
    este "N-No way!!!"
    show story 003-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "G-Get off me, [mc]!"
    este "And where do you think your hands are touching!"
    este "Stupid! Creep! Hentai!"
    show story 003-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "What are you talking about!?"
    mc "You're the one who jumped on me!!!"
    show story 003-28 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/silvia.mp3"
    silv "Ehehehehehe..."
    silv "Don't stop on my account..."
    silv "I just love watching you two get all lovey-dovey..."
    show story 003-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    este "..."
    show story 003-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "N-No way..."
    este "How long were you standing there, [mil!c]?"
    show story 003-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hmm..."
    silv "I walked in at the moment you jumped into your hero's dashing arms..."
    silv "But really now, I wish you would show more affection toward each other."
    silv "You two were practically inseparable as kids..."
    silv "Now you're always at each other's throats."
    show story 003-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Ugh..."
    este "I'm going to be sick..."
    show story 003-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    "Estelle ran upstairs as fast as she could..."
    play sound "audio/door.mp3" volume 3
    "We could hear her slamming her bedroom door shut..."
    show story 003-34 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    silv "*Sigh*"
    silv "That girl should really be more honest with her feelings..."
    silv "I guess she is at that age, after all..."
    show story 003-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm..."
    mc "Well, I'd love it if we were as close as we were before, but..."
    mc "...We aren't children anymore, [mil!c]."
    show story 003-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "..."
    mc "Huh?"
    mc "What's with that look?"
    show story 003-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hehe..."
    silv "I'm just happy to hear that from you..."
    silv "And call it a hunch but I believe Estelle wishes that you were closer to her, too."
    show story 003-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "You and your hunches..."
    mc "Well, it's getting late."
    mc "I should probably head to bed."
    show story 003-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Eh?"
    silv "But what about the {b}first night{/b}?"
    show story 003-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "What's that?"
    show story 003-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "The first night is a tradition!"
    silv "If you're Scarlet Contract has been bought out, you have a responsibility to share the bed with your owner on the first night..."
    silv "Or else, {i}God{/i} will punish you."
    show story 003-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Pretty sure that's some silly myth."
    mc "If that were true, I would have heard about it when I bought the contracts..."
    silv "..."
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3.0
    show story 003-40 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    show story 003-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Time for bed..."
    mc "Got to wake up early in the morning..."
    show story 003-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(Crap, I can't forget how soft Estelle's ass felt when she gave me that hug earlier...)"
    mc "(It was difficult to not give her cheeks a firm squeeze...)"
    mc "(...n-not that I see her as a woman or anything.)"
    mc "(I mean, she's my little [sil]...)"
    show story 003-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    play sound "audio/knock.mp3" volume 3
    "*KNOCK* *KNOCK*"
    show story 003-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Huh?"
    mc "Who is it?"
    show story 003-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "[mc], it's me..."
    este "Can I have a word?"
    show story 003-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Uh..."
    mc "Sure, I guess..."
    play sound "audio/door.mp3" volume 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "Whatever she wanted, wasn't going to be quick..."
    "Estelle closed the door behind her, and locked it shut..."
    "Then, she walked over and sat down on my bed..."
    $ renpy.pause(.5, hard=True)
    show story 003-45 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    mc "(Estelle looks sexy in her nightgown...)"
    mc "(...she smells good, too.)"
    mc "(When did she grow up and become a woman?)"
    show story 003-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Er..."
    este "[mc], do you normally sleep without a shirt on..."
    show story 003-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Y-Yeah..."
    mc "It's a lot more comfortable..."
    show story 003-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "I-It's more comfortable for me too, but I still have the decency to put on a shirt, you know?"
    este "Ugh, that's why boys are so gross!"
    show story 003-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Estelle, what did you want to talk about?"
    show story 003-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Oh..."
    este "Um, don't get the wrong idea..."
    este "I didn't come here because I wanted to..."
    este "I came here because [mil!c] told me that I {i}had{/i} to..."
    este "Something about the {b}first night{/b} or whatever."
    show story 003-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Aw..."
    mc "And here I thought you were thinking of me."
    show story 003-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "..."
    este "A-Also..."
    este "I wanted to pick up where we left off..."
    show story 003-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "What?"
    show story 003-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Y-You were going to kiss me earlier, right?"
    show story 003-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I'm pretty sure that {i}you{/i} were the one trying to kiss me..."
    show story 003-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "N-No way!"
    este "W-Who wants to kiss a loser like you!"
    este "I'd never want to kiss my big [bil]! T-That's so gross!"
    show story 003-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Uh-huh..."
    mc "Whatever you say, Estelle..."
    show story 003-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Er..."
    este "I-I hate leaving things unsettled, so..."
    show story 003-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "So hurry up and kiss me quick so I can leave this disgusting room!"
    show story 003-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Nah..."
    show story 003-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Eh?"
    este "W-What did you just say?"
    show story 003-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I'm not going to kiss someone who doesn't want to be kissed."
    mc "That just wouldn't be right, even if I do control your Scarlet Contract."
    show story 003-50-1 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "..."
    show story 003-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Okay, fine..."
    este "I-I do want to kiss..."
    show story 003-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Can you say that louder?"
    mc "I don't think I heard you correctly."
    show story 003-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "I-I said I want a kiss from you..."
    show story 003-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "B-But not for the reason you think!"
    este "I just want to see what it's like is all!"
    este "It's definitely not because I like you or anything!"
    show story 003-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "To be honest, I wasn't really sure how this was done either..."
    "I don't have any experience with kissing girls..."
    "But being both older and the man around here, I knew I had to take charge."
    show story 003-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Okay, I'll do it..."
    mc "Close your eyes and I'll give you a kiss."
    show story 003-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Ah..."
    este "A-Alright..."
    show story 003-53 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    "Estelle closed her eyes and plucked her lips..."
    "She clearly trusted me..."
    "Most girls wouldn't dare close their eyes in front of a man while half-naked and vulnerable..."
    show story 003-54 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 003-53-1 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "There..."
    mc "All done."
    show story 003-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Eh?"
    este "B-But you only kissed me on the forehead..."
    show story 003-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Well, yeah..."
    mc "That's what you wanted right?"
    mc "Isn't that the kind of kiss that a big [bil] gives his little [sil]?"
    show story 003-55 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "N-No!"
    este "I wanted you to kiss me right {i}here{/i}..."
    este "...on the lips."
    show story 003-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "O-On the lips!?"
    mc "...Like we're lovers!?"
    show story 003-50-1 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "..."
    "There's a longing in her eyes..."
    "She really wants me to kiss her there..."
    show story 003-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Okay, I understand..."
    mc "Close your eyes one more time, Estelle."
    show story 003-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Ah..."
    este "S-Sure, but remember to be gentle..."
    este "...it's my first time."
    show story 003-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "She closes her eyes again and squeezes her lips..."
    "Estelle is so beautiful..."
    "I could feel her hot breath seeping into my nostrils..."
    mc "..."
    mc "(Here goes nothing...)"
    show story 003-56 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show estebought_02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    pause
    este "Mmn..."
    este "Mmn... Chu... Muah..."
    "This isn't just a peck on the lips..."
    "I'm literally making out with my little [sil]..."
    "I can taste the inside of her mouth... and she's not breathing a word of complaint..."
    "I'm amazed by how much I'm enjoying this..."
    este "Nyun... Mmm... Chu..."
    este "Mmn... Chu... Muah..."
    "Estelle's soft moans were a surprise..."
    "She was enjoying this as much as I was..."
    hide estebought_02
    show story 003-51 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    este "Ah..."
    este "T-That's it?"
    show story 003-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I can't believe we just did that, Estelle..."
    mc "We're [bil] and [sil]..."
    show story 003-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "I can't believe it either..."
    este "I can't believe I just lost my {i}virginity{/i}..."
    este "...it wasn't as painful as I thought it'd be."
    show story 003-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "WAIT, WHAT!?"
    show story 003-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "You better not tell anyone about this..."
    este "I'd die of embarrassment if people knew I lost my virginity to my own big [bil], got it!?"
    show story 003-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Estelle, just to be clear, we didn't have..."
    show story 003-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Good night, [mc]..."
    este "See you tomorrow!"
    este "Hehe..."
    show story 003-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    play sound "audio/door.mp3" volume 3
    mc "..."
    mc "I don't think Estelle knows what sex is..."
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "[yel]Estelle's Scarlet Contract has increased the weekly Waifu Tax."
    "[yel]Your relationship with Estelle has reached a new level!"
    $ renpy.end_replay()
    play music "audio/days.mp3"
    call advanceday
    call respawn
    call charquest
    jump mcroomlabel

label serebought:
    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    "After paying her fee, I signed off on the paperwork for Serena's Scarlet Contract..."
    "Laureate reminded me that my [yel]Waifu Tax{/color} will be increasing, so I better [yel]have money available{/color} before continuing any further..."
    "...because if I don't, this might end up with a [oj]GAME OVER{/color}."
    play sound "audio/coins.mp3" volume 3
    show love_laur at up_happy
    "[yel]You paid $10,000 to Laureate!"
    hide love_laur at up_happy
    hide screen storescreen
    $ renpy.pause(3, hard=True)
    "Serena has been my neighbor for as long as I can remember..."
    "She often came over to our house because her grandfather was busy with work..."
    "Because of this, we became the best of friends..."
    "We'd play together, go to and from school together, and even do sleepovers in each other's homes..."
    "..."
    "But things started to change when we entered puberty..."
    "Serena was an early bloomer... Her body shaped and developed rather quickly..."
    "She easily became one of the most popular girls in school by virtue of beauty alone..."
    "As for me? Well..."
    "I was the type of guy who sat at the back of class and couldn't wait for school to end..."
    "..."
    "When I started to see Serena as more than a friend, I began to distance myself from her..."
    "I was afraid that our relationship would change if she knew that I viewed her as a desirable woman..."
    "And the more popular Serena became, the less time she had to spend with me..."
    $ renpy.pause(3, hard=True)
    play music "audio/sad_05.mp3"
    show story 023-01 with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 023-02 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    mc "She looks like she's having fun..."
    show story 023-03 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    show story 023-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "*Sigh*"
    mc "What can I do to get her alone...?"
    show story 023-05 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    gen8 "Yo! Wassup, [mc]!"
    show story 023-06 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    gen9 "Whatcha' up to, bruh?"
    show story 023-07 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Oh, it's you two..."
    show story 023-07-1 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "What do you fucking assholes want?"
    show story 023-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen9 "Want to head over to the arcade with us after school?"
    gen9 "Or maybe I can stream something for you guys..."
    show story 023-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Nah..."
    mc "I have something to do today..."
    show story 023-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen8 "..."
    gen8 "You were checking out the cheerleaders, weren't you?"
    show story 023-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen8 "Specifically, Serena-san?"
    show story 023-11 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    show story 023-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen9 "Bruh..."
    gen9 "Everyone knows that Serena's hot as fuck, but let's be real..."
    show story 023-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen9 "Girls like her are on another level... They don't want anything to do with average [yel]joes{/color} like us."
    show story 023-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Maybe..."
    show story 023-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen8 "Hey, man..."
    gen8 "I know that you and Serena were close in middle school, but..."
    show story 023-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen8 "Times change... She probably has studs sliding into her DM's every single day..."
    show story 023-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen8 "People like us just can't compete with that..."
    show story 023-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Serena's not like that..."
    mc "She's... {i}special{/i}..."
    show story 023-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen9 "No, really bruh..."
    gen9 "I bet guys fap to her every day..."
    show story 023-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen9 "I'd be lying to the Goddess if I said I didn't..."
    show story 023-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Fuck you, asshole!"
    show story 023-21 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "Hey!"
    sere "Don't treat your friends like that!"
    show story 023-22 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Serena..."
    show story 023-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    gen8 "W-Whoa!"
    gen8 "Serena-san, has anyone ever told you how dazzling your [yel]armpits{/color} look when you do your cheers!?"
    show story 023-23-1 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "What...?"
    show story 023-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    gen9 "I-If you, uh, ever need any help with your homework, don't hesitate to ask!"
    gen9 "Heck, I don't mind doing it for you if I could just sniff your [yel]feet{/color} or maybe keep one of your used socks!"
    show story 023-24-1 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    show story 023-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Can you assholes leave us alone?"
    mc "Serena wants to speak with me."
    gen8 "..."
    gen9 "..."
    show story 023-26 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "..."
    show story 023-27 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "You know..."
    show story 023-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I'm starting to question your choice in friends, [mc]..."
    show story 023-29 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mc "Seems like your practice went well..."
    show story 023-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Yep!"
    show story 023-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "It's our last one before graduation so we wanted to make it extra special!"
    show story 023-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh..."
    mc "Well, that's good to hear..."
    show story 023-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    show story 023-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "So what brings you to the gym today, [mc]?"
    show story 023-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Were you waiting for practice to end just so you could see me?"
    show story 023-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...Maybe."
    show story 023-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hey, [mc]..."
    show story 023-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Prom is coming up, you know?"
    show story 023-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I'm not really into it or anything, but I guess it might be fun with the {i}right{/i} person..."
    show story 023-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(D-Damn, I'm choking up again...)"
    mc "(No, I can't give up! I'm here because I absolutely have to ask her!)"
    with vpunch
    mc "H-Hey, Serena..."
    mc "I was wondering... if you aren't too busy... Would you be interested in going to..."
    show story 023-39 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    gen1 "Serena!!!"
    gen1 "Me and the girls are going out for smoothies!!! Want to come!?"
    show story 023-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Ah...!"
    sere "Sure, just give me a minute...!"
    show story 023-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    mc "..."
    show story 023-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Er..."
    show story 023-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Was there something you wanted to ask me?"
    show story 023-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "No, it's nothing..."
    mc "Have fun with your friends..."
    show story 023-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Oh..."
    show story 023-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Well, see you later then, [mc]..."
    show story 023-45 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mc "Damn... I couldn't ask her today, either..."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 023-46 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    show story 023-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "It's almost the end of the year..."
    mc "No more school... No more homework... No more waking up in the early morning..."
    show story 023-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I don't know what my future holds, but I'm sure I'll land a decent job and find my place in the world!"
    show story 023-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "That's when I'll finally have some independence in my life!"
    show story 023-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 023-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Can't say I'll miss being a student very much..."
    mc "My grades aren't impressive... I'm not very popular... and I suck at sports..."
    show story 023-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "But despite all that..."
    mc "There's one thing that I absolutely have to do before I leave here..."
    show story 023-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "If I don't do it now, I might end up regretting it for the rest of my life..."
    show story 023-50 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "This necklace... I spent the entire year saving up for it..."
    show story 023-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "That's why I have to ask her out to prom... I have to tell her how I really feel..."
    mc "...before it's too late."
    show story 023-52 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    sere "You girls go on ahead..."
    sere "...I need to get something from my locker first."
    show story 023-53 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "(It's Serena...!)"
    mc "(Perfect! It looks like her friends are leaving...)"
    show story 023-54 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mc "Hey, Serena...?"
    show story 023-55 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Eh?"
    show story 023-56 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Oh, hey there, [mc]."
    show story 023-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "What's up?"
    show story 023-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(I can't back out... Today's the last day I can ask her out to prom...!)"
    show story 023-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Er..."
    sere "You okay? You look like you're about to faint..."
    show story 023-60 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "Here, let me..."
    with vpunch
    mc "!?"
    show story 023-61 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hmm, it's not a fever..."
    sere "Do you want me to walk you to the nurse?"
    show story 023-58 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    with vpunch
    mc "S-Serena-san! There's something I want you to have!"
    show story 023-62 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Here you are! It's not much, but..."
    mc "I've been saving up everything I have to get this for you, Serena!"
    show story 023-63 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "This is... a {i}necklace{/i}?"
    show story 023-62 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(Oh god! She must hate it!)"
    mc "(I knew this was a stupid idea!)"
    show story 023-64 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    gen1 "Pfft..."
    gen1 "This loser actually went ahead and did it!"
    show story 023-65 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen2 "Ahaha!"
    gen2 "Didn't that boy from Class C offer Serena a gold ring the other day?"
    show story 023-66 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen1 "Oh yeah! He was like..."
    with vpunch
    gen1 "'OMG SERENA MY FAVORITE WAIFU PLEASE MARRY ME!!!'"
    show story 023-65 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen2 "Ahaha! He was on his knees, begging Serena to go out with him!"
    show story 023-67 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    sere "..."
    show story 023-68 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hey..."
    sere "Can you girls cut it out? [mc] is trying to tell me something important..."
    show story 023-65 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    gen2 "Get it through your head, loser!"
    gen2 "Serena is cute and popular... You? You're weird and creepy!"
    show story 023-66 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen1 "That's right!"
    gen1 "Don't tell me you were thinking about asking Serena to the prom?"
    gen1 "A nobody like you needs to learn his place! You're no different than the dozen other otaku weeb nerds who tried asking her out!"
    show story 023-67 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 023-69 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Take the necklace, Serena..."
    show story 023-70 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Keep it or trash it... It doesn't matter anymore..."
    show story 023-71 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "I..."
    show story 023-72 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I-I have to go now... See you later, Serena..."
    show story 023-73 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Wait a second..."
    show story 023-74 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "[mc]..."
    $ renpy.pause(1, hard=True)
    stop music fadeout 3.0
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 023-75 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 023-76 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "..."
    show story 023-77 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Geez..."
    sere "You really had this room prepared just for me?"
    show story 023-78 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "We have [mil!c] and Estelle to thank for that..."
    show story 023-79 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "There was a lot of stuff in here. If they didn't already start cleaning, I would have been stuck here for a while."
    show story 023-80 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Geez..."
    sere "I don't deserve to have you as neighbors..."
    show story 023-79 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Well..."
    mc "Everyone in the house likes you, so it only makes sense that we want to help."
    show story 023-78 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I know that your debt is settled, but that shouldn't stop you from coming over to our place more often."
    mc "Heck, I doubt anyone would mind if you just {b}lived{/b} here."
    show story 023-81 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Ah..."
    show story 023-80 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I mean, living in an empty house by yourself does get pretty lonely..."
    show story 023-82 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 023-78 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Well, it's late..."
    show story 023-79 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I should probably head to bed..."
    show story 023-83 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "See you in the morning, Serena..."
    show story 023-84 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play music "audio/sad_02.mp3"
    sere "Hold on..."
    show story 023-85 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mc "(The way she's looking at me right now...)"
    show story 023-86 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "[mc]..."
    show story 023-87 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Everyone in the house is asleep, right?"
    show story 023-85 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...Y-Yeah."
    show story 023-87 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Then..."
    show story 023-86 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Just for today, will you sleep here with me?"
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 023-88 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    with vpunch
    mc "*GULP*"
    show story 023-89 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "[mc]..."
    show story 023-90 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "You're going to make me nervous if all you're going to do is stare..."
    show story 023-88 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I've dreamt about you for years, Serena..."
    mc "That's why, I want to savor this view for as long as I can..."
    show story 023-91 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    show story 023-92 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "You know, [mc]..."
    show story 023-89 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I've thought about this for a long time... about doing it with {i}you{/i}..."
    show story 023-88 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "During senior year..."
    mc "I wanted desperately to ask you out to prom..."
    mc "But you were so popular, so beautiful..."
    mc "That's why... I could never muster the courage to ask..."
    show story 023-89 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "[mc]..."
    show story 023-94 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "That was a long time ago, wasn't it?"
    show story 023-95 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "The two of us have grown up a lot since then..."
    show story 023-89 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "...And had you asked me to the prom all those years ago."
    show story 023-94 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I would have said {b}yes{/b}..."
    show story 023-96 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "Because I love you, [mc]..."
    show story 023-97 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 023-98 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    sere "Eh!?"
    sere "W-What are you doing!?"
    show story 023-99 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Something I've been wanting to do for a while!"
    mc "I want to eat that sweet pussy of yours!"
    show story 023-100 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    show serebought_02
    pause
    sere "Ahn..."
    sere "No, stop [mc]!"
    mc "Mmm..."
    mc "(She's ridiculously wet!)"
    mc "(I can feel her juices seeping down my throat!)"
    sere "[mc]..."
    sere "I-It's dirty down there..."
    hide serebought_02
    show story 023-101 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    sere "Ahn...!"
    sere "[mc], I feel weird...!"
    show story 023-102 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show serebought_03
    pause
    mc "..."
    mc "(She's thrusting her hips and begging me to taste her...)"
    mc "(Serena must really like having her pussy licked...)"
    sere "Don't stop... Keeping licking me..."
    sere "Yes, right there!"
    scene whitescreen with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 023-102 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    sere "NOOO!!!"
    $ renpy.pause(1, hard=True)
    with vpunch
    $ renpy.pause(1, hard=True)
    with vpunch
    $ renpy.pause(1, hard=True)
    show story 023-103 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mc "Delicious..."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 023-104 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    sere "..."
    show story 023-105 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Oh my god..."
    show story 023-106 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I'm so sorry, [mc]... I swear I didn't mean to get it all over your face..."
    show story 023-108 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Haha..."
    show story 023-107 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You're so cute, Serena... I didn't expect you to squirt like that..."
    show story 023-105 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I-I ruined our first time together..."
    show story 023-106 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "You must think I'm a big pervert now..."
    show story 023-107 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "What do you mean, Serena?"
    show story 023-108 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Your juices taste {b}delicious{/b}!"
    show story 023-109 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "[mc]..."
    sere "I'm starting to think that you're the bigger pervert here..."
    show story 023-110 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 023-111 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Take a look down here..."
    mc "How about you help {i}me{/i} now?"
    show story 023-112 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Ah..."
    sere "Like this?"
    show story 023-113 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    show serebought_04
    pause
    mc "Oh, yeah..."
    mc "Your fingers feel nice and smooth..."
    sere "Really..?"
    sere "[mc], you're so lewd..."
    hide serebought_04
    show story 023-114 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "That's enough..."
    show story 023-115 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Eh?"
    sere "Did I mess up?"
    show story 023-116 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "No, no..."
    show story 023-114 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I'm just ready to put it in your now..."
    show story 023-115 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Ah..."
    show story 023-117 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "O-Okay, I'm ready for you..."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 023-118 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show serebought_01
    mc "..."
    mc "(She's soaking wet...)"
    mc "(Serena wants this as much as I do...)"
    sere "Stop teasing me and put it in, [mc]..."
    sere "I can't wait anymore."
    hide serebought_01
    show story 023-119 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 023-120 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    sere "Ahhhnnn..."
    show story 023-121 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "A-Are you alright? Did I hurt you?"
    show story 023-122 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I'm okay..."
    show story 023-123 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I just... didn't expect you to be so {b}big{/b}..."
    show story 023-121 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(When a girl tells you that your dick is big, a man can't help but feel something...)"
    show story 023-124 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    show story 023-125 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "What are you waiting for, lover boy?"
    show story 023-126 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Go ahead and fuck me already..."
    $ renpy.pause(1, hard=True)
    show story 023-127 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    show serebought_05
    pause
    mc "..."
    mc "Fuck, Serena..."
    mc "Your pussy feels so good..."
    sere "Your dick feels good too, [mc]..."
    sere "I'm happy... ahn... that we can do this... together..."
    hide serebought_05
    show story 023-128 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    show serebought_06
    pause
    mc "..."
    mc "I've thought about this... for years..."
    mc "About touching you... tasting you... {i}fucking{/i} you..."
    sere "[mc]..."
    mc "..."
    mc "Serena... I'm going to..."
    scene whitescreen with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 023-129 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    with vpunch
    $ renpy.pause(1.5, hard=True)
    with vpunch
    mc "Aaarrrggghhh!!!"
    $ renpy.pause(.5, hard=True)
    show story 023-130 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "..."
    show story 023-131 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "[mc]..."
    sere "You came so much..."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 023-132 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    sere "..."
    show story 023-133 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "[mc], before we go to bed..."
    show story 023-134 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I was thinking about what you said before..."
    show story 023-135 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "About what?"
    show story 023-133 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Well..."
    show story 023-134 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I know that my debt is cleared, so I won't lose the house, but..."
    show story 023-137 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I'd really like it if you and the others would let me stay here..."
    show story 023-135 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Serena..."
    show story 023-138 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I-I know that it's a lot to ask, but..."
    show story 023-134 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "It's lonely to stay in an empty house..."
    show story 023-139 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    sere "And I promise I'll be good! I'll cook! And clean! And..."
    show story 023-135 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You don't even have to finish..."
    show story 023-136 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "In my eyes, you're already a member of the household."
    show story 023-137 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "[mc]..."
    stop music fadeout 3.0
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    play sound "audio/ding.mp3" volume 3
    "[yel]Serena's Scarlet Contract has increased the weekly Waifu Tax."
    "[yel]Your relationship with Serena has reached a new level!"
    $ renpy.end_replay()
    play music "audio/days.mp3"
    call advanceday
    call respawn
    call charquest
    jump sereroomlabel

label makobought:
    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "With enough savings in my account, combined with Makoto's own, I was able to afford her Scarlet Contract..."
    play sound "audio/coins.mp3" volume 3
    show love_laur at up_happy
    "[yel]You paid $10,000 to Laureate!"
    hide screen storescreen
    $ renpy.pause(1, hard=True)
    show story 018-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/laureate02.mp3"
    laur "..."
    show story 018-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Superbly done, [mc]."
    show story 018-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "To think that you would secure the contract of a descendent of one of the [yel]Six Heroes{/color}..."
    show story 018-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "You mentioned them before..."
    mc "The heroes are the ones who vanquished the [yel]Evil Goddess{/color} from Scarlet, right?"
    show story 018-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Indeed!"
    show story 018-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Though they are known only by their sobriquets, the Six Heroes are revered and beloved by the people of Scarlet to this very day."
    show story 018-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Now let me think..."
    show story 018-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "I do seem to recall that the Komatsu Clan's hero, [yel]The Shepherd{/color}, was known for her timid and quiet nature..."
    show story 018-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "...but that would change quickly, once she got {i}angry{/i}."
    show story 018-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "She had some serious rage problems... She'd swing her mighty hammer so violently that the earth itself would shake..."
    show story 018-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "I'd imagine it'd be a pretty gruesome sight for her enemies, with their blood and guts spilled all over the place... Hehehehe..."
    show story 018-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "W-Why do you sound excited when you say that?"
    show story 018-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Is that so...?"
    show story 018-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Anyway, I'll go ahead and finalize these papers, [mc]."
    show story 018-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Also, your [yel]Waifu Tax{/color} will increase after today..."
    laur "So if you don't want to get {b}[oj]soft-locked{/color}{/b}, you better go {b}back{/b} and make sure you have a little extra money before you continue any further."
    show story 018-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "And congratulations on adding yet another girl to your harem."
    $ renpy.pause(1, hard=True)
    stop music fadeout 3.0
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    "After Laureate finished the paperwork, I returned to the Builders Guild to tell Makoto the news..."
    "Though everything successfully went according to plan, Makoto appeared glassy-eyed and emotionless..."
    "I could tell that there was a deep sense of regret over everything she had done..."
    $ renpy.pause(1, hard=True)
    show story 018-10 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/sad_02.mp3"
    mc "..."
    mc "Makoto, are you sure you're okay?"
    show story 018-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Huh?"
    show story 018-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Oh, yeah... I just can't believe that this is finally happening..."
    show story 018-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I've been telling myself that this was all for the Builders Guild, but..."
    show story 018-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Now that it's done, I don't know what to think or how to feel..."
    show story 018-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "It's like there's an emptiness inside my heart..."
    show story 018-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I feel as though I've let my family down by forfeiting the landmarks they've built up for generations..."
    show story 018-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Makoto..."
    mc "If you're having second thoughts, maybe we can void the contract..."
    mc "...maybe Laureate will be able to do something."
    show story 018-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "The princess won't be happy to hear that..."
    show story 018-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "And even if she did do something about it, the woman I sold the land to definitely won't sell it back to me."
    show story 018-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Makoto, don't forget about why you did this in the first place."
    mc "You wanted Pandoria to speak to you again... and you wanted to save the Builders Guild..."
    mc "Sure, you had to give up a lot... but think about what you gained in return."
    show story 018-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "..."
    mc "..."
    mc "Makoto, I'm sorry..."
    mc "This is all my fault... Maybe if we had never met, none of this would have happened..."
    show story 018-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "[mc]..."
    mako "I have to admit, I was having second thoughts throughout this entire ordeal..."
    show story 018-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I kept asking myself the same questions, 'Am I really making the right decision by surrendering my family's property?'"
    show story 018-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "'Would saving the Builders Guild really bring me happiness?'"
    show story 018-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "The truth is, even before I met you, I was reluctant and even thought about quitting my career as a builder..."
    mako "If there was no Builders Guild to look after, I'd be free to pursue other things and maybe live out the rest of my life without stressing over my family's name..."
    show story 018-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "But in the end, the reason why I didn't give up was because of {b}you{/b}, [mc]..."
    show story 018-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "That's the other major reason why I wanted to do this..."
    show story 018-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I wanted to be closer to {b}you{/b}, [mc]... and I couldn't think of a future without you..."
    show story 018-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I never thought I'd ever meet someone more important to me than Pandy, but..."
    show story 018-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "To me, you're more important than her and the Builders Guild combined..."
    show story 018-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Makoto..."
    mc "You're important to me, too... I promise I'll treat you with the love you deserve..."
    show story 018-19 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mako "Thank you, [mc]..."
    mako "I'm expecting great things out of you."
    show story 018-20 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 018-21 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mako "..."
    show story 018-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "[mc], d-don't stare so much..."
    show story 018-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...Why not?"
    mc "You're beautiful and I want to see you."
    show story 018-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "R-Really?"
    show story 018-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "But I don't look or act like a girl..."
    show story 018-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I don't know about that..."
    mc "The more I see you naked like this, the more I realize how much of a woman you are..."
    mako "..."
    show story 018-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Fine..."
    show story 018-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "There, now you can see everything..."
    show story 018-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Beautiful..."
    mc "But I still can't see {i}all{/i} of you, yet..."
    mc "Not with that eyepatch in the way..."
    show story 018-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mako "Ah...!"
    show story 018-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "No way, [mc]...! This eyepatch is a symbol of who I am!"
    show story 018-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm..."
    mc "Now that I think about it, I remember you wearing your eyepatch even when you were at the hot springs..."
    show story 018-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Y-Yeah..."
    show story 018-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I'm actually kind of self-conscious about my eye... I don't take off my eye-patch, like ever... Unless it's to swap or wash it..."
    show story 018-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 018-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "S-Speaking of which..."
    show story 018-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Pandy told me about what happened at the hot springs..."
    show story 018-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Er, about how I passed out after seeing your..."
    show story 018-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mako "{b}P-P-PENIS{/b}!!!"
    show story 018-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "T-There I said it..."
    show story 018-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh, I remember..."
    mc "That was pretty funny..."
    show story 018-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mako "No, it wasn't!"
    show story 018-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "How can I call myself a woman if I freak out from seeing my lover's p-penis?"
    show story 018-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I've even been trying to research them on the MagiNet but the mosiacs always get in the way..."
    show story 018-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "*GULP*"
    mc "Y-You've been researching about sex? Just for me?"
    show story 018-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Y-Yeah..."
    show story 018-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I did say that I was preparing for this moment, right?"
    show story 018-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Don't feel bad, Makoto. I used to think vaginas were gross... back when I was little kid..."
    mc "But over time, I realized how amazing they can be!"
    mc "For example, they're really warm, tight, and squishy...!"
    show story 018-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "[mc], you really aren't making me feel better..."
    show story 018-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "What I'm trying to say is..."
    mc "The more times you see a penis, the more desensitized you will be toward them in the future..."
    mc "That's why it'd be a good idea for you to see mines now..."
    mc "Then maybe next time, you won't feel the urge to want to faint..."
    show story 018-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "...I don't know."
    show story 018-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I have a feeling I'll faint the moment I see it..."
    show story 018-38 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    show story 018-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "How about you try touching it over my pants then?"
    show story 018-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Maybe if you feel its shape, you'll be more confident with seeing one..."
    show story 018-38-1 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mako "Eh!? T-Touch it!?"
    mako "W-Wait, why is there a bulge..."
    show story 018-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Because I'm hard..."
    show story 018-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Seeing you acting like a woman is getting me horny..."
    show story 018-38-1 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I-I did this... to you?"
    show story 018-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Of course you did..."
    mc "It's under my pants, so you won't see anything... How about you give it a try and cop a feel?"
    show story 018-38-1 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "..."
    mako "O-Okay, I guess we can try that..."
    mako "It's my responsibility to take care of you, after all..."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 018-42 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    show story 018-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "How does it feel?"
    show story 018-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I-I can feel it twitching..."
    mako "Is it normally supposed to be like this?"
    show story 018-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Only when I'm aroused..."
    mc "How about you try massaging it?"
    mc "It'll make me feel even better..."
    show story 018-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    show makobought_01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    pause
    mako "How's this?"
    mako "Am I doing it properly?"
    mc "Mmm..."
    mako "Eh?"
    mako "Am I too rough?"
    mc "No, no, no..."
    mc "It feels just right... Keep rubbing me there..."
    hide makobought_01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    show story 018-45 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    show story 018-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Makoto..."
    mc "I need to take my dick out now..."
    show story 018-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mako "Eh?"
    mako "B-But if you do that, I'll see it..."
    show story 018-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Come on, Makoto..."
    mc "I need to feel your skin... You're just torturing me like this..."
    show story 018-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "..."
    show story 018-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "A-Alright, but..."
    show story 018-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "If you're going to pull it out, you might as well just put it inside of me..."
    show story 018-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Are you sure you're ready?"
    mc "If you're having second thoughts, we can try this again some other time."
    show story 018-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Y-Yeah..."
    mako "The Builders Guild needs its male heir..."
    show story 018-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "That's why... I need you to fuck me, [mc]..."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 018-52 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    show story 018-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I'd really prefer it if you faced me, Makoto..."
    mc "I want to see your face as we make love..."
    show story 018-55 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I'm sorry, [mc]..."
    show story 018-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "But I just know for certain I'll pass out if I see {i}it{/i}..."
    show story 018-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Maybe next time, then..."
    show story 018-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "[mc]..."
    mako "According to this book I read about babymaking, you're supposed to keep thrusting until the white stuff comes out..."
    show story 018-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Y-Yeah..."
    mc "I know how babies are made, Makoto..."
    show story 018-56 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "And you're supposed to do it deep inside me..."
    show story 018-55 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Can your penis even reach that far?"
    show story 018-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "YOU SAYING MY DICK IS SMALL!?"
    show story 018-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Ah..."
    show story 018-56 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I-I don't know... I've never really seen one..."
    show story 018-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Look, Makoto..."
    mc "Just trust me. I know what I'm doing."
    show story 018-56 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I... trust you, [mc]..."
    show story 018-52 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show makobought_02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    pause
    mako "...Ouch."
    mc "Are you alright, Makoto?"
    mako "Y-Yeah..."
    mako "It hurts a little, but I'm okay..."
    mc "..."
    mc "(I'm actually doing it...!)"
    mc "(I'm taking Makoto's first time! I'm fucking her virgin pussy...!)"
    mc "(And my {b}goddess{/b}! She's amazingly tight!)"
    hide makobought_02
    show story 018-55 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mako "Ahn..."
    show story 018-56 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "[mc], it feels... kind of good..."
    show story 018-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "What was that?"
    show story 018-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I-I said it's starting to feel good..."
    show story 018-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "You know what? I'm going to make you feel even better then!"
    show story 018-57 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mako "Eh?"
    mako "W-What are you..."
    show makobought_03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Ah... Aaaahn...!"
    mako "[mc], y-you're too rough!"
    mc "Fuck, Makoto!"
    mc "You're just too damn cute!"
    mc "I'll go right ahead and put that baby you want so bad inside of you!"
    mako "N-No way!"
    scene whitescreen with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 018-58 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    $ renpy.pause(1, hard=True)
    with vpunch
    mako "Ah..."
    mako "It's all warm and sticky..."
    show story 018-59 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mc "Insemination complete."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 018-60 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "Makoto..."
    mc "That was amazing..."
    show story 018-61 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Thank you, [mc]..."
    show story 018-62 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "With this, I'll be able to save the Builders Guild."
    show story 018-60 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Y-Yeah..."
    mc "But why do you still look so disappointed?"
    mc "..."
    with vpunch
    mc "W-Was I not good enough...?"
    show story 018-61 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "No, no, no..."
    show story 018-63 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "It's just that..."
    show story 018-64 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "After today, you no longer have any reason to be with me now that I have your baby inside."
    show story 018-63 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "...our business with each other is officially over."
    show story 018-65 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Why would you think that?"
    show story 018-63 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I-Isn't that obvious...?"
    show story 018-64 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "After I get a big belly, I'm going to look even more uglier..."
    show story 018-63 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "...I'm sure you wouldn't even want to be seen in public with me."
    show story 018-65 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Makoto, don't be ridiculous... I'd never think that way."
    mc "And once the baby is out, I'll want to spend even more time with you..."
    mc "I can't let my son's mother down, can I?"
    show story 018-61 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "[mc]..."
    show story 018-62 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Thank you..."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3.0
    "I decided to leave Makoto at the Builder's Guild for the night..."
    "The moment I reached home, I fell asleep almost immediately..."
    play sound "audio/ding.mp3" volume 3
    "[yel]Makoto's Scarlet Contract has increased the weekly Waifu Tax."
    "[yel]Your relationship with Makoto has reached a new level."
    $ renpy.end_replay()
    play music "audio/days.mp3"
    call advanceday
    call respawn
    call charquest
    jump mcroomlabel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
