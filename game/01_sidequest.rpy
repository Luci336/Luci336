

label cula00:
    hide screen status01
    hide screen storescreen
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show street02_cula 01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh..."
    mc "I've never seen you around here before..."
    mvcula "..."
    mc "Um, hello?"
    show street02_cula 02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvcula "Sorry..."
    mvcula "I've been told that I shouldn't get friendly with strangers."
    mvcula "...particularly if they are of the opposite sex."
    show street02_cula 01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Er..."
    mc "Do I really look {i}that{/i} intimidating?"
    show street02_cula 03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvcula "No, not really."
    mvcula "You actually look quite weak to me."
    show street02_cula 01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm..."
    mc "I see a bunch of flowers... does that mean you sell them?"
    mc "Perhaps for 1 gil?"
    show street02_cula 03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvcula "Not to you."
    mvcula "And I'm more in the business of {b}buying{/b} flowers..."
    mvcula "...particularly rare ones."
    mvcula "In fact, that's precisely the reason why I'm sitting out here right now."
    show street02_cula 01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You're sitting out here just to {i}buy{/i} flowers?"
    mc "Hold on, isn't it a little dangerous for you to be doing business out this late?"
    mc "What if someone tries to attack you?"
    show street02_cula 02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvcula "Hmph..."
    mvcula "What's the point of living if you choose to live in fear?"
    mvcula "And this is the only time of day in which I can buy flowers from people."
    mvcula "The rest of my day is spent doing other things."
    show street02_cula 01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I see..."
    with vpunch
    mc "Hey, your uniform!"
    mc "I recognize it! It's the uniform for [yel]Scarlet Magic Academy{/color}, right!?"
    mc "My little [sil] actually goes there!"
    show street02_cula 03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvcula "I don't care."
    mvcula "Unless you have any flowers to sell, please leave me alone."
    show street02_cula 01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Can I at least have your name?"
    show street02_cula 02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvcula "..."
    mvcula "Who honestly cares about my name?"
    mvcula "I'm more of an NPC character, anyway... Not like I'll ever win a [oj]Patreon Poll{/color} or anything..."
    mvcula "...I don't even get my own theme song."
    show street02_cula 01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "You're not very positive, are you?"
    play music "audio/days.mp3"
    jump street02_culatalk_label



label silv01_01:

    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 002-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/silvia.mp3"
    silv "..."
    show story 002-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Oh [mc], honey..."
    silv "There you are..."
    show story 002-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "What's up, [mil!c]?"
    show story 002-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "I was wondering if you could run a small errand for me..."
    silv "I'd do it myself but I'm currently preoccupied."
    show story 002-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I don't mind lending a hand, [mil!c]."
    mc "Tell me what you need me to do."
    show story 002-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Well..."
    silv "The flowers around the house are wilting..."
    silv "So I was wondering if you could get us some new ones."
    show story 002-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm..."
    mc "I know that there are some flowers at the park."
    mc "Should I go pick a few there?"
    show story 002-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "No, no, no, [mc]..."
    silv "Those flowers will wilt after only a few weeks..."
    silv "What we need are special flowers imbued with magic!"
    silv "And there just so happens to be a young woman around the corner who sells them!"
    silv "...though, I heard that she is cold toward strangers."
    show story 002-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Ah, I see..."
    mc "You want me to get a few from her, right?"
    show story 002-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Right!"
    silv "I hope that's not too much to ask."
    show story 002-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Not at all."
    mc "Leave it to me."
    show story 002-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Thank you, [mc]."
    silv "I'll go head and get my purse..."
    show story 002-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "That's alright, [mil!c]."
    mc "I did promise I'd take care of you when I bought your Scarlet Contract, remember?"
    mc "That includes financially, as well."
    show story 002-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hehe..."
    silv "My little man is taking care of me..."
    silv "That makes me so happy..."
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3.0
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    play music "audio/days.mp3"
    jump livingroomlabel

label silv01_02:

    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show street02_cula 01 with Dissolve(1.5)
    mc "Hey, Flower Girl..."
    mc "I heard that you have magical flowers for sale..."
    show street02_cula 03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvcula "I do have magical flowers..."
    mvcula "...but I won't sell them to just {i}anyone{/i}."
    show street02_cula 01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Huh?"
    mc "I don't understand..."
    show street02_cula 02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvcula "I'm saying that I'm willing to part with my magical flowers..."
    mvcula "...but only if the right conditions are met."
    show street02_cula 01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm, I see..."
    mc "And how does one satisfy those special conditions of yours?"
    mc "I'd really like to buy one of your flowers..."
    show street02_cula 03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvcula "Like people, flowers are living entities."
    mvcula "Therefore, I refuse to give them away haphazardly."
    mvcula "For me to sell you my magic flowers, you'll have to tell me the reason {i}why{/i} you want them."
    show street02_cula 01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I see..."
    mc "Well, the flowers in my house are dying, and I'd like new ones to replace them."
    mc "Is that a good enough reason?"
    show street02_cula 02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mvcula "Fuck off..."
    mvcula "Flowers aren't something you pick up just because they're pretty to look at."
    mvcula "Unless you have a better reason why you want my flowers, you can get lost."
    show street02_cula 01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Damn..."
    mc "And [mil!c] really wanted those flowers..."
    mc "I guess I'll have to tell her the bad news."
    show street02_cula 03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvcula "You..."
    mvcula "...are giving these flowers to your... [mil]?"
    show street02_cula 01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Y-Yeah..."
    mc "Why? Is that bad?"
    show street02_cula 03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvcula "No, not at all..."
    mvcula "The sincerity of giving a flower to a loved one is a respectable use of a flower..."
    mvcula "Very well, I will sell them to you."
    show street02_cula 01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh, wow..."
    mc "Thanks a bunch, er, Flower Girl."
    mc "How much do I owe you?"
    show street02_cula 03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvcula "Just this once, you can have these for free..."
    mvcula "I'm just satisfied knowing how you plan on using them."
    show street02_cula 01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Are you sure about that?"
    mc "I'd feel bad if you went out of business..."
    show street02_cula 02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvcula "Hmph."
    mvcula "Don't worry about me, I'm doing fine financially."
    show street02_cula 01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I see..."
    mc "Thanks again..."
    mc "I'll be sure to let my [mil!c] know about your generosity."
    play sound "audio/coins.mp3" volume 3
    show love_cula at up_happy
    "[yel]Flower Girl gave you a magical flower!"
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    play music "audio/days.mp3"
    $ inventory_magicflower += 1
    if (inventory_tutorial == False):
        $ inventory_tutorial = True
        play sound "audio/ding.mp3" volume 3
        call screen tutorialscreen_06 with Dissolve(1.5)
        $ renpy.pause(1.5, hard=True)
        while endgame != True:
            pause
    elif True:
        jump street02_culatalk_label

label silv01_03:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 002-04 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/silvia.mp3"
    mc "Hey, [mil!c]..."
    mc "I brought you the magical flowers you wanted."
    show story 002-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Oh, [mc]!"
    silv "Thank you so much!"
    silv "You're my hero..."
    silv "Is there anything that you'd like as a reward?"
    show story 002-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "A... reward?"
    "My cock twitched at the thought..."
    mc "My reward is..."
    with vpunch
    mc "Your smile, [mil!c]!"
    mc "There's nothing more satisfying to me than seeing you happy!"
    show story 002-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Aw, sweetheart..."
    silv "It's true, I haven't been this happy in years."
    show story 002-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Still..."
    silv "I do feel a little bad that I sent you out this late..."
    silv "...and I even made you use your own pocket money."
    show story 002-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh, about that..."
    mc "It turns out that the Flower Girl is a really nice person, after all."
    mc "She gave me these flowers here for free."
    show story 002-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Ah, that was awfully kind of her..."
    silv "Maybe I should bake her a pie for the next time I see her..."
    show story 002-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "[mil!c!]..."
    mc "You've always been like that..."
    show story 002-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hehe..."
    silv "Sorry, I just can't help it..."
    show story 002-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Alright, well..."
    mc "It's getting late, I think I'll have a shower before I head to bed."
    show story 002-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hold on, honey..."
    silv "How about a {i}kiss{/i} as a reward?"
    show story 002-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...a kiss?"
    show story 002-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Uh-huh..."
    silv "Don't tell me that you're too old for a kiss from your own [mil]..."
    show story 002-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu:
        "Accept the kiss..." if True:
            $ renpy.block_rollback()
            show story 002-09 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            with vpunch
            "*SMOOCH*"
        "Reject the kiss..." if True:
            $ renpy.block_rollback()
            mc "No, I think I'm..."
            show story 002-09 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            with vpunch
            "*SMOOCH*"
    show story 002-04 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    "It was just a light kiss on the cheek, but it was enough to make me turn red..."
    mc "T-Thanks, [mil!c]..."
    show story 002-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hehe..."
    silv "I'll leave you alone now."
    show story 002-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I think... I'll go have my shower now."
    show story 002-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Alrighty, dear..."
    silv "Thanks again for your help."
    show story 002-10 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    silv "..."
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/days.mp3"
    show story 002-11 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play sound "audio/shower.mp3" volume 3
    mc "..."
    mc "These last few days have been exhausting..."
    mc "But I won't give up!"
    mc "[mil!c] and Estelle are counting on me..."
    show story 002-12 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Speaking of which..."
    mc "This boner of mine refuses to go down..."
    mc "Why did I get hard from [mil!c]'s kiss?"
    stop sound
    play sound "audio/door.mp3" volume 3
    show story 002-13 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Huh?"
    show story 002-14 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "[mil!c]!"
    mc "I-I'm using the shower here!"
    show story 002-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hehe..."
    silv "I know that."
    silv "But skinship is a very important part of a healthy master-slave relationship!"
    silv "That's why I want to come and help clean you!"
    show story 002-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I told you, it doesn't have to be that way, [mil!c]."
    mc "Don't you think that you're taking this Scarlet Law thing too seriously?"
    show story 002-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Of course I am!"
    silv "During my years in the academy, I took Maid Training as my primary..."
    silv "And the one thing they drill into your head is the importance of keeping your master happy!"
    show story 002-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "The thought of her calling someone else her {i}master{/i} was a little unsettling..."
    mc "[mil!c], exactly how many masters have you served?"
    show story 002-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "None, actually..."
    silv "Unfortunately, I flunked out of Maid Academy before I had the chance to do it professionally..."
    silv "...that's why I ended up as a homemaker."
    show story 002-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh..."
    mc "I think you've mentioned that to me before."
    with vpunch
    mc "Wait, how the heck does anyone fail at being a maid!?"
    show story 002-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Eh?"
    silv "Being a maid is very, very serious business...."
    silv "The constant responsibility and pressure you're under is no joke!"
    silv "That's why I have nothing but the utmost respect for women who wear the maid's cloth!"
    show story 002-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...Sure."
    mc "If you say so."
    show story 002-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "..."
    mc "..."
    mc "Uh, why are you looking at me like that?"
    show story 002-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Because it's time for me to wash you..."
    silv "...my {i}master{/i}."
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "After a bit of coaxing, [mil!c] manages to enter the shower booth with me..."
    "Before I turned the other way, I noticed that she didn't bother to remove her towel as she stepped in."
    $ renpy.pause(.5, hard=True)
    show story 002-22 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 002-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    show silv01_03_01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    pause
    mc "..."
    mc "(Alright, calm down...)"
    mc "(It's just my [mil] scrubbing my back here...)"
    mc "(...{b}my hot MILF of a [mil]{/b} who jerked me off the other day.)"
    mc "(Nothing wrong with that...)"
    with vpunch
    mc "(W-Wait, what am I thinking!?)"
    mc "(This is my [mil], I can't be thinking about her like that...)"
    mc "(...I just hope she doesn't notice my boner.)"
    hide silv01_03_01 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 002-24 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    silv "..."
    silv "How's that feel, honey?"
    show story 002-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Erm..."
    mc "Great, actually."
    mc "Your fingers feel really soft."
    show story 002-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "That's good to hear..."
    silv "Would you like me to take care of {i}that{/i}, too?"
    show story 002-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Huh? What's {i}that{/i}?"
    show story 002-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "I mean your dick..."
    silv "It's been hard ever since I kissed you."
    show story 002-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "W-WHAT!?"
    show story 002-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Come now, don't be shy..."
    silv "I did wash it when you were a baby, didn't I?"
    silv "And it's very important to keep it clean or else you might get an infection..."
    show story 002-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah, but..."
    show story 002-30 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    silv "Ow..."
    show story 002-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "S-Shit..."
    mc "Sorry, I don't know why I got so nervous..."
    show story 002-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "That's okay..."
    silv "I know that you're not used to seeing me like this yet."
    show story 002-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "*GULP*"
    mc "(H-Her tits are huge...)"
    show story 002-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Ah..."
    silv "[mc], your thing is touching my leg..."
    show story 002-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Are you sure you don't want me to take care of it for you?"
    show story 002-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "Y-Yeah, I'm sure!"
    mc "I think I'm done with my shower!"
    mc "Love you, [mil!c]!"
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "I scrambled back to my bedroom, and dried myself off..."
    "It took a while, but my dick eventually calmed down."
    $ renpy.pause(.5, hard=True)
    show mcroom_night with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    $ renpy.end_replay()
    jump mcroomlabel

label silv02_01:

    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 010-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/silvia.mp3"
    mc "..."
    mc "Dinner was delicious today, [mil!c]."
    mc "Well, your food is always delicious..."
    show story 010-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Uh-huh..."
    este "I'm totally stuffed!"
    show story 010-03 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    silv "*Sniff* *Sniff*"
    silv "Just how many more of these dinners will we share together?"
    silv "You two are adults now... and it won't be long before I'm no longer needed..."
    silv "The only joy an old lady like myself has left in life is to spend what little time she has with her household..."
    silv "The day you both move out of the house... I'll... I'll..."
    with vpunch
    silv "WAAAAAAAAHHH!!!"
    show story 010-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Wow, [mil!c]..."
    mc "I had no idea you felt that way..."
    show story 010-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Y-Yeah..."
    este "If spending time together is what makes you happy..."
    show story 010-06 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "...then [mc] and I will make a better effort to hang out with you more often."
    show story 010-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "*Sniff* *Sniff*"
    silv "R-Really? Do you mean that?"
    show story 010-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    silv "Oh, you two are the best! I can't wait for all the household bonding we'll do!"
    show story 010-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "That's right... I am the best..."
    show story 010-10 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "Now then..."
    este "...I'm going to stare mindlessly at my phone until it's time for bed."
    show story 010-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yup, same here."
    mc "Nothing like a household bonding session than watching videos in the privacy of your own room."
    show story 010-12 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    silv "Eh!?"
    silv "B-But..."
    show story 010-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Peaceee!!!"
    show story 010-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Later everyone!"
    show story 010-15 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play sound "audio/slam.mp3" volume 3
    with vpunch
    silv "Noooo!!! Stoooooppp!!!"
    silv "The evening will not be wasted today on your phones!!!"
    silv "Us three are going to spend some quality time together!!!"
    silv "A-And I won't hear any lip about it from either of you!!!"
    show story 010-16 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    este "..."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "After nodding our heads sheepishly, [mil!c] decided that the three of us would spend the rest of the evening cleaning the house..."
    "Estelle and I both feigned a smile, pretending as though we were having fun..."
    "When the evening ended, we could tell that it was important for her to do stuff like this... every once in a while."
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    play music "audio/days.mp3"
    $ renpy.pause(.5, hard=True)
    jump mcroomlabel

label silv02_02:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 010-17 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "*Yawn*"
    mc "(Feels like I've been waking up earlier and earlier...)"
    mc "(I guess that's how it is when I'm living on a schedule.)"
    mc "..."
    mc "(I smell something good over at the kitchen)"
    show story 010-18 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    with vpunch
    mc "(W-Whoa, what's she wearing...?)"
    show story 010-19 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    silv "Eh?"
    show story 010-20 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play music "audio/silvia.mp3"
    silv "..."
    show story 010-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Oh my..."
    silv "[mc], you're up rather early..."
    show story 010-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Y-Yeah..."
    mc "Good morning, [mil!c]."
    mc "..."
    show story 010-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Is there something wrong?"
    show story 010-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "N-No, not really..."
    mc "Just why are you only in an apron?"
    show story 010-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Oh my..."
    silv "You're blushing so profusely... Could it be that you're getting a reaction from seeing me like this?"
    show story 010-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "T-That doesn't answer the question!"
    show story 010-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Ah..."
    silv "Do you recall when we did our {b}household bonding{/b}?"
    show story 010-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Whoever was in charge of the laundry forgot to put the clothes in the washing machine..."
    silv "...Because of that, I now have to wait until they've finished drying before I have something proper to put on."
    show story 010-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(H-Her milkers are {i}huge{/i}...)"
    show story 010-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Er, [mc]..."
    silv "Are you even listening to me?"
    show story 010-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Huh?"
    mc "Oh, yeah... laundry... right..."
    show story 010-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hmm..."
    silv "[mc], do you know who was on laundry duty?"
    silv "Was it you...? Or Estelle...?"
    show story 010-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "Actually, that was supposed to be my job..."
    "But I didn't know that I had to wash [mil!c] and Estelle's clothes, too..."
    "I only assumed that she only meant {i}my{/i} clothes."
    menu:
        "This is on me..." if True:
            $ renpy.fix_rollback()
            mc "Er..."
            mc "Sorry, [mil!c], but this is my fault..."
            mc "I didn't realize that you wanted me to wash everyone elses clothes, too."
            show story 010-24 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "I see..."
            silv "Well, I'm glad that you're being honest."
            show story 010-25 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            with vpunch
            mc "I'll make things right! I'll go ahead and put them in the washing machine right away!"
            show story 010-21 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "No, that'll be fine, sweetheart."
            silv "I've already taken the liberty of doing it myself, so there's no harm done."
            show story 010-22 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Speaking of which..."
            silv "The clothes should be finished in the dryer by now..."
            show story 010-21 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "I'll hurry along and get dressed."
            silv "Enjoy your breakfast, dear."
            show story 010-27 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            mc "..."
            mc "(That didn't go the way I wanted it to...)"
            $ renpy.pause(.5, hard=True)
            $ renpy.end_replay()
            play sound "audio/ding.mp3" volume 3
            "[yel]HINT: You can replay this scene in the gallery."
            play music "audio/days.mp3"
            $ renpy.pause(.5, hard=True)
            jump livingroomlabel
        "Blame Estelle..." if True:
            $ renpy.fix_rollback()
            mc "..."
            with vpunch
            mc "I-I'm pretty sure Estelle was in charge of the laundry!"
            show story 010-26 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Hmm..."
            silv "Is that right?"
            show story 010-28 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "*GULP*"
            mc "(Maybe it's her {i}womanly intuition{/i} but [mil!c] always seems to know when I'm lying...)"
            mc "(It's like she can stare directly into my soul and pull out the truth...)"
            silv "...."
            mc "..."
            with vpunch
            mc "Y-Yeah..."
            mc "Definitely not lying here! Nope, not me!"
            show story 010-29 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "..."
            mc "..."
            with vpunch
            mc "Y-Yup! Telling the truth here! Honest Abe would be proud!"
            silv "..."
            mc "Er..."
            mc "[mil!c], w-why are you looking at me like that?"
            show story 010-21 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Oh no, sweetheart..."
            silv "It's just that..."
            show story 010-22 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "...I couldn't help but notice that large tent poking out from between your legs."
            show story 010-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            with vpunch
            mc "I-I can explain!"
            show story 010-21 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "[mc], there's nothing to explain..."
            silv "I understand very well that you find me to be sexually attractive."
            silv "This isn't the first time you've seen me like this, if I'm not mistaken."
            show story 010-20 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "I know that, but..."
            show story 010-21 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "[mc], don't be ashamed."
            silv "It's completely natural for a young man to feel this way toward the female body."
            show story 010-22 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "If anything, I'd be more concerned if you didn't have an erection after seeing me like this."
            show story 010-30 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "And I promised, remember?"
            silv "I'll take care of my {i}master{/i}... Whenever he needs me..."
            show story 010-23 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            show story 010-30 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Don't feel ashamed, baby..."
            silv "As I've said, I'm here to {i}serve{/i}."
            show story 010-31 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            silv "Now I'll just lean over the counter like this..."
            silv "...so you can go ahead and do what you need to do, [mc]."
            mc "..."
            scene black with Dissolve(1.5)
            $ renpy.pause(1.5, hard=True)
            "I don't know what came over me next..."
            "...but the next thing I knew, my legs were moving in her direction."
            $ renpy.pause(.5, hard=True)
            scene black with Dissolve(1.5)
            $ renpy.pause(1.5, hard=True)
            show story 010-32 with Dissolve(1.5)
            $ renpy.pause(1.5, hard=True)
            mc "..."
            mc "([mil!c] is practically offering her ass to me...)"
            mc "..."
            mc "(Fuck it! I'm going to do it!)"
            mc "(I wonder if it's as soft as it looks...)"
            show story 010-33 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "..."
            mc "..."
            mc "(She's not resisting...)"
            mc "(I guess it's okay to touch...)"
            show silv02_02_01 with Dissolve(1.5)
            $ renpy.pause(1.5, hard=True)
            pause
            mc "(D-Damn...)"
            mc "(Her ass feels so good...)"
            hide silv02_02_01
            show story 010-34 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "..."
            show story 010-35 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "[mc], honey..."
            silv "Are you sure that that's all you want to do?"
            show story 010-36 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            show story 010-38 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "I mean, wouldn't it be faster if you took {i}it{/i} out?"
            show story 010-37 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            mc "W-What?"
            show story 010-35 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "[mc]..."
            silv "I don't mean to rush you, but I still have to get to work on time..."
            silv "I'd prefer if you took care of your problem now before I have to go..."
            show story 010-37 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "...I understand."
            show story 010-39 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            mc "..."
            mc "(She says it's okay, so...)"
            show silv02_02_02 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            pause
            mc "(Oh GODDESS! This is amazing...!)"
            mc "(Here I am, grinding my dick on [mil!c]'s ass...)"
            mc "(I feel like I'm getting close, but what I really want to do is...)"
            mc "(...stick it inside.)"
            hide silv02_02_02
            show story 010-40 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            silv "(Hmm...)"
            silv "(I know that I said that this was okay, but...)"
            show story 010-41 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "(...maybe I'm being too pushy.)"
            silv "([mc] is such a kind boy... It shouldn't be a surprise that he doesn't want to go all the way with an old lady like me...)"
            show story 010-42 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "[mil!c]..."
            mc "I'm going to put it in..."
            show story 010-43 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            silv "Eh?"
            show story 010-37 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Is that okay?"
            mc "You said we have to be quick, right?"
            show story 010-43 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "Er..."
            silv "Y-Yes, that's fine, sweetheart..."
            silv "I did... say that I would... take care of you..."
            show story 010-44 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            with vpunch
            silv "Ahn..."
            silv "I-It's inside..."
            show story 010-45 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            silv "(Geez...)"
            silv "(...Now I'm the one starting to have second thoughts.)"
            show story 010-46 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            show silv02_02_03 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            pause
            silv "Ahn... Ahn..."
            silv "So... good..."
            mc "[mil!c], a-are you alright?"
            mc "Should I stop?"
            silv "N-No... that's... alright..."
            silv "Ahn... ahn... ahn...!"
            silv "A-Actually... I want you to..."
            silv "...keep going faster."
            hide silv02_02_03
            show story 010-47 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            show silv02_02_04 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            pause
            mc "Like this?"
            silv "Y-Yes, sweetheart..."
            silv "Ahn... ahn... ahn... ahn..."
            mc "[mil!c]..."
            mc "I'm... really close..."
            silv "Go... ahn... ahead... dear..."
            silv "Fill up... this old woman's... PUSSY!!!"
            scene whitescreen with Dissolve(1)
            $ renpy.pause(2, hard=True)
            mc "UGHHH!!!"
            $ renpy.pause(1, hard=True)
            show story 010-48 with Dissolve(1.5)
            $ renpy.pause(1.5, hard=True)
            silv "Ah... There's so much..."
            silv "I knew it..."
            silv "Young cock... really is... the {b}BEST{/b}!!!"
            $ renpy.pause(1, hard=True)
            scene black with Dissolve(1.5)
            $ renpy.pause(1.5, hard=True)
            $ renpy.end_replay()
            play music "audio/days.mp3"
            $ renpy.pause(.5, hard=True)
            jump livingroomlabel



label este01_01:

    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(2, hard=True)
    play sound "audio/door.mp3" volume 3
    show story 004-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "*Sigh*"
    mc "Another long and stressful work day..."
    show story 004-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Huh?"
    show story 004-03 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    play music "audio/estelle.mp3"
    mc "Estelle?"
    mc "What are you doing inside my room?"
    show story 004-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Eh?"
    este "Oh, hey [mc]..."
    este "I was just messing around with your computer."
    este "You know, to see what sites you've been visiting and stuff."
    show story 004-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "You can't just go around barging into people's room like this!"
    mc "Get out now!!!"
    show story 004-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Aww..."
    este "But I like hanging out in your room."
    este "You're always visiting weird websites so I can't help but get curious."
    show story 004-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "(Luckily for me, I deleted my browser history last night...)"
    mc "(Otherwise, she would have seen that little [sil] hentai I like to watch...)"
    show story 004-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hey, Estelle..."
    mc "The least you could do is respect my privacy."
    mc "They teach you not to dig through people's stuff in elementary school."
    show story 004-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Sure, sure!"
    este "I just finished up here, anyway!"
    este "And all I did on your computer was check out that folder you have..."
    este "...you know, the one with those anime girls or whatever?"
    show story 004-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Explain yourself."
    show story 004-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Well..."
    este "Since you and [mil!c] are working so hard for the house, I figured I could do the same..."
    este "That's why I'm trying to become an {b}influencer{/b} and help the household in my own way..."
    este "...I'm a cute girl and cute girls can make a ton of money or something on the MagiNet, right?"
    show story 004-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "What kind of influencer are you trying to become?"
    mc "...like an OnlyScarlet girl or something?"
    show story 004-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Nah, they rejected my application..."
    este "So I made an account on another social media platform instead."
    show story 004-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Estelle..."
    mc "You aren't thinking about doing anything weird, right?"
    mc "Like showing off your body or something for money?"
    mc "...or possibly even your {i}feet{/i}?"
    show story 004-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "O-Obviously, I have to show my body to make videos, right?"
    este "And I think one of the videos has my feet in it..."
    show story 004-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "Estelle, I absolutely forbid you from doing this."
    show story 004-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "W-What!?"
    este "Why can't I!?"
    show story 004-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "What do you mean, {i}why{/i}!?"
    mc "I don't want the whole world gawking at you like you're some sex object, that's why!"
    mc "...knock on wood."
    show story 004-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "H-Hey, you can't do that!"
    este "It's my body and I can do whatever I want with it!"
    show story 004-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Actually..."
    mc "I have your Scarlet Contract, so..."
    show story 004-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "HAH!!!"
    este "YOU THINK YOU CAN CONTROL ME JUST BECAUSE YOU HAVE MY SCARLET CONTRACT!?"
    show story 004-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Legally, you can't object to anything I..."
    show story 004-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "SCREW YOU, [mc!u]!!!"
    este "I HATE YOU, YOU STUPID JERK!!!"
    show story 004-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    play sound "audio/door.mp3" volume 3
    mc "..."
    "The guilt starts to sink in after I see the tears in her eyes..."
    "For me to invoke her Scarlet Contract like that, I knew that I had crossed the line..."
    show story 004-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Damn, I might have went too far."
    mc "She's right, I acted like a total jerk..."
    mc "But who wants to see their little [sil] plastered all over the internet for the world to see?"
    mc "...knock on wood."
    show story 004-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "*Sigh*"
    mc "I should probably go make things up with her..."
    mc "But first, she was messing around on my computer..."
    mc "Maybe I should check out what she was doing..."
    play sound "audio/ding.mp3" volume 3
    "[yel]You can now stalk Estelle's Tik Tok on your computer!"
    show story 004-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I should go find and apologize to Estelle."
    mc "She should be somewhere in the house, still."
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    play music "audio/days.mp3"
    jump mcroomlabel

label este01_02:

    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3
    show story 003-39 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/silvia.mp3"
    mc "[mil!c]?"
    mc "Have you seen Estelle around?"
    show story 003-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Oh dear..."
    silv "I saw her crying a few minutes ago..."
    silv "When I tried to ask her what was wrong, she ran out the front door."
    show story 003-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Do you know what happened to her?"
    show story 003-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah..."
    mc "I might have said some stuff to her..."
    mc "...stuff that I'm not exactly proud of."
    show story 003-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hmm..."
    silv "I'm sure you two will make up."
    silv "You two were always close, after all."
    show story 003-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "[mil!c], do you have any idea where she went?"
    mc "I want to go apologize to her immediately."
    show story 003-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Well..."
    silv "Where does she usually go when you two have a fight?"
    silv "I do seem to recall this happening on more than one occasion."
    show story 003-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Estelle and I got into a lot of heated arguments..."
    mc "And whenever that happened, she'd try to run away from home."
    mc "Every time I went searching for her, I'd find her at the [yel]park{/color}..."
    show story 003-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hehe..."
    silv "Then I'll leave her to you, [mc]."
    silv "Bring Estelle back home safely, okay?"
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    play music "audio/days.mp3"
    jump livingroomlabel

label este01_03:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 004-17 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    este "..."
    show story 004-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "*Sniff* *Sniff*"
    show story 004-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "[mc], that stupid jerk..."
    este "How dare he treat me like that..."
    show story 004-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    play sound "audio/owl.mp3" volume 3
    este "G-Geez..."
    este "Was the park always this scary at night..."
    este "W-What if some creepy guys try to kidnap me?"
    este "M-Maybe I should..."
    show story 004-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "There you are..."
    show story 004-22 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    este "EEP!!!"
    show story 004-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Oh..."
    este "It's just you..."
    show story 004-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hey, Estelle..."
    mc "I've come to escort you home."
    show story 004-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "D-Don't pop up like that next time!"
    este "...Not that I was scared or anything."
    show story 004-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Uh-huh..."
    mc "Whatever you say..."
    show story 004-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hmph!"
    este "How'd you know I was here?"
    show story 004-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I'm your [bil]."
    mc "That means I know all of your secret hiding places."
    show story 004-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "..."
    show story 004-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Look, come home, Estelle."
    mc "It's getting dark..."
    mc "[mil!c] will be worried."
    show story 004-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "So what?"
    este "You going to bring up my Scarlet Contract again if I don't come with you?"
    este "...jerk."
    show story 004-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I'm really sorry, Estelle."
    mc "I didn't mean to boss you around like that."
    mc "That was me being insensitive, and I won't ever do it again."
    show story 004-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "..."
    este "Y-You know..."
    este "When you bought out my Scarlet Contract, I was happy..."
    show story 004-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Not just because I'd get to stay home with you and [mil!c], but because I knew you wouldn't act like a total creep..."
    este "But what you said earlier... it sounded exactly like what a creep would say..."
    show story 004-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Estelle..."
    mc "What I said was in the heat of the moment."
    mc "No man wants to see their little [sil] posing on the internet, and I suppose I overreacted."
    show story 004-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "[mc]..."
    este "I-It's not like I'm doing anything weird..."
    este "Everyone else is working so much for the house, and I didn't want to be left behind..."
    show story 004-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Estelle, do you remember what I said after I bought your Scarlet Contract?"
    mc "I said that I'd take care of both you and [mil!c], and I meant it."
    mc "And if you feel as though that you've become a burden to me, well, that just means I'm not fulfilling my promise to you."
    show story 004-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "[mc]..."
    este "T-Thank you..."
    show story 004-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Now come on..."
    mc "What do you say we go home together?"
    mc "[mil!c]'s getting worried."
    show story 004-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Ah..."
    este "O-Okay..."
    show story 004-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Wait a second..."
    show story 004-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "What's wrong?"
    show story 004-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Well, since you're here..."
    este "C-Can you help me make a video for my Tik Tok?"
    este "I'm not that good at making them on my own..."
    show story 004-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "And I'd feel much safer at night with you around, too..."
    show story 004-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Sure thing, Estelle."
    mc "We can make as many as you'd like."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(2, hard=True)
    play music "audio/estelle.mp3"
    show story 004-38 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    este "..."
    show story 004-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hehe..."
    este "Look at me! Look at me!"
    este "Hey, are you looking!? Huh!? [mc], are you watching me!?"
    show story 004-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah, yeah, yeah..."
    mc "Isn't a little dangerous for you to be standing on that rock though?"
    mc "You might slip and fall..."
    show story 004-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "But it'll make for an awesome video!"
    este "Hurry up, [mc]! Record me over here!"
    show story 004-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Geez, you're getting way too into this..."
    mc "Haven't we already taken enough?"
    mc "If we aren't home soon, [mil!c] might really get mad..."
    show story 004-43 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play sound "audio/camera.mp3" volume 3
    este "Come on, [mc]..."
    este "I never have a cameraman and this is so much fun!"
    este "Snap a few pictures of this pose...."
    show story 004-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    play sound "audio/camera.mp3" volume 3
    este "...and this."
    show story 004-45 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Hey!!!"
    mc "Quit moving around so much or else you're going to..."
    show story 004-46 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    este "W-Whoa..."
    show story 004-46-1 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play sound "audio/splash.mp3" volume 3
    "*SPLASH*"
    show story 004-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "*Sigh*"
    show story 004-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "AAAHHH!!!"
    este "HELP ME, [mc!u]!!!"
    show story 004-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "The crap I have to deal with..."
    show story 004-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Welp, at least it'll make for a great video..."
    with vpunch
    mc "WORLD STAR!!! WORLD STAR!!!"
    mc "Here I come, Estelle!"
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play sound "audio/splash.mp3" volume 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 004-50 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "*Huff* *Huff*"
    este "*Huff* *Huff*"
    show story 004-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "What the hell was that, Estelle?"
    mc "Why didn't you swim to shore by yourself?"
    mc "You're supposed to be a great swimmer..."
    show story 004-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "My ankle..."
    este "I think I sprained it when I fell..."
    show story 004-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Are you going to be alright?"
    show story 004-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "I-It hurts..."
    este "But it'll probably be better in a few days."
    show story 004-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Do you think you can walk back home?"
    show story 004-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "I-I think so..."
    show story 004-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "If you aren't sure, how about I carry you instead?"
    show story 004-55 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "Eh?"
    este "N-No way!"
    este "You just want to be lewd, don't you?"
    este "Creep! Pervert! Hentai!"
    show story 004-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "It's really not like that at all..."
    mc "I'm only suggesting it because it'll be faster that way."
    mc "Since your ankle is hurt, you're going to be hobbling, right?"
    mc "It'd make more sense for me to just pick you up and carry you home."
    show story 004-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Ah..."
    este "T-That's true..."
    show story 004-56 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Well, whatever..."
    mc "The house isn't too far away."
    mc "Let's hurry up and go..."
    show story 004-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "W-Wait..."
    este "Okay, fine... You can carry me..."
    show story 004-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "But don't get the wrong idea!"
    este "I just don't want people seeing us and thinking we're a pair of perverted streakers is all!"
    show story 004-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Oh god, what if people think we're [bil] and [sil] streakers!"
    este "W-We'd have to move out of town, and..."
    show story 004-60 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Relax, Estelle."
    mc "No one in the neighborhood is ever outside at this hour..."
    show story 004-61 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "And I did say that I didn't want people ogling at you, right?"
    mc "If someone does see us, you'll be covered up since you'll be on my back."
    show story 004-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "I-I guess so..."
    show story 004-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Okay, fine then!"
    este "I'll let you carry me!"
    $ renpy.pause(.5, hard=True)
    show story 004-62 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 004-63 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 004-64 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mc "(Crap, I'm getting a reaction from touching her...)"
    mc "(Estelle's skin is so smooth... Her thighs are so soft...)"
    mc "(It's hard to think of her as anything but a woman...)"
    show story 004-65 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "Hey, this is kind of fun!"
    este "What are you standing around for?"
    show story 004-65-1 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Giddy up, horsey!"
    este "Onward to victory!"
    show story 004-66 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "R-Right..."
    mc "Here we go..."
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 004-67 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mvcula "..."
    show story 004-68 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvcula "Heh..."
    show story 004-69 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mvcula "...Huh?"
    show story 004-70 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "..."
    mvcula "..."
    mc "..."
    show story 004-71 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "H-Hey there..."
    mc "We'll be on our way..."
    mc "Have a, uh, good night..."
    show story 004-72 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvcula "..."
    show story 004-73 with Dissolve(.7)
    $ renpy.pause(.7, hard=True)
    show story 004-74 with Dissolve(.7)
    $ renpy.pause(.7, hard=True)
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(2, hard=True)
    "When we arrived home, Estelle made a beeline for her bedroom..."
    "[mil!c] asked me why we were both half-naked..."
    "After a long explanation, I returned to my bedroom..."
    $ renpy.pause(1, hard=True)
    $ renpy.end_replay()
    play music "audio/days.mp3"
    jump mcroomlabel

label este02_01:

    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3
    show story 005-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/estelle.mp3"
    este "..."
    mc "..."
    mc "Estelle, I'm happy about your enthusiasm toward reading..."
    mc "...but it's almost time for dinner."
    mc "Put that book away and get ready to eat."
    show story 005-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Huh?"
    este "Oh, yeah, sure... whatever..."
    show story 005-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hold on..."
    mc "W-What exactly are you reading?"
    show story 005-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Eh?"
    este "O-Oh, it's just, uh, this shoujo manga I picked up..."
    este "It's full of, uh, girly stuff and junk."
    este "You wouldn't be interested in it."
    show story 005-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "Shoujo, my ass!"
    mc "That's a hentai you're reading!"
    show story 005-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "N-No, it's not!"
    show story 005-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "Wait, how would {i}you{/i} know what this is!?"
    este "Did you already read this {i}manga{/i} or something!?"
    show story 005-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Argh..."
    mc "(I recognize it because I have that same hentai inside my room...)"
    mc "(Luckily, Estelle doesn't know anything about my secret hentai stash I keep under my bed...)"
    show story 005-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hah!"
    este "Nothing to say, huh?"
    este "Creep! Pervert! Hentai!"
    show story 005-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "D-Don't try and reverse the question!"
    mc "Explain to me why you're reading hentai in the middle of the living room!"
    show story 005-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Ah..."
    este "Er, it's for, um, studying..."
    este "Y-You know, about reproduction and stuff."
    show story 005-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah, okay..."
    mc "You should be learning about that from a {i}textbook{/i}, not a nudie comic book."
    show story 005-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hey..."
    este "Keep your voice down or else [mil!c] might hear us."
    show story 005-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hold on a second..."
    mc "I recognize those crinkled up pages..."
    with vpunch
    mc "That's {i}my{/i} hentai, isn't it!?"
    show story 005-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "W-Well, yeah..."
    este "It was just lying around in your drawer, and I couldn't help but get curious."
    show story 005-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I'm confiscating this..."
    show story 005-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "H-Hey!"
    este "Give that back, you jerk!!!"
    este "I need that book to learn!"
    show story 005-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Not only are you a thief, you're a lying thief."
    mc "I mean, really? You're learning about reproduction at a {i}magic academy{/i}?"
    mc "At least come up with a better excuse next time."
    show story 005-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "But I am being serious!"
    este "We really are learning about reproduction at the academy!"
    este "And now I'm going to fail my class because you took away the only {i}material{/i} I have to learn about it!"
    show story 005-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Uh-huh."
    mc "Where the heck is your textbook then?"
    mc "If you're learning about reproduction, shouldn't they have given you a book?"
    show story 005-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Oh, about that..."
    este "They ran out of stock at the school store, so I had to mail order one through a catalog."
    este "It should have arrived already at [yel]Kujikawa's Store{/color}..."
    este "You know, the place that [yel]Serena{/color} works at?"
    show story 005-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah, I know the place."
    mc "But if you know that the book's already arrived, why the heck haven't you picked it up yet?"
    mc "You literally had the entire day to do it."
    show story 005-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Oh, uh..."
    este "I-I'm just being lazy, I guess?"
    show story 005-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    play music "audio/days.mp3"
    jump livingroomlabel

label este02_02:

    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3
    show street01_serestore 01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/serena.mp3"
    mc "Hey there, Serena."
    mc "Got a moment?"
    show street01_serestore 02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hi, [mc]."
    sere "What's wrong?"
    show street01_serestore 01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I'm here because of Estelle."
    mc "She apparently has a textbook that needs to be picked up from your store."
    show street01_serestore 06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Yeah, I've actually been meaning to talk to her about that..."
    sere "She told me that she'd pick it up a month ago, but never did."
    sere "I guess she's busy or something..."
    show street01_serestore 07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "She hasn't picked it up in over a month!?"
    mc "That little..."
    show street01_serestore 08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hey, relax [mc]..."
    sere "Estelle probably has a lot on her mind right now..."
    sere "She does attend that fancy pancy [yel]Scarlet Magic Academy{/color}, after all."
    show street01_serestore 01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Serena..."
    mc "You're always quick to defend her, aren't you?"
    mc "...but you don't know how Estelle really is."
    show street01_serestore 03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hehe, is that right?"
    sere "Maybe it's something only [bil]s and [sil]s know about..."
    sere "I wouldn't know, seeing as how I'm an only child."
    show street01_serestore 01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Alright, well..."
    mc "Do you still have that textbook, Serena?"
    mc "I guess I'll act as messenger pigeon and deliver it to her."
    show street01_serestore 02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Yeah, it's in the back..."
    sere "It'll be [yel]$300{/color}."
    show street01_serestore 01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "$300!?"
    mc "She didn't even pay for it yet!?"
    show street01_serestore 06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Oh, right..."
    sere "Her card bounced shortly after the order was placed..."
    sere "That's why I wanted to go talk to her about it."
    sere "I guess she forgot to put money in her account."
    show street01_serestore 07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Goddamnit, Estelle..."
    mc "I'm starting to understand why she didn't bother to pick up the textbook herself..."
    show street01_serestore 06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "So what should I do about it?"
    sere "Should I send it back?"
    if (money >= 300):
        show street01_serestore 01 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "Nah, I guess I'll pay for it..."
        mc "Estelle desperately needs that book for class, even though she'll probably never pay me back for it."
        play sound "audio/coins.mp3" volume 3
        show love_sere at up_happy
        "[yel]You paid Serena $300."
        $ money -= 300
        hide love_sere at up_happy
        show street01_serestore 03 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        sere "Hehe..."
        sere "You two are so close."
        sere "I'm so jealous."
    elif True:
        show street01_serestore 07 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "I'm a little short on money..."
        mc "Can I give you what I have now and pay you back later?"
        show street01_serestore 06 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        sere "Er..."
        sere "If Estelle needs the book, I suppose I can pay the difference..."
        play sound "audio/depress.mp3" volume 3
        show sad_sere at up_happy
        "[yel]You paid Serena $[money]..."
        "Serena looks disappointed that she has to pay the rest..."
        $ money = 0
        hide sad_sere at up_happy
        show street01_serestore 07 with Dissolve(.5)
        $ renpy.pause(.5, hard=True)
        mc "Sorry about that, Serena..."
        mc "I owe you one."
    show street01_serestore 02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hey, [mc]..."
    sere "Don't forget to always have money in your pocket."
    sere "You never know when you might need it..."
    show street01_serestore 01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(She's right, I can't forget about the [yel]Waifu Tax{/color}.)"
    mc "(I should make sure I have money on me at all times.)"
    mc "..."
    mc "Why the heck are these books so damn expensive anyway?"
    mc "It doesn't make any sense."
    show street01_serestore 06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Well, you know how those prestigious schools operate..."
    sere "They come out with new versions of the same book every year (with very minor changes) and force students to buy them."
    sere "That way, they'll generate more revenue since the old and used books become obsolete."
    show street01_serestore 07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...Sounds about right."
    mc "Well, I'm going to head off and give this book to Estelle."
    mc "See you later, Serena."
    show street01_serestore 03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "See ya!"
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    play music "audio/days.mp3"
    jump streetlabel_01

label este02_03:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3
    show story 005-11 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/estelle.mp3"
    mc "..."
    with vpunch
    mc "Estelle! I got your damn textbook right here!"
    show story 005-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Eh?"
    este "Oh yeah, sure..."
    este "Put it on the shelf over there for me, alright?"
    show story 005-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 005-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    play sound "audio/slam.mp3" volume 3
    este "H-Hey!!!"
    show story 005-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "What the heck was that for!?"
    este "You almost hit me with that thing!"
    show story 005-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "How about you show a bit of gratitude for once!?"
    mc "Someone else had to pay for your stupid book because you {i}forgot{/i} to load money into your account!"
    mc "But something tells me you already knew that!"
    show story 005-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Ah..."
    este "R-Right, thank you, [mc]..."
    show story 005-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "...and don't yell at me."
    este "Creep... Pervert... Hentai..."
    show story 005-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "[mil!c]'s paying for your tuition, you know?"
    mc "Would you like to explain to her how you've been going to class for an entire month without your textbook?"
    show story 005-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "P-Please don't tell her..."
    este "I might have... spent all of her money on candy..."
    show story 005-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Figured as much."
    mc "You really need to be more responsible, Estelle."
    mc "You're not a little kid anymore."
    show story 005-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "I-I know that!"
    este "I'm still trying my best to become a mage, okay!?"
    show story 005-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I won't tell her."
    mc "But you need to get your shit together."
    show story 005-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "T-Thanks..."
    este "But at least you know that I wasn't lying!"
    este "The nudie comic I {i}borrowed{/i} from you really was for school..."
    show story 005-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah, yeah, yeah..."
    mc "I think I'm going to head out for a snack."
    mc "You have a whole month's worth of studying to catch up on."
    show story 005-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "H-Hold on..."
    este "Aren't you going to stay here with me?"
    show story 005-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Huh?"
    mc "But you already have your textbook..."
    show story 005-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "I-I know..."
    este "It's just that you've been helping me study lately, and I..."
    show story 005-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Y-You know what? Forget it."
    este "It's not like you care whether I fail or not..."
    este "...jerk."
    show story 005-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "*Sigh*"
    mc "Fine then, I'll help."
    show story 005-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hehe, thanks..."
    show story 005-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Er, not that I wanted to study with you or anything..."
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "Several minutes later..."
    "Estelle appears enthusiastic about studying..."
    "As for me, I can't say that I was half as thrilled..."
    scene black with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 005-20 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    este "..."
    show story 005-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "None of this makes any sense..."
    show story 005-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "[mc], why would any girl want that disgusting thing inside of her?"
    show story 005-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Huh?"
    mc "Did you say something?"
    show story 005-24 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    este "Argh, you aren't even paying attention!"
    este "I'm definitely going to fail my class at this rate!"
    este "And it's going to be all your fault!"
    show story 005-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Are you kidding me?"
    mc "What's not to understand?"
    mc "A man and a woman lay with each other and babies are made."
    mc "If you think of it as anything more than that, you're bound to get confused."
    show story 005-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Eh?"
    este "[mil!c] told me that babies come from storks after you get married..."
    show story 005-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You're kidding, right?"
    mc "Then again, you've only ever been to an all-girl school..."
    mc "Damn segregation of the sexes..."
    show story 005-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Oh, wow..."
    este "[mc], you sound like you're an expert on this..."
    este "I guess that makes sense, given how you like staring at nudie anime girls all day."
    show story 005-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "It's embarrassing enough without having you bring it up..."
    mc "And for someone who constantly tells me that I'm a {b}creep{/b}, a {b}pervert{/b}, and a {b}hentai{/b}, you sure are clueless about sex..."
    show story 005-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hey, [mc]..."
    este "Do you also have one of these {i}penis{/i} things?"
    show story 005-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Of course..."
    mc "Every guy has one."
    mc "It's what makes a man a man."
    show story 005-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "Gross!"
    este "And something like that is supposed to enter me down there, someday!?"
    show story 005-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Pfft..."
    mc "At this rate, that won't be happening for a very long time..."
    show story 005-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hmm..."
    este "[mc], can you show me yours?"
    este "I need to see a real penis in person."
    show story 005-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "WHAT!?"
    show story 005-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Y-Yeah..."
    este "Don't make it awkward. I just want to see it, is all."
    este "Y-You know, for research purposes..."
    show story 005-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "There's no way I'm showing my little [sil] my dick!"
    show story 005-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hey!"
    este "Don't get full of yourself! I just want to compare it to the one in the book!"
    este "I-It's not like I want to see it or anything!"
    show story 005-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I don't know..."
    mc "Something about this doesn't seem right..."
    show story 005-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "If you prefer..."
    este "Maybe I should go outside and ask some bum to show me theirs instead!"
    este "I'm sure you'd enjoy that, wouldn't you!?"
    este "Creep! Pervert! Hentai!"
    show story 005-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Alright, alright, I get it."
    mc "You just want to see, right?"
    mc "You better not tell [mil!c] about this..."
    show story 005-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hehe..."
    este "Whip it out and let's see the goods..."
    show story 005-30 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    show story 005-31 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 005-32 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "There..."
    mc "Are you satisfied?"
    show story 005-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hmm..."
    este "It's different compared to the book..."
    este "Yours is all floppy and sad looking..."
    show story 005-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "YOU SAYING MY DICK IS SMALL!?"
    show story 005-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Well, I thought it'd be {b}bigger{/b} and {b}longer{/b}..."
    este "You know, like in that nudie book of yours..."
    show story 005-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "You do realize that it's only small like this because I'm not {i}hard{/i}?"
    mc "Trust me, you wouldn't be talking like that if you saw it in its entirety."
    show story 005-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "Then hurry up and get it {i}hard{/i} then!"
    este "I'm waiting!"
    show story 005-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I can't do that..."
    mc "Not without some kind of {i}stimulation{/i}..."
    mc "I need to be excited before it can {i}grow{/i}."
    show story 005-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Eh?"
    este "W-What does that mean?"
    este "Are you supposed to do jumping jacks or something?"
    show story 005-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "No, no, no..."
    mc "You see, a guy gets excited when he sees a..."
    show story 005-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm..."
    mc "Should I even be talking to you about this?"
    mc "I'm starting to think this was a bad idea..."
    show story 005-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hey, you can't back out of this now!"
    este "Tell me or else I'm going to tell [mil!c] about your nudie anime comic book!"
    show story 005-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "*Sigh*"
    mc "Alright, alright, I get it."
    mc "Look, a grown woman's body does something to a man..."
    mc "It's how we get {i}excited{/i}."
    mc "Do you understand?"
    show story 005-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Oh..."
    este "I think I've heard of this before..."
    este "A girl is supposed to touch it or something, right?"
    show story 005-41 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    este "...like this?"
    show story 005-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "*GULP*"
    mc "W-What do you think you're doing!?"
    mc "More importantly, who told you about this!?"
    show story 005-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "F-From my girlfriends..."
    este "They said that guys like it when you touch them down there."
    este "Is that true?"
    show story 005-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "W-Well, yeah..."
    mc "But you're my [sil]..."
    show story 005-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Y-You say that, but..."
    este "Why does it feel like it's getting harder in my hand?"
    show story 005-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Estelle..."
    mc "Can you try stroking it a little."
    mc "It'll make me feel good..."
    show story 005-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Stroking?"
    show story 005-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Y-Yeah..."
    mc "Like moving your hand up and down."
    show story 005-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Ah..."
    este "Okay..."
    show story 005-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    show este02_03_01 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    pause
    "Estelle's fingers are so slender and soft..."
    "Immediately, I can sense blood rushing down my lower half..."
    "Even though she was sloppy and inexperienced, Estelle's handjob felt a million times better compared to my own..."
    hide este02_03_01
    show story 005-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Ah..."
    este "I-It's actually working..."
    este "Your penis is all big and hard now..."
    show story 005-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "E-Estelle..."
    mc "Could you maybe..."
    mc "...you know, let me feel your..."
    show story 005-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "F-Feel my what...?"
    show story 005-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...your tits."
    mc "I need to touch them."
    show story 005-49 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    este "Eh!?"
    este "No way! That's disgusting!"
    este "Creep! Pervert! Hentai!"
    show story 005-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Come on, Estelle..."
    mc "Can you really say that when your hand was just on my dick?"
    mc "And I already showed you mines..."
    mc "...isn't it only fair that you show me yours?"
    show story 005-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "..."
    show story 005-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "O-Okay, I understand..."
    este "But you better not tell anyone about this!"
    show story 005-53 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 005-54 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 005-55 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    este "T-There..."
    este "Are you happy now?"
    show story 005-56 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Um..."
    mc "Estelle, I can't see them if you cover them up..."
    show story 005-55 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Oh... right..."
    show story 005-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "T-There, you go..."
    show story 005-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "W-Wow..."
    mc "You've really grown up, Estelle..."
    show story 005-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "[mc]..."
    este "They're not too small, are they?"
    este "I know that most guys prefer bigger ones..."
    show story 005-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Not at all..."
    mc "They're beautiful... just the perfect size for me to squeeze them..."
    mc "Maybe I can't call you my sweet little [sil] anymore..."
    show story 005-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Eh!?"
    este "B-But I like it when you call me that..."
    show story 005-60 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I'm really close, Estelle..."
    mc "Do you think you can finish me off?"
    show story 005-61 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "H-Huh?"
    este "Oh... s-sure..."
    este "That's when that white stuff is supposed to come out, right?"
    show story 005-62 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    play sound "audio/knock.mp3" volume 3
    "*KNOCK* *KNOCK*"
    silv "Estelle? [mc]?"
    silv "Are you two in there?"
    silv "It's almost time for dinner."
    mc "..."
    este "..."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(2, hard=True)
    "We scrambled to put our clothes back on..."
    "When I opened my mouth to comment on what we did, Estelle ushered me out of her bedroom."
    $ renpy.pause(1, hard=True)
    $ renpy.end_replay()
    play music "audio/days.mp3"
    jump mcroomlabel

label este03_01:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 025-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    show story 025-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Heh... It's been a long wait, but it's finally here..."
    show story 025-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "The new release for my favorite anime is coming out on physical form! I've had the collector's edition pre-ordered for months!"
    mc "And since everyone's busy today, I'll have the whole place to myself!"
    show story 025-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 025-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "The only problem is... picking it up..."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump livingroomlabel

label este03_02:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 025-06 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/casual.mp3"
    tori "..."
    show story 025-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    tori "Mornin', sir..."
    tori "Welcome to Weebs 'R' Us, what can I do for you today?"
    show story 025-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Er... Y-Yeah..."
    mc "I'm here for a pre-order I placed several months ago..."
    show story 025-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    tori "Right, right..."
    show story 025-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    tori "Could I please have your order number, along with the name you used when the pre-order was made?"
    show story 025-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "2156969. The name I used was, uh, '{i}Dudebro{/i}'."
    show story 025-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    tori "Give me one moment..."
    show story 025-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    play sound "audio/keyboard.mp3" volume 3
    tori "..."
    tori "... ..."
    tori "... ... ..."
    stop sound fadeout 3.0
    show story 025-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    tori "Ah, I see it..."
    show story 025-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    tori "Your order is for a limited edition box set of [yel]'My Little [sil!c]'s Feet Can't Be This Cute'{/color} by JYP Games, correct? Can you confirm this for me?"
    show story 025-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "...Y-Yes."
    show story 025-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    tori "Hehehe... I'm sorry, but could you speak up?"
    tori "I couldn't hear your confirmation."
    show story 025-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Y-Yeah, that's what I ordered."
    show story 025-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    tori "Hehehe... Roger that... I'll be right back with your order..."
    show story 025-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    tori "...{i}Bro{/i}!"
    show story 025-15 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    with vpunch
    mc "Welp, that was embarrassing..."
    $ renpy.pause(.5, hard=True)
    show story 025-16 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "But oh well, that's why I came here prepared with my disguise... That way, even if someone sees me, they won't recognize me."
    mc "It's a good thing that weebs can walk into a store like this and have people think it's cosplay..."
    show story 025-17 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    tori "I'm baaack~!"
    tori "And I got your order right here~!"
    show story 025-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh, that was fast..."
    show story 025-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    tori "No, not you..."
    show story 025-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    tori "I have your package ready, Miss Mao Fluffy Kitty Princess God!"
    show story 025-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...Miss Mao Fluffy Kitty Princess God?"
    show story 025-20 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    laur "Oh boy! That's me!"
    show story 025-21 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    laur "Hehe... I can't believe it's finally here!"
    laur "The latest entry of [yel]Three Houses{/color}! I can't wait to see what happens next!"
    show story 025-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    tori "Thank you for shopping at Weebs 'R' Us..."
    tori "As for you, Mr. DudeBro, I'll be right back with your order..."
    mc "..."
    mc "Laureate?"
    show story 025-23 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    laur "Eh!?"
    show story 025-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "L-Laureate? Who is this Laureate that you speak of?"
    show story 025-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "My name is Miss Mao Fluffy Kitty Princess God! I'm just a regular normie bystander, that's all!"
    show story 025-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Relax, Princess... It's me..."
    show story 025-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    laur "[mc]!?"
    laur "Er, w-what are you doing here? Why are you wearing that ridiculous disguise?"
    show story 025-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Isn't Three Houses an eroge? Why are you buying a hentai game?"
    show story 025-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    laur "H-Hey! Just what are you insinuating!?"
    show story 025-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "I'm a pure-hearted princess! Beloved and revered by many!"
    laur "The audacity of your shameless accusation deserves capital punishment! Not even the Goddess could save you from then on!"
    show story 025-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 025-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "L-Look, this game is for Ferry, okay...?"
    show story 025-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Yeah, that's right! She asked me to pick it up for her... That's the only reason why I'm here!"
    show story 025-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Suuure..."
    mc "Have fun with Three Houses... I heard it's a great game with loads of action packed lewdness..."
    show story 025-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    laur "[mc], you're the worst!"
    laur "And like you're one to talk! What business do you have here, anyway?"
    show story 025-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "I-I'm here for the same reason as you! To pick up a non-lewd package for someone who isn't me!"
    mc "You think I want to be here? Of course not! I'm not a creepy otaku!"
    mc "Weebs are weirdos! I bet they've never kissed a girl in their lives!"
    show story 025-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    tori "Excuse me, Mister DudeBro?"
    show story 025-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    tori "Your order for one limited edition box set of [yel]'My Little [sil!c]'s Feet Can't Be This Cute'{/color} is ready for pick-up!"
    show story 025-33 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    laur "..."
    mc "..."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    $ renpy.end_replay()
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump streetlabel_01

label este03_03:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 025-34 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    show story 025-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Heh, now that the embarrassing part is out of the way..."
    show story 025-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Let us divulge in depravity! Time to take off my pants and whip out my..."
    show story 025-37 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "Hey, can you pipe down?"
    este "I'm reading something here..."
    $ renpy.pause(1, hard=True)
    show story 025-38 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/estelle.mp3"
    mc "..."
    with vpunch
    mc "E-Estelle!? What the hell are you doing inside my room!?"
    show story 025-39 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    with vpunch
    mc "H-Hold on! What are you reading there!?"
    show story 025-40 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "Eh?"
    show story 025-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Oh, just some books I found under your bed..."
    show story 025-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Y-You little..."
    mc "T-That's my... my... my..."
    show story 025-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "[mc], you're really disgusting, you know that!?"
    show story 025-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "I want to know why you have so much little [sil] hentai hidden inside your room!"
    show story 025-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 025-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "'Sexy Little [sil!c]s from Outer Space'..."
    este "'Slutty [sil!c]s Who Do whatever You Ask'..."
    este "'Pregnant and Obedient Little [sil!c]s With Juicy Milkers'..."
    show story 025-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "What the heck are with these disturbing titles?"
    show story 025-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "I-It's not mine! I'm just holding them for a friend!"
    show story 025-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hold on..."
    este "What do you got in your hands right now!?"
    show story 025-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...N-Nothing."
    show story 025-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "Yoink!"
    show story 025-49 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "My Little [sil!c]'s Feet Can't Be..."
    show story 025-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    este "..."
    este "[mc]..."
    $ renpy.pause(1, hard=True)
    show story 025-51 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show este03_03_01
    este "You big dummy!"
    este "Why would you waste perfectly good money on this junk when you have a {i}real-life{/i} little [sil] right here!?"
    mc "You got it all wrong, Estelle!"
    mc "I swear I only play and watch these things for the plotline!"
    mc "It's just a fantasy, okay!? People wouldn't actually want to do lewd things with their [sil]s in real-life!"
    mc "E-Even if they were really hot..."
    mc "...and had cute feet."
    hide este03_03_01
    show story 025-52 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "Geez, [mc]..."
    este "Aren't you a failure as a big [bil] for thinking about me like that?"
    show story 025-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "I get that I'm super duper cute and the only girl willing to talk to you, but still..."
    show story 025-54 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    with vpunch
    mc "Don't be full of yourself!"
    mc "Just because I own this stuff, doesn't mean I look at you in the same way I do with [sil]s from my hentai!"
    show story 025-55 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "The evidence suggests otherwise!"
    show story 025-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "I won't stand by and let you insult 2D [sil]s!"
    mc "They're a million times better than real-life ones! Comparing yourself to a pure-hearted 2D [sil] is the same as comparing night and day!"
    show story 025-56 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "You're out of your mind!"
    show story 025-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "I'm cuter and better than any stupid anime [sil] you know!"
    show story 025-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Oh, please!"
    mc "The perfect little [sil] doesn't exist! That's why 2D is far superior to 3D!"
    mc "In 50 more years, every man will have their own personal 2D [sil] onahole! And you know what!? I'm more than looking forward to seeing when that happens!"
    show story 025-55 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "You're crazy!"
    este "A 2D [sil] is just a drawing! How can they compare to someone who has flesh and blood like me!?"
    show story 025-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You're disrespecting 2D again! I won't stand for it!"
    mc "Take a look and compare yourself to a {i}real{/i} 2D [sil]!"
    mc "They're sweet, kind, and obedient! They actually listen to their big [bil]s!"
    show story 025-55 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "A-And? I tick all of those boxes..."
    show story 025-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Hahahaha! Now who's the crazy one?"
    mc "You never listen and you're always going through my stuff!"
    mc "You're far from perfect! I've played hentai games with better personalities than you!"
    show story 025-59 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "Grrr..."
    show story 025-60 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "I-I do listen! I'm the best little [sil] you know!"
    este "There's no way I'll ever lose to a [sil] from any hentai game you've ever played!"
    with vpunch
    este "Stupid! Bakka! Idiot! Dummy! Moron! Poopy butt-head!"
    show story 025-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Is that right!?"
    mc "If you're so sure of yourself, then you wouldn't mind doing what I ask right now!"
    show story 025-60 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "Name it!"
    este "I'll do anything and prove to you that 3D is better than 2D!"
    show story 025-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Then try lifting up your skirt right now!"
    show story 025-61 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Eh!? M-My skirt!?"
    show story 025-62 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "Creep! Pervert! Hentai!"
    show story 025-63 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "As expected..."
    mc "You only prove my point... anime [sil]s are so much cuter..."
    show story 025-64 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "..."
    show story 025-65 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "F-Fine, I'll do it..."
    show story 025-66 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "Y-You will!?"
    show story 025-65 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Yes..."
    show story 025-62 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "But only to prove to you how much better real-life [sil]s are!"
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 025-68 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    $ renpy.movie_cutscene("images/videos/este03_03_02.webm", delay=None, loops=0, stop_music=False)
    show story 025-67
    este "..."
    show story 025-69 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "There! Are you satisfied!?"
    show story 025-70 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "R-Real-life [sil]s are definitely cuter than anime [sil]s, right!?"
    show story 025-67 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(I-I can't believe she actually did it...)"
    mc "(S-She's acting like the [sil] from my games right now...)"
    mc "(...and to be totally honest, my dick is reacting to her being so submissive.)"
    show story 025-71 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "H-Hey, quit staring..."
    show story 025-70 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Go ahead and tell me I'm the best [sil] in the world now..."
    show story 025-67 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "T-That's a start..."
    mc "But a {i}real{/i} anime [sil] would also..."
    with vpunch
    mc "...s-she'd also pull down her panties!"
    show story 025-71 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Eh!?"
    este "You're kidding! Isn't this enough!?"
    show story 025-67 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "A-Absolutely not!"
    mc "A 2D [sil] wouldn't even hesitate! She'd take off her panties for me in an instant!"
    mc "Yes! In fact, it's part of her sacred duty to do so! Little [sil]s {i}exist{/i} to show off their bodies to their older [bil]s!"
    show story 025-69 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "B-But I've never shown my {i}special spot{/i} to anyone before..."
    show story 025-67 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "How pitiful..."
    mc "Estelle, you have one major flaw about your character design..."
    show story 025-71 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Eh?"
    show story 025-67 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You lack resolve. This is why you'll never beat 2D."
    show story 025-73 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "..."
    show story 025-72 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "O-Okay, fine... I understand..."
    este "Here goes nothing..."
    $ renpy.pause(.5, hard=True)
    show story 025-74 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "*GULP*"
    mc "(T-The carpet matches the drapes...!)"
    $ renpy.pause(.5, hard=True)
    show story 025-75 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "Is that... enough for you?"
    show story 025-76 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 025-77 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    este "Eh!?"
    este "W-Where do you think you're touching!?"
    show este03_03_03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    pause
    mc "Wow..."
    mc "It's so warm and squishy..."
    este "Ah..."
    este "[mc], you can't... it's dirty..."
    este "I-I haven't taken a bath yet..."
    mc "That just makes it even better..."
    este "N-No..."
    mc "Estelle... You're wet..."
    mc "Could you have been... getting off from reading my hentai?"
    este "Eh?"
    este "O-Of course not! That's disgusting! How could you even think that!?"
    hide este03_03_03
    show story 025-78 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "[mc]... I feel weird..."
    este "It's tingly and warm down there..."
    show story 025-76 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mc "(Seeing Estelle like this is so hot...)"
    mc "(She's become the ideal [sil]... She'll do anything I ask...)"
    mc "(Would I be an evil bastard if I demanded more from her?)"
    show story 025-75 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "H-Hey..."
    este "Isn't this enough? You're just standing there..."
    show story 025-76 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "(...Fuck it!)"
    mc "(I came this far... I might as well go all the way!)"
    mc "..."
    with vpunch
    mc "E-ESTELLE!!! TAKE OFF THE REST OF YOUR CLOTHES!!!"
    mc "YOUR BIG [bil!u] DEMANDS IT!!!"
    show story 025-79 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    este "Eh?"
    este "A-All of my clothes? Why? I-Isn't this enough?"
    show story 025-80 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Not a chance!"
    mc "I'm going to {i}fuck{/i} you, right here and now!"
    mc "Wait, scratch that..."
    with vpunch
    mc "I'm not going to just fuck you... I'm going to fuck you right in the {b}ass{/b}!"
    mc "That's right!!! I'm going to take your anal virginity!!!"
    show story 025-81 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "[mc], you..."
    show story 025-82 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Maybe I'm not the perfect little [sil]..."
    show story 025-83 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    este "But you're {i}definitely{/i} the worst big [bil] ever!"
    show story 025-84 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play sound "audio/explosion.mp3" volume 3
    with vpunch
    este "HIII-YAAAHHH!!!"
    $ renpy.pause(.5, hard=True)
    show story 025-85 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "(S-Shit...)"
    mc "(I... guess... I went too... far...)"
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    "I was unconscious for the rest of the day..."
    "By the time I woke up, it was already dark outside..."
    $ renpy.end_replay()
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump mcroomlabel



label azul01_01:

    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3
    show story 006-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "*Yawn*"
    show story 006-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yet another lazy morning..."
    show story 006-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh right, I promised Azula that'd I play with her today."
    mc "She can't ever leave the park, so she must be bored..."
    show story 006-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Now that I think about it, I do feel a little bad."
    mc "I mean, she's constantly providing me with, uh, {i}relief{/i} and she never asks for anything in return..."
    mc "Even if she's always saying that I'm helping her with my {b}essence{/b}, I can't help but think I'm being selfish..."
    show story 006-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm..."
    mc "Maybe I should do something for her..."
    show story 006-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I know! I'll get her something as a way of showing my appreciation!"
    show story 006-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Er..."
    mc "Then again, what do Vallas even like?"
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "I made my way over to Kujikawa's Store..."
    "Luckily for me, Serena was already open for business."
    $ renpy.pause(.5, hard=True)
    show street01_serestore 04 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/serena.mp3"
    sere "..."
    show street01_serestore 09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "You're here early, [mc]."
    sere "What's the occasion?"
    show street01_serestore 04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "No reason, really."
    mc "I just promised a friend I'd see her today."
    show street01_serestore 10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "{b}'Her?'{/b}"
    sere "...So you're seeing a girl then, huh?"
    show street01_serestore 11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah..."
    with vpunch
    mc "Wait, I mean I promised to {i}play{/i} with her this morning!"
    show street01_serestore 10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "{b}'Play?'{/b}"
    sere "...So you're the type to do the {i}deed{/i} during the morning, huh?"
    sere "[mc], you dirty dog..."
    show street01_serestore 11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "N-No, I mean..."
    mc "She's just a friend of mine..."
    mc "I'm here because I want to get something to show her my gratitude."
    show street01_serestore 10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "{b}'Get her something?'{/b}"
    sere "...So you haven't gotten around to confessing yet, but you will with your {i}gift{/i}?"
    show street01_serestore 11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "N-No!"
    mc "Look, I just want to get her a gift as a way of saying thanks!"
    mc "You know, because she's been {i}helping{/i} me out lately!"
    show street01_serestore 09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Oh, I totally understand that!"
    sere "...So what exactly have you two been doing together?"
    show street01_serestore 04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(2, hard=True)
    stop music fadeout 3
    "After a long and awkward silence, I picked up my goods and left the store."
    if (money >= 100):
        play sound "audio/coins.mp3" volume 3
        show love_sere at up_happy
        "[yel]You paid Serena $100."
        $ money -= 100
        hide love_sere at up_happy
    elif True:
        play sound "audio/coins.mp3" volume 3
        show love_sere at up_happy
        "[yel]You paid Serena $[money]."
        $ money = 0
        hide love_sere at up_happy
    stop music fadeout 3.0
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    play music "audio/days.mp3"
    jump streetlabel_01

label azul01_02:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3
    show story 006-07 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/azula.mp3"
    azul "..."
    show story 006-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Are you ready, [mc]?"
    show story 006-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Y-Yeah..."
    mc "Let's get started."
    show story 006-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Okay..."
    azul "Then I'll use my hands to milk the essence out of you..."
    show story 006-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    show azul01_02_01 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    pause
    azul "..."
    azul "How is that, [mc]?"
    azul "Does it feel good?"
    mc "Y-Yeah..."
    mc "I'm getting close..."
    hide azul01_02_01
    show story 006-10 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "AAAARRRRRGGGGG!!!"
    show story 006-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Ah..."
    azul "Well done, my male companion!"
    azul "I can feel my powers growing already!"
    show story 006-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "It's all over your face though..."
    mc "...and there's a lot."
    show story 006-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Yes, it's a good amount..."
    azul "A high quantity of essence speaks volumes for a male Valla's virility..."
    show story 006-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "And given that you're still young, the quality is pristine, as well."
    azul "I'm very certain that you'll keep me satisfied for a very long time."
    show story 006-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Right..."
    mc "Well, we better wrap things up here..."
    mc "Or else someone might stumble on us and see what we're doing..."
    show story 006-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Hold on, [mc]. Allow me to clean you up..."
    azul "It's shame to let good essence go to waste..."
    show story 006-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "W-Whoa!!!"
    show azul01_02_02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    pause
    mc "(Her mouth feels... {i}incredible{/i}...)"
    mc "(Azula isn't just sucking my dick...)"
    mc "(S-She's forcibly making me want to cum again...)"
    azul "*SLURP*"
    azul "Thash *SLURP* gmoodsh *SLURP* emmsence..."
    hide azul01_02_02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "S-Shit..."
    mc "Here's... another... round..."
    scene whitescreen with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 006-15 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    $ renpy.pause(1, hard=True)
    show story 006-16 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    azul "..."
    mc "..."
    show story 006-17 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    azul "Delicious..."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 006-18 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    mc "Azula, you keep saying that you're getting stronger every time we do this, but..."
    mc "What do you plan on doing once your power returns?"
    show story 006-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Well..."
    azul "My current objective is to reclaim my full physical form so that I can leave this park without disappearing."
    azul "After that, I plan on taking back the land as the Goddess of Scarlet again."
    show story 006-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I see..."
    mc "Hey, have you spoken to anyone else here besides me?"
    mc "You know, since your awakening..."
    show story 006-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "A few humans pass by every so often, but..."
    azul "...I don't show myself unless it's for you, [mc]."
    azul "The more time I spend in my physical form, the longer it'll take for me to reach a full recovery."
    show story 006-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I feel awful that you're always by yourself."
    show story 006-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Hehe..."
    azul "Don't feel that way, [mc]. You've been a great help to me."
    azul "I'm in your debt."
    show story 006-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh right..."
    show story 006-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Here, I have something for you..."
    show story 006-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Eh?"
    azul "What is this? Human sustenance?"
    show story 006-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "It's a cake..."
    mc "I figure it's the least I can do since you can't leave the park yourself..."
    mc "Wait, what have you been eating, anyway?"
    show story 006-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "*Sniff* *Sniff*"
    show story 006-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "It smells... {i}tasty{/i}..."
    show story 006-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Can I really have this, [mc]?"
    show story 006-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah..."
    mc "You didn't have cake during your time, Azula?"
    show story 006-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Hmm..."
    azul "Not of this quality..."
    show story 006-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Hold on, human food isn't poisonous or anything to Vallas, right?"
    mc "The last thing I'd want is for you to get sick..."
    show story 006-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Well..."
    azul "If you're able to consume this, I shouldn't have any problems doing the same."
    azul "You do have Valla blood, after all."
    show story 006-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Alright, then..."
    mc "Eat up, Azula, and then we can play together like I promised."
    show story 006-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "*Nom* *Nom*"
    show story 006-30 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    azul "Hehe..."
    azul "...So good!"
    show story 006-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Thank you, [mc]!"
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(2, hard=True)
    stop music fadeout 3.0
    "I spent the next few hours hanging out with Azula..."
    "The more I spoke of the modern world, the more intrigued she seemed to become..."
    "I knew that she couldn't wait to leave the park and explore Scarlet on her own..."
    $ renpy.end_replay()
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump parklabel_04

label azul01_03:

    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3
    $ renpy.pause(1, hard=True)
    show story 007-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/azula.mp3"
    azul "..."
    show story 007-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Excellent work as usual, my male companion."
    azul "I can already feel your power surging through me!"
    show story 007-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "That's good, Azula..."
    mc "I'm glad that I can be of some use."
    show story 007-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "..."
    mc "..."
    show story 007-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...Is something wrong?"
    show story 007-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "I was just wondering..."
    azul "Did you happen to bring any more human edibles for me?"
    azul "You know, like the sugary pastry from before?"
    show story 007-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Er..."
    mc "Sorry, Azula..."
    mc "I didn't bring anything with me today..."
    show story 007-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Oh..."
    azul "I suppose it makes sense..."
    azul "You get to leave the park whenever you want, so of course you aren't thinking of me..."
    azul "...I, on the other hand, am unable to do anything except anxiously await your return."
    show story 007-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "I'm sorry, Azula!"
    mc "I'll definitely bring you something next time!"
    show story 007-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Eh?"
    azul "Will you, truly?"
    show story 007-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah..."
    mc "My [mil] is really great at baking sweets."
    mc "She does it for fun, and we usually have a lot more than we can eat."
    show story 007-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Amazing..."
    azul "You're telling me that there's a being capable of creating such tasty morsels without devouring them all by herself?"
    azul "Humans are certainly interesting creatures, indeed!"
    show story 007-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Right..."
    mc "I promise I'll bring some for my next visit."
    mc "Be good and wait patiently until then, okay Azula?"
    show story 007-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Got it, [mc]!"
    azul "I'll be on my best behavior until then!"
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(2, hard=True)
    stop music fadeout 3.0
    $ renpy.pause(1, hard=True)
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    play music "audio/days.mp3"
    jump parklabel_04

label azul01_04:

    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3
    show story 007-09 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    show story 007-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Night, Estelle."
    show story 007-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Good night, [mc]..."
    show story 007-14 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play sound "audio/door.mp3" volume 3
    show story 007-15 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "(I should head to bed myself...)"
    show story 007-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    play sound "audio/fall.mp3" volume 3
    with vpunch
    "*THUMP*"
    mc "Huh?"
    mc "What's that sound? It came from the living room..."
    mc "[mil!c] and Estelle are both in their rooms..."
    show story 007-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I should check it out..."
    mc "...better safe than sorry."
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 007-16 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "(...)"
    mc "(There's definitely someone here...)"
    mc "(I can see a shadow over by the kitchen...)"
    show story 007-17 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "(It's not much but this is the only {i}weapon{/i} I could find...)"
    mc "(Alright, I'll open the lights and...)"
    mc "(3... 2... 1...)"
    mc "ALEXA... LIGHTS!!!"
    show story 007-18 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "YOU MOTHER FUCKER, I'M GOING TO MURDER..."
    show story 007-19 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 007-20 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play music "audio/azula.mp3"
    azul "Eh?"
    azul "Oh, hey there, [mc]!"
    show story 007-21 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "A-Azula!?"
    mc "What the heck are you doing inside my house!?"
    mc "I was this close to cracking your skull open..."
    show story 007-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Eh!?"
    azul "[mc], what are you doing pointing that dangerous looking sword at me..."
    show story 007-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Huh? This?"
    mc "...It's just a plastic bat."
    mc "[mil!c] doesn't want {i}real{/i} weapons inside the house..."
    show story 007-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Hehe..."
    azul "You know, having you point a weapon at me is quite nostalgic!"
    azul "It really takes me back to when I was still alive..."
    show story 007-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Azula..."
    mc "What are you doing here?"
    mc "Wait, I thought you said that you can't leave the lake without disappearing..."
    show story 007-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "About that..."
    azul "I just couldn't wait any longer, you see..."
    azul "When you told me that you had tasty treats at your place, I knew I had to come..."
    azul "...even at the cost of disappearing forever, I absolutely had to take my chance for more cake."
    show story 007-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Hehe, aren't I a brave heroine?"
    show story 007-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Azula..."
    mc "You risked your own life... just for cake..."
    mc "Do you have any idea how stupid that sounds..."
    show story 007-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "It's all thanks to you, [mc]."
    azul "My body has recovered to a point where I can now freely explore Scarlet on my own two feet."
    azul "Soon, I'll have enough power to take over Scarlet again."
    azul "And when that happens, the reckoning will begin..."
    show story 007-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I see..."
    mc "Well, that's good news, I suppose."
    mc "But you have to get out of here quick..."
    mc "I don't know how [mil!c] and Estelle will react if they see you..."
    show story 007-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Aw, come on..."
    azul "Spending an eternity as a water spirit will make you go hungry..."
    azul "All I had to eat were leaves and berries at the park..."
    azul "And since all of my friends and family are dead (probably), I don't have anywhere else to go but here..."
    show story 007-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 007-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "You don't mind, do you?"
    azul "As a male Valla, isn't it your instinct to care for and protect your harem?"
    show story 007-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Harem?"
    mc "Azula, what are you talking about...?"
    show story 007-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Honestly, this is all your fault to begin with..."
    azul "You tempted me with the forbidden fruit..."
    azul "...It's only natural for a curious Goddess like myself to desire more."
    show story 007-28 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mv2 "Eh?"
    mv2 "[mc], who are you speaking to at this hour?"
    show story 007-29 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 007-30 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    silv "Oh dear..."
    silv "[mc], honey, if you were planning on bringing a girl over in the middle of the night, you could have at least told me."
    show story 007-31 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    este "Hey, you blue-haired hussy!"
    este "You better stay away from [mc] if you know what's good for you!"
    show story 007-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Don't worry, [mc]... I'll protect you."
    show story 007-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "*Sigh*"
    mc "I can't believe this is happening..."
    show story 007-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "[mil!c]. Estelle. This is Azula."
    mc "She's my... er..."
    show story 007-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "I'm Azula, a Valla and the God of this land!"
    azul "...and [mc] here is my male companion!"
    show story 007-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hmm..."
    silv "Perhaps you should explain, honey..."
    show story 007-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "God of the land? Valla?"
    este "More importantly, why did she call you her '{i}male companion{/i}'..."
    este "S-She isn't your '{b}girlfriend{/b}', right?"
    show story 007-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Geez..."
    mc "This is going to take a while..."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "I start to tell them the story from the very beginning..."
    "I tell them about hearing Azula's voice inside my head..."
    "And how I've been supplying her with my {b}essence{/b}, in order to power her up."
    "..."
    "Although, I didn't bother to explain to them how that process was done, exactly."
    scene black with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 007-36 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    silv "I see, I see..."
    silv "I think I understand what's going on now..."
    show story 007-37 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    silv "Azula, please make yourself at home."
    silv "We would be honored to have the 'Goddess of Scarlet' as our guest."
    show story 007-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "Well, I don't trust her one bit!"
    este "How can you both believe her nonsense?"
    este "She's clearly lying to take advantage of us!"
    show story 007-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Aw, but I'm not lying..."
    azul "I really am the Goddess of Scarlet who was resurrected thanks to [mc]'s essence..."
    show story 007-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Estelle, she's the real deal."
    mc "I mean, take a look at her..."
    mc "Would a normal human being have horns like Azula?"
    show story 007-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "S-So what?"
    este "It's a big world out there!"
    este "How do you know she won't kill us all in our sleep the moment her {i}powers{/i} return!?"
    show story 007-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hmm..."
    silv "Now that I think about it..."
    silv "...this isn't the first time I've met someone with horns."
    show story 007-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Your father, [mc], had horns too."
    show story 007-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "WHAT!?"
    mc "Why is this the first time I'm hearing about this!?"
    show story 007-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Oopsie..."
    silv "I never thought much of it..."
    silv "Seeing his horns became normal after a while."
    show story 007-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Ah, that would explain how you acquired your Valla blood, [mc]."
    azul "Where is the man now?"
    azul "I would certainly love to meet a Valla of this era."
    show story 007-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...He's gone."
    mc "He left shortly after I was born."
    show story 007-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "I see..."
    azul "How very unfortunate..."
    azul "I would have been very interested in hearing about why there are no Vallas in this modern day Scarlet."
    azul "Back during my time, Vallas were quite abundant, you see..."
    show story 007-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I don't even know if the man is dead or not..."
    mc "Not that I care, anyway."
    show story 007-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Hmm..."
    azul "If he hasn't returned, it most likely means that he's dead."
    show story 007-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...How do you know that?"
    show story 007-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Because of the grim nature of male Vallas..."
    azul "All of them tend to go on insane killing sprees in order to protect their harems."
    show story 007-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "And when that happens, they end up losing their minds and getting themselves killed."
    azul "The fact that he hasn't returned most likely means that he is no longer of this world."
    show story 007-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "..."
    este "Hey, why do you keep calling him a {i}Valla{/i}?"
    este "Are they supposed to be dangerous or something?"
    este "Also, stop talking to [mc] as if you two were a couple..."
    show story 007-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Oh, they are most definitely dangerous creatures..."
    azul "Vallas are extremely violent toward other Vallas of the same-sex..."
    azul "In fact, they kill each other all of the time..."
    show story 007-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Back in my day, it was quite normal to see a pool of blood in the middle of a dirt road."
    azul "Male Vallas kill other male Vallas for their harems...."
    azul "And female Vallas are extremely hostile toward other female Vallas in their pursuit for more {i}essence{/i}."
    show story 007-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(I really hope Estelle doesn't ask what essence is...)"
    show story 007-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Hmm..."
    azul "You know, now that I think about it..."
    azul "I can detect some Valla blood inside of you, young Estelle."
    azul "Albeit, it's incredibly weak compared to [mc]."
    show story 007-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Eh?"
    este "I-I'm a Valla, too?"
    show story 007-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Uh-huh, I'm almost certain of it..."
    azul "However, your magical aura is still weak compared to the average female Valla."
    azul "Perhaps you need to acquire some essence for yourself."
    show story 007-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "A-Are you sure about that, Azula?"
    mc "I mean the part where Estelle might be a Valla..."
    show story 007-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Sure am!"
    azul "Her personality is also matching of a female Valla."
    show story 007-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "What do you mean?"
    show story 007-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "I said it already, didn't I?"
    azul "Female Vallas are extremely aggressive toward other female Vallas."
    azul "The fact that she's overly protective of you is proof of it."
    show story 007-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "But don't worry, [mc]... I'm not like other Valla..."
    azul "I one hundred percent won't slaughter her..."
    azul "I'm more than happy to share your {i}essence{/i} with other girls."
    show story 007-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "WHAT!?"
    mc "I-I have no intention of philandering!"
    show story 007-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Hehe... You know what's funny?"
    azul "Male Vallas always say the same thing, but they somehow end up with a harem of girls anyway..."
    show story 007-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "H-Hey! I'm not overprotective at all!"
    este "I just don't like it when [mc] is standing next to other women is all!"
    show story 007-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "A-And who would like him? He's a creep! A pervert! And a hentai!"
    este "Isn't that right, [mc]?"
    este "Tell her that no other girl would ever want to tolerate you except me..."
    show story 007-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Sure, Estelle. Whatever you say."
    show story 007-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hehe..."
    silv "I love it when you two are lovey-dovey..."
    show story 007-55 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Well, it was a pleasure meeting you all..."
    azul "I suppose I'll have to go back to the lake..."
    azul "Back to... the cold... dark... and lonely lake..."
    show story 007-56 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "A vulnerable... beautiful Goddess like myself..."
    azul "Without even a fire to keep me warm at night..."
    azul "Who knows what would happen if a dastardly man decided to stumble upon my half-naked body..."
    azul "Will I even be around to see the next morning? I don't even know..."
    show story 007-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu:
        "Welp, see you later, Azula!" if True:
            $ renpy.fix_rollback()
            show story 007-58 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "[mc], I'm really disappointed in you..."
            silv "I thought you said that Azula was your friend?"
            show story 007-57 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Actually, I never said that she was my..."
        "Hol' up..." if True:
            $ renpy.fix_rollback()
            mc "Azula, I can't let you go back outside alone..."
            show story 007-52 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            azul "Eh!?"
            azul "Does that mean you'll let me stay..."
            show story 007-57 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            mc "I'll be more than happy to walk you back to the lake."
            mc "It's not too far off, so..."
            show story 007-58 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            silv "[mc], there is much that you need to learn about women..."
            silv "There is no way that we can allow Lady Azula to sleep under those conditions."
    show story 007-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Lady Azula, you are more than welcome to stay here if you'd like."
    silv "Consider our home, your home."
    show story 007-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Sweetness!"
    azul "I'll bunk up with [mc]!"
    show story 007-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Eh!?"
    este "A-A boy and a girl aren't allowed to share the same bed together!"
    este "Only married people can do that!"
    show story 007-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Estelle's right."
    silv "Azula, you'll have to bunk with Estelle for the duration of your stay."
    show story 007-55 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Aw, but I really want to sleep with my male companion..."
    azul "...or at least have my own room."
    azul "I'm a goddess, so I at least deserve that much..."
    show story 007-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Y-Yeah..."
    este "And I don't want to have to share my room with this harlot either..."
    este "It's not fair..."
    show story 007-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hmm..."
    silv "Well, we do have a spare room in the house, but..."
    silv "...it's in dire need of repairs."
    silv "Perhaps [mc] can do something about that."
    show story 007-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Huh?"
    mc "Why me?"
    show story 007-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Well, you {i}are{/i} the master of this household, correct?"
    silv "It's your responsiblity to provide proper working conditions for your slaves."
    silv "Otherwise, we might revolt and give you a [red]'BAD END'{/color}."
    show story 007-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm..."
    mc "Fair enough, but what should I do about it?"
    mc "I don't know anything about fixing rooms..."
    show story 007-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "The first thing you should do is inquire at the [yel]Builders Guild{/color}."
    silv "They'll give you a quote to repair the room."
    show story 007-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Alright then..."
    mc "I'll get to it when I have the time."
    show story 007-60 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "That sounds like a grand quest for our hero!"
    azul "[mc], can I still count on you to continue providing me with your {i}essence{/i} in the future?"
    show story 007-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Uh..."
    mc "I-I don't mind, but..."
    mc "...why would you need more if you already have your physical form back?"
    show story 007-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Because I still need more power if I'm to take over Scarlet again..."
    azul "And a female Valla draws strength from her male companion..."
    azul "...that's why I'll be counting on you, partner."
    show story 007-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "H-Hey..."
    este "What is this {i}essence{/i} thing that you two keep talking about?"
    show story 007-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Er..."
    mc "Estelle, I'll tell you about it some other time..."
    show story 007-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Nonsense!"
    azul "It's very important for a female Valla to learn about essence as soon as they are of age!"
    show story 007-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Essence is something that a male Valla provides for a female Valla..."
    azul "Basically, you get them really excited and then you make them..."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(2, hard=True)
    stop music fadeout 3.0
    este "AAAAAHHHHHH!!!"
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump mcroomlabel



label laur01_01:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 009-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    show story 009-02 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play sound "audio/phone.mp3" volume 2
    "*RRRNNNNNNGGGGGG*"
    stop sound
    show story 009-03 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Hmm..."
    mc "Who's calling me this early in the morning?"
    show story 009-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hello?"
    show story 009-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    play music "audio/sad.mp3"
    laur "*Yawn*"
    laur "Good... morning... [mc]..."
    show story 009-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "P-Princess Laureate?"
    mc "How did you even get my number?"
    show story 009-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "[mc], we need... to talk..."
    laur "Can you... stop by... and speak to me later?"
    laur "It's a matter of... life and death... so..."
    show story 009-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...Of course!"
    mc "I'll stop by your suite immediately!"
    show story 009-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "*YAWN* Nah..."
    laur "Don't come now..."
    laur "Come at, um... [yel]midnight{/color}..."
    laur "Yes... *YAWN* midnight will be perfect..."
    show story 009-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Er..."
    mc "Sure thing, Princess, but can I ask what it is that you want to..."
    show story 009-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    "*BEEP*"
    show story 009-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm..."
    mc "I guess I should stop by her suite later at midnight..."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(2, hard=True)
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    play music "audio/days.mp3"
    jump livingroomlabel

label laur01_02:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3
    show story 009-07 with Dissolve(1.5)
    $ renpy.pause(2, hard=True)
    mc "Hmm..."
    mc "Laureate said that she wanted to speak to me at midnight, but..."
    mc "...I don't see her around."
    mc "Maybe she's upstairs..."
    $ renpy.pause(1, hard=True)
    show story 009-08 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Hey, Princess... Are you..."
    show story 009-09 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "*GULP*"
    show story 009-10 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 009-11 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    laur "..."
    show story 009-12 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    laur "Eh?"
    laur "[mc]...?"
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "I hustled back downstairs as quickly as I could..."
    "Though it was for only a few brief seconds, the image of Laureate's perfect body was etched vividly into my head..."
    $ renpy.pause(.5, hard=True)
    show story 009-14 with Dissolve(1.5)
    $ renpy.pause(2, hard=True)
    mc "..."
    show story 009-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I'm so dead..."
    mc "I just saw her... the {i}princess'{/i}... milky cream body..."
    show story 009-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "But damn, what a sight..."
    mc "I'll never wash these eyes for as long as I live..."
    show story 009-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Oh dear..."
    laur "Please don't do that, [mc]..."
    laur "Hygiene is very important for a young gentleman."
    $ renpy.pause(.5, hard=True)
    show story 009-20 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/laureate.mp3"
    with vpunch
    mc "P-Princess..."
    mc "About what just happened... I swear it was an accident..."
    show story 009-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "I believe you..."
    laur "I know you didn't mean to perv on me like that."
    show story 009-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "...because if you did, I'd have you castrated, stripped, and paraded across Scarlet as a lesson to perverts everywhere."
    show story 009-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Hehe, just kidding!"
    show story 009-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Er..."
    mc "I'm grateful that you trust me, but how can you be so sure?"
    mc "I mean, we've only just met..."
    show story 009-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Oh, did I not mention it before?"
    laur "[yel]I was blessed with the unique ability to read minds."
    show story 009-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "...it's one of my many {i}special{/i} powers."
    show story 009-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...I can't tell if you're being serious or not."
    show story 009-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Hehe... I'll leave it at that."
    show story 009-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "So what brings you to my suite at this late of an hour?"
    show story 009-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Uh, you don't remember?"
    mc "You asked me to visit you at midnight today..."
    show story 009-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Eh?"
    laur "That doesn't sound like something I'd say..."
    show story 009-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Summoning a man to my chambers during the hour of the wolf is hardly something a pure-hearted maiden such as myself would ever do..."
    laur "Perhaps you really did have lewd intentions, [mc]... and this was just your pitiful excuse for if you got caught..."
    show story 009-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "But you did, Princess! You called me this morning!"
    mc "You even said that it was a matter of life and death!"
    show story 009-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Hmm... is that so?"
    show story 009-25 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    laur "Oh, wait! I remember now!"
    laur "You're right. I did call you earlier, didn't I?"
    show story 009-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Princess..."
    show story 009-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "[mc], do you recall our very first meeting?"
    laur "...about what you promised to do for me?"
    show story 009-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Of course..."
    mc "I said that I'd do {i}anything{/i} to save [mil!c] and Estelle."
    show story 009-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Hehe..."
    laur "I'm glad that you remember..."
    laur "As for me, I have a tendency to forget these sort of things."
    show story 009-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Anyway, it's about time I collect the {i}debt{/i} that you owe me."
    laur "Do you intend on keeping your promise, [mc]?"
    show story 009-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Of course!"
    mc "I'm a man of my word! I'll pay back every penny I owe you!"
    show story 009-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "No, no, no..."
    laur "I don't care about the money. I want something {i}else{/i} from you instead, [mc]."
    show story 009-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...What is it?"
    mc "I'll do anything you ask, Princess!"
    show story 009-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Hmm..."
    laur "So if I say '{b}give your life to me{/b}', you'd do it without any hesitation?"
    show story 009-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "...My life!?"
    show story 009-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Aww..."
    laur "I guess you won't, huh?"
    show story 009-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "When I said that I'd do anything to save my household..."
    mc "I truly meant it."
    mc "That's why, if its my life you want, you can have it."
    show story 009-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Hehe..."
    laur "Don't worry, [mc]. I have no intention of throwing it away..."
    show story 009-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "You're worth far more to me alive."
    show story 009-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Whew..."
    mc "That's a relief..."
    show story 009-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "...But I wasn't joking when I said I wanted your {i}life{/i}, [mc]."
    laur "You see, I'm in need of protection."
    laur "While Ferry is a quality guardian, I desire a '{b}knight{/b}' who will also swear to protect me when trouble arises."
    show story 009-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You... want me to become a {i}knight{/i}?"
    mc "The Princess's Knight!?"
    show story 009-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Uh-huh."
    laur "If I'm ever in danger, will you promise to swoop in and save me?"
    laur "Like a true knight would for his princess?"
    show story 009-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "W-Wow..."
    mc "That's a great honor, but..."
    mc "Hmm..."
    show story 009-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "You disagree?"
    show story 009-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "It's not that..."
    mc "It's just... well... I don't know if I can live up to your expectations..."
    mc "I don't have any training... nor am I particularly strong..."
    show story 009-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "That's okay, [mc]."
    laur "You're special to me... in your own way..."
    laur "Having your presence on my side is enough to put me at ease."
    show story 009-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "Something about this girl made my heart flutter..."
    "It was as if there was nothing she could say that would make me hate her..."
    show story 009-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "That being said..."
    laur "[mc], if you desire to become stronger..."
    laur "I can arrange for someone to personally train you."
    show story 009-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Well, if you think it'll help me..."
    mc "I don't mind training."
    show story 009-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Hehe... How wonderful!"
    laur "I know that you won't disappoint me..."
    show story 009-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "...my {b}knight{/b}."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(2, hard=True)
    stop music fadeout 3.0
    "Laureate explained to me that my '{b}personal trainer{/b}' will be available at the [yel]Park{/color} during the evening and night..."
    "I suppose I should visit when I get the chance..."
    $ renpy.end_replay()
    play sound "audio/ding.mp3" volume 3
    "[yel]Laureate will now pay you when you spend time with her."
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump cityhalllabel_01

label laur01_03:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3
    show story 009-29 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    show story 009-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Estelle was right... This park is kinda spooky at night..."
    mc "But Laureate said that my trainer would meet me here..."
    show story 009-31 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mv2 "..."
    mv2 "<Target hostile detected...>"
    mv2 "<Initiating offensive protocol...>"
    show story 009-32 with Dissolve(1.5)
    $ renpy.pause(2, hard=True)
    show story 009-33 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    with vpunch
    mc "W-What!?"
    play sound "audio/fall.mp3" volume 3
    show story 009-34 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "Ugh..."
    show story 009-35 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "W-Whoa..."
    mc "Don't kill me..."
    show story 009-36 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play music "audio/ferry.mp3"
    ferr "..."
    show story 009-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "<Hostile grounded...>"
    ferr "<Suggestion: Eliminate target before enemy reinforcements arrive...>"
    show story 009-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "E-Eliminate!?"
    mc "Hold on, Ferry! It's me! Your {i}best friend{/i}, [mc]!"
    show story 009-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "<Assessing target threat level...>"
    show story 009-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "... ... ..."
    show story 009-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "<Threat level: Minimal...>"
    show story 009-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Whew, thank Goddess..."
    show story 009-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Wait, you don't see me as a threat?"
    mc "That's damaging to a man's pride y'know?"
    show story 009-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "...Target is harmless."
    ferr "<Suggestion: Release target or risk future ramifications...>"
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 009-39 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    with vpunch
    mc "Ferry, what the heck was that all about!?"
    mc "Were you seriously about to kill me!?"
    show story 009-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "<Scanning voice recognition...>"
    show story 009-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "... ... ..."
    show story 009-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "<Scanning complete...>"
    ferr "<Target: [mc]... Status: Civilian... Power Level: Under 9000...>"
    show story 009-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Ah, so it's you, [mc]..."
    ferr "I've been expecting you."
    show story 009-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "It's good to see you too, Ferry."
    show story 009-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Apologies for earlier."
    ferr "My night vision modules are currently undergoing maintenance..."
    show story 009-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "As such, my system is having difficulties separating hostiles from civilians."
    show story 009-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Night vision modules?"
    mc "Ferry, you're not making any sense."
    show story 009-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "You should be on your guard, [mc]."
    ferr "There have been reports of various oddities within this area lately."
    show story 009-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "If you intend on becoming the princess' knight, one must take necessary precautions whenever possible."
    show story 009-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...Sure"
    mc "So can I assume that you're the one that Laureate assigned to train me?"
    show story 009-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "That is indeed correct."
    ferr "As I am well-versed in the highest level of 'Maid Bujutsu', Her Highness believes that it would be beneficial for me to oversee your knightly training."
    show story 009-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...I see."
    show story 009-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Hmm..."
    ferr "I detect some minor disappointment?"
    show story 009-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "No, no, not at all."
    mc "It's just that... is a maid really qualified to train me?"
    show story 009-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "How shameful..."
    ferr "I'll have you know that I take great pride in my work as a maid."
    show story 009-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "[yel]I've even graduated top of my class in Scarlet's most pretigious maid university."
    show story 009-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Sorry, I didn't mean to offend you..."
    mc "It's just... well... being a maid can't be too..."
    show story 009-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "...You do not want to finish that sentence."
    show story 009-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "N-Nevermind then..."
    mc "Let's just start our training."
    show story 009-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Very well..."
    ferr "First, we'll begin with some exercises so that I can better gauge your {i}specs{/i}."
    show story 009-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Follow me and we shall begin..."
    show story 009-48 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "...Specs?"
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show park01_ferrrun 05 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "The rest of the evening was spent running with Ferry..."
    show park01_ferrrun 06 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    "Her stamina was endless... There was no way I could keep up with her..."
    "When it came time to return home, my legs were ready to fall off my body..."
    $ renpy.pause(.5, hard=True)
    $ renpy.end_replay()
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/days.mp3"
    jump parklabel_01



label mako01_01:

    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3
    show story 011-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/silvia.mp3"
    mc "..."
    mc "[mil!c]? Estelle? What's going on?"
    mc "Were you two waiting for me?"
    show story 011-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Uh-huh..."
    silv "Both Estelle and I have noticed how hard you've been working lately."
    silv "So we've decided to treat you to something {i}nice{/i}."
    show story 011-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hehe..."
    este "I was the one who came up with the idea!"
    show story 011-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "So hurry up and praise me, [mc]!"
    menu:
        "Praise Estelle..." if True:
            show story 011-20-01 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            show story 011-20-02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Hehe... I'm great..."
        "Ignore her..." if True:
            show story 011-20-03 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            este "H-Hey..."
    show story 011-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "So what's this about something {i}nice{/i}?"
    mc "*GULP*"
    mc "(C-Can this be...)"
    with vpunch
    mc "(The legendary 3P H-Scene with my [mil] and [sil]!?)"
    mc "(This soon, already!?)"
    show story 011-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "Eww, [mil!c]..."
    este "[mc] is thinking of something weird again, isn't he?"
    show story 011-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Creep! Pervert! Hentai!"
    show story 011-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "N-No, I'm not!"
    mc "I'm just thinking about what it is you two got me!"
    show story 011-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hehe..."
    silv "I love it when you two are lovey-dovey..."
    show story 011-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Anyway, here you are [mc]..."
    silv "It was expensive, so I hope you like it."
    show story 011-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "This is..."
    mc "...a coupon for [yel]Scarlet Hot Springs{/color}?"
    show story 011-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Uh-huh!"
    show story 011-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Estelle and I wanted to show our appreciation for how hard you've been working, [mc]."
    silv "So we decided to treat you to a one-day rest-and-relaxation trip to the onsen!"
    show story 011-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hehe..."
    este "You love it, don't you [mc]!?"
    show story 011-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Go ahead and praise me!"
    menu:
        "Praise Estelle..." if True:
            show story 011-20-01 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            show story 011-20-02 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            este "Hehe... Well-deserved..."
        "Ignore her..." if True:
            show story 011-20-03 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            este "Oi..."
    show story 011-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "W-Wow..."
    mc "Thanks, you two. I don't know what to say..."
    mc "(H-Hold on...)"
    mc "(I'm about to go dipping in the hot springs with Estelle and [mil!c]!"
    mc "(T-That means... I'm going to... see them both... {b}naked{/b}!)"
    mc "(Maybe... just maybe... I'll get that 3P H-Scene, after all...)"
    show story 011-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Geez, [mc]..."
    este "Can you be any less tact?"
    show story 011-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "You have the most obvious perverted smirk on your face right now..."
    show story 011-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...Wait a second."
    mc "Why is there only {i}one{/i} coupon here?"
    show story 011-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Er..."
    silv "Sorry, sweetheart."
    show story 011-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "The [yel]kind-hearted Fox Girl{/color} who sold this coupon to me said it was the last one."
    silv "...and she gave it to me at a huge discount."
    show story 011-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...I see."
    show story 011-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Oh, [mc]..."
    silv "You look disappointed... Did you not want to go by yourself?"
    show story 011-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "N-No, I love the gift..."
    mc "It's just that..."
    mc "...{i}nevermind{/i}."
    mc "(I just wish we could all go together...)"
    mc "(...n-not that I want to see my [mil] and [sil] naked or anything.)"
    mc "..."
    show story 011-18 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "Come here, you two!"
    mc "I love you both so much..."
    show story 011-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Aww..."
    silv "We love you too, [mc]."
    show story 011-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Geez, [mc]..."
    este "Y-You're too close, you big dummy..."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump mcroomlabel

label mako01_02:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "After heading outside, I began my trek to Scarlet Hot Springs..."
    "It was my first time visiting and I couldn't wait to dip my body in their warm waters..."
    $ renpy.pause(1, hard=True)
    scene onsen01_night with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    mc "This is the place..."
    mc "Scarlet Hot Springs, one of the biggest tourist attractions in Scarlet..."
    mc "...Wait, what's up with that sign?"
    with vpunch
    mc "...Closed until further notice!?"
    with vpunch
    mc "...Trespassers will be shot and killed!?"
    with vpunch
    mc "I've been looking forward to this trip all day..."
    menu:
        "Sneak inside..." if True:
            $ renpy.fix_rollback()
            mc "..."
            with vpunch
            mc "Screw it! I don't care if the place is closed!"
            mc "It's a damn hot spring! It can't be completely shut down, right!?"
        "Don't risk it..." if True:
            $ renpy.fix_rollback()
            mc "..."
            mc "Yeah, how stupid would I be to try and enter after seeing a sign like that?"
            mc "..."
            mc "......."
            mc "... ... ... ..."
    mc "Alright, I'm just going to hop the fence..."
    mc "Here goes nothing..."
    show story 012-01 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "HYUUUUHHH!!!"
    show story 012-02 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play sound "audio/fall.mp3" volume 3
    mc "..."
    show story 012-03 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Heh..."
    mc "Never underestimate a man who watches ninja anime..."
    scene black with Dissolve(1.5)
    play sound "audio/splash.mp3" volume 3
    $ renpy.pause(3, hard=True)
    show story 012-04 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    show story 012-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Ahh... This is the life..."
    mc "I should sneak in here more often..."
    show story 012-06 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 012-07 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    stop music fadeout 3
    mv2 "..."
    mv2 "Ahhh... This is the life..."
    show story 012-08 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mv2 "I should come in here more often..."
    show story 012-09 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show mako01_02_01 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play music "audio/makoto.mp3"
    mako "Ah... The water feels so good..."
    mako "I can feel my worries slowly fading away..."
    mc "..."
    mc "(S-Shit... What should I do?)"
    mc "(I'm trespassing... I don't want to be {b}shot and killed{/b}...!)"
    mc "(Hold on... that voice...)"
    mako "..."
    mako "So much has happened lately..."
    mako "Pandy's speaking to me again... but that'll only last if I can seduce [mc]..."
    mako "Of course, that's going to be impossible..."
    mako "He'll probably never notice me..."
    mako "...since I don't look or act like a girl."
    mako "*Sigh*"
    hide mako01_02_01
    show story 012-10 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "M-Makoto!!!"
    show story 012-11 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mako "EEHHH!!!???"
    mako "[mc], w-what are you..."
    mako "W-Wait, did you hear..."
    show story 012-12 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Everything you said just now isn't true!!!"
    mc "You're really cute and I love spending time with you!!!"
    show story 012-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "..."
    mc "..."
    show story 012-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oops..."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    play sound "audio/splash.mp3" volume 3
    $ renpy.pause(3, hard=True)
    show story 012-15 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    mako "..."
    show story 012-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "[mc]..."
    mako "What the heck are you doing here!?"
    show story 012-17 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mc "(M-Makoto's breasts...)"
    mc "(Can this fog {i}please{/i} just go away...)"
    show story 012-18 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mako "Er..."
    mako "[mc], you're staring..."
    show story 012-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "R-Right..."
    show story 012-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "So explain what you're doing here, [mc]..."
    mako "Didn't you see the sign? This place is supposed to be off-limits to the public."
    show story 012-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Ah... well, you see..."
    mc "I had this coupon for the hot springs, but..."
    mc "I didn't realize that the place was closed down..."
    mc "That's when I came up with the brilliant idea to hop over the fence..."
    show story 012-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Oh..."
    mako "So you snuck in here, huh?"
    show story 012-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I didn't peg you for being a rebel, [mc]."
    show story 012-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I'm, uh, assuming you had the same idea?"
    show story 012-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Nah, I'm actually here legally..."
    show story 012-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "You see, Scarlet Hot Springs was actually built and managed by my family for thousands of years..."
    show story 012-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "In other words, this place belongs to me."
    show story 012-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "Y-You own these hot springs!?"
    show story 012-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Uh-huh..."
    mako "Well, only for a little while longer..."
    show story 012-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I figured I'd soak in the waters for one last time before I sell the place..."
    mako "[yel]In fact, I already have a buyer lined up..."
    show story 012-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Makoto..."
    mc "Can it be that... you're trying to raise money for your Scarlet Contract?"
    show story 012-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Yup..."
    show story 012-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Even with the money I've inherited, I still won't have enough..."
    mako "That's why I'm going to try and raise more funds by selling some real estate."
    show story 012-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I don't know, Makoto..."
    mc "I mean, this place was built and owned by your ancestors for thousands of years, right?"
    mc "Selling the place... feels wrong."
    show story 012-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I understand what you mean, [mc]."
    mako "And believe me, it wasn't easy for me to make this decision..."
    show story 012-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "But as much as I love the onsen, I love the Builders Guild and Pandoria even more."
    mako "That's why... I have to sell it..."
    show story 012-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "The easiest solution would be to just marry you, but..."
    show story 012-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Oh no, no, no!"
    mako "That's okay, [mc]! I know you said that you weren't ready!"
    show story 012-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Frankly, I don't think I'm ready for marriage either..."
    show story 012-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...That's still better than having your freedom taken from you."
    show story 012-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Heh, maybe..."
    mako "But you know, [mc], I have a feeling that you'll be a great owner."
    show story 012-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Call it my {b}Builder's intuition{/b}."
    show story 012-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Makoto..."
    mc "You're awfully optimistic, aren't you?"
    show story 012-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Maybe..."
    show story 012-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "But yeah, marriage is also a very important decision."
    show story 012-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "...and who knows, m-maybe we can get married in the future."
    mako "It's not unusual for an owner to marry his slave, after all..."
    show story 012-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I suppose only time will tell..."
    show story 012-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Oh, by the way..."
    mako "Pandoria says that we're ready to start fixing your room."
    show story 012-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "So whenever you have the funds, you can speak to me and we'll begin."
    show story 012-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Got it."
    mc "And how much will it be?"
    show story 012-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Eh..."
    mako "She estimates about [yel]$1,000{/color}."
    show story 012-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Hope you have enough."
    show story 012-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "That's not too bad..."
    mc "I'll speak to you when I'm ready to fix the room."
    show story 012-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Roger that!"
    show story 012-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Well, I think I should be getting out, Makoto."
    mc "I've been here for a while..."
    show story 012-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Ah, wait up, [mc]!"
    mako "I'll go ahead and wash your back while you're here."
    show story 012-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "Y-You want to wash my back?"
    show story 012-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Sure, it's a Komatsu tradition..."
    mako "Part of being a courteous host or whatever."
    show story 012-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I actually used to wash my dad's back every time we came here together."
    show story 012-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Uh, Makoto?"
    mc "Why are you washing your dad's back...?"
    show story 012-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Er..."
    mako "[mc], please don't be creepy..."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play sound "audio/splash.mp3" volume 3
    "Makoto closed her eyes as I stepped out of the water..."
    "I was grateful that she did since my dick was already fully erect from staring at her naked body..."
    $ renpy.pause(1, hard=True)
    show story 012-28 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show mako01_02_02 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mako "..."
    mako "[mc], you have superb back muscles..."
    mako "I bet you'd make a great builder if you tried."
    mc "Thanks, Makoto..."
    mc "...I guess."
    mako "Hehe..."
    mako "This is so nostalgic, I remember doing this for my father back when I was a toddler..."
    mako "But then when I got older, he suddenly stopped wanting to go to the hot springs with me..."
    mako "He never gave me a reason why..."
    mc "..."
    mc "Your father is a good man."
    mako "He really was a great person..."
    mako "If you met him, I'm sure that he'd like you a lot, [mc]..."
    mako "...even though he did threaten to smash every guy who approached me with Pandy."
    mc "..."
    hide mako01_02_02
    show story 012-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Okay, we're all done here..."
    show story 012-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh? I can get up now?"
    show story 012-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "No, no, no..."
    mako "I meant that you should turn around."
    mako "You know, so I can do your front..."
    show story 012-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "T-That's okay!"
    mc "I can do that part myself!"
    show story 012-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Nonsense..."
    mako "A Komatsu always finishes what she starts..."
    show story 012-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "...It's one of our family mottos."
    show story 012-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You know..."
    mc "I'm starting to think your family has a lot of mottos..."
    show story 012-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Hehe, so you get it then, right?"
    show story 012-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Hurry up and turn around so I can wash your front."
    show story 012-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(Whenever this girl brings up her family's name, I know better than to argue with her...)"
    show story 012-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Alright fine..."
    mc "Let's get this over with..."
    $ renpy.pause(.5, hard=True)
    show story 012-35 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mako "..."
    show story 012-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "[mc], I'm going to remove your towel, okay?"
    mako "...so I can clean your lower half."
    show story 012-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "I-Is that really necessary?"
    show story 012-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Eh?"
    mako "I thought I made myself clear..."
    show story 012-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "A Komatsu always finishes what she..."
    show story 012-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Alright, alright!"
    mc "I get it already..."
    show story 012-38 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 012-39 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 012-40 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 012-41 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mako "Eh...?"
    mako "W-Why does it... look like this..."
    mc "..."
    mc "Er, Makoto... Are you okay?"
    show story 012-42 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play sound "audio/fall.mp3" volume 3
    with vpunch
    mc "Makoto!!!???"
    show story 012-43 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mc "She's knocked out cold..."
    mc "What happened to her?"
    pand "*Sigh*"
    pand "I had a feeling this would happen..."
    mc "Pandoria...?"
    mc "Is that you?"
    pand "Indeed..."
    pand "You see, Makoto has a habit of fainting whenever she sees a penis..."
    pand "It happened all the time during her trips to the hot springs."
    mc "..."
    show story 012-44 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    pand "..."
    pand "Where are you going, [mc]?"
    show story 012-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "To find her a bed..."
    mc "She owns the hot springs, right? It shouldn't be a problem if she stays overnight."
    show story 012-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    pand "No, no, no..."
    pand "[mc], this is the perfect opportunity for a {b}breeding{/b} session..."
    pand "The Komatsu Clan needs its male heir!"
    show story 012-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "WHAT!?"
    mc "YOU WANT ME TO DO {i}IT{/i} WHILE SHE'S UNCONSCIOUS!?"
    show story 012-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    pand "Did I not make myself clear?"
    pand "Or perhaps you do not know how it's done..."
    pand "You're supposed to stick her with the pointy end..."
    show story 012-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "I-I know how it's done!"
    mc "It's just that..."
    show story 012-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    pand "What is it then?"
    pand "You feel guilty about having sex with an unconscious body?"
    pand "Do not be ashamed, [mc]..."
    pand "During my early years, it was completely normal for humans to mate and breed whenever possible..."
    pand "...naturally, that includes while a mate is asleep."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "I'm ashamed to say that I was actually thinking about doing it..."
    "But in the end, I'm just not that type of person..."
    "...and this isn't that type of game."
    "I blocked out Pandoria's voice and covered Makoto with a clean towel..."
    "Then I carried her off to a room inside the hot springs."
    $ renpy.end_replay()
    $ renpy.pause(1, hard=True)
    play sound "audio/ding.mp3" volume 3
    "[yel]Onsen has been added to the Map Screen."
    play sound "audio/ding.mp3" volume 3
    "[yel]Makoto is now ready to fix a room for Azula... for a price!"
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump onsenlabel

label mako02_01:

    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 015-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/silvia.mp3"
    silv "..."
    show story 015-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Good morning, [mc]..."
    show story 015-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Morning, [mil!c]."
    show story 015-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "One of your friends stopped by earlier..."
    silv "He apparently had something he wanted to speak to you about."
    show story 015-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "{i}He...{/i}?"
    mc "I think they got the wrong person, because I don't have any..."
    mc "..."
    mc "(I don't want to tell her that I don't have any guy friends...)"
    show story 015-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Oh no, dear... He definitely knew you personally."
    show story 015-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "I invited him inside but he hesitated when I told him that you were still in bed..."
    silv "He asked if he could leave you a message instead."
    show story 015-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...What did he say?"
    show story 015-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Just that he wanted to meet you at the [yel]beach{/color} this afternoon."
    show story 015-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "...you know, the famous beach at the outskirts of town?"
    show story 015-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah, I know about it..."
    mc "I'm just wondering who this person is and why they'd want to meet me there."
    mc "...I hope I'm not in trouble or anything."
    show story 015-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hehe..."
    show story 015-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Don't worry, [mc]. He looked quite friendly enough."
    silv "...Perhaps a little timid, if anything."
    show story 015-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Alright, if you say so."
    mc "I'll go meet him at the beach later today."
    show story 015-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hold on, [mc]..."
    silv "Aren't you forgetting something?"
    show story 015-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Um..."
    show story 015-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Your swim trunks, silly."
    show story 015-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Komisari's rule states that you can't go to the beach without one."
    show story 015-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "How could I have forgotten something as important as that!?"
    mc "But wait..."
    mc "I don't fit in any of my old trunks anymore..."
    show story 015-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hehe, don't worry."
    show story 015-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "I'm sure you can pick up a new pair at [yel]Kujikawa's store{/color}."
    silv "Last I checked, they sell swim trunks."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3.0
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump livingroomlabel

label mako02_02:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 015-07 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/serena.mp3"
    mc "..."
    mc "Hey, Serena. Do you have a moment?"
    show story 015-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "For you, [mc], you can have two moments."
    show story 015-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "What can I do for you?"
    show story 015-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I'm planning on visiting the beach today, but I need a new pair of swim trunks."
    mc "Do you happen to sell them here?"
    show story 015-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hehe, you're just in luck!"
    show story 015-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "We do have an assortment of beach attire here."
    show story 015-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "And they happen to be quite the {i}hit{/i} recently."
    show story 015-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Is that right?"
    mc "That makes sense. It has been pretty warm outside..."
    show story 015-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Nah, there's another reason why the beach is getting popular..."
    show story 015-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Apparently, it's being bought out by some rich celebrity."
    sere "And that celebrity is driving up interest all across Scarlet by promoting the place."
    show story 015-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Interesting..."
    with vpunch
    mc "Wait, won't that mean the beach will be packed with people now!?"
    mc "...How will I be able to find the person who's looking for me!?"
    show story 015-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Er..."
    sere "You're going to the beach to '{b}meet someone{/b}', [mc]?"
    show story 015-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "...like, with a {b}girl{/b}?"
    show story 015-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "N-No! Of course not!"
    mc "The person I'm meeting up with is a guy..."
    show story 015-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Oh, okay..."
    show story 015-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Who is it then? Is it someone I know?"
    show story 015-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...I actually have no idea."
    show story 015-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Eh?"
    sere "Y-You don't know!? Then could this mean..."
    show story 015-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    sere "...that this might be a meeting for a {b}confession{/b}!?"
    show story 015-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "You're being ridiculous, Serena!"
    mc "And I'll have you know that I only like girls!"
    show story 015-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Ah, that's a relief..."
    show story 015-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "N-Not that there's anything wrong with that!"
    show story 015-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Y-Yeah..."
    mc "So about going to the beach..."
    show story 015-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Right, right..."
    sere "Step inside and we'll take care of that right away!"
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3.0
    "After a bit of browsing, I paid Serena for my purchase and left the store."
    if (money >= 200):
        play sound "audio/coins.mp3" volume 3
        show love_sere at up_happy
        "[yel]You paid Serena $200."
        $ money -= 200
        hide love_sere at up_happy
    if (money < 200):
        play sound "audio/coins.mp3" volume 3
        show love_sere at up_happy
        "[yel]You paid Serena $[money]."
        $ money = 0
        hide love_sere at up_happy
    play sound "audio/ding.mp3" volume 3
    "[yel]Beach has been added to the Map Screen."
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump streetlabel_01

label mako02_03:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    scene beach01_morning_stand with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    mc "That's weird. I figured the beach would be packed today..."
    mc "How come there isn't anyone around?"
    mc "..."
    mc "It should make it easier to find the person who's looking for me."
    mc "But in hindsight, I probably should have asked [mil!c] for a general description of the guy..."
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump beachlabel_01

label mako02_04:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 016-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    show story 016-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I've searched high and low, but can't find anyone here..."
    mc "This is so strange. I've always remembered the beach being crowded with people."
    show story 016-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Maybe this was all an elaborate prank..."
    mc "Maybe some sick asshole just wanted to see me in swim trunks..."
    show story 016-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...Yeah, that has to be it."
    show story 016-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "HALT!!!"
    show story 016-05 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play music "audio/adeline.mp3"
    with vpunch
    mvadel "You there!!!"
    mvadel "What do you think you're doing trespassing on private property!?"
    show story 016-06 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    show story 016-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Trespassing on private property? What are you talking about?"
    show story 016-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvadel "Do not make me repeat myself."
    mvadel "What. Are. You. Doing. Here."
    show story 016-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I'm just hanging at the beach..."
    mc "Is that a problem?"
    show story 016-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvadel "It is indeed a serious problem!"
    mvadel "This area is off-limits to the public as ordered by my fair lady."
    show story 016-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Wait, what!?"
    mc "The beach has always been open to everyone..."
    show story 016-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Hold on a minute..."
    mc "Are you supposed to be the mystery person that I'm here to meet?"
    mc "[mil!c] said that it was a guy..."
    show story 016-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvadel "Eh?"
    mvadel "You're meeting someone here, too?"
    show story 016-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvadel "Ah! Yes, yes, I see..."
    show story 016-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvadel "You must be {b}Master Komatsu{/b}, then."
    show story 016-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvadel "I've been delegated by my fair lady to speak with you today on her behalf."
    show story 016-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm..."
    mc "So you're looking to meet a {b}Master Komatsu{/b}, huh?"
    show story 016-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    menu:
        "Yes, I am Master Komatsu..." if True:
            $ renpy.fix_rollback()
            show story 016-18 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            mc "Yes, I am Master Komatsu!"
            show story 016-16 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Pleased to meet you!"
        "No, I am not Master Komatsu..." if True:
            $ renpy.fix_rollback()
            show story 016-17 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Hmm..."
            mc "I think there's a misunderstanding..."
    show story 016-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvadel "Your reputation precedes you, Master Komatsu..."
    show story 016-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvadel "Only a handful of nobles possess the influence to rival my fair lady."
    show story 016-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvadel "Truly, it is an honor to meet a man who even she holds in such high regard."
    show story 016-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 016-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You're looking for Makoto, aren't you?"
    mc "What's your reason for wanting to meet her?"
    show story 016-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mvadel "Eh?"
    mvadel "Wait, so you're not Master Komatsu?"
    show story 016-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "No. I am not."
    show story 016-25 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mvadel "I-Impossible..."
    show story 016-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvadel "To think that I would make such a grevious mistake..."
    show story 016-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvadel "Now that I think about it, you look nothing like Master Komatsu..."
    show story 016-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 016-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvadel "Ah... I'm so ashamed... I'm not fit to call myself my lady's maid..."
    show story 016-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvadel "There's only one thing left for me to do..."
    show story 016-29 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 016-30 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    with vpunch
    mc "W-What the heck are you doing!?"
    show story 016-31 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mvadel "*Sniff* *Sniff*"
    show story 016-32 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mvadel "Please, sir! Punish me as you see fit!"
    show story 016-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvadel "The only way a fool of a maid such as myself will ever learn her lesson is through physical punishment."
    show story 016-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvadel "That is why I must implore you..."
    show story 016-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvadel "Take this riding crop and punish my bottom until it is swollen and red, just as my lady would..."
    show story 016-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvadel "Though your punishment will serve as only a temporary fix compared to the chastisement my fair lady will deliver me once I explain to her my failure."
    show story 016-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "I-I'm not going to punish you!"
    show story 016-36 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mako "H-Hey, you two!!!"
    mako "What's going on over here!?"
    show story 016-37 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mako "[mc], you're awful!"
    mako "Just what were you about to do to this poor lady!?"
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "After a brief explanation, the mystery maid recomposed herself."
    "Apparently, she and Makoto were expecting each other..."
    $ renpy.pause(1, hard=True)
    show story 016-38 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mvadel "Ah, I understand now..."
    show story 016-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvadel "So {i}you{/i} are Master Makoto, and this here is [mc]..."
    show story 016-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvadel "Yes, yes, yes. I knew that all along. Since you are here, my mission will now be a success..."
    show story 016-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I think you have a few loose screws in your head, lady..."
    show story 016-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvadel "Your chivalry was much appreciated, Master Makoto."
    show story 016-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvadel "This savage brute was a breadth away from violating my voluptuous elven body with his big, long stick."
    show story 016-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oi, oi..."
    mc "Now that you know our names, maybe it would be appropriate if you gave us yours."
    show story 016-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvadel "Ah, pardon me for my lack of courtesy..."
    show story 016-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "I am called [yel]Adeline{/color}, a maid in service of Scarlet's Champion, [yel]Joanne Marie Madison 'Maple' Mablethorpe{/color}."
    show story 016-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "It is an honor to make your utmost acquaintance."
    show story 016-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Another maid, really?"
    mc "This dev is seriously running out of ideas..."
    show story 016-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Pleased to meet you, Adeline..."
    show story 016-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I'm assuming you're here to discuss the sale of the beach on behalf of Miss Maple?"
    mako "Where is she, anyway? It was her idea in the first place to meet up here."
    show story 016-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "Your deduction is absolutely correct, Master Komatsu."
    show story 016-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "My lady regrets to inform you that she will not be able to attend today's meeting..."
    show story 016-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "Due to her high social standing as [yel]Champion{/color}, she is an extremely busy woman."
    show story 016-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "She begs you for her forgiveness."
    show story 016-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Aw, okay..."
    mako "That's a shame. I really wanted to meet her."
    show story 016-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "Rest assured, she is still fully committed in acquiring [yel]Komatsu Beach{/color} from you, Master Makoto..."
    show story 016-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "As such, she has assigned me to personally tell you that the money wired to your account has been a success, both for the beach {i}and{/i} for Komatsu Hot Springs!"
    show story 016-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Komatsu Beach?"
    mc "Makoto, this beach is yours?"
    show story 016-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Heh, did I not mention that before?"
    show story 016-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "The Komatsu Clan owns several acres of land all across Scarlet."
    show story 016-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Unfortunately, I'm going to have to give up some it though... Both the beach and the hot springs..."
    show story 016-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "That is correct..."
    adel "My humble master is pleased that you're willing to surrender such a prominent and historic landmark to her."
    show story 016-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "Be at ease, the beach will certainly be well taken care of under Lady Maple's watchful eye."
    show story 016-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Makoto, are you sure this is what you want to do?"
    mc "This is all for your Scarlet Contract, isn't it..."
    show story 016-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Heh..."
    mako "Think it's too much? Don't worry, [mc]. It's just a beach."
    show story 016-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "The... future of the Builders Guild... is much more important, anyway."
    show story 016-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "Hehe... I suppose that concludes our business here."
    show story 016-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "I wish you both a splendid day..."
    show story 016-53 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mvtori "Ah, there you are!"
    show story 016-54 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mvtori "Where do you think you're going without us, Makoto-kun!?"
    mvhana "Nya~ Nya~"
    show story 016-55 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mako "..."
    show story 016-56 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Sheesh... Look, you two..."
    show story 016-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I've been trying to explain that I'm not a..."
    show story 016-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "What do you think of my new bikini, Makoto-kun?"
    show story 016-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "Does it get your heart racing? I wore it just for you..."
    show story 016-60 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mako "Eh!?"
    show story 016-62 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvhana "Nya~ Nya~"
    mvhana "Makoto-kun, do you prefer girls with larger breasts or smaller ones..."
    show story 016-61 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvhana "This information is very relevant to my interests."
    show story 016-63 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mako "B-Breasts...!?"
    mako "What do they have to do with anything!?"
    with vpunch
    mako "[mc] isn't so shallow that he cares about that sort of thing!"
    show story 016-65 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "Oh, Hana! I saw this in a magazine once!"
    show story 016-67 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "If a guy starts blushing when you ask them about breasts, it means that he likes {i}medium-sized{/i} breasts..."
    show story 016-68 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvhana "Nya~ Nya~"
    mvhana "You're always right, Tori. Makoto-kun must like medium-sized breasts! Nyah~!"
    show story 016-66 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "...just like mine."
    mvtori "Do you like my breasts, Makoto-kun?"
    show story 016-64 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Um..."
    mako "A-As I've been trying to tell you two, I'm not a..."
    show story 016-67 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "Would you like to rub lotion on my back, Makoto-kun?"
    mvtori "...or my front, if you'd prefer."
    show story 016-66 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "If it's you, I don't mind..."
    show story 016-69 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Geez, you girls..."
    show story 016-70 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "You really ought to show a little bit more modesty, y'know?"
    mako "Guys like that sort of thing... I think..."
    show story 016-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mvtori "KYAAAAAHHH!!!"
    mvtori "He's sooooo pure-hearted..."
    show story 016-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "That's what I love about you..."
    show story 016-61 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvhana "Nya~ Nya~"
    mvhana "Rub me first, Makoto-kun!"
    show story 016-62 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvhana "I've been a reeaaally bad kitty lately, and only a belly rub will calm me down..."
    show story 016-71 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    adel "..."
    show story 016-72 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "Ahem..."
    show story 016-73 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "Excuse me, but you vulgar girls must leave the premise immediately."
    show story 016-74 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "Eh?"
    mvtori "Why is that?"
    show story 016-75 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "Because you are trespassing on private property."
    show story 016-73 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "Komatsu Beach is now officially owned by my fair lady, Joanne Marie Madison 'Maple' Mablethorpe."
    show story 016-76 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mvhana "Nyah~!?"
    mvhana "Trespassing? But we've been coming to the beach since, like, forever!"
    show story 016-74 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "Yeah, what she said!"
    mvtori "It's not fair! What kind of jerk wants to keep a beach all to themselves!?"
    show story 016-75 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "Hmph."
    adel "Indeed, the beach was previously made available to the general public under Master Komatsu's management..."
    show story 016-73 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "But now that it has been acquired by Lady Maple, all visitors are required to {b}pay a fee{/b} in order to enter the beach."
    show story 016-77 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mvtori "What the heck!?"
    mvtori "She's {i}charging{/i} people to use the beach!? That's so unfair!!!"
    show story 016-78 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvhana "Nya~ Nya~"
    mvhana "This puuurrrson is purrrre evil, I tell you! Nyah~!"
    show story 016-79 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "Be that as it may, rules are rules..."
    show story 016-80 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "...and it is my duty to enforce the rules laid out by my fair lady."
    show story 016-81 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "So leave now before I make you leave by force."
    show story 016-82 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "Rules, you say?"
    show story 016-83 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "Aren't you breaking a very important rule right now?"
    show story 016-84 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    adel "Eh?"
    adel "W-What are you talking about?"
    show story 016-85 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvhana "Nya~ Nya~"
    mvhana "The rules state that all visitors must come to the beach in a swimsuit..."
    show story 016-86 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvhana "And you're clearly not in a swimsuit, are you? Nyah~!"
    show story 016-82 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "Yeah, Miss."
    show story 016-83 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "You call yourself a maid and don't even know that much?"
    show story 016-84 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    adel "Eh!? N-No way..."
    show story 016-87 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "Ahem. I mean, I knew that... "
    show story 016-88 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "I was simply testing the locals on their knowledge of proper beach attire, is all."
    adel "And congratulations, you two passed the test."
    show story 016-89 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "*Sniff* *Sniff*"
    show story 016-90 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "N-Now if you will excuse me, I have... uh... important things to do..."
    show story 016-91 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    adel "But rest assured, I'll be back! Mark my words!"
    show story 016-92 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 016-93 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mvhana "..."
    mvtori "..."
    show story 016-94 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "Well, we better leave before she gets back, Makoto-kun."
    show story 016-95 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "The last thing I'd want is another lecture..."
    show story 016-96 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvhana "Nya~ Nya~"
    mvhana "Aye, [yel]Miss Kanae{/color} gives us enough of an earful..."
    show story 016-97 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvhana "If she finds out that we've been getting into trouble outside of school again, she'll give us detention for a month! Nyah~!"
    show story 016-98 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Geez, you girls... Learn to behave yourselves..."
    show story 016-94 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "Buh-bye! I'll send you some more of my homework to smash later!"
    show story 016-97 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvhana "Nya~ Nya~"
    mvhana "Until nya-ext time, Makoto-kun! Nyah~!"
    show story 016-99 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 016-100 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mako "..."
    mc "..."
    show story 016-101 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Well, that just happened..."
    show story 016-102 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You're quite the stud, aren't you, Makoto?"
    show story 016-103 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Sheesh, what a headache..."
    show story 016-104 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I get attention where I don't want it most..."
    show story 016-105 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Haha..."
    mc "So now that we're alone, we can finally talk together..."
    show story 016-106 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Am I right in assuming that {i}you{/i} were the mystery person who stopped by my house this morning and spoke to my [mil]?"
    show story 016-107 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Uh-huh..."
    show story 016-108 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I wanted to tell you that I almost have enough for my Scarlet Contract..."
    show story 016-109 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "But since you were asleep, I figured we could meet up at the beach instead. I was supposed to meet this [yel]Lady Maple{/color} or whatever here, anyway."
    show story 016-110 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...Enough for your Scarlet contract?"
    mc "That's by selling your family's hot springs and beach, right?"
    show story 016-111 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Y-Yeah..."
    show story 016-112 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "That was the only way. I don't regret it. This was all to save the Builders Guild."
    show story 016-110 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Makoto..."
    mc "You know, I've been thinking..."
    show story 016-113 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "The more I spend time with you, the more I seem to..."
    mc "...really like you."
    show story 016-114 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "[mc]...?"
    mako "W-What are you saying all of a sudden..."
    show story 016-115 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "What I'm trying to say is that..."
    show story 016-116 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Even if I don't control your Scarlet Contract... maybe with a little more time, it's possible that we..."
    show story 016-117 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    adel "I'm... back..."
    show story 016-118 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    adel "*Huff* *Huff*"
    show story 016-119 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    adel "Now where are you two little brats hiding!"
    adel "I'm not done scolding you yet!"
    show story 016-120 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "*GULP*"
    show story 016-121 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "(Holy elven milkers...)"
    show story 016-122 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    adel "KYAAAAHHH!!!"
    show story 016-124 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "W-Where do you think you're looking at, pervert!?"
    show story 016-123 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 016-122 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    adel "T-This... was the only swimsuit they had left that would fit me, okay!?"
    adel "A prim and proper maid like myself would never wear anything so lewd, otherwise!"
    show story 016-125 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "Now enough babbling and direct me to those two delinquents immediately!"
    show story 016-126 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mako "..."
    show story 016-127 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Er, Miss..."
    mako "The girls are already long gone..."
    show story 016-128 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    adel "Eh?"
    adel "A-Are you saying that I've come all this way for no reason?"
    show story 016-129 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "*Sniff* *Sniff*"
    show story 016-130 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "Forgive me Lady Maple, for I have failed you once again..."
    show story 016-131 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "There is only one thing left for me to do..."
    show story 016-132 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 016-133 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    with vpunch
    mc "What are you doing!?"
    show story 016-134 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    adel "I am not even worthy of being alive!"
    show story 016-135 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "Please, sirs! Take this blade and drive it upon my neck!"
    show story 016-136 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    adel "Perhaps my death will serve as a soothing afterthought for my lady once she learns of my shame..."
    show story 016-137 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "..."
    mc "..."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    $ renpy.end_replay()
    "Makoto has enough for her Scarlet Contract..."
    "I'll need to speak with Laureate to discuss further details with her..."
    "It's a terrible thought, knowing that she sacrificed so much for this to be done, but..."
    "...it only proved how serious Makoto was about saving the Builders Guild."
    play sound "audio/ding.mp3" volume 3
    "[yel]Dating has been unlocked at the beach!"
    $ adelmet = True
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    show screen tutorialscreen_08 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    while endgame != True:
        pause
    jump beachlabel_01



label ferr01_01:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3
    show story 014-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/ferry.mp3"
    mc "*Huff* *Huff"
    show story 014-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "It's no use, Ferry... I'm too exhausted to go any further..."
    show story 014-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Hmm..."
    ferr "At your current rate, you'll never become a proper knight for Her Highness, much less a qualified maid in Scarlet."
    show story 014-04 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "That's a bit harsh, Ferry..."
    show story 014-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "But you're right... I don't know what Laureate sees in me to make her think I'll be a good knight."
    show story 014-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "..."
    show story 014-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "We can rest here, if you'd like."
    ferr "I don't mind waiting for you to recover."
    show story 014-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Really?"
    mc "Thanks, Ferry..."
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 014-09 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "Ahh..."
    mc "My legs were going to fall off if we kept training."
    show story 014-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Take your time and rest, [mc]."
    ferr "The last thing I would want is for you to pick up an injury."
    show story 014-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    ferr "..."
    show story 014-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Hmm?"
    ferr "Why are you staring at me like that?"
    show story 014-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Nah, it's just..."
    mc "Well, when I first met you, you seemed awfully distant and unfriendly..."
    show story 014-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "But after spending more time together, I can see that you do have a caring side to you, after all."
    show story 014-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Hmph."
    ferr "Hate to break it to you but you are mistaken..."
    show story 014-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "I am simply selecting the most optimal choice to complete my mission."
    ferr "An injury here would only be detrimental toward further training."
    show story 014-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "In this line of business, one is not long for this world. You best remember that as you continue to serve Her Highness as her knight."
    show story 014-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "That's grim to hear, Ferry..."
    mc "But I guess it was an awkward thing for me to say in the first place..."
    show story 014-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    ferr "..."
    show story 014-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "<Target appears to be in distress...>"
    ferr "<Suggestion: Apologize to target...>"
    show story 014-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "..."
    show story 014-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "My apologies, [mc]... That was rude of me."
    show story 014-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "I just... don't quite process those types of thoughts very well."
    show story 014-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Ferry?"
    show story 014-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "...I don't know how to explain."
    ferr "I'm {i}different{/i} compared to other people."
    show story 014-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah, you certainly are."
    show story 014-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I don't know anyone who is as strong as you, Ferry."
    show story 014-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "No, what I mean to say is..."
    show story 014-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "...nevermind."
    show story 014-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "What's wrong?"
    show story 014-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "[mc]..."
    ferr "Can I trust you to keep a secret?"
    show story 014-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...Of course."
    show story 014-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Hmm..."
    ferr "[mc], I want your word..."
    show story 014-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "...because if you tell anyone, I'll definitely have to silence you permanently."
    ferr "And I promise that it'll be in the most elegant but brutal way possible."
    show story 014-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Yeesh..."
    mc "You know what, maybe I'm better off not knowing..."
    show story 014-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Hmm..."
    ferr "Then again, this would be an excellent opportunity to test your knightly vows."
    ferr "After all, a good knight must be capable of keeping his word."
    show story 014-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Geez..."
    mc "I promise I won't tell anyone, alright?"
    show story 014-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "The truth is, I'm not a normal human being, [mc]."
    ferr "I'm actually an [yel]Android{/color}, model CMBT-x90..."
    show story 014-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "On the outside, I appear to have flesh and bone..."
    show story 014-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "...but inside, my body contains gears and circuits that keep me running."
    show story 014-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "How is that even possible...?"
    mc "I mean, I always thought there was something odd about you, Ferry..."
    show story 014-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "But an android? That's very hard to believe..."
    mc "Who is capable of such technology?"
    show story 014-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "<Error 403...>"
    ferr "<Unable to disclose confidential information...>"
    show story 014-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Er, Ferry?"
    show story 014-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Apologies, [mc]..."
    ferr "But my system will not allow me to name the person who worked on me..."
    show story 014-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "This [yel]scientist{/color}, for whatever reason, wishes to remain anonymous."
    show story 014-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "That's alright..."
    mc "Either way, I'm amazed to have met you, Ferry."
    show story 014-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I can't say I have any android friends, y'know?"
    show story 014-30 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    ferr "...Friend?"
    ferr "I'm your... {i}friend{/i}, [mc]?"
    show story 014-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Of course..."
    mc "I mean, we've been spending a lot of time together, haven't we?"
    show story 014-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "How strange..."
    ferr "For some reason when you said that, my body felt... {i}tingly{/i}..."
    show story 014-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Perhaps my systems are undergoing maintenance again."
    ferr "Don't worry though, I'm feeling {i}normal{/i} now."
    show story 014-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Er..."
    show story 014-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "That's enough..."
    show story 014-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Are you ready to continue on with your training for tonight?"
    show story 014-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah, I'm good now..."
    mc "Though, I wish there was a place where we could go get drinks..."
    mc "I'm parched from all this exercise..."
    show story 014-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "That's to be expected..."
    ferr "According to my database, however, the closest convenience store operating at this hour is..."
    show story 014-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "... ... ..."
    show story 014-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "...four miles away."
    show story 014-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Four miles!?"
    mc "Geez, I'm better off just returning home to get water..."
    show story 014-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Fear not, [mc]... For a maid is always prepared for the worst..."
    show story 014-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "I have cold and refreshing water on me as we speak."
    show story 014-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "R-Really?"
    mc "Wow, you're amazing, Ferry! You really are the elite maid you say you are!"
    mc "Wait a second..."
    mc "Where are you hiding that water? I never see you bring anything to the park..."
    show story 014-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Allow me to explain..."
    show story 014-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "{size=22}You see, within the core of my body is a cooled condenser that operates alongside my evaporator unit to help regulate my body's internal temperature and keep my systems from overheating. During this process, moisture condensation invitably occurs alongside my evaporator coils as cold refrigerant surges through them. As heat is then drawn from the air, the moisture continues to condense. The result is clean water that falls down into a 'drain hole' where it is cooled and stored for future use. Of course, this water also runs through a septic tank that is personally fitted into my body to help purify and clean the water for the purpose of being used as a beverage in the case of dire emergencies."
    show story 014-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    ferr "..."
    show story 014-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Basically, my body has the function to store cold, clean water like a refrigerator."
    show story 014-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh, okay. That makes perfect sense."
    mc "Now how does one go about extracting that water...?"
    mc "*GULP*"
    with vpunch
    mc "D-Don't tell me that it comes out the way I think it does..."
    mc "...because this isn't that type of game."
    show story 014-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    ferr "How vulgar!"
    ferr "Androids have no need for a bathroom, in case that's what you were wondering!"
    show story 014-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Right..."
    show story 014-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Dispensing the liquid is a simple task..."
    show story 014-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "All you need to do is press your lips against mine, and I will distribute the water down your throat."
    show story 014-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "I-Isn't that the same as kissing!?"
    show story 014-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Kissing...?"
    ferr "Is that what this is?"
    show story 014-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Well, yeah..."
    mc "If two people press their lips together, that's a kiss no matter how you slice it."
    show story 014-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "I see..."
    ferr "How strange. I never thought of it that way."
    show story 014-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...?"
    mc "Ferry, has anyone ever kissed you before?"
    mc "You know, like on the lips?"
    show story 014-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Why would I want that?"
    show story 014-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Kissing is a pointless act. It serves no purpose except to spread germs."
    show story 014-40 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    show story 014-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Well, if you don't feel awkward about kissing, I suppose I shouldn't either."
    mc "After all, we're only doing this because I'm thirsty..."
    show story 014-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Alright, I'll have a drink out of you then, Ferry."
    mc "Here goes nothing..."
    show story 014-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    show ferr01_01_01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    pause
    ferr "Mmmf... mmmf..."
    mc "Mmm... mmm..."
    mc "(W-Whoa... water really is coming out of Ferry's mouth...)"
    ferr "Mmm... *slurp* ...mmm..."
    mc "..."
    mc "(Maybe it's just me...)"
    mc "(But I think Ferry is enjoying this...)"
    hide ferr01_01_01
    show story 014-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 014-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Ah..."
    ferr "What's wrong, [mc]? Why did you suddenly stop?"
    show story 014-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh, I'm good now..."
    mc "Thanks to you, I'm fully hydrated."
    show story 014-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "...I see."
    show story 014-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...You taste good though, Ferry."
    show story 014-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Er, I mean the water you provided is tasty."
    show story 014-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "..."
    show story 014-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "What's wrong?"
    mc "Did you want to continue kissing?"
    show story 014-53 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    ferr "!?"
    show story 014-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "H-How absurd."
    ferr "Don't be full of yourself, I only did this because you were parched."
    show story 014-55 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Er..."
    show story 014-56 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Then why are you still holding my hand..."
    show story 014-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Holding your hand?"
    show story 014-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "..."
    mc "..."
    show story 014-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "<Unknown error detected...>"
    show story 014-60 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "An error...?"
    show story 014-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "<Suspicious heat signals emanating within core...>"
    ferr "<Suggestion: Eliminate source of distress...>"
    show story 014-60 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "W-Whoa..."
    mc "You don't mean me, right?"
    show story 014-61 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Ugh..."
    ferr "[mc], we should call it a day."
    show story 014-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "For some reason, my body felt weird."
    ferr "I can only assume that there is internal damage to my processing unit."
    show story 014-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Um... if you say so..."
    show story 014-62 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 014-63 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    ferr "..."
    show story 014-64 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Forgive me for my lack of professionalism, but I'll be heading out now..."
    show story 014-65 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Have a good night, [mc]."
    show story 014-66 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Sure thing..."
    mc "We'll pick this up next time, okay Ferry?"
    show story 014-67 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "...next time?"
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/days.mp3"
    $ renpy.end_replay()
    jump parklabel_02



label sere01_01:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 019-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/estelle.mp3"
    este "..."
    show story 019-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 019-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Estelle, it's my turn to watch TV."
    mc "There's this very original anime involving a guy who dies and comes back to life as..."
    show story 019-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "Hush, [mc]!"
    este "Can't you see I'm watching Mao Mao?"
    show story 019-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oi, oi..."
    mc "I've been meaning to watch this series since it was announced!"
    mc "And you hogged the TV yesterday! It's only fair that I get my chance now!"
    show story 019-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Ugh, how annoying..."
    show story 019-07 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    este "[mil!c]!!! [mc] is pestering me again!!!"
    show story 019-08 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    silv "[mc], don't bother your [sil], dear."
    show story 019-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You little..."
    show story 019-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "By the way..."
    este "Have you put the {i}moves{/i} on Serena yet? She told me that you've been working with her at the store."
    show story 019-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "W-What do you mean!?"
    mc "We're just really good friends!"
    show story 019-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Oh, please..."
    este "I've seen the way you act when you're around her..."
    show story 019-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Everyone in the neighborhood knows that you have a crush on Serena."
    show story 019-13 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    silv "Very true."
    show story 019-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Y-You guys don't know what you're talking about...!"
    show story 019-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "And besides, I'm sure she doesn't think of me as anything more than a friend..."
    show story 019-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Geez, [mc]..."
    este "Serena won't be single forever, y'know?"
    show story 019-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Do you really want to enter that secret [oj]NTR route{/color} just because you're afraid to confess to her?"
    show story 019-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 019-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "You better tell her how you feel before another man comes around and snatches her away from you..."
    show story 019-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "In fact, you might want to do it now so that I can watch Mao Mao in peace."
    show story 019-18 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mc "(As hard as it is to admit, Estelle's right...)"
    mc "(If I don't tell Serena how I truly feel about her, I might end up regretting it for the rest of my life...)"
    show story 019-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "(Alright then! No more being a bitch! I'll go right up to Serena and tell her how much she means to me!)"
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3.0
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    play music "audio/days.mp3"
    jump livingroomlabel


label sere01_02:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 019-20 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/serena.mp3"
    mc "..."
    show story 019-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "(I told myself that I'd ask her out today, but...)"
    mc "(Why am I suddenly feeling nervous?)"
    show story 019-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "(Normally, I'm really comfortable with speaking to her...)"
    mc "(But everytime I think of Serena as anything more than a friend, I just freeze up...)"
    show story 019-22 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "You okay there, [mc]?"
    show story 019-23 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Huh?"
    mc "Oh, yeah. It's just been a slow day..."
    show story 019-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hehe..."
    show story 019-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Don't go slacking on me, [mc]. There's always something to do, even when there aren't any customers around."
    show story 019-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "For instance..."
    show story 019-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Take a look at the floor over there. You see the dust ball that needs picking up?"
    show story 019-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "R-Right..."
    mc "I'll get to it then..."
    show story 019-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "That's okay, [mc]..."
    show story 019-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "As your senpai here at the store, I'll show you how it's done."
    $ renpy.pause(.5, hard=True)
    show story 019-28 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "Now pay attention, [mc]..."
    sere "The trick to managing a store is to keep the place as clean and presentable as possible..."
    show story 019-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "No one wants to shop at a filthy store, right?"
    show story 019-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Huh?"
    mc "O-Oh yeah, sure..."
    show story 019-30-1 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "(I'm too busy staring at her ass to hear what she said...)"
    show story 019-31 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show sere01_02_01
    pause
    mc "..."
    mc "(Goddess, I wish I could see what's underneath...)"
    mc "(Azula said I'm a Valla right? Shouldn't I have some special powers like x-ray vision or something?)"
    mc "..."
    mc "(Fuck it, nothing beats the power of imagination...)"
    $ renpy.pause(.5, hard=True)
    hide sere01_02_01
    show story 019-32 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    show story 019-33 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "See here, [mc]?"
    sere "You're supposed to take your time and make sure you pick up the dirty bits..."
    sere "That's the best way to clean up, y'know? Wipe it up and down, all around..."
    show story 019-34 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mc "(T-The way her ass keeps swaying...)"
    mc "(My hands feel like they're moving on their own...)"
    mc "(It's triggering various primal impulses within me...)"
    menu:
        "Give her buns a squeeze..." if True:
            $ renpy.fix_rollback()
            show story 019-35 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            mc "..."
            mc "(Fuck it, I'm going for it...)"
            mc "(If she says anything, I'll just act like I'm leaning in for a closer look.)"
            show story 019-36 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "(Yeah, that'll definitely work... I'm such a genius.)"
            mc "(It's just a light touch, anyway... I bet she won't even notice a thing...)"
            mc "(Yup, yup... Definitely not sexual harassment or anything...)"
            show story 019-37 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "(Just got to be extra careful though...)"
            mc "(I don't want Serena to see my degenerate side...)"
            $ renpy.pause(.5, hard=True)
            show story 019-38 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            show story 019-39 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            with vpunch
            sere "...!?"
            show story 019-40 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "(Is he... touching my butt?)"
            show story 019-41 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "(Oh, [mc]...)"
            show story 019-42 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "(If it's {i}you{/i}, I don't mind...)"
            $ renpy.pause(.5, hard=True)
            scene black with Dissolve(1.5)
            $ renpy.pause(1.5, hard=True)
            "Sensing that her body was tensing up, I immediatelly pulled my fingers away..."
            "For some reason, it felt as though she knew that I was molesting her..."
            "But if that were the case, why didn't she say anything?"
            $ renpy.pause(1, hard=True)
        "Resist primal urges..." if True:
            $ renpy.fix_rollback()
            mc "..."
            show story 019-31 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            mc "(It's too risky...)"
            $ renpy.pause(.5, hard=True)
            scene black with Dissolve(1.5)
            $ renpy.pause(1.5, hard=True)
    stop music fadeout 3.0
    "The atmosphere became awkward between Serena and I..."
    "In the end, I wasn't able to ask her out on a date..."
    $ renpy.end_replay()
    $ renpy.pause(.5, hard=True)
    call charwork ("serena_overtime")
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump streetlabel_01

label sere02_01:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 020-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    show story 020-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I think I'm a genius..."
    show story 020-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I've figured out the best way to express my true feelings for Serena without having to tell her in person..."
    show story 020-04 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "Behold... the awesome power of the {b}LOVE LETTER{/b}!!!"
    show story 020-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Once she reads this, my future with her is set..."
    show story 020-06 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "Hiya, [mc]!"
    sere "What's with that weird smirk on your face?"
    $ renpy.pause(.5, hard=True)
    show story 020-07 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play music "audio/serena.mp3"
    mc "Oh, Serena..."
    mc "Just the person I wanted to see..."
    show story 020-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "You're up early..."
    show story 020-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "What? Were you waiting for me before work or something?"
    show story 020-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(D-Damn, I'm choking up again...)"
    mc "(She's right there... all I need to do is give her my letter...)"
    mc "(No, wait... What if she doesn't like me? What if she thinks my letter is stupid?)"
    show story 020-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Eh?"
    sere "[mc], what's that in your hand?"
    show story 020-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Is that an invitation to join the ranks of a certain popular 'fighting' game!?"
    show story 020-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "S-Serena, there's something I want to give you!"
    mc "It's a letter for your eyes only! To show how much you mean to..."
    show story 020-14 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mvtori "BWAHAHAHAHAHAHA!!!"
    mvtori "It was just so lame that I wanted to {i}puke{/i}!!!"
    show story 020-15 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mvhana "Nyaaah~?"
    mvhana "He really tried that?"
    show story 020-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "Uh-huh..."
    mvtori "That dork from the academy across the street really gave me a {b}LOVE LETTER{/b}!!!"
    show story 020-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "He slipped it into my shoe box, thinking I wouldn't notice..."
    show story 020-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvhana "Nya~ that's so lame..."
    show story 020-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "I know right?"
    show story 020-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "Love letters are such {i}faux pas{/i}... Only geeks and losers have the nerve to try something as old-fashioned as that!"
    show story 020-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvhana "Nya~ Nya~"
    mvhana "You're right as always, Tori!"
    show story 020-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "Now if you {i}really{/i} want to impress a girl, you need to show her your {b}masculine{/b} side!"
    show story 020-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "You know, walk right up to her... take her hand... and ask her out!"
    show story 020-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "None of that lame-beta-pussy shit, y'know!?"
    show story 020-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvhana "Nya~ Nya~"
    mvhana "Spineless guys are the worst!"
    show story 020-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvhana "But what did you do with the letter after you were done with it?"
    show story 020-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "I gave it to my cat to tear it up, of course..."
    show story 020-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "He was spilling his guts, telling me how I was {b}the one{/b} and that it was love at first sight..."
    show story 020-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "It was so disgusting that the letter needed to be snuffed out from existence."
    show story 020-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvhana "Nyahaha~!"
    mvtori "Bwahahaha!"
    $ renpy.pause(.5, hard=True)
    show story 020-21 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "..."
    show story 020-22 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "Geez, schoolgirls sure are noisy nowadays, aren't they?"
    show story 020-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "(S-Shit, I knew this was a stupid idea...!)"
    mc "(I can't believe I spent the entire night trying to come up with the right words for her in my letter...!)"
    show story 020-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Er..."
    sere "[mc], wasn't there something you wanted to give me?"
    show story 020-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 020-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "N-No, not at all...!"
    mc "That piece of paper is trash! It belongs in the bin!"
    show story 020-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Oh..."
    show story 020-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(Damnit, those girls are right...)"
    mc "(Serena doesn't want a loser! She wants a {b}man{/b}!)"
    mc "(I'm going to do it! I'm going to ask her out on a date!)"
    $ renpy.pause(.5, hard=True)
    show story 020-27 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "S-SERENA-SAN!!!"
    mc "THERE'S SOMETHING I'VE BEEN MEANING TO ASK YOU EVER SINCE WE WERE LITTLE!!!"
    show story 020-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Eh!?"
    sere "[mc], w-what are you doin'!?"
    show story 020-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Oh, geez... People are staring at us..."
    show story 020-27 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "I KNOW IT'S SUDDEN, BUT..."
    mc "I'D BE HONORED IF YOU'D ALLOW ME TO TAKE YOU OUT SOMEWHERE!!!"
    show story 020-30 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    sere "EEEHHH!?"
    sere "A-A confession!?"
    show story 020-31 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mc "(There I said it! I can't go back now!)"
    mc "(What's the worst she can say to me?)"
    mc "(I definitely won't jump off my roof if she rejects me... Well, probably not...)"
    show story 020-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "[mc], c-could it be..."
    sere "That you're asking me out on a {b}date{/b}!?"
    show story 020-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "... ..."
    mc "... ... ..."
    show story 020-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "A... date?"
    with vpunch
    mc "N-Not at all!"
    mc "I'm just asking if, you know, you had some free time... maybe we could get some lunch or something..."
    show story 020-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Oh, geez... So this won't be a date, after all?"
    sere "You got me all flustered for nothing..."
    show story 020-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(I think I fucked up...)"
    show story 020-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Er, well, I guess I don't mind..."
    show story 020-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "We can go ahead and grab a quick bite during my lunch break..."
    show story 020-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "So that's a yes?"
    show story 020-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Well, yeah..."
    show story 020-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I mean, it's just lunch, right? I don't mind grabbing a bite with you..."
    show story 020-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Anyway, I'm going to open the store..."
    show story 020-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "See you later, [mc]."
    show story 020-42 with Dissolve(1)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    show story 020-43 with Dissolve(1)
    $ renpy.pause(1.5, hard=True)
    with vpunch
    mc "WOOO!!!"
    mc "She said {i}YES{/i}!!!"
    mc "I'm the happiest man in the world!!!"
    show story 020-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "This is great..."
    mc "Now, I have to make everything perfect... I want to show Serena a good time..."
    show story 020-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm... Now how should I go about that?"
    show story 020-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Maybe I should ask [mil!c]... I mean, she's been in relationships before, right?"
    $ renpy.pause(1, hard=True)
    $ renpy.end_replay()
    stop music fadeout 3.0
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    play music "audio/days.mp3"
    jump streetlabel_01

label sere02_02:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 020-47 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/silvia.mp3"
    silv "..."
    show story 020-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Good afternoon, [mc]..."
    show story 020-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "[mil!c]..."
    mc "Can I ask you something?"
    show story 020-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Of course, dear..."
    silv "What's on your mind?"
    show story 020-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You see, there's this girl I know..."
    mc "I asked her out on a date and I was wondering if you had any ideas for where we could go..."
    show story 020-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Oh, my..."
    silv "Who's the lucky lady that seduced my little man's heart?"
    show story 020-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Is it someone I know? You have been surrounding yourself with a number of cute girls recently..."
    show story 020-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "[mil!c]! That's not important!"
    show story 020-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "It's Serena, isn't it?"
    show story 020-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "I know you've had a crush on her since you were little..."
    show story 020-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "[mil!c], come on!"
    mc "I need a place to take her {i}quick{/i}! There's not a lot of time left!"
    show story 020-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hehe..."
    show story 020-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Well, there is that new cafe that opened up in the area recently..."
    show story 020-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "[yel]Evergarden Cafe{/color}... I believe it's called..."
    show story 020-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "It's ran by a [yel]maid{/color} just around the corner... You can't miss it..."
    show story 020-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...A cafe?"
    mc "That sounds perfect, [mil!c]!"
    show story 020-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hehe... Good luck, dear..."
    stop music fadeout 3
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    play music "audio/days.mp3"
    jump livingroomlabel

label sere02_03:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 020-54 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    $ renpy.movie_cutscene("images/videos/sere02_03_01.webm", delay=None, loops=0, stop_music=False)
    mc "..."
    mc "Huh? Wasn't that..."
    show story 020-55 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play music "audio/ferry.mp3"
    mc "Ferry?"
    show story 020-56 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "...?"
    mc "What brings you here?"
    show story 020-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Good afternoon, [mc]."
    show story 020-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "It's a pleasure to see you at this time of day."
    show story 020-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah, usually I see you at night..."
    mc "Is Laureate with you?"
    show story 020-61 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Negative..."
    show story 020-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "As I am currently undergoing maintenance, Her Highness believed it would be best to take time off for myself."
    show story 020-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I see..."
    mc "Hold on, why did you decide to come all the way here?"
    show story 020-60 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "..."
    show story 020-61 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "No particular reason."
    show story 020-60 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm..."
    mc "You were staring at that new cafe just now, weren't you?"
    mc "[yel]Evergarden Cafe{/color}...? I was just about to head there myself..."
    show story 020-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "You are mistaken..."
    show story 020-61 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "I don't care what goes on inside that cafe..."
    ferr "...nor am I interested in the [yel]maid{/color} who works there."
    show story 020-60 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(I don't think she's being entirely honest...)"
    show story 020-61 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Anyway..."
    ferr "I do believe I hear Her Highness calling my name..."
    show story 020-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Pretend you never saw me loitering here, [mc]."
    show story 020-56 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Huh? But I don't hear anyone..."
    show story 020-62 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Farewell..."
    show story 020-63 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 020-64 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mc "She's really fast..."
    mc "Oh, right...!"
    mc "It's about time for my date! I have to go meet up with Serena!"
    $ renpy.pause(1, hard=True)
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 020-65 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    sere "..."
    show story 020-66 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "[mc], what's going on?"
    show story 020-67 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I thought we were just going out for a quick bite..."
    show story 020-68 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "What do you mean?"
    mc "This {i}is{/i} for a quick bite."
    show story 020-67 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Er..."
    sere "I thought you meant something like hot dogs or a burger..."
    show story 020-66 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "...not a place as fancy as this."
    show story 020-69 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm... That's weird..."
    mc "Is this place even open? There aren't any customers around..."
    show story 020-70 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    sere "[mc], are you even listening to me!?"
    show story 020-66 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I can't keep the store closed for too long..."
    show story 020-67 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "And more importantly, the reason why this place has no customers is because..."
    show story 020-65 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mv2 "Oh my..."
    mv2 "It appears we have guests..."
    show story 020-71 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play music "audio/violetta.mp3"
    mv2 "..."
    show story 020-72 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "Welcome home, {i}Young Master{/i}..."
    show story 020-73 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "It will be my honor to serve you today..."
    show story 020-74 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "M-Master!?"
    show story 020-75 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Eh!?"
    sere "[mc], you cheater!"
    show story 020-76 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "Oh, my apologies for the misunderstanding..."
    show story 020-77 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "It's my policy to welcome every guest at my cafe as {b}Master{/b}..."
    show story 020-76 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "Speaking of which..."
    show story 020-77 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "Allow me to cordially welcome you two to my cafe, the one and only Evergarden..."
    show story 020-89 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "...Ca...fe."
    show story 020-78 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "..."
    mv2 "... ..."
    mv2 "... ... ..."
    show story 020-79 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mv2 "Zzz..."
    sere "..."
    sere "Er, is she asleep?"
    mc "..."
    with vpunch
    mc "Wake up!"
    show story 020-80 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mv2 "..."
    show story 020-81 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "Pardon my rudeness, Young Master..."
    show story 020-82 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "...but what was your name again?"
    show story 020-83 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I'm [mc], and this here is Serena..."
    mc "...also, we've never met before."
    show story 020-81 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "Is that so?"
    show story 020-84 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "In that case, allow me to formally introduce myself..."
    show story 020-85 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    viol "You may address me as [yel]Violetta{/color}, the humble maid who owns this fine estabalish..."
    show story 020-90 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    viol "...ment."
    show story 020-79 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    viol "Zzz..."
    sere "..."
    mc "..."
    with vpunch
    mc "Wake up!"
    show story 020-80 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    viol "..."
    show story 020-82 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    viol "Oh dear, oh dear... My apologies, Young Master..."
    show story 020-81 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    viol "What were we talking about again?"
    show story 020-83 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Er..."
    mc "You were just about to show us our seats..."
    show story 020-84 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    viol "Yes, yes... That's right..."
    show story 020-86 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    viol "Please follow me..."
    show story 020-87 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    viol "I have a lovely little spot for {b}couples{/b} such as yourselves..."
    show story 020-88 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    sere "Eh?"
    sere "C-Couples!?"
    with vpunch
    mc "R-Right! We're just friends!"
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 020-91 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    sere "..."
    show story 020-92 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Psst... [mc], I think we should leave..."
    show story 020-93 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Huh?"
    mc "But we just got here..."
    show story 020-94 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I know, but..."
    show story 020-92 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I-I can't keep the store closed for too long..."
    show story 020-95 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I was expecting something quick for lunch, you know? Nothing overly fancy like this..."
    show story 020-91 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(Shit...)"
    mc "(Serena doesn't look like she's having a good time...)"
    mc "(I need to say something to impress her...)"
    show story 020-93 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Pfft... You think this place is fancy?"
    with vpunch
    mc "I dine in restaurants like this all the time!"
    show story 020-94 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "[mc], that's not important..."
    show story 020-92 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I've also heard mixed reviews about Evergarden Cafe..."
    show story 020-96 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Apparently, the service here is really {i}slow{/i}..."
    show story 020-97 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    viol "Zzz..."
    mc "..."
    sere "..."
    show story 020-96 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "But more importantly..."
    show story 020-92 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "This place is {i}really{/i} expensive..."
    show story 020-95 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I don't think I can afford to eat here..."
    show story 020-93 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(I'm the man here, I got to show Serena my good side...)"
    mc "..."
    with vpunch
    mc "Don't worry about a thing, Serena!"
    mc "It was my idea to come here in the first place! So it's only fair that I treat you!"
    show story 020-98 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Eh?"
    sere "You mean..."
    show story 020-99 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "That's right!"
    mc "I'll pay for everything, so you can just focus on eating as much as you want!"
    mc "Think of today as an all-you-can-eat buffet!"
    show story 020-100 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Oh boy, [mc]!"
    sere "You're the best!"
    show story 020-99 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Heh..."
    mc "Now let's take a look at the menu..."
    show story 020-101 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    pause
    mc "..."
    with vpunch
    mc "(H-HOLY HOT HELL!?)"
    mc "(THESE PRICES ARE INSANE!!!)"
    show story 020-102 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "Oooh!"
    sere "The broiled filet mignon sounds tasty..."
    show story 020-103 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Or maybe I should go with the sticky honey roast...."
    show story 020-104 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "You know what!"
    show story 020-105 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "If you're paying! I'll just get both!"
    show story 020-106 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "O-On second thought, maybe you're right... maybe we should go somewhere else..."
    mc "Y-You said that you wanted hot dogs, right?"
    show story 020-107 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    viol "Pardon my rudeness, Young Master... But if I may interject..."
    show story 020-108 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    viol "As a licensed and honorable maid of Scarlet, my culinary skills boast a wide range of specialty meals including these 'hot dogs' that you desire..."
    show story 020-109 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    viol "The sausages used are of the highest grade of quality, finely cultivated by the most reputable butchers Scarlet has to offer..."
    show story 020-107 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    viol "Naturally, top ingredients require top dollar... as reflected upon by the price!"
    show story 020-111 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Oooh, that does sound tasty!"
    show story 020-110 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I'll try one of those, too! Along with a plate of sticky honey roast and filet mignon!"
    show story 020-109 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    viol "Excellent choice, my lady..."
    show story 020-112 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    viol "And what would you like to order, Young Master?"
    show story 020-113 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I-I'll just have a croissant..."
    $ renpy.pause(1, hard=True)
    stop music fadeout 3.0
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    "It took hours for Violetta to finally finish our food..."
    "When I walked over to the kitchen to see what was going on, I found her fast asleep..."
    "There didn't seem to be anyone else working at the cafe except her..."
    "By the time we were ready to leave, the sun had already set..."
    "In the end, the food was delicious but the prices made the visit unbearable..."
    if (money >= 500):
        play sound "audio/coins.mp3" volume 3
        show love_viol at up_happy
        "[yel]You paid Violetta $500."
        $ money -= 500
        hide love_viol at up_happy
    elif True:
        play sound "audio/coins.mp3" volume 3
        show love_viol at up_happy
        "[yel]You paid Violetta $[money]."
        $ money = 0
        hide love_viol at up_happy
    play sound "audio/ding.mp3" volume 3
    "[yel]You can now purchase 'Parfaits' from Violetta... while she's awake..."
    if (inventory_tutorial == False):
        $ inventory_tutorial = True
        play sound "audio/ding.mp3" volume 3
        show screen_tutorial_06 with Dissolve(1.5)
        $ renpy.pause(1.5, hard=True)
        pause
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 020-114 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/relax.mp3"
    mc "..."
    mc "(That costed me a lot of money...)"
    mc "(I don't know if I can continue to take Serena to fancy places like that in the future...)"
    show story 020-115 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    mc "..."
    mc "(Serena doesn't look very happy...)"
    show story 020-116 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Er..."
    mc "Did you not have a good time, Serena?"
    mc "You looked like you were enjoying yourself earlier..."
    show story 020-117 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Oh, I had a ton of fun, [mc]..."
    sere "Thank you for bringing me with you."
    show story 020-116 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "If you had a good time, why the long face?"
    show story 020-118 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "*Sigh*"
    sere "Because it's already night..."
    show story 020-119 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "The store was closed for basically the entire day, so I lost a ton of business..."
    show story 020-116 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Where has your grandfather been, Serena?"
    mc "You're a young woman... it's not fair for him to make you have to take care of his store on your own."
    show story 020-115 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    mc "Serena..."
    mc "I know how important he is to you, but you can't continue to let him dictate your..."
    show story 020-120 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    sere "[mc], stop it..."
    show story 020-118 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Grandpa died last year..."
    show story 020-116 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 020-119 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "The store belongs solely to me now..."
    show story 020-118 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I stopped seeing you around, so I guess you weren't aware..."
    show story 020-116 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I'm sorry, Serena... I really didn't know..."
    show story 020-117 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "That's okay..."
    sere "But I really wish you were around to comfort me, though..."
    show story 020-118 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "He really liked you, you know?"
    show story 020-119 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Even Estelle and your [mil] sent their condolences..."
    show story 020-114 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(I completely ruined the mood...)"
    mc "(Serena loved her grandfather... He was such a friendly person...)"
    show story 020-117 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Anyway..."
    sere "I should probably get going..."
    show story 020-116 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh..."
    mc "Let me walk you home at least, Serena..."
    show story 020-119 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "No, not today..."
    sere "There's somewhere else I need to be..."
    show story 020-117 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "See you later, [mc]..."
    show story 020-121 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 020-122 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    show story 020-123 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I ruined everything, didn't I?"
    mc "I can't help but think I was being insensitive..."
    mc "Serena must really hate me now..."
    $ renpy.end_replay()
    stop music fadeout 3
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/days.mp3"
    jump streetlabel_01


label sere03_01:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 021-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    show story 021-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Serena's been avoiding me lately..."
    mc "I feel bad... I wonder if it's because of what I said the other night..."
    show story 021-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Speak of the devil..."
    mc "I should probably go try and make up with her..."
    $ renpy.pause(.5, hard=True)
    show story 021-04 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play music "audio/serena.mp3"
    mc "Good morning, Serena!"
    mc "How's it hanging?"
    show story 021-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Is that you, [mc]?"
    show story 021-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Sorry, I'm a bit busy right now..."
    show story 021-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I was thinking about the other night..."
    mc "You know, after we went to that cafe?"
    show story 021-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Oh?"
    sere "Don't worry about it, [mc]..."
    show story 021-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Well, lately it feels like you've been avoiding me..."
    mc "We rarely walk home together after work anymore..."
    show story 021-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Ah..."
    sere "W-Well, I've been busy at night... Not much I can do about that..."
    show story 021-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Everything alright?"
    mc "Anything you want to talk to me about?"
    show story 021-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Actually..."
    sere "Now that you mention it, there's something {i}important{/i} I have to discuss with you..."
    show story 021-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Just give me a minute to put these boxes inside the store first..."
    mc "..."
    with vpunch
    mc "S-Something {i}important{/i}!?"
    show story 021-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Y-Yeah, it's regarding work..."
    sere "Do you mind opening the door for me and stepping aside?"
    sere "These boxes are heavy..."
    show story 021-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I knew it was a bad idea to go to that stupid cafe..."
    mc "It's all [mil!c]'s fault..."
    mc "She's the one who recommended that we go there..."
    show story 021-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    sere "[mc], are you even listening!?"
    sere "Move so I can..."
    show story 021-08 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    sere "W-Whoa!!!"
    show story 021-09 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "Serena!"
    mc "I'll save you!"
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play sound "audio/fall.mp3" volume 3
    $ renpy.pause(1.5, hard=True)
    show story 021-10 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    sere "Ouch..."
    show story 021-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Thanks for breaking my fall, [mc]..."
    show story 021-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Are you alright?"
    show story 021-13 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "MMMRRR...!"
    show story 021-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Eh?"
    sere "[mc], speak up... I can't understand what you're saying..."
    show story 021-15 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "MMMMRRR...!!! YYYMMMRRR!!! AAAMMMSSS!!!"
    show story 021-16 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "S-Stop moving your mouth so much..."
    show story 021-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "It feels weird..."
    show story 021-18 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "GMMTTT...!!! OOOMMMFFF!!! MMMRRREEE!!!"
    show story 021-19 with Dissolve(0.5)
    $ renpy.pause(0.5, hard=True)
    show sere03_01_01
    pause
    sere "Ahn..."
    sere "O-On second thought, don't stop..."
    sere "Keep moving... your lips..."
    mc "MMMRRRMMMPPPHHH!!!"
    sere "Ah, yes..."
    sere "Right there, [mc]... It's perfect...!"
    stop music fadeout 3.0
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    "Serena eventually got off me... after a few minutes..."
    "I'd never admit it to her, but it felt pretty good to have her sit on my face like that..."
    $ renpy.pause(1, hard=True)
    show story 021-20 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    sere "..."
    show story 021-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Great, now my goods and all over the place..."
    show story 021-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "*Sigh* I got even more work to do..."
    show story 021-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I'm sorry, Serena..."
    mc "I didn't mean to distract you like that."
    show story 021-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "That's okay..."
    show story 021-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "It was an accident."
    show story 021-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hey, let me help out around the store..."
    mc "I know I wasn't supposed to come today, but..."
    show story 021-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    show story 021-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "[mc], that's actually what I wanted to talk to you about..."
    show story 021-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...?"
    show story 021-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Starting today, I don't want to see you in the store again..."
    show story 021-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "...not as a colleague, I mean."
    show story 021-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I don't understand."
    show story 021-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I'm saying you're {b}fired{/b}, [mc]..."
    show story 021-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I can't afford to keep you around the store anymore."
    show story 021-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "That's why I have to let you go."
    show story 021-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Is it because of what I..."
    show story 021-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "[mc], ask yourself this..."
    show story 021-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Why did you want to come work with me in the first place?"
    show story 021-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Because of [mil!c] and Estelle."
    mc "I needed money for their Scarlet Contracts..."
    show story 021-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "That's right..."
    show story 021-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "And now that you have them back, you don't have any reason to be here anymore."
    show story 021-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "That's not true, Serena..."
    mc "I enjoy spending time with you..."
    show story 021-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    mc "..."
    mc "Didn't you enjoy spending time with me?"
    show story 021-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Why'd you have to go and say something like that...?"
    show story 021-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Serena, there's something I've been meaning to tell you since we were little..."
    mc "You see, I've always lo..."
    show story 021-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "[mc]..."
    show story 021-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Please don't finish that sentence..."
    show story 021-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 021-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I'm going to clean up and open the store now..."
    show story 021-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "But I'd appreciate it if you left me alone..."
    show story 021-33 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    $ renpy.pause(1, hard=True)
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    "I returned back home shortly afterward..."
    "Although there were no physical wounds on my body, I could feel a sharp aching pain in my chest..."
    "Serena, the girl whom I had a crush on since I was little, did not share the same affection for me..."
    $ renpy.end_replay()
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump mcroomlabel


label sere03_02:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 021-34 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/wind.mp3" volume 2
    mc "..."
    show story 021-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Sure is a beautiful night..."
    mc "Was the moon always this bright?"
    show story 021-36 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "*GLUG* *GLUG*"
    show story 021-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Ahhh..."
    show story 021-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "The girl I like despises me..."
    mc "Is there any point in going on?"
    show story 021-37 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    este "Hey, [mc]!"
    este "Stop being so edgy and get down from there!"
    silv "Leave him be, Estelle!"
    silv "This is just a phase he's going through..."
    silv "It happens to every young man with a broken heart..."
    show story 021-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "*Sigh*"
    show story 021-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "As if those two could understand my struggle..."
    mc "I won't ever meet another girl like Serena again..."
    show story 021-38 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Huh? Isn't that..."
    show story 021-39 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    with vpunch
    mc "Is that Serena!?"
    mc "W-What's she wearing!?"
    mc "It looks like... she's all dressed up to go on a date!?"
    show story 021-40 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 021-38 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    show story 021-36 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "*GLUG* *GLUG*"
    show story 021-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Makes sense... A girl as beautiful as Serena probably gets asked out by Chads every day..."
    show story 021-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "But what part of that asshole is better than me, huh!?"
    mc "I bet I'm better looking! I bet my dick is bigger than his!"
    show story 021-36 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "*GLUG* *GLUG*"
    show story 021-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu:
        "Tail her..." if True:
            $ renpy.fix_rollback()
            show story 021-35 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            show story 021-41 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Alright, I'm going to follow her..."
            mc "But only because I'm curious of the asshole she's seeing..."
        "Keep drinking..." if True:
            $ renpy.fix_rollback()
            show story 021-36 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            mc "*GLUG* *GLUG*"
            show story 021-35 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            mc "You know what? So what if she's going out with someone..."
            mc "I don't care about her... There's plenty of other girls out there waiting for me..."
            show story 021-41 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "..."
            mc "Alright, I'll follow her..."
            mc "...but only because I want to see the asshole she's going out with."
    $ renpy.pause(1, hard=True)
    stop music fadeout 3.0
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "I carefully followed Serena, making sure not to be spotted..."
    "She seemed to be going in the direction of City Hall..."
    $ renpy.pause(1.5, hard=True)
    show story 021-42 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/serena.mp3"
    sere "..."
    show story 021-43 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mc "(Looks like she's stopping here...)"
    mc "(Who could she be waiting for?)"
    show story 021-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "(Oh shit! Someone's coming!)"
    mc "(That must be the bastard she's meeting!)"
    show story 021-44 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    gen6 "..."
    show story 021-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen6 "You're late."
    show story 021-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Sorry..."
    show story 021-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "It took longer than I thought to..."
    show story 021-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    gen6 "I don't want to hear your excuses..."
    gen6 "If you want to work for me, you sure as hell better be on time."
    show story 021-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Y-Yes, sir..."
    show story 021-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen6 "Hmm, whatever..."
    gen6 "Hold the sign up..."
    show story 021-49 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "Like this?"
    show story 021-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen6 "Right..."
    gen6 "Now repeat after me..."
    show story 021-51 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    gen6 "Maple's Pizzeria! So good, you'll swallow every cheesy bite!"
    gen6 "...Because if it ain't Maple's pizza, it ain't real pizza!"
    show story 021-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(W-What the hell is he saying?)"
    show story 021-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Er..."
    show story 021-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Maple's Pizzeria. So good you'll swallow every meaty bite."
    sere "...Because if it ain't Maple's pizza, it ain't real pizza."
    show story 021-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen6 "*Sigh*"
    gen6 "You rookies piss me off..."
    show story 021-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "W-What did I do wrong?"
    show story 021-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    gen6 "It's every {b}cheesy{/b} bite! Not every {b}meaty{/b} bite!"
    gen6 "And you need to say it with more passion in your voice! More emotion~! More fervor~!"
    show story 021-51 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    gen6 "MAPLE'S PIZZERIA!!! SO GOOD, YOU'LL SWALLOW EVERY CHEESY BITE!!!"
    gen6 "...BECAUSE IF IT AIN'T MAPLE'S PIZZA!!! IT AIN'T REAL PIZZA!!!"
    show story 021-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen6 "See? Like that!"
    show story 021-55 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Geez..."
    sere "Maybe I'm not suited for this job after all..."
    show story 021-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen6 "Hmm..."
    gen6 "You know what, I never realized how much of a {i}cutie{/i} you are up close..."
    show story 021-56 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen6 "How about it? I can think of a much better job for you than the pizzeria."
    show story 021-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    sere "Excuse me...!?"
    show story 021-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I already have a {b}boyfriend{/b}..."
    show story 021-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 021-60 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen6 "Is that so?"
    gen6 "Well, he must not be taking very good care of you if you have to work this late at night."
    show story 021-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu:
        "Jump in to defend Serena..." if True:
            $ renpy.fix_rollback()
            jump sere03_02_01
        "Continue watching from a distance..." if True:
            $ renpy.fix_rollback()
            show story 021-57 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Well, if he were around..."
            show story 021-61 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "He'd jump right here and kick your butt for even looking at me funny!"
            show story 021-57 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Uh-huh! That's the sort of man he is! He'll protect his friends and family until the bitter end!"
            show story 021-60 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            gen6 "Now, now... Don't be like that..."
            gen6 "You said that you needed money, right?"
            show story 021-62 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            gen6 "I'm not looking for anything permanent... And there's a love hotel right over there..."
    show story 021-63 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu:
        "Jump in to defend Serena..." if True:
            $ renpy.fix_rollback()
            jump sere03_02_01
        "Continue watching from a distance..." if True:
            $ renpy.fix_rollback()
            show story 021-59 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "..."
            show story 021-57 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Didn't you hear what I just said!?"
            show story 021-61 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Back off before I send my boyfriend at you!"
            show story 021-54 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            gen6 "Hah!"
            gen6 "You think you can fool me? I bet you don't even have a boyfriend!"
            gen6 "Because if you did, he'd swoop in right now and protect you!"
            show story 021-64 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "..."
            show story 021-56 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            gen6 "Don't be shy, sweetheart. I promise you'll enjoy it as much as I will."
    show story 021-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu:
        "Jump in and defend Serena..." if True:
            $ renpy.fix_rollback()
            jump sere03_02_01
        "Continue watching from a distance..." if True:
            $ renpy.fix_rollback()
            sere "..."
            show story 021-65 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "You know what!"
            show story 021-66 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            with vpunch
            sere "Screw you, asshole!"
            show story 021-67 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "I don't need a boyfriend to protect me from trash like you!"
            show story 021-68 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            gen6 "Oi, Oi!"
            gen6 "What do you think you're doing!?"
            show story 021-69 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "I'm a strong, independent woman who don't need no man!"
            show story 021-70 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            with vpunch
            play sound "audio/explosion.mp3" volume 3
            sere "HIII-YAAAAHHH!!!"
            "*BONK*"
            play sound "audio/fall.mp3" volume 3
            show story 021-71 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "*Huff* *Huff*"
            show story 021-72 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            mc "..."
            show story 021-73 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            with vpunch
            mc "Way to go, Serena!!!"
            mc "Where did that come from!?"
            show story 021-74 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "Eh?"
            sere "[mc], is that you?"
            show story 021-75 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            sere "W-Wait, did you really just see all that and not do anything...?"
            show story 021-76 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Let's get out of here quick before he wakes up!"
    $ renpy.pause(1, hard=True)
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    jump sere03_02_02


label sere03_02_01:

    show story 021-77 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    show story 021-78 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "Hey asshole! What do you think you're doing!?"
    show story 021-79 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    sere "Eh!?"
    sere "[mc], what are you doing here!?"
    show story 021-80 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen6 "Hey! Who the hell is this homeless man!?"
    gen6 "He smells like he's been drinking all night!"
    show story 021-81 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "H-Him...?"
    sere "Er... he's my..."
    show story 021-82 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "I'm her {b}BOYFRIEND{/b}!!!"
    show story 021-83 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "[mc]..."
    show story 021-84 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "HYYYUUUTTT!!!"
    show story 021-85 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play sound "audio/explosion.mp3" volume 3
    "*BONK*"
    show story 021-86 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play sound "audio/fall.mp3" volume 3
    sere "..."
    mc "..."
    show story 021-87 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "He's down for the count..."
    mc "Let's get out of here, Serena..."
    $ renpy.pause(1, hard=True)
    jump sere03_02_02

label sere03_02_02:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 021-88 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    sere "Whew..."
    show story 021-89 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I think we lost him..."
    show story 021-90 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Nevermind that..."
    mc "What were you doing with that creep?"
    show story 021-88 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Oh..."
    show story 021-91 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "That was my manager... from my other job..."
    show story 021-89 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Well, I guess he's my ex-manager now..."
    show story 021-92 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 021-93 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Serena, why are you working a second job?"
    mc "Is that the reason why you stopped walking home with me?"
    show story 021-88 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    sere "You don't understand, [mc]..."
    show story 021-90 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Try me..."
    show story 021-91 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "*Sigh*"
    sere "Alright then..."
    show story 021-89 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "The truth is, I've been having some financial difficulties..."
    show story 021-88 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "That's the reason why, you know, I had to let you off the store..."
    show story 021-91 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I just couldn't afford to keep paying your wages..."
    show story 021-93 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Serena..."
    show story 021-94 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "The only reason why I hired you in the first place was because you needed to help your [mil] and [sil]..."
    show story 021-95 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "And also, because I haven't seen you in a while, I figured it would be nice to be together again..."
    show story 021-96 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 021-97 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Well, that's a relief..."
    mc "I thought you fired me because you were mad at me."
    mc "You know, after what I said about your grandfather..."
    show story 021-95 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Oh, not at all, [mc]..."
    show story 021-88 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "What's done is done, I've already accepted my loss..."
    show story 021-91 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Sure, I cried when he passed... but I told myself that I wouldn't mope over it anymore."
    show story 021-89 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Because I know he wouldn't want that from me, either."
    show story 021-93 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I wish I knew..."
    mc "I was gone at a time when you needed me most..."
    show story 021-91 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "His health was already deteriorating... I knew he didn't have a lot of time left..."
    show story 021-88 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "But the biggest problem came after he passed away."
    show story 021-93 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "What happened?"
    show story 021-91 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hospital fees."
    show story 021-89 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "The medicine needed to sustain his life was more expensive than I thought..."
    show story 021-88 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Of course, I couldn't bear to tell him about it... He was already in enough pain..."
    show story 021-89 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "So I ended up having to take out loans in order to keep him alive..."
    show story 021-93 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "There's no way he would have ever wanted you to do that..."
    show story 021-89 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I know..."
    show story 021-94 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "In hindsight, I wish I read the fine print more carefully..."
    show story 021-88 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "My emotions got the better of me... I accepted the interest rates, no matter how outrageous they were..."
    show story 021-89 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Because of that, I've been trying to find a second job..."
    show story 021-91 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Well, multiple jobs, I mean..."
    show story 021-93 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Serena, you've been through so much..."
    mc "You're normally so cheerful that I never notice the other things going on in your life."
    show story 021-91 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Yeah..."
    sere "At my current rate, I'm probably going to lose the house..."
    show story 021-88 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "When that happens, I don't know what I'll do... I don't have any family left to turn to..."
    show story 021-93 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "If that's the case..."
    show story 021-97 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You can always move in with me at our place."
    show story 021-98 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Eh?"
    sere "W-What are you saying?"
    show story 021-97 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I'm saying that you should just come live with [mil], Estelle, and I."
    show story 021-99 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "It'd be convienent, too... We live right next door so the transition wouldn't be too much to deal with..."
    mc "We'd make you feel right at home, for sure... We practically see each other every day, anyway."
    show story 021-95 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "[mc]..."
    sere "Do you really mean that?"
    show story 021-99 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Of course..."
    mc "You're just as important to me as any member of the household."
    show story 021-97 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Though, I'd probably have to go over it with [mil] and Estelle first..."
    mc "But if they care for you as much as I do, I'm sure it won't be a problem..."
    show story 021-95 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Thank you, [mc]..."
    show story 021-91 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "But I'm afraid that even if I sell the house, I still won't be able to cover half the debt I owe..."
    show story 021-100 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...Damnit."
    mc "I wish there was more that I could do."
    show story 021-101 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    laur "Hey, you two!!! I have a brilliant idea!!!"
    $ renpy.pause(1, hard=True)
    play music "audio/laureate02.mp3"
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 021-102 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    laur "..."
    sere "..."
    mc "..."
    show story 021-103 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Princess... Is that you?"
    show story 021-104 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    sere "Eh?"
    sere "T-That's the p-princess!?"
    show story 021-105 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Drat..."
    show story 021-106 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Looks like you saw through my disguise..."
    show story 021-107 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    sere "S-She really is the princess!"
    sere "I never would have guessed!"
    show story 021-108 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Why are you dressed like that, Princess?"
    show story 021-109 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Hehe..."
    laur "Pardon the ruse, I merely wished to partake in an evening stroll without drawing the attention of the masses..."
    show story 021-110 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Also, check it out..."
    show story 021-111 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    laur "I picked up this cool t-shirt at the shopping district..."
    laur "Pretty '{b}rad{/b}', don't you think?"
    show story 021-112 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 021-108 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Princess, no one says '{b}rad{/b}' anymore..."
    mc "They say stuff like 'lit', 'dope', and 'dank', nowadays."
    show story 021-113 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Aww..."
    laur "I'm really behind in the times, huh?"
    show story 021-108 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Where's Ferry?"
    mc "Is it really safe for you to be out this late at night by yourself?"
    show story 021-114 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "I'll be all around in the dark... I'll be everywhere..."
    show story 021-115 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Wherever you can look... Wherever there's a fight..."
    show story 021-114 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "So hungry people can eat... I'll be there..."
    show story 021-116 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    sere "..."
    show story 021-117 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Hehe..."
    laur "Maybe I'm your guardian angel, [mc]..."
    show story 021-118 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "I'm always there... watching over you... and ready to pounce when you need me most...!"
    show story 021-119 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Er..."
    sere "[mc], how and why do you know the princess?"
    show story 021-120 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Princess Laureate is amazing!"
    mc "She's a big reason why [mil!c] and Estelle are still with me today!"
    show story 021-117 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Flattery will get you nowhere..."
    show story 021-118 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "I treat all my citizens the same... Probably... Maybe... Maybe not..."
    show story 021-121 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "More importantly, I couldn't help but overhear the predicament you find yourself in, young lady!"
    show story 021-122 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Er..."
    sere "You actually look and act a lot younger than I do..."
    show story 021-123 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hold on..."
    mc "What do you mean by that, Princess? Do you think you can help Serena?"
    show story 021-124 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "No, not exactly..."
    show story 021-125 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "If she agreed and signed a contract, she has to honor it..."
    show story 021-124 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "That's one of the [yel]Scarlet Laws{/color}, after all."
    show story 021-126 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    show story 021-127 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "However..."
    laur "There is a nuclear option to rid oneself of said debt in an instant..."
    show story 021-128 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "...and that's by surrendering your Scarlet Contract to the state."
    show story 021-123 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "W-Wait, you can't mean..."
    show story 021-129 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Uh-huh..."
    show story 021-130 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Basically, you give us the right to sell your Scarlet Contract at a discounted sum and {b}BOOM{/b}, you're debt free!"
    show story 021-131 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...I'm confused."
    mc "How does that make any sense?"
    show story 021-125 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Hmm... How should I explain..."
    show story 021-124 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "You see, everyone born within Scarlet is {b}magically{/b} entered into a database to be sold at a price based on one's worth..."
    show story 021-127 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "These numbers are ever-changing, and [yel]no one in Scarlet has the power to amend these prices{/color}..."
    show story 021-128 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "If someone tried to do that, a powerful [yel]curse{/color} would erupt in said person's body and take away their life!"
    show story 021-121 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "However, if you meet certain strict conditions, such as owing lots of money, you have the option to 'surrender' your Scarlet Contract..."
    show story 021-128 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "When that happens, we are able to formally alter the price of your Scarlet Contract at a much lower-than-average rate without any magical repercussions."
    show story 021-123 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "That doesn't make any sense..."
    show story 021-129 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "The purpose of this is to entice potential buyers, and a sale generally happens within a week."
    show story 021-130 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "It's kind of like filing for bankruptcy... except it's permanent!"
    show story 021-131 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm, I think I get it now..."
    mc "You're saying that if Serena surrenders her contract, she will be clear of all her debt..."
    show story 021-109 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Correct."
    show story 021-113 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "However, the satisfaction ratings from the girls being sold in this way is abysmal..."
    show story 021-133 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "I can only assume that the {i}Owners{/i} who look for these types of deals mistreat them because they view the girls as being {i}defected{/i}..."
    show story 021-132 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Because, as I've previously mentioned, you can only surrender your Scarlet Contract if you meet certain criteria, those criterias being a last resort."
    show story 021-134 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Oh, no..."
    show story 021-135 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I wouldn't want to have that kind of fate..."
    show story 021-136 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "And I won't let that happen!"
    mc "You're my {i}friend{/i}! I won't hand you over to another man!"
    show story 021-137 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Oh, [mc]..."
    show story 021-109 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Hehe..."
    show story 021-106 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Anyway, I've said my piece..."
    show story 021-105 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "I better return to my room before Ferry catches me skipping out on my princess-ly duties again."
    show story 021-138 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Ciao!"
    show story 021-139 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 021-140 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "..."
    mc "..."
    show story 021-141 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Geez..."
    mc "The princess sure does come up with some weird things to say, don't you think?"
    mc "I mean, having someone buy your Scarlet Contract? That's a bit too much..."
    show story 021-142 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    show story 021-143 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Serena?"
    show story 021-144 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Eh?"
    show story 021-145 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "O-Oh, yeah..."
    show story 021-146 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I mean, I wouldn't totally be opposed to it if, you know, the person I was being sold to wasn't a complete jerk..."
    show story 021-147 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...Serena?"
    mc "What are you thinking?"
    show story 021-148 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "N-Nothing..."
    show story 021-149 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 021-150 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Don't worry, Serena. We'll figure out a solution to this problem of yours."
    show story 021-147 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "And we'll do it together! I'll even help you with your finances if I have to!"
    show story 021-144 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I'm not sure..."
    show story 021-145 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Like I said, I'm about to lose the roof over my head if I don't pay the next few monthly bills..."
    show story 021-147 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Alright, that's the first thing we'll do..."
    show story 021-150 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "We'll go over to my house and have a talk with my [mil] and Estelle."
    mc "I'll convince them to let you stay over, just in case you do lose the house."
    show story 021-146 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "[mc]..."
    show story 021-148 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Thank you..."
    show story 021-149 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 021-147 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh, and one more thing..."
    mc "Back at town square... I overheard what you said to that guy earlier..."
    show story 021-150 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You know, about you having a, um, {b}boyfriend{/b}?"
    mc "Just wondering if, er, you really did have one or not..."
    show story 021-148 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Geez, [mc]..."
    show story 021-146 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "You're such a big dummy, you know that?"
    stop music fadeout 3
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    "I walked Serena back to her home..."
    "Her mind was clearly in thought, as she did not say anything else except to wish me a good night..."
    $ renpy.end_replay()
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/days.mp3"
    jump streetlabel_01

label sere04_01:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    play music "audio/serena.mp3"
    show story 019-23 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    sere "..."
    show story 019-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Thanks for helping out at the store today, [mc]..."
    show story 019-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Here's your pay for today."
    show story 019-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "T-That's alright, Serena! There's no way I can accept this from you!"
    mc "I'm just helping out around the store because I don't have any other plans today!"
    show story 019-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hehe... Don't be like that!"
    show story 019-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I always have to pay someone for their services! It's just the right thing to do!"
    show story 019-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 022-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    show story 022-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Sheesh..."
    sere "This is why I didn't want to tell you about my problem in the first place..."
    show story 022-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Now you're going to go ahead and make things awkward between us..."
    show story 022-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I just can't get it out of my mind..."
    mc "You need this money more than I do."
    show story 022-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Maybe that's true, but I don't want our relationship to change just because of money..."
    show story 022-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Life isn't free, y'know? And I already feel indebted to you, [mc]..."
    show story 022-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Fine, I'll accept your money..."
    with vpunch
    mc "But I still haven't given up! We'll think of a solution to your debt!"
    show story 022-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    show story 022-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hey, [mc]..."
    sere "I was wondering if you talked to your [mil] about having me stay over or not..."
    show story 022-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "You know, that thing you blatantly blurted out the other night?"
    show story 022-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "No, not yet..."
    mc "To be honest, I wasn't completely sure if that's what you wanted to do."
    mc "I don't mind asking them, of course... Though, I'm pretty sure they'll agree to help."
    show story 022-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I see..."
    show story 022-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "If you want, we can talk to them about it together."
    mc "It'd seem more genuine if you were there with me in person."
    show story 022-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I don't know..."
    show story 022-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I mean, the last thing I'd want is for my {i}in-laws{/i} to think I'm a mooch..."
    show story 022-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...In-laws?"
    show story 022-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    sere "I-I mean, sure [mc]! Let's see what they have to say!"
    show story 022-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 022-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Besides..."
    show story 022-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I've been doing a lot of thinking, lately..."
    show story 022-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Not just regarding money, but about my future, too..."
    show story 022-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...?"
    $ renpy.pause(1, hard=True)
    stop music fadeout 3.0
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "Serena and I spent the rest of the afternoon at the store..."
    "She agreed to follow me back home and meet with [mil!c] and Estelle after we were done with work..."
    call charwork ("serena_overtime")
    $ renpy.pause(1, hard=True)
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump streetlabel_01

label sere04_02:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 022-11 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    sere "..."
    show story 022-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "[mc], I'm getting nervous..."
    show story 022-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "What am I doing? Should I even be here?"
    show story 022-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Relax, Serena..."
    mc "There's nothing to worry about... You've been over our house a dozen times before..."
    show story 022-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I know, but..."
    show story 022-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "What if they don't like me? What if they think I'm some charity case?"
    show story 022-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Ugh, this is so stupid... They're going to hate me for this..."
    show story 022-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "They won't think that way..."
    mc "Estelle considers you a big sister, and [mil!c] has been preaching that you and I, uh..."
    show story 022-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Oh my... Now this a pleasant surprise..."
    show story 022-17 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play music "audio/silvia.mp3"
    silv "..."
    show story 022-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Serena-chan, what brings you here today?"
    show story 022-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Are you here to announce your plans to run away and elope with my [mc]?"
    show story 022-20 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    sere "E-Elopement!?"
    sere "But I'm not ready for marriage!"
    show story 022-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Er..."
    show story 022-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I mean, how are you doing this evening?"
    show story 022-23 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "Eh, Serena?"
    este "It's been a while since your last visit. Did you come over to play?"
    show story 022-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "H-Hey, Estelle..."
    show story 022-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "No, not here to play... Just here to talk..."
    show story 022-26 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    este "Don't get too close to him, Serena!"
    show story 022-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "He's a {b}huge{/b} pervert! He'll definitely try and make you do weird stuff like pull down his pants and touch his...!"
    show story 022-28 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "Oi, oi!"
    mc "Stop scaring her! She's already nervous as it is!"
    show story 022-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Oh dear..."
    show story 022-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "This does seem serious... Is something wrong, Serena?"
    show story 022-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Er..."
    sere "I don't know how to explain..."
    show story 022-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "You see..."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "I explained Serena's financial situation to [mil!c] and Estelle..."
    "Both of them were as surprised as I was at the news... I don't think either of them expected her to be in such a bad state of affairs..."
    $ renpy.pause(3, hard=True)
    show story 022-33 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "...And that's about the gist of it."
    mc "What do you think? Can Serena stay with us if worst comes to worst? Just until she can get back on her feet?"
    mc "She doesn't have anyone else to turn to... I can't leave her like this on her own..."
    show story 022-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "..."
    silv "... ..."
    silv "... ... ..."
    show story 022-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Ah, I knew it was too much to ask..."
    show story 022-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I'm sorry to have been a bother..."
    show story 022-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "Serena definitely won't be a burden on us!"
    mc "She's a hard worker! She'll help out around the house and pay her own dues!"
    show story 022-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I...I don't know..."
    show story 022-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "As much as I'd like to, I'm already penny pinching as it is..."
    show story 022-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hmm..."
    silv "Serena-chan, I figured something was going on with you, but it was too difficult to tell because you were always smiling..."
    show story 022-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "To think that things have escalated to this point..."
    show story 022-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    show story 022-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Next time, trust and confide in us much sooner, okay?"
    show story 022-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "That way, we can all pitch in together and help..."
    show story 022-41 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    sere "Eh?"
    sere "T-Together? Then does that mean..."
    show story 022-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "That's right, Serena!"
    show story 022-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "This household sticks together! We'll do everything we can to help!"
    show story 022-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "See, what'd I say?"
    mc "I knew they would say {b}yes{/b}."
    show story 022-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "*Sniff* *Sniff* Y-You guys..."
    show story 022-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I didn't know what to do... There was no one else I could turn to..."
    show story 022-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "That's why I'm glad... I'm so happy that I have great friends and neighbors like you all..."
    show story 022-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "...especially you, [mc]."
    show story 022-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Heh..."
    show story 022-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "That being said..."
    silv "How long do you suppose it'll take before your debt is settled?"
    show story 022-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "To be honest, I'm not entirely sure..."
    show story 022-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I feel like I'll be an old lady with gray hairs by the time I can fully pay it off..."
    show story 022-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Oh my..."
    show story 022-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "As much as I hate to admit it, perhaps the princess is right..."
    show story 022-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Having your Scarlet Contract surrendered might be the best course of action here..."
    show story 022-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "No way..."
    show story 022-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "[mc], can't we do something?"
    show story 022-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Maybe if I talk to the princess, I can..."
    show story 022-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "No, [mc]..."
    show story 022-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Your [mil]'s right... this is on me."
    show story 022-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "It's my responsibility... I got myself into this mess, it only makes sense that I get myself out..."
    show story 022-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "That's why... I want to do what the princess suggested..."
    show story 022-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "Eh!?"
    este "Serena, you can't do that!"
    este "You'll end up with someone more perverted than [mc]!"
    show story 022-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "Estelle's right! I won't let you go through with it!"
    mc "And you heard what the princess said! People sold in this way usually end up being miserable for the rest of their lives!"
    show story 022-55 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Probably..."
    show story 022-56 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "But that's why I'd like it if '{b}you{/b}' were the one to buy my Scarlet Contract, [mc]..."
    show story 022-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "W-What!?"
    show story 022-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "You heard me."
    show story 022-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Maybe it's a selfish request, but if it's with you, I'm okay with it..."
    show story 022-60 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "That way, I won't have any regrets about where I go..."
    show story 022-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "After meeting your household and seeing how receptive they are of me, I know I'll be in good hands..."
    show story 022-61 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Serena-chan..."
    silv "We'd be more than delighted to accommodate you."
    show story 022-62 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "In my eyes, you're already a member of the household."
    show story 022-63 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hehe..."
    este "Serena, if this pervert doesn't buy your Scarlet Contract, then I will!"
    show story 022-64 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "I'd love to have you here!"
    show story 022-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Goddamnit, everyone..."
    mc "I really do have the best household ever..."
    show story 022-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Thank you all..."
    show story 022-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I've already done my research at City Hall..."
    show story 022-60 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "With the {b}reduced{/b} price, my Scarlet Contract will be [yel]$10,000{/color}."
    show story 022-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "What do you think, [mc]? Can you do this favor for me?"
    stop music fadeout 3.0
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "Serena is adamant on her decision."
    "To buy her Scarlet Contract, I'll have to speak to Laureate."
    $ renpy.pause(1, hard=True)
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump livingroomlabel


label sere05_01:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 024-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/silvia.mp3"
    silv "..."
    show story 024-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Morning, dear!"
    show story 024-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Good morning, [mil!c]!"
    show story 024-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "I'll be heading off to work now..."
    show story 024-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "You two behave, okay?"
    show story 024-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You can count on me!"
    play sound "audio/door.mp3" volume 3
    show story 024-08 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    show story 024-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Good morning, Estelle..."
    show story 024-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Yeah... Yeah..."
    show story 024-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 024-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Shouldn't you be in school?"
    show story 024-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Geez, are you my dad?"
    show story 024-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "I still have an hour before I absolutely have to go."
    show story 024-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    $ renpy.pause(.5, hard=True)
    play sound "audio/door.mp3" volume 3
    show story 024-09 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "*Huff* *Huff*"
    show story 024-10 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Huh? What's wrong Serena?"
    mc "Did something happen at work?"
    show story 024-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    sere "[mc], thank goodness! I need your help!"
    show story 024-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "There's someone {i}sleeping{/i} inside my house and I don't know who it is!"
    show story 024-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "W-What!?"
    show story 024-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I went over to pick up some supplies before opening the store..."
    show story 024-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "And that's when I heard snoring coming from my bedroom!"
    show story 024-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I got scared and came over here to find you immediately..."
    show story 024-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Alright, let's go check it out..."
    stop music fadeout 3.0
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 024-14 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/serena.mp3"
    mc "..."
    show story 024-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "(I can't believe I'm inside Serena's room...)"
    mc "(This place is smells so good... The last time I was in here, we were just kids...)"
    show story 024-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Why are you just standing there, [mc]?"
    show story 024-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Get to finding our intruder!"
    show story 024-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oi, oi..."
    mc "What are you doing here, Estelle? Shouldn't you be getting ready for school?"
    show story 024-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hey, this is an emergency!"
    show story 024-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Serena's my friend too, you know? It only makes sense that I want to help!"
    show story 024-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Emergency, huh? Is that why you sound so excited?"
    show story 024-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hehe..."
    este "Don't worry, Serena. I'll protect you from this pervert..."
    show story 024-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hey... Stop messing around, you two..."
    show story 024-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Take a look over there..."
    show story 024-22 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    with vpunch
    mc "A-A tail!?"
    show story 024-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Oh my goddess!"
    este "It's a {b}dog girl{/b}!"
    show story 024-20 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "Er..."
    sere "I believe the more accurate term is [yel]half-breed{/color}..."
    show story 024-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "A half-breed..."
    mc "I heard that they're supposed to be dangerous... You rarely see one in Scarlet..."
    show story 024-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Eh?"
    este "How can someone {i}that{/i} cute be dangerous?"
    show story 024-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "I want to go over there and pet her!"
    show story 024-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "No, [mc] is right... We have to be careful..."
    show story 024-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Apparently, half-breeds are [yel]kill on sight{/color} in Scarlet."
    show story 024-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "What should we do, [mc]?"
    show story 024-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm..."
    mc "I'll go over there and ask it to leave..."
    show story 024-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You girls stay back in case it's unstable..."
    $ renpy.pause(.5, hard=True)
    show story 024-29 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mc "(Whoa... She's actually really cute up close...)"
    show story 024-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "Hey, [mc]!"
    este "Ask her if she'd let me feel her fluffy tail!"
    show story 024-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Estelle, you're going to spook her if you speak too loud..."
    show story 024-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu:
        "Be gentle..." if True:
            $ renpy.fix_rollback()
            mc "..."
            show story 024-32 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Excuse me, Miss Dog Girl..."
            mc "You're sleeping in my friend's room and need to leave right now."
        "Be forceful..." if True:
            $ renpy.fix_rollback()
            show story 024-33 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            mc "Hey, Miss Dog Girl!"
            mc "You're sleeping in my friend's room and need to leave right now!"
    show story 024-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mv2 "Grrr..."
    $ renpy.pause(.5, hard=True)
    show story 024-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 024-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm..."
    mc "This isn't working..."
    show story 024-37 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    este "Wow... She's sooo gorgeous..."
    show story 024-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "I'm going to pet her tail..."
    show story 024-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Hey, didn't you listen to what I said?"
    mc "She might be dangerous! Stay back or else you might get hurt!"
    show story 024-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hehe... I'm going to tame her and name her Scruffles..."
    show story 024-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Serena, can you take a video for my [oj]Tik Tok{/color}?"
    show story 024-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm..."
    mc "I guess I'll just pick her up and carry her outside..."
    show story 024-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Okay, just be careful though..."
    show story 024-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Like I said, half-breeds are considered dangerous in Scarlet..."
    show story 024-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Wait a second, [mc]..."
    este "It says here that stray dogs might bite and give you an infection if you don't know how to handle them..."
    show story 024-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "That's what I've been trying to tell you..."
    mc "You'd rather listen to something you see on the MagiNet over me?"
    show story 024-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hmm, let me see..."
    este "Okay, it says here that you should try to approach the animal slowly to avoid scaring her..."
    show story 024-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Alright..."
    mc "So just be gentle as I carry her out? Got it..."
    show story 024-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hold on..."
    este "First, you should lay down next to it and put your body on the same level as the puppy..."
    show story 024-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Why would I do that...?"
    show story 024-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "It's supposed to be a form of building trust with an animal... and it shows them that you mean them no harm."
    show story 024-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Uh... Alright, if you say so..."
    $ renpy.pause(.5, hard=True)
    show story 024-48 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mc "(She's really soft and warm...)"
    show story 024-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hey, was it really necessary for me to take off my shirt?"
    show story 024-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Definitely..."
    este "Skinship is the ultimate form of sincerity..."
    show story 024-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...If you say so."
    show story 024-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Aw, this is so cute..."
    sere "I want to take a picture of [mc] cuddling up with the puppy girl..."
    show story 024-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "This is stupid! I'm just going to go ahead and pick her up!"
    show story 024-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mv2 "Grr..."
    show story 024-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Now look what you did!"
    este "You have to cuddle up with her! It's the only way to soothe a wild puppy's heart!"
    show story 024-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Aren't I doing that already!?"
    show story 024-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "No, no, no..."
    este "Cuddling doesn't mean just lying down with her and giving her a belly rub..."
    este "You also have to tell your pup that you love her!"
    show story 024-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I-I love you..."
    show story 024-54 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mv2 "Ehehehe~"
    show story 024-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "See!? It's working!"
    show story 024-56 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hehe..."
    sere "Now tell her that 'Daddy will keep you safe, my perfect little fur angel'..."
    show story 024-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Yeah! Do it, [mc]! Do it!"
    show story 024-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Aren't you two enjoying this a little too much?"
    show story 024-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hehe... Make sure you send this video to me later, Estelle..."
    show story 024-62 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "Alright, this is getting ridiculous! I'm just going to carry her outside!"
    show story 024-63 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mv2 "NUUUUUUU!!!"
    $ renpy.pause(.5, hard=True)
    show story 024-64 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "Look what you did, [mc]! You made her upset!"
    show story 024-65 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "No, I don't think so..."
    show story 024-66 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "That was clearly a groan... Maybe she's in pain?"
    show story 024-67 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Eh? You think so?"
    show story 024-68 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "L-Let me check my phone..."
    show story 024-69 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "*Sigh*"
    show story 024-70 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Now what do we do?"
    show story 024-71 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Okay, I got it!"
    show story 024-72 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "It says here that she might be feeling sick or anxious because of the change in environment..."
    show story 024-73 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Maybe..."
    sere "I mean, she does look kind of upset right now..."
    show story 024-74 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Ah, it says that we should check her temperature..."
    show story 024-71 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Do you happen to have a thermometer around, Serena?"
    show story 024-75 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Y-Yeah, I keep one in the bathroom..."
    show story 024-76 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Perfect! Bring it over quick!"
    show story 024-77 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    show story 024-78 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Are you sure this is all necessary?"
    mc "We came here to get rid of her... not play doctor!"
    show story 024-79 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "Hey, do you want to do this right or not!?"
    show story 024-80 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "If Scruffles dies here, there'll be blood on your hands, [mc]!"
    show story 024-81 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Goddamnit..."
    show story 024-82 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "Found the thermometer, Estelle..."
    show story 024-83 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Should I go ahead and stick it in her mouth?"
    show story 024-84 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Nope..."
    este "Apparently, the safest way to take a wild puppy's temperature is..."
    show story 024-85 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "...by sticking it up her {b}butt{/b}."
    show story 024-86 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "..."
    show story 024-87 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    show story 024-88 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 024-89 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "What are you both looking at me for?"
    show story 024-91 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Isn't stuff like this the job for an older [bil]?"
    show story 024-90 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Y-Yeah, [mc]... You can't expect a lady to do something so {i}dangerous{/i}, right?"
    show story 024-92 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Ugh..."
    $ renpy.pause(.5, hard=True)
    show story 024-93 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mc "I don't know... She's a dog, but she's also a {i}girl{/i}..."
    mc "Sticking something up their butts without permission seems a little wrong..."
    este "Just do it, [mc]!"
    este "The MagiNet says it's perfectly fine so it must be true!"
    mc "..."
    mc "Here goes nothing..."
    stop music fadeout 3.0
    $ renpy.pause(.5, hard=True)
    show story 024-94 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 024-95 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 024-96 with Dissolve(1)
    $ renpy.pause(3, hard=True)
    show story 024-97 with Dissolve(1)
    $ renpy.pause(2, hard=True)
    mv2 "Nuuu... Nuuu..."
    show story 024-98 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "...Eh?"
    show story 024-99 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Push the tip in deeper, [mc]!"
    este "Really get up her rabbit hole!"
    mc "Got it..."
    show story 024-100 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    mv2 "KYYYAAAHHH!!!"
    play music "audio/celestia.mp3"
    $ renpy.pause(3, hard=True)
    show story 024-101 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mv2 "..."
    show story 024-102 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "Ahem... Now that I'm awake..."
    show story 024-103 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mv2 "What the heck is wrong with you people!?"
    mv2 "How dare you stick something up my butt!? Did you think I wouldn't notice!?"
    show story 024-104 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Er, sorry about that..."
    show story 024-105 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "We're really sorry..."
    show story 024-106 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "Wow... She's sooo cute!"
    show story 024-107 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "I can't wait to bring you home, {i}Scruffles{/i}!"
    show story 024-108 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mv2 "S-Scruffles...!?"
    mv2 "I'm not your pet, y'know!?"
    show story 024-109 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Estelle, you apologize too."
    show story 024-110 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Ah, right..."
    este "I'm really sorry, Miss Dog Girl..."
    show story 024-107 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "...Now can I touch your fluffy tail?"
    show story 024-108 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mv2 "S-Scary!"
    mv2 "You {i}animals{/i} think I'm a dog!?"
    show story 024-111 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "W-Well, yeah..."
    show story 024-112 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "There wasn't much information on half-breeds online, so I had to read up on dogs instead..."
    show story 024-113 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mv2 "I'm a [yel]FOX GIRL{/color}! Not a dog! A FOX!"
    mv2 "And if anything, I'm more human than animal!!!"
    show story 024-114 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "Sheesh, this is why I can't stand humans..."
    show story 024-112 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hehe..."
    este "I'm going to train you to become obedient and strong, Scruffles!"
    este "Then I'll use you to battle other animals and capture them too!"
    show story 024-113 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mv2 "Hey, cut it out!"
    mv2 "I already have a name so stop calling me Scruffles!"
    show story 024-115 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Aww..."
    show story 024-116 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    cele "The name's [yel]Yuuna Celestine{/color}, at your service!"
    show story 024-117 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "But you all can just call me [yel]Celestia{/color}!"
    show story 024-118 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I'm [mc], and this is Serena and Estelle..."
    mc "It's nice to meet you and all, Celestia, but you're trespassing on private property... That bed your sleeping on belongs to Serena."
    show story 024-119 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    cele "Trespassing!? Me!? Why, I'd never...!"
    show story 024-120 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "I simply found an empty abode and decided to use it for shelter! Can't blame a fox girl for that!"
    show story 024-121 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Don't tell me you think you own the land just because a piece of paper says you do!? Hah!"
    show story 024-118 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "You know what? Serena, it looks like you were right..."
    mc "Half-breeds really are dangerous... We better call an exterminator to take care of this pest..."
    show story 024-119 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    cele "S-Scary!"
    show story 024-120 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Hold on! I'm not dangerous! Can't you see how well-behaved I am?"
    show story 024-122 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "How can someone as cute as me be considered dangerous?"
    show story 024-105 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Er, well, it is kinda true..."
    show story 024-123 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Half-breeds are supposed to be very combative... They attack and cause mayhem for humans all the time..."
    show story 024-120 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Sure, that's true for the prototypical [yel]feral{/color} half-breed..."
    show story 024-121 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "But I'm obviously tame! I was raised and domesticated by humans since I was a wee little cub!"
    show story 024-115 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Awww..."
    este "Then that must mean you already have an owner..."
    show story 024-124 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "..."
    show story 024-118 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Anyway, it was nice meeting you Celestia, but..."
    mc "You're still going to have to leave... This house belongs to Serena..."
    show story 024-125 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "W-What!? But I like it here!!!"
    show story 024-120 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "It's so nice and warm inside! Usually, I'm sleeping outside in the elements with only leaves to keep me warm!"
    show story 024-118 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "I want you to pick up your things and be out of here within the hour!"
    show story 024-119 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "S-Scary!"
    cele "Humans really are the worst!"
    show story 024-126 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hehe..."
    sere "You know, [mc]... I haven't really been spending much time here ever since I started living with you guys."
    show story 024-127 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Who knows? This might be a good opportunity. You know, to keep the place occupied and all..."
    show story 024-128 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Serena... You're too kind..."
    show story 024-129 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Well, Celestia seems friendly enough..."
    show story 024-126 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Plus, I'm also interested in learning more about half-breeds since I've never met one before..."
    show story 024-127 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Of course, she will still have to {i}pay her dues{/i}... I've been thinking about turning my house into an apartment, anyway."
    show story 024-130 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Pay... my dues?"
    show story 024-118 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...She means {i}rent{/i}."
    mc "Serena is willing to let you stay in her home, as long as you afford your time here."
    show story 024-120 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Ohhh, I get it!"
    show story 024-122 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Sure thing! I don't have a problem with that!"
    show story 024-121 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "But I can't pay for it right now~! You're going to have to meet me later tonight for that~!"
    stop music fadeout 3.0
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    $ renpy.end_replay()
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump streetlabel_01

label sere05_02:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 024-131 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    show story 024-132 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Celestia said to meet her here, but..."
    mc "Where is that crazy fox girl...?"
    $ renpy.pause(.5, hard=True)
    show story 024-133 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    cele "Hah~!"
    cele "You looking for me~!?"
    show story 024-134 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "HYUUUTTT!!!"
    $ renpy.pause(.5, hard=True)
    play music "audio/celestia.mp3"
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 024-135 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    mc "What were you doing up in that balcony?"
    show story 024-136 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Eh?"
    show story 024-138 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Oh, nothing suspicious... just peeking through windows to see if anyone's inside..."
    show story 024-137 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "More importantly... Where are your friends?"
    show story 024-135 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "It's late..."
    mc "I figure I might as well take care of this since I live close by."
    show story 024-136 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Right you are, Mister [mc]..."
    show story 024-138 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Because now, I am willing to negiotiate the terms of my tenure!"
    show story 024-135 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah, about that..."
    show story 024-139 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Here... Serena asked me to give you this letter."
    show story 024-140 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "What's this?"
    show story 024-141 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "The expected sum of your monthly bill to stay in her house..."
    mc "You can pay in cash, credit, check, or whatever..."
    show story 024-142 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    cele "Eh!? You want {i}that{/i} much!?"
    cele "But I don't have that kind of money!"
    show story 024-135 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "What do you mean?"
    mc "Serena is being generous here... This is like a quarter of what places in this area usually go for."
    show story 024-142 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    cele "Scary!"
    cele "The world sure is expensive!"
    show story 024-135 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "What do you do for a living, anyway?"
    show story 024-138 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Hah! I'm glad you asked!"
    show story 024-137 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "You're staring at a one-of-a-kind professional peddler... and a connoisseur of jewelry and all things shiny!"
    show story 024-136 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "That's right! It's your friendly neighborhood swindler, [yel]Yunna Celestine{/color}, at your service!"
    show story 024-135 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "In other words... you're {i}unemployed{/i}..."
    show story 024-143 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Hey, don't say that! I take pride in my work!"
    show story 024-144 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "You better not disrespect my craft or else you're going to regret it!"
    show story 024-145 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I knew this was a waste of time..."
    mc "Have a good night, Miss Yuuna Celestine."
    show story 024-142 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    cele "H-Hold on!"
    show story 024-136 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Look, I can't give you any money but I can offer you the next best thing!"
    show story 024-146 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    cele "Feast your eyes on this..."
    show story 024-147 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Is that raggedy old thing a... {i}doll{/i}?"
    show story 024-150 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Not just any doll..."
    show story 024-148 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "This right here is a bonafide genuine explosive beanie doll! Something you won't get just anywhere!"
    show story 024-149 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Simply give the doll to someone you hate... Then when they give the doll a hug..."
    show story 024-150 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    cele "{b}KA-BLAMO!!!{/b} Say sayonara to your enemies!"
    show story 024-147 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I'm done wasting my time here..."
    show story 024-149 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Aw, c'mon..."
    show story 024-148 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Is sharing a piece of land you don't even use really worth more than this handmade doll?"
    show story 024-150 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "If you think about it, money is just a piece of paper! It's because you humans are so obsessed with it that it has any real value!"
    show story 024-147 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Why don't you just get a real job?"
    mc "You're pretty and have a way with words... There's bound to be something out there you can do that's {i}less{/i} shady..."
    show story 024-144 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Sorry, no can do!"
    show story 024-143 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Peddling is my passion! I find random junk... er, {i}goods{/i}... and sell them for a premium!"
    show story 024-145 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "You're hopeless..."
    show story 024-151 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "..."
    show story 024-152 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Okay, it's decided!"
    show story 024-153 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Since you've displayed such a keen interest in my trade, I'll allow you the great honor of working with me, Mister [mc]!"
    show story 024-151 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "W-What!? I never agreed to..."
    show story 024-152 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Too late! No take backs!"
    show story 024-143 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Or would you prefer to see this fox girl sad..."
    show story 024-144 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Because if that's the case, maybe I'll tell the Holy Knights about how I woke up to find your {i}stick{/i} up my naked bottom while I was asleep..."
    show story 024-151 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You're the devil..."
    mc "Fine I'll help you with your stupid sales!"
    show story 024-154 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    cele "Mwuhahaha~! Excellent~!"
    cele "Welcome aboard, my apprentice~!"
    $ renpy.pause(1, hard=True)
    stop music fadeout 3.0
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play sound "audio/ding.mp3" volume 3
    "[yel]You became Celestia's apprentice."
    play sound "audio/ding.mp3" volume 3
    "[yel]Yuuna Celestine's Character Card has been added to the Relationship Screen."
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump streetlabel_04

label cele01_01:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 024-135 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/celestia.mp3"
    cele "..."
    show story 024-138 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Hehe~!"
    cele "Welcome to your first day on the job, [mc]!"
    show story 024-143 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Be warned, though! I'm just like a tiger mom! I'll scold you every time you mess up!"
    show story 024-145 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah, yeah..."
    mc "What are you going to make me do?"
    show story 024-152 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "I'm glad you asked..."
    show story 024-153 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Today's mission is stocking up on {i}inventory{/i}..."
    show story 024-137 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "We're going to get us some valuable goods to sell and re-sell!"
    show story 024-135 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Okay, and what is that exactly?"
    show story 024-152 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "I'm glad you asked!"
    show story 024-153 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "We'll be patroling the streets of Scarlet for {i}treasure!{/i}"
    show story 024-143 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "You know, electronics, gadgets, shiny objects... That sort of deal..."
    show story 024-152 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "And we'll do so by going through the [yel]trash bins{/color} around town!"
    show story 024-151 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hold on..."
    mc "You're saying you want to go through people's trash!?"
    show story 024-153 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Yep!"
    cele "People in Scarlet throw away valuable stuff all the time!"
    show story 024-152 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "It takes a good eye to determine what we can sell and what we can't!"
    show story 024-151 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Is that even legal?"
    show story 024-136 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Sure, why not!?"
    show story 024-137 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Besides my job as a peddler, I'm also certified to provide legal advice!"
    show story 024-135 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Y-You're qualified to practice law!?"
    show story 024-138 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Sure am!"
    cele "I became one after I found a license for legal studies in the bin a few months ago!"
    show story 024-135 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 024-137 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Now enough with your yapping!"
    cele "No one said that peddling is easy... Go ahead and start digging through the trash for valuable {i}treasures{/i}..."
    show story 024-136 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "I expect quality results by the end of the night!"
    $ renpy.pause(.5, hard=True)
    stop music fadeout 3.0
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated."
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    play sound "audio/ding.mp3" volume 3
    show screen tutorialscreen_10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    pause
    jump streetlabel_04

label cele01_02:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 026-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/celestia.mp3"
    mc "..."
    show story 026-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Nothing in here but trash..."
    mc "Is this really what Celestia does for a living?"
    show story 026-03 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    silv "[mc], honey?"
    silv "D-Did you just pick that banana out of the trash...?"
    show story 026-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "[mil!c]!?"
    mc "T-This isn't what it looks like..."
    show story 026-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "[mc], I know that times are tough, but..."
    show story 026-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "If you're hungry, you can always just ask me for money..."
    show story 026-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "No, [mil!c]! You don't understand... I'm just doing this to help my..."
    show story 026-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Here, let me grab my purse back home..."
    show story 026-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "I know that you're a man and don't want to piggyback off me anymore but I can't bear to see you like this, honey..."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "After some embarrassing back and forths, [mil!c] returned home looking concerned for me..."
    $ celetreasure += 1
    $ celeevents += 1
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated."
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump street04_trashcan_label

label cele01_03:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 026-08 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/celestia.mp3"
    mc "..."
    mc "(Discarded panties that someone threw away...)"
    show story 026-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "(I wonder who they belong to...?)"
    mc "(They look pretty clean... Well, I'd honestly prefer if they were a little {i}dirty{/i}...)"
    show story 026-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 026-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "(You know, if I give them a sniff, I might be able to figure out the answer to my question...)"
    show story 026-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "(Y-Yeah, that's it... It's not like I get off from wanting to smell the lingering scent of women's underwear... I'm just satisfying a completely normal human urge for curiosity!)"
    show story 026-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "(Alright, I'm going to do it... No one's around, anyway...)"
    show story 026-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "(Hehe... In a way... I guess you could call this {i}treasure{/i}...)"
    show story 026-12 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    azul "As expected of my male companion...!"
    azul "Your pervertedness is on a totally different level!"
    show story 026-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "A-Azula!?"
    mc "H-How long were you standing there!?"
    show story 026-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Oh, don't stop on my part! I approve of your panty sniffing!"
    show story 026-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "The more ferociously horny the man, the stronger the output of essence!"
    show story 026-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "What do you mean!? I wasn't going to do anything weird with these!"
    show story 026-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Ehhh? Don't lie about something so silly, [mc]!"
    show story 026-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "I've been standing here for a few minutes now, just watching to see what you would do!"
    azul "Go on! Don't let me get in the way of your degeneracy!"
    show story 026-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "Azula ruined the moment... My boner faded into nothingness..."
    $ celetreasure += 1
    $ celeevents += 1
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated."
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump street01_trashcan_label

label cele01_04:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 026-18 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/celestia.mp3"
    mc "..."
    show story 026-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Well, this was a colossal waste of time..."
    mc "I didn't find anything except junk..."
    show story 026-20 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    cele "Heeeyyy there, apprentice!"
    show story 026-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "How was your first night of searching? Did you find any goodies?"
    show story 026-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Nope..."
    show story 026-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "It's hard to find {i}treasure{/i} if you don't even know what you're looking for..."
    show story 026-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Ah, don't worry about it..."
    show story 026-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Some nights are slow like this... Sometimes there just aren't any goodies around to loot..."
    show story 026-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "So don't get all depressed and mopey, okay!? You'll get them next time, champ!"
    show story 026-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Don't worry. I won't."
    show story 026-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Alright, let's call it for the night..."
    show story 026-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Get some good rest, tiger! Next time, we'll be doing some more fun stuff!"
    show story 026-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I don't know about that..."
    mc "This feels like a waste of time... I helped you out today, but don't expect me to do it again next time."
    show story 026-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "And besides..."
    mc "All of this garbage collecting has left me in need of a shower... I smell like crap..."
    show story 026-24 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    cele "*Sniff* *Sniff*"
    show story 026-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Aye, I'm rather stinky myself..."
    show story 026-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "I think I'll go ahead and take a bath at the lake like I always do."
    show story 026-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 026-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hold on... Do you mean the lake over at the park?"
    mc "You're telling me that you take off your clothes until you're {b}naked{/b}, dip yourself in the water while {b}naked{/b}, and scrub your {b}naked{/b} body?"
    show story 026-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "That's a lot of emphasis on the word {i}naked{/i}, but yes..."
    show story 026-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "You silly humans probably think we half-breeds go around licking ourselves clean, huh? Well think again!"
    show story 026-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "I told you already, didn't I? I'm more human than beast! I know how to wash myself in water just like you humans do!"
    show story 026-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 026-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Anyway, that's enough work for today..."
    show story 026-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Toodles~!"
    show story 026-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 026-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah, there's no way I'm missing an opportunity like this..."
    show story 026-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "(Before going back home, I need to have myself a good peek...)"
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated."
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump streetlabel_04

label cele01_05:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 026-29 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    show story 026-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Shit, am I really doing this?"
    mc "What if I get caught? Everyone will know how much of a pervert I am..."
    show story 026-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    play sound "audio/splash.mp3" volume 3
    "*SPLASH* *SPLASH*"
    show story 026-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "That must be her..."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 026-33 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/casual.mp3"
    cele "La la, la la la la la na na na na na~~!"
    cele "If our love is running out of time~! I won't count the hours, rather be a coward~!"
    show story 026-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "When our worlds collide~! I'm gonna drown you out before I lose my mind~!"
    $ renpy.pause(.5, hard=True)
    show story 026-43 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    show story 026-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "This was a genius idea!"
    mc "Yeah, I'm a pervert... so what!? I get to see a fox girl bathing in a lake! Stuff like this only happens in anime!"
    show story 026-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    cele "Eh?"
    cele "H-Hey, is someone out there!?"
    $ renpy.pause(.5, hard=True)
    show story 026-37 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    cele "W-Whoever you are, you better come out now!"
    show story 026-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "I'm warning you! I'll bite out your eyeballs if you try anything funny, got it!?"
    show story 026-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu:
        "Show yourself to Celestia..." if True:
            $ renpy.fix_rollback()
            jump cele01_05_02
        "Remain silent..." if True:
            $ renpy.fix_rollback()
            pass
    "*SILENCE*"
    show story 026-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 026-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "..."
    show story 026-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "I-I'm getting out of here..."
    show story 026-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    cele "But not because I'm scared or anything!"
    show story 026-40 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play sound "audio/splash.mp3" volume 3
    show story 026-35 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    show story 026-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Damn, Celestia ran away..."
    show story 026-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Maybe this wasn't the result I wanted..."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    play sound "audio/ding.mp3" volume 3
    "[yel]HINT: You can replay this scene in the gallery."
    $ renpy.end_replay()
    play music "audio/days.mp3"
    jump parklabel_04

label cele01_05_02:

    stop music fadeout 3.0
    show story 026-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "..."
    show story 026-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Alright, if you aren't going to come out, then..."
    show story 026-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    cele "I'm going to scream! And when I do, everyone in Scarlet will come to know the {i}beast{/i} that you are!!!"
    show story 026-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Hold on a second, Celestia!"
    mc "Don't scream! It's just me!"
    show story 026-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Eh? [mc]?"
    cele "What are you doing all the way over here!?"
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 026-47 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/celestia.mp3"
    cele "..."
    mc "..."
    mc "(What's up with the mask?)"
    mc "(She always seems to put it on whenever we're talking...)"
    show story 026-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Now then..."
    show story 026-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    cele "What the heck were you doing lurking in the bushes!? Were you trying to prank me or something!?"
    show story 026-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "D-Definitely not doing anything suspicious!"
    show story 026-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Hey..."
    cele "Didn't you say you were going back home?"
    show story 026-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Er, yeah... I was going to... but then I started to hear singing!"
    with vpunch
    mc "Y-Yeah, that's right! The singing was so loud that I couldn't help but find the source!"
    show story 026-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Ohhh, okay!"
    show story 026-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "That makes perfect sense! If I were you, I'd probably do the same!"
    show story 026-55 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mc "(Look at her little fox nipples...)"
    mc "(They look so nice and soft... I want to squeeze them so bad...)"
    show story 026-53 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    cele "Well, you certainly scared the crap out of me!"
    show story 026-56 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "To be honest, I thought you were some evil human poachers who go out of their way to catch and enslave fox girls!"
    show story 026-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "W-What!?"
    mc "I'd never do something like that!"
    show story 026-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Hehe~! I know~!"
    show story 026-56 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "You're a good person, [mc]! Even though you're the crappiest peddler I've ever met!"
    show story 026-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Y-Yeah... A {i}good{/i} person... with {i}good{/i} intentions..."
    mc "I better return home before I feel any more guilty..."
    show story 026-56 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Hold on..."
    cele "Didn't you say that you needed a bath?"
    show story 026-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Huh?"
    mc "Well, yeah... I still do..."
    show story 026-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Then come on!"
    show story 026-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Take off your clothes and join me in the lake! The water feels good tonight!"
    show story 026-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "You want me to join you in your bath!?"
    show story 026-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Suuure, why not?"
    show story 026-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "I'm a fox girl who believes in efficiency! No point in running home to wash yourself if you can just do it right here!"
    show story 026-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "And you don't think it's, uh, weird? You know, to bath together with a man you've only just met..."
    show story 026-56 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Why are you talking as if I should be worried?"
    show story 026-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Like I said, you're a good person, [mc]! I {i}trust{/i} you completely!"
    show story 026-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You're surprisingly naive..."
    with vpunch
    mc "Wait, are you saying you don't consider me a threat as a man!"
    show story 026-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Of course not!"
    show story 026-56 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "What kind of boss would I be if I were afraid of my measly apprentice?"
    show story 026-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You little..."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    "I stripped out of my clothes and hopped into the water with her..."
    "Celestia didn't seem to mind at all... She continued to scrub herself in the lake's waters..."
    "Naturally, my dick was already fully engorged... I wanted to slide myself into her pussy right then and there..."
    $ renpy.pause(1, hard=True)
    show story 026-60 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    cele "Ah, doesn't this feel great?"
    cele "Bathing in the moonlight... Hearing the sound of the crickets... Nature at it's finest!"
    show story 026-61 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "What do you think, [mc]? Living as a half-breed isn't so bad is it?"
    show story 026-62 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Huh...?"
    show story 026-63 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh, yeah sure... Nature's bounty sure is wonderful..."
    show story 026-64 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Now you're learning the way of a half-breed, [mc]!"
    show story 026-67 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "You see, all those material things you humans are so obsessed with is obsolete!"
    cele "What matters is living your best life! Experiencing new things and going on amazing adventures!"
    show story 026-65 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I really don't want to hear that coming from you..."
    show story 026-66 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "..."
    show story 026-67 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Hey, [mc]..."
    show story 026-68 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Mind scrubbing me while you're here?"
    show story 026-65 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Y-You want me to scrub you!?"
    show story 026-69 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Uh, sure... I'll just..."
    $ renpy.pause(.5, hard=True)
    show story 026-70 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show cele01_05_01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "There..."
    cele "Oooh..."
    cele "[mc], you have such firm hands..."
    mc "..."
    mc "(Her skin is silky smooth...)"
    mc "(Are all half-breeds like this? Does she not care where I'm touching?)"
    mc "(Damn that, fox girl... Does she seriously not consider me as a man!?)"
    hide cele01_05_01
    cele "..."
    show story 026-71 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "So [mc]..."
    cele "You're coming back to help me peddle again, right?"
    show story 026-72 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Huh?"
    mc "Oh, about that..."
    mc "Honestly, peddling feels like a waste of time..."
    mc "Like I said before, I don't mind helping you occasionally but I don't want it to be a permanent thing."
    show story 026-73 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Really, [mc]?"
    cele "Even though you're molesting me right now?"
    show story 026-74 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "If I scream really, really loud... I wonder how long it'll take for someone to come find us?"
    $ renpy.pause(.5, hard=True)
    show story 026-57 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    with vpunch
    mc "H-Hold on! I wasn't doing anything weird like that! I was just scrubbing you!"
    show story 026-75 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Hehe~! But wasn't your dick rubbing my butt just now~!?"
    show story 026-77 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Gee, what should I do~!? My shameless apprentice is thinking about raping me~! Isn't that like a serious crime or something~!?"
    show story 026-78 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You little shit..."
    mc "This was all planned, wasn't it..."
    show story 026-77 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Hehe~! Maybe~!"
    show story 026-75 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "But I guess that means you'll be reporting to work again, huh [mc]?"
    show story 026-78 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Goddamnit..."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    $ renpy.end_replay()
    play music "audio/days.mp3"
    jump parklabel_04

label cele02_01:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 027-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    cele "..."
    show story 027-02 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    cele "I better take these down..."
    show story 027-03 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    cele "..."
    show story 027-04 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "*Yawn*"
    mc "Apprentice [mc], reporting for duty..."
    $ renpy.pause(1, hard=True)
    play music "audio/celestia.mp3"
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 027-05 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    with vpunch
    cele "H-Hey!"
    cele "What do you think you're doing trying to scare me like that!"
    show story 027-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Huh?"
    mc "What's that in your hand?"
    show story 027-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "You mean this...?"
    show story 027-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Oh... Just very important documents that you shouldn't concern yourself over..."
    show story 027-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    cele "Wait, don't try to change the subject! Why are you here!?"
    show story 027-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Don't you remember? You said that you wanted to meet up tonight."
    show story 027-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Oh, was that today...? I totally forgot!"
    show story 027-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Excellent work, [mc]! Your enthusiasm for peddling is praiseworthy!"
    show story 027-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Riiight..."
    mc "Why are we always meeting out this late, anyway?"
    mc "I'm tired, you know? Unlike you, I don't sleep during the day."
    show story 027-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Oh, about that..."
    show story 027-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Maybe I'm nocturnal! You know, to better hunt during the night while my prey is fast asleep!"
    show story 027-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Sure, sure..."
    mc "So what are you going to make me do this time?"
    mc "Let me guess, more dumpster diving?"
    show story 027-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    cele "Eh!? No way! Definitely don't touch the trash cans tonight!"
    show story 027-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Er, I mean... Today, we're jumping straight to the fun stuff! You know, {b}selling{/b} our goods!"
    show story 027-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh boy... I'm {i}sooo{/i} excited..."
    show story 027-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "As you should be!"
    show story 027-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Today, we'll be going to [yel]City Hall{/color} to make some cash!"
    show story 027-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Wait, you want to go to City Hall at this hour?"
    show story 027-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Yeah, why not?"
    show story 027-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "No reason..."
    mc "I just... always seem to have bad experiences every time I go there at night..."
    show story 027-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Hehe~!"
    cele "Then let's get to it already~! Time to make ourselves some moola~!"
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    stop music fadeout 3.0
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    play music "audio/days.mp3"
    jump streetlabel_04


label cele02_02:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 027-17 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/casual.mp3"
    cele "..."
    mc "..."
    show story 027-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "So is it normally supposed to be this slow?"
    show story 027-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "What do you mean?"
    show story 027-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "There's literally no one outside right now..."
    mc "How the heck are we going to sell anything if there aren't any customers around?"
    show story 027-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Patience, my dear apprentice..."
    show story 027-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "You'll see! We'll sell and make it rich someday!"
    show story 027-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Everyone's already in bed... We're just wasting our time here."
    show story 027-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "If we came here during the morning, it'd be a completely different story."
    show story 027-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Gee, [mc]..."
    cele "For a young human, you sure are negative!"
    show story 027-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I'm just being realistic..."
    show story 027-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "No one's going to come out this late at night..."
    show story 027-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Don't lose faith~! Don't give up~!"
    cele "It’s about drive~! It’s about power~! We stay hungry, we devour~!"
    show story 027-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Ugh..."
    mc "What the heck are we even selling here, anyway?"
    show story 027-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "I'm glad you asked, [mc]!"
    show story 027-23 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    cele "Today, we'll be selling these genuine, hand-crafted... {b}voodoo dolls{/b}!"
    show story 027-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Perfect for when you want to put a curse on someone you hate!"
    show story 027-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I hope you're kidding... Voodoo dolls...? That's the most ridiculous thing I've ever heard..."
    show story 027-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Of course not, my apprentice!"
    show story 027-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "This voodoo doll contains magical properties! If you say a person's name three times fast, they'll be cursed!"
    show story 027-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh god..."
    mc "Who would be stupid enough to buy one of these..."
    show story 027-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "What? Don't believe me?"
    show story 027-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Care to test your luck, then!? Maybe you should buy one and see for yourself!"
    show story 027-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "If nothing bad happens to you within 24 hours, I {i}promise{/i} I'll give you a full refund!"
    show story 027-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "No one's going to believe that bullshit! Much less pay you good money for it!"
    show story 027-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Hehe~!"
    cele "Then shall I put your name into this voodoo doll~? Maybe then, you'll regret doubting me~!"
    show story 027-27-1 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu:
        "It's bullshit..." if True:
            $ renpy.fix_rollback()
            show story 027-25 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "You're full of it."
            show story 027-26 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            cele "Oh, really?"
            show story 027-24 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            cele "Don't say I didn't warn you! If something bad happens in the near future, don't blame me!"
        "Maybe she's telling the truth..." if True:
            $ renpy.fix_rollback()
            show story 027-25 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            mc "Oh, wooow... Aaanything but that... I'm quaking in my loafers."
            show story 027-26 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            cele "Hehe~!"
            show story 027-24 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            cele "Don't worry, [mc]~! You're my precious apprentice! I'd {i}never{/i} do anything that would endanger your life~!"
    $ renpy.pause(.5, hard=True)
    show story 027-28 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    gen7 "Oi, you over there!"
    $ renpy.pause(.5, hard=True)
    show story 027-29 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    cele "..."
    show story 027-30 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    cele "Awesome! Potential customers!"
    show story 027-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Good luck on the sale, [mc]! Don't screw this up!"
    show story 027-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Uhhh..."
    mc "They don't look like customers, Celestia..."
    mc "If anything... they kind of look pissed..."
    show story 027-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    gen7 "Hey, fox girl!"
    gen7 "I want my money back on that exploding beanie doll you sold me the other day!"
    show story 027-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Sorry, pal! But I live by a strict policy called, {b}NO REFUNDS{/b}!!!"
    show story 027-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "[mc], I forgot to mention that you'll meet some losers like this every once in a while."
    show story 027-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    gen7 "Oh, I better get my money back!"
    gen7 "That doll almost killed my best friend! He gave it a hug and it exploded right on his face!"
    show story 027-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen10 "Poor bastard will never be the same again..."
    show story 027-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh god..."
    mc "So the dumb things do work..."
    show story 027-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Ugh, unruly customers are the worst..."
    show story 027-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Didn't you hear what I said... no returns and no refunds... So you better beat it before I get angry!"
    show story 027-40 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    gen10 "You little bitch!"
    gen10 "If you don't give us back our money, I'm going to..."
    show story 027-41 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    gen7 "Hold on a second..."
    gen7 "This chick... Don't she look like that girl on the [yel]posters{/color}?"
    show story 027-42 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    cele "Eh?"
    show story 027-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen7 "Hmm..."
    gen7 "Now that I think about it..."
    show story 027-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "{i}Poster{/i}...?"
    mc "Uh, Celestia... What are they talking about?"
    show story 027-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    cele "Scary!!!"
    show story 027-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "[mc], these are those evil human poachers I told you about!"
    show story 027-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "You know, the ones who go out of their way to catch and enslave fox girls for reasons too gruesome to say!"
    show story 027-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen7 "Oh, I'm going to catch you, alright!"
    gen7 "I'm going to catch you, turn you in to the Holy Knights, and let them have their way with you, you lying fox!"
    show story 027-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen10 "No, screw that! Forget about the bounty!"
    gen10 "This half-breed is tame! If we capture her, she can fetch an even higher price on the black market!"
    gen10 "Rich fucks love 'em! Since they aren't humans, they aren't afforded the same rights that we have!"
    show story 027-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen7 "Hmmm, that ain't a bad idea..."
    gen7 "A good-for-nothing half-breed like you can make us a lot of money with your body! Hahaha!"
    show story 027-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    cele "Scary!!!"
    cele "Humans sure are dangerous creatures!!!"
    show story 027-52 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Now hold on just a second..."
    mc "There's no need to be irrational... Sure, maybe she's not the most likeable character, but she's still a living, breathing resident of Scarlet!"
    show story 027-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    cele "Yeah! You tell 'em, [mc]!"
    show story 027-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "In fact, I don't mind letting you take care of these bums in my stead!"
    show story 027-55 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Wait, what?"
    show story 027-56 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    gen11 "Aye, I won't let you talk down to my boss like that!"
    gen11 "That is why I, her precious apprentice, shall defend her honor by kicking both of your asses right here and now!"
    show story 027-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    gen7 "You fucking bastard..."
    show story 027-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    gen10 "You think we're afraid of you!?"
    show story 027-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hey, wait a minute!"
    mc "I'm saying that we shouldn't condone violence! We should talk out our problems, and..."
    show story 027-59 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    gen11 "Aye, I'm done talking to you bums!"
    gen11 "Raise up your dukes! It's 'bout damn time we settle this with fisticuffs!"
    show story 027-60 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Oi, Oi!!!"
    mc "You aren't making this situation any easier!!!"
    show story 027-61 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen10 "Fuck you, asshole! You want to throwdown!?"
    show story 027-62 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen7 "You better stay out of this if you know what's good for you!"
    show story 027-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "You bastards are in big trouble now!"
    show story 027-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Once my apprentice gets angry, there's no stopping him! He undergoes training under a waterfall every morning to calm his raging heart!"
    show story 027-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "So yeah, I'll leave these goons to you, [mc]!"
    show story 027-55 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Celestia, for the love of god... stop it..."
    show story 027-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "If you need some help, don't worry! I'll come save you... {i}probably (not){/i}!"
    show story 027-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Later, everyone!"
    $ renpy.pause(.5, hard=True)
    show story 027-63 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "That little..."
    show story 027-64 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    gen10 "Hey, she's getting away!!!"
    show story 027-65 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    gen7 "Don't bother..."
    gen7 "You heard what she said... We're going to have to deal with her apprentice first before we get to her!"
    show story 027-66 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "God fucking damnit..."
    stop music fadeout 3.0
    show story 027-67 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Huh?"
    $ renpy.pause(.5, hard=True)
    show story 027-68 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play music "audio/belle.mp3"
    mc "It's... raining...?"
    $ renpy.pause(.5, hard=True)
    show story 027-69 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mv2 "...I won't forgive you."
    mv2 "You're all trash... the lot of you..."
    show story 027-70 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    gen10 "Guh...!"
    show story 027-71 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    gen7 "W-Wha...!?"
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 027-72 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    with vpunch
    mc "What the hell just happened!?"
    show story 027-73 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mv2 "Don't worry, they're still alive."
    mv2 "Unlike {i}her{/i}, I don't kill without reason... Even if they are bottom of the barrel filth."
    $ renpy.pause(.5, hard=True)
    show story 027-74 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "You..."
    mc "Thank you for helping me..."
    show story 027-75 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "...Don't be a fool."
    mv2 "I'm not your ally. Get in my way, and I'll see you to an early grave."
    show story 027-74 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "*GULP*"
    mc "Are you an... {i}angel{/i}?"
    show story 027-76 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "...Why?"
    mv2 "Just why would you choose to align yourself with {i}her{/i}?"
    show story 027-77 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Huh?"
    show story 027-76 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "'[yel]The False Goddess{/color}'..."
    show story 027-75 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "Has she already seduced you with her words...?"
    show story 027-76 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "Had I realized it sooner, I would have stopped you from falling for her trap."
    show story 027-75 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "Now, it's too late... Even I don't know what will become of you..."
    show story 027-74 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I don't understand..."
    show story 027-77 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "..."
    show story 027-76 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "Telling you now would only endanger your life even further... I'm certain that you'll learn the truth, soon enough..."
    show story 027-75 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "Know that the more you assist the '[yel]False Goddess{/color}', the further you lead Scarlet down its spiraling path of despair..."
    $ renpy.pause(.5, hard=True)
    show story 027-78 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Wait a second... Why does it seem like you know who I am?"
    mc "Are you... someone I've met before?"
    show story 027-80 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "..."
    show story 027-79 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "You are but a tadpole, frolicking in your little pond..."
    mv2 "But its because of your feebleness that you are still alive today..."
    show story 027-80 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "...Know that there is no place for 'our kind' in this modern day of Scarlet."
    show story 027-78 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Who are you?"
    show story 027-80 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "..."
    show story 027-79 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "I'm the '[yel]hero{/color}' of Scarlet..."
    show story 027-80 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv2 "...and the only hero that it needs."
    $ renpy.pause(.5, hard=True)
    show story 027-81 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    $ renpy.pause(.5, hard=True)
    show story 027-82 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "The rain stopped..."
    mc "I should probably go... The Holy Knights won't believe my story even if I did tell them what happened..."
    mc "She said that she didn't kill them, so they should wake up... hopefully..."
    $ renpy.pause(1, hard=True)
    $ renpy.end_replay()
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    stop music fadeout 3.0
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    play music "audio/days.mp3"
    jump streetlabel_01

label cele02_03:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 027-83 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    cele "..."
    show story 027-84 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Whew, looks like I'm safe..."
    show story 027-85 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Poor, [mc]... He's probably dead by now..."
    show story 027-86 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    cele "..."
    show story 027-87 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    cele "WAAAHHH!!! I'M SO SORRY, [mc!u]!!! WAAAHHH!!!"
    cele "ANOTHER PERSON IS DEAD BECAUSE OF MEEE!!! WAAAAHHH!!!"
    show story 027-88 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "..."
    show story 027-89 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "I guess a eulogy is in order..."
    show story 027-90 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    cele "Ahem... Where should I start?"
    show story 027-91 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    cele "[mc] was a good man... a kind man with a gentle soul..."
    cele "Sure, he was pretty stupid... naive... a simp... and the worst peddler I'd ever seen..."
    cele "But gosh darn it, he was the best apprentice a fox girl could've asked for! His sacrifice will never be forgotten!"
    show story 027-92 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 027-93 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "Boo."
    $ renpy.pause(.5, hard=True)
    play music "audio/celestia.mp3"
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 027-94 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    with vpunch
    cele "WAAAHHH!!!"
    cele "[mc!u]!!! IS THAT REALLY YOU!!!??? YOU'RE REALLY ALIIIVEEE!!!???"
    show story 027-95 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "No thanks to you, you little shit!"
    mc "Why the hell did you abandon me like that!?"
    show story 027-94 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    cele "WAAAHHH!!!"
    cele "YOU'RE SOOO CRUEL!!! DID YOU TURN INTO A [yel]GHOST{/color} TO HAAAUNTTT MEEE~~~!!!"
    show story 027-95 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Stop that or you'll wake everyone in the neighborhood up."
    show story 027-96 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Hehe~ Alrighty then~!"
    show story 027-97 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Woops, almost forgot about my mask..."
    show story 027-98 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "You got some explaining to do."
    show story 027-99 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Look, I'm sorry [mc]..."
    show story 027-100 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "...but I always run away when I'm under stress!"
    cele "It's a psychological phenomenon, really... You can't judge me for that!"
    show story 027-101 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Screw you, Celestia!"
    mc "I thought we were friends! But clearly, you don't think of me that way!"
    show story 027-102 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "[mc], you are my dear friend! My {i}best{/i} friend, actually!"
    show story 027-103 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Then why the hell did you bail on me like that!?"
    show story 027-102 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "I admit it! I'm a coward, alright!?"
    show story 027-104 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "When my fight or flight instinct kicks in, I just have to run and run until I can't run any longer!"
    show story 024-142 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    cele "So pleeeaaassseee forgive me! It's not my fault I'm like this! I'm hardwired to be this way because of my foxy nature!"
    cele "Blaming me for that situation is the same as blaming your cat for eating food you left on the table! It just isn't right!"
    cele "You're discriminating against me for something I have no control over! WAAAHHH!!! LIFE ISN'T FAIR!!!"
    show story 024-155 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah, okay... Sounds like BS to me!!!"
    show story 024-142 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    cele "WAAAHHH!!! I'M SOOO SOOORRRYYY!!!"
    cele "I'M GOING TO KEEP CRYING UNTIL YOU FORGIVE ME!!! WAAAHHH!!!"
    cele "THAT'S RIGHT I WON'T STOP!!! AND I HOPE THE PEOPLE LISTENING IN KNOW THAT YOU'RE MAKING A CUTE GIRL CRY!!!"
    show story 024-155 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    menu cele02_03_menu:
        "Don't forgive her..." if True:
            mc "Oh, please!"
            mc "Your crocodile tears won't work on me!"
            show story 024-142 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            with vpunch
            cele "WAAAHHH!!! I'M SOOO SOOORRRYYY!!!"
            cele "THAT'S WHY I'M GOING TO KEEP CRYING UNTIL YOU FORGIVE ME!!! WAAAHHH!!!"
            show story 024-155 with Dissolve(.5)
            $ renpy.pause(.5, hard=True)
            jump cele02_03_menu
        "Forgive her..." if True:
            pass
    mc "..."
    mc "Fine, I get it..."
    show story 027-102 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Eh?"
    cele "So you'll forgive me?"
    show story 027-103 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah, yeah... I forgive you..."
    mc "Not like I have a choice, anyway."
    show story 027-104 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Hehe~! You sure you won't regret it~!?"
    show story 027-103 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 027-105 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    cele "Amazing, [mc]!"
    show story 027-106 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "You're the best apprentice a fox girl could ever ask for!"
    show story 027-107 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah... I guess I am..."
    show story 027-108 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Hehe~!"
    show story 027-106 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    cele "Now then~ About our next assignment~!"
    $ renpy.pause(1, hard=True)
    stop music fadeout 3.0
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    "Even though she betrayed me..."
    "Even though it was hard to trust her..."
    "I believed Celestia's words that night... I believed that she did consider me her friend... Maybe the only one she had..."
    $ renpy.end_replay()
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump streetlabel_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
