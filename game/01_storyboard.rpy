label prologue:

    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 10
    mv "..."
    mv "I see..."
    mv "I've finally found you, at last..."
    mv "Can you hear me?"
    mv "...if so, what is your name?"
    $ mcname = renpy.input("My name is... (Default: Sieg)") or "Sieg"
    $ persistent.repname1 = mcname
    mc "..."
    mc "I'm [mc]..."
    mc "Why do I keep hearing your voice in my dreams?"
    mv "..."
    mv "You will learn soon enough..."
    mv "But not now..."
    mc "...Why?"
    mv "Because you're going to wake up..."
    mc "What?"
    mv "Wake up..."
    mv "Wake up... Wake up..."
    scene whitescreen with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 001-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    with vpunch
    este "I said wake up!"
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 001-02 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play music "audio/estelle.mp3"
    mc "Ugh, Estelle..."
    mc "Did you have to barge into my room like that?"
    mc "I was having a good dream..."
    show story 001-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Good morning to you too, [mc]..."
    este "Well, it's actually noon, now..."
    este "More importantly, shouldn't you be grateful that someone as cute as me is willing to take the time to wake you up?"
    show story 001-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    if (inc == True):
        "This is my little [sil], [yel]Estelle."
    elif True:
        "The girl in front of me is named [yel]Estelle."
        $ sil = renpy.input("She's my little... (Default: roommate)") or "roommate"
        $ persistent.repname2 = sil
        "Yeah, Estelle's my little [sil]..."
        $ bil = renpy.input("...and if she's my little [sil], that means I'm her big... (Default: roommate)") or "roommate"
        $ persistent.repname4 = bil
        "That's right, I'm her big [bil]."
    "She attends some fancy magic academy in the hopes of becoming a mage, someday..."
    "However..."
    "Truth be told, her magic ability isn't very impressive..."
    "...and of course, she'll never admit that."
    show story 001-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "Ew, what are you mumbling about?"
    este "Let me guess, you're mad at me because I interrupted your pervy dream!"
    este "Ugh, why do I have to live with such a pervert?"
    show story 001-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "I don't know when it happened but Estelle's attitude toward me has been awful, lately..."
    "I guess I can't blame her..."
    "I'm certainly not the type of person she can be proud about..."
    "What a shame, considering how close we were back when we were kids..."
    mc "..."
    with vpunch
    mc "Goddamnit, Estelle!"
    mc "Can you stop berating me and just tell me why you're here!"
    show story 001-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Eh?"
    este "D-Don't yell at me..."
    este "[yel]She{/color} wants to have a word with the two of us together..."
    este "...so I came here to get you."
    show story 001-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    if (inc == True):
        "By {b}she{/b}, she's referring to [mil!c]..."
    elif True:
        $ mil = renpy.input("By {b}she{/b}, she's referring to our... (Default: landlady)") or "landlady"
        $ persistent.repname3 = mil
    mc "..."
    mc "Nah, I don't feel like speaking to [mil!c]..."
    mc "I'm going back to bed."
    show story 001-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "Eh!?"
    este "You can't do that!"
    este "[mil!c] said that it was very important!"
    show story 001-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    este "..."
    show story 001-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "I-I'm going ahead of you..."
    este "...so you better not be late."
    show story 001-09 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3
    mc "..."
    mc "I suppose I should see what she wants."
    mc "But first, let's head to the bathroom for a shower."
    mc "...I stink."
    scene mcroom_day with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/days.mp3"
    play sound "audio/ding.mp3" volume 3
    show screen tutorialscreen_01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    while endgame != True:
        pause

label prologue_02:

    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    scene bathroom_day with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    mc "Let's wash up."
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play sound "audio/shower.mp3" volume 2
    "As the stream of hot water splashes across my skin, I'm reminded of the depressing state of my livelihood..."
    "Why was it that I was afraid of seeing [mil!c]?"
    "It's not like she's some terrible person..."
    "...No, if anything, she's too {i}nice{/i} of a person."
    "If it were up to me, I would have kicked myself out of this house a long time ago..."
    stop sound fadeout 1
    $ renpy.pause(.5, hard=True)
    scene bathroom_day with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/days.mp3"
    mc "..."
    mc "How long am I going to stay like this?"
    mc "I have to do better..."
    mc "Not just for [mil!c] and Estelle, but for myself..."
    jump bathroomlabel

label prologue_03:

    hide screen status01
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    scene livingroom_day with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "Huh?"
    mc "Where is everyone? I thought they'd be here by now..."
    mc "Maybe they're somewhere else in the house..."
    mc "*Sigh* I better go find them."
    jump livingroomlabel

label prologue_04:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/undress.mp3" volume 3
    "As I crept closer to her bedroom, I hear movement coming from within [mil!c]'s bedroom..."
    "There was also the sound of gentle fabric being shuffled around..."
    "Her door was slightly ajar..."
    "I don't know what compelled me to do it, but I found myself tip-toeing closer and closer to have myself a peek..."
    stop music fadeout 1
    $ renpy.pause(1, hard=True)
    show story 001-10 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 001-11 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 001-12 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 001-13 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 001-14 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    with vpunch
    silv "Eh?"
    silv "I-Is someone there?"
    mc "..."
    with vpunch
    mc "C-Crap, I've been found out..."
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 001-15 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/silvia.mp3"
    silv "..."
    show story 001-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "[mc]..."
    silv "Were you spying on me just now?"
    show story 001-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "S-Sorry, I should have knocked first..."
    mc "Estelle said that you were looking for me..."
    mc "...so I figured you'd be in your room."
    show story 001-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "That's okay..."
    silv "You're at that age, after all..."
    show story 001-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "And it's perfectly healthy to be curious!"
    silv "...even if that object of curiosity is your own [mil]!"
    show story 001-18 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    "I can't think straight..."
    "They're so damn huge..."
    "How have I not noticed how big they were before?"
    show story 001-16 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    silv "Uh, [mc]..."
    silv "Eyes up here, hun."
    show story 001-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "S-Sorry..."
    mc "So, uh, what did you want to speak with me about?"
    show story 001-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hehe..."
    silv "You know, I just realized that it's been a while since we last spoke like this..."
    silv "Usually, you're holed up inside your bedroom with your video games."
    show story 001-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah..."
    mc "I should really get out more..."
    show story 001-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "That's alright..."
    silv "I'm just worried about you, you know?"
    silv "I'd really just like it if you sat down and ate with us again..."
    show story 001-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I'll... think about it..."
    mc "So what do you need from me?"
    show story 001-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Ah..."
    silv "There's something important that I have to discuss with you and Estelle..."
    silv "But before that, can you go to the living room and wait for me?"
    show story 001-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Huh?"
    mc "Why can't we talk here?"
    show story 001-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Er..."
    silv "Because I still need to put on my clothes..."
    show story 001-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "R-Right... I'll see you soon..."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    $ renpy.end_replay()
    stop music fadeout 3
    jump hallwaylabel_01

label prologue_05:

    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 001-20 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    mc "I can't believe what I just saw..."
    mc "My first pair of {i}real{/i} tits in the flesh..."
    mc "...and they just so happen to belong to my own [mil]."
    mc "..."
    "Yeah, that just sounds pathetic..."
    "...but not as pathetic as wanting to take care of this raging boner of mine by jacking off to her."
    este "Ew..."
    este "Why do you have a disgusting grin on your face?"
    este "Let me guess, you're thinking about something perverted again."
    show story 001-21 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Geez, Estelle..."
    mc "Here you are, telling me not to be late..."
    mc "...and somehow, you end up being even later than me!"
    show story 001-22 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    silv "Settle down, you two."
    silv "I have something very important to discuss with you both."
    show story 001-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    play music "audio/sad.mp3"
    mc "..."
    "There was a grim look on her face..."
    "Normally, [mil!c] is the most cheerful person you'd ever meet..."
    "Whatever she had to say was going to be bad news..."
    show story 001-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "What's wrong, [mil!c]?"
    show story 001-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hmm..."
    silv "I don't know how to say this, but..."
    silv "It appears that someone has triggered my [yel]Scarlet Contract{/color}..."
    show story 001-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...Your Scarlet Contract?"
    show story 001-27 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    este "Ooh, ooh!"
    este "I know the answer to this one!"
    este "A Scarlet Contract is the bounty placed on a person living in Scarlet since their birth..."
    este "Basically, if you're of age and unwed, you're legally able to be bought and sold as a slave..."
    este "And since [mil!c] had her contract triggered, that means that she'll..."
    show story 001-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "She'll..."
    show story 001-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "..."
    mc "..."
    show story 001-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You're joking, right?"
    mc "Are you saying that someone is going to take you away from us?"
    show story 001-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Unfortunately, that is the case..."
    silv "It hasn't been finalized yet, but once that person puts up the money, I cannot refuse him."
    silv "That is the [yel]Scarlet Law{/i}..."
    show story 001-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "I didn't know what to say..."
    "It felt as though my lungs were being forcibly torn apart..."
    "My rock, and the only woman to have ever shown me such unconditional love was going to be taken away from me just like that..."
    "All because of a piece of paper and some ridiculous law..."
    show story 001-30 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    este "NEVER!!!"
    este "I won't let that happen!"
    este "You can't leave us, [mil!c]!"
    este "We need you here!"
    show story 001-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Estelle..."
    silv "Unfortunately, there's more..."
    silv "Apparently, this same buyer is interested in {i}you{/i}, as well..."
    silv "He seems to have a... er... {i}fetish{/i}... for the relationship we share..."
    show story 001-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "N-No..."
    este "I won't go..."
    show story 001-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Honey, you can't refuse..."
    silv "You are unwed and legally of age..."
    silv "The law of the land dictates that you must honor your contract..."
    silv "...or else, a [yel]terrible curse{/color} will befall you."
    show story 001-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "Is this really happening?"
    "The horrible news is too surreal..."
    "Although my lips moved to protest, no words could come out of my mouth..."
    silv "..."
    show story 001-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "The buyer is already preparing the funds..."
    silv "You and I will have no choice but to be sold to him."
    show story 001-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "When that happens, you'll be on your own, [mc]..."
    silv "I'm sorry that I won't be able to take care of you, anymore."
    show story 001-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "I'm going to lose [mil!c]... Estelle..."
    "I'll never see them again..."
    "I feel... light-headed... like I'm going to faint..."
    "This pervert was going to buy and snatch them up, just like that..."
    "And he wasn't going to buy them out of love..."
    "He was going to buy them to fuck them..."
    "The sick bastard was probably going to use them like sex slaves, fucking them repeatedly on a daily basis..."
    "And if he ever got tired of them, he'd just open his wallet and find someone new..."
    show story 001-31 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    este "HEY, [mc!u]!!!"
    este "SAY SOMETHING, WON'T YOU!?"
    este "YOU'RE A MAN, SO TELL HER THAT YOU'LL NEVER LET US GO!!!"
    show story 001-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    silv "..."
    "[mil!c] stared at me hard, awaiting my much-needed chivalry..."
    "But no matter how much I tried to speak, I simply couldn't muster up the words..."
    "My lips just refused to budge..."
    "My mind was lost in a daze, struggling to process what was going on..."
    show story 001-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "That's okay..."
    silv "I understand that it's a lot to take in, [mc]..."
    silv "The deal won't be finalized for another few weeks..."
    silv "I just wanted to tell you ahead of time, [mc], so that you can properly plan for our departure..."
    silv "You're going to have to find yourself a job and support yourself..."
    show story 001-33 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    silv "I'm so sorry, sweetheart..."
    silv "I always envisioned that the three of us would be together..."
    silv "But it appears that I won't be around to take care of you anymore..."
    show story 001-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Y-You can't be serious..."
    este "Can't you just tell him that you don't want to be his slave?"
    este "If they have any sense of decency, they'll stop what they're doing once realize that they're tearing us apart..."
    show story 001-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Estelle..."
    silv "Unfortunately, people aren't that simple..."
    silv "We don't know what kind of person our buyer will be..."
    silv "He may be cruel... or kind... Either way, there's nothing we can do about it..."
    silv "Our lives will be in {i}his{/i} hands, end of story."
    show story 001-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "I-I don't care if he's nice or not..."
    este "I just don't want the three of us to be separated..."
    este "It's not fair..."
    show story 001-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Oh, I understand, Estelle..."
    silv "But to be honest, these last few years have been rough on me..."
    silv "Every day is pretty much the same deal..."
    silv "I go to work, come home, have dinner, and sleep..."
    silv "...rinse and repeat."
    silv "I could do with a change in the monotony..."
    show story 001-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Who knows? Maybe I'll enjoy living with... someone I don't know..."
    silv "M-Maybe it'll be interesting to experience something new..."
    show story 001-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "She says that, but I can tell that she isn't being completely truthful..."
    "I think that [mil!c] was trying to convince herself that everything was going to be alright."
    "But I wasn't certain if she was lying to be optimistic..."
    "...or if she was lying because she didn't want me to worry."
    show story 001-35 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 001-36 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "This is... too much..."
    mc "This can't be... real..."
    show story 001-37 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3
    "My body goes numb..."
    "My eyes slam shut. The muscles in my legs turn to jelly..."
    play sound "audio/fall.mp3" volume 3
    "I fall to the ground, but can hear both [mil!c] and Estelle cry out my name..."
    $ renpy.pause(3, hard=True)
    show mcroom_day with Dissolve(3)
    $ renpy.pause(3, hard=True)
    mc "..."
    "I don't know how long I was out, but I groggily realize that I'm back in my bed..."
    "Was it all a dream?"
    "No, that's just wishful thinking..."
    "I'm going to lose both my [sil] and my [mil], and there's nothing I can do about it."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "Judging from the silence, both [mil!c] and Estelle were likely out of the house."
    "After a bit of contemplating, I somehow find the strength to stand up and walk..."
    $ renpy.pause(1, hard=True)
    show story 001-38 with Dissolve(3)
    $ renpy.pause(3, hard=True)
    play music "audio/wind.mp3" volume 2
    mc "..."
    show story 001-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Sure is beautiful out today, isn't it?"
    mc "Has the weather alway been this good?"
    show story 001-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "What have I been doing with my life?"
    mc "After I dropped out of school, it's like I've lost all of my ambition..."
    mc "Nowadays, my days are wasted hiding in my bedroom and playing video games..."
    show story 001-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Everyone moves on from their homes, eventually..."
    mc "...I just didn't think it'd end up being like this."
    mc "Maybe if I were around more often, I could have appreciated their presence all the more..."
    show story 001-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "They say that you don't know what you got 'til it's gone..."
    mc "But what else can I do but watch them go?"
    mc "This is the Scarlet Law..."
    mc "Everyone born into the country has a Scarlet Contract placed on their heads..."
    mc "And if someone matches the price on their contract, they have every right to buy and own them."
    mc "Maybe it's unfair, but that's just how things are around here..."
    show story 001-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Maybe it won't be so bad..."
    mc "Maybe they'll move to a tropical paradise where it's warm all year round..."
    mc "It'll be like starting a whole new adventure for them, right?"
    stop music fadeout 3.0
    $ renpy.pause(.5, hard=True)
    scene whitescreen with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 001-40 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 001-41 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 001-42 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    show story 001-43 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    este "You got to help us, [mc]!"
    este "I don't want to leave Scarlet..."
    este "I want us to be together, forever..."
    show story 001-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I'm sorry, you two..."
    mc "There's nothing that I can do..."
    show story 001-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "That's alright, honey..."
    silv "Remember to eat well while we're gone..."
    silv "You have to keep your body healthy, okay?"
    silv "And know that Estelle and I will always love you..."
    show story 001-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "No..."
    show story 001-45 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "NOOO!!!"
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 001-38 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/wind.mp3" volume 2
    mc "..."
    "The more I thought about it, the more my body started to tremble..."
    "I stared down off the roof, directly at the brick and stone road..."
    "I've always been afraid of heights..."
    "...but today, the fall looked especially tempting."
    menu:
        "End the pain..." if True:
            $ renpy.block_rollback()
            show story 001-46 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            stop music fadeout 3.0
            mc "..."
            mc "Goodbye, cruel world..."
            scene black with Dissolve(3)
            $ renpy.pause(3, hard=True)
            play sound "audio/fall.mp3" volume 3.0
            $ renpy.pause(1.5, hard=True)
            "Suicide is no laughing matter."
            "If you or someone you know is struggling emotionally or having a difficult time, there is help available."
            "The National Suicide Prevention Lifeline (US) provides 24/7, free and confidential support for people in distress."
            "You can contact them over the phone at: 1-800-273-8255"
            "Stay safe."
            $ renpy.pause(1, hard=True)
            show gameover with Dissolve(3)
            $ renpy.pause(3, hard=True)
            play music "audio/sad.mp3"
            while endgame != True:
                pause
        "Hold on for dear life..." if True:
            $ renpy.block_rollback()
            pass
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "How easy would it be..."
    mc "...to end my suffering."
    mc "All I'd need to do is..."
    scene whitescreen with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mv "Hold, [mc]!"
    mv "Do not give up on hope just yet."
    mv "There is still something that you can do to save them."
    show story 001-38 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    mc "Okay, yeah..."
    mc "I must really be losing my fucking mind."
    mc "Because right now, I swear I just heard a voice inside my head..."
    show story 001-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv "..."
    mv "[mc], I am not just a voice..."
    mv "I am the [yel]God of Scarlet..."
    show story 001-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "No way..."
    mc "This voice... I recognize it..."
    mc "You sound exactly like the woman I've been hearing in my dreams..."
    show story 001-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv "That's because I am that very same person..."
    mv "In this modern age, you people refer to my whispers as the Lady of the Lake."
    mv "But before your time, I once ruled this land as my own..."
    show story 001-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "What do you want from me?"
    show story 001-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv "..."
    mv "I can tell you how you can save your household..."
    mv "But alas, my power grows weak..."
    mv "I'll need your assistance if I'm to help you."
    show story 001-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "What can I do?"
    show story 001-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv "..."
    mv "You must first seek me out..."
    mv "Find me at [yel]Scarlet Park{/color}..."
    mv "Only there will I be able to help you save the ones you care about..."
    show story 001-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3
    "The strength in her voice vanished..."
    "Maybe I was losing my mind..."
    "Maybe I was going crazy..."
    "But her words felt so real, so vivid..."
    "I felt compelled to help her..."
    "The alternative would be to sit around and do nothing..."
    $ renpy.pause(.5, hard=True)
    show hallway01_day with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/days.mp3"
    mc "She said that she'll be at [yel]Scarlet Park{/color}..."
    mc "I should go find her..."
    $ renpy.pause(.5, hard=True)
    "If you ever find yourself stuck, you can check out the quest log to see what you can do..."
    "As you are probably aware, the map function is disabled during the prologue..."
    "Try finding your way to Scarlet Park on your own."
    "{b}HINT:{/b} The door in the living room will lead you outside of the house."
    $ renpy.pause(.5, hard=True)
    jump hallwaylabel_01

label prologue_06:

    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 001-47 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    mc "Alright, the Lady of the Lake said to find her at Scarlet Park..."
    mc "It's not too far from here..."
    $ renpy.pause(.5, hard=True)
    mv2 "Oh, wow!"
    mv2 "Is that really {i}you{/i}, [mc]!?"
    $ renpy.pause(.5, hard=True)
    show story 001-48 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/serena.mp3"
    mc "..."
    with vpunch
    mc "Serena!?"
    show story 001-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hey there, [mc]!"
    sere "Boy, it feels as though I haven't seen you in months..."
    sere "How's life treating you?"
    show story 001-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "This is Serena, a friend of mine who lives next door."
    "She's the same age as me, and we used to go to school together."
    mc "Hey, Serena."
    mc "Sorry, but I have to go..."
    mc "There's something that I need to take care of."
    show story 001-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    sere "Eh?"
    sere "What's the rush?"
    sere "Can't stick around to chat with an old friend?"
    show story 001-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Er..."
    mc "I've just been busy with, uh, {i}stuff{/i}..."
    "I can't tell her that I've been doing nothing except playing video games in my room all day..."
    show story 001-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hmm..."
    sere "Is everything alright?"
    sere "You look a little pale..."
    show story 001-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Yeah, I'm fine..."
    mc "I just... need to go out for a walk."
    show story 001-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    sere "[mc], you aren't in any trouble or anything, right?"
    sere "Possibly with the [yel]Powder Girls{/color}?"
    show story 001-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Powder girls?"
    mc "Who are they?"
    show story 001-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Oh, you haven't seen the news?"
    sere "The Powder Girls are a gang of thugs who have been harassing folks in our area lately..."
    sere "They seem to target men, for some reason..."
    sere "If you're in trouble with them, you can tell me..."
    show story 001-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "Serena's the type of girl who is always willing to lend a hand to her friends, but..."
    "...I just don't have the time to explain everything."
    mc "I'm sorry, Serena, but I really have to go."
    mc "We can talk about it later."
    show story 001-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    sere "You promise?"
    show story 001-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Y-Yeah..."
    show story 001-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Okay, I guess I understand..."
    sere "If you want to speak to me, you know where to find me."
    show story 001-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Right..."
    mc "Are you still working at your [yel]grandpa's convenience store{/color}?"
    show story 001-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Uh, y-yeah..."
    sere "It's just across the street..."
    sere "...so if you need anything, let me know."
    sere "See you later, [mc]."
    show story 001-47 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "Alright, now that there are no more distractions..."
    mc "Let's head over to [yel]Scarlet Park{/color}..."
    mc "To get there, [yel]all I have to do is make a left from here."
    play sound "audio/ding.mp3" volume 3
    "[yel]Serena's Character Card has been added to the Relationship Screen."
    $ seremet = True
    $ renpy.pause(.5, hard=True)
    play music "audio/days.mp3"
    jump streetlabel_01

label prologue_07:

    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show park01_day with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    mc "Well, here I am..."
    mc "But there isn't anyone else here."
    mc "..."
    with vpunch
    mc "Of course there isn't anyone here!"
    mc "Why would there be!?"
    mc "I'm just losing my mind from all the shit that's been happening!"
    scene whitescreen with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mv "Calm yourself, [mc]..."
    mv "Follow my voice... Not too far, now..."
    mv "Don't you want to save your loved ones?"
    show park01_day with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/days.mp3"
    mc "..."
    mc "She's right, I can hear her voice more clearly than before..."
    mc "I should keep searching around the park..."
    jump parklabel_01

label prologue_08:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show park04_day with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/sad.mp3"
    mc "..."
    mc "Where are you, Lady of the Lake?"
    mc "I don't know why... but I can feel that you're close..."
    mv "..."
    mv "I'm sorry, [mc]..."
    mv "...but it appears that my power is waning."
    mv "I don't have much time left before I disappear again..."
    mc "..."
    mc "Please, you can't..."
    mc "I came all this way for a chance to save [mil!c] and Estelle..."
    mv "Hmm..."
    mv "I've only just awakened, thanks to you, [mc]..."
    mv "Because of that, I believe you have a power within you that lies dormant..."
    mv "Like me, you also possess the blood of the [yel]Valla{/color}..."
    mc "V-Valla?"
    mc "I've never heard that word before..."
    mv "How strange..."
    mv "That is the name of our ancient people before we were thrown into the chaos..."
    mv "From the time of my reawakening, I can sense that our numbers have dwindled to the point of extinction..."
    mv "What a pity... though, perhaps it is for the best..."
    mc "..."
    mc "Lady of the Lake, I don't care about any of that."
    mc "You said that you could help me with my problem."
    mc "Please... You have to tell me how I can save [mil!c] and my [sil] from the Scarlet Law!"
    mv "Yes..."
    mv "The Scarlet Law is quite troublesome, even during my time..."
    mv "But with my help, it's possible to end it all."
    mv "That is why I need your assistance, [mc]."
    mv "By using your {i}power{/i}, you can call me forth..."
    mc "..."
    "This was sounding suspicious..."
    "The Lady of the Lake wasn't making any sense."
    "{b}End it all?{/b} Was she suggesting that she had the ability to stop the Scarlet Law?"
    "Even more, what {i}power{/i} of mine was she referring to?"
    "I don't have any magical powers..."
    "...was she plotting to use me as a blood sacrifice or something to resurrect herself?"
    mv "..."
    mv "You humans have a very active imagination..."
    mv "Why would I use you as a blood sacrifice when I need you alive?"
    mc "..."
    with vpunch
    mc "H-How'd you know what I was thinking!?"
    mv "Oh, that's one of my many special Valla abilities..."
    mv "I can read your mind easily, especially if you lack the {i}magical aura{/i} to shield me from your thoughts."
    mc "..."
    mc "This is getting too weird..."
    mc "Just tell me what I have to do to save you."
    mv "Very well..."
    mv "For my revival, I require your {i}power{/i}..."
    mv "The power of {i}life{/i}..."
    mv "To bring forth my body, you must provide me with your [yel]essence{/color}..."
    mc "Essence...?"
    with vpunch
    mc "You really are planning on killing me, aren't you!?"
    mv "No, [mc]..."
    mv "Like I said earlier, I need you alive."
    mv "A female Valla draws strength from her male companion."
    mv "I require your {i}essence{/i}, the magical fluid that only a male Valla can provide..."
    mv "Only then will my physical body appear."
    mc "..."
    mc "Okay, fine..."
    mc "But when you say {i}essence{/i}, I have no idea what you're talking about."
    mv "Ah, forgive me..."
    mv "It has been many millennias since I last spoke to someone, personally."
    mv "Despite not possessing a full-bound body, I can still hear the thoughts of those around me..."
    mv "In this modern age, the term {i}essence{/i} can roughly be translated to {i}semen{/i}, in your native tongue."
    mv "So yes, I require your semen if I'm to awaken."
    mc "..."
    mc "Y-You're joking, right?"
    mv "Joking?"
    mv "Is this really the time to joke around?"
    mv "I need your essence..."
    mv "...simply cum inside the lake and I'll be revived."
    mc "..."
    with vpunch
    mc "You want me to cum inside the lake!?"
    mc "Are you out of your mind!?"
    mv "This is a situation most dire, [mc]."
    mv "I thought that you wanted to save your loved ones?"
    mc "..."
    mc "Okay, now I know for sure that I'm losing my fucking mind..."
    mv "Please, [mc]..."
    mv "I'm struggling to find the strength to even speak..."
    mv "A male Valla's essence contains wondrous healing properties..."
    mv "You will see for yourself, if you just cum inside the lake for me."
    mc "..."
    "A mysterious voice is telling me to cum inside a lake to revive her..."
    "And yet, somehow, I don't feel that she's lying..."
    "Given my current mental state, I was willing to believe anything if it meant saving [mil!c] and Estelle..."
    mc "..."
    with vpunch
    mc "Fuck it..."
    mc "What else do I have to lose?"
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3
    "I glanced around the park, making sure that there was no one around..."
    "...I also checked for any cameras to make sure that this wasn't some sick prank."
    play sound "audio/zipper.mp3" volume 3
    "Then slowly, I began to undo the zipper of my pants..."
    "My eyes slam shut..."
    "I take hold of my flaccid cock, jerking it slowly from the base of my shaft..."
    mv "..."
    mv "Excellent, [mc]... It appears that you're willing to help me..."
    mv "So as the God of this land, allow me to do you a great service..."
    mv "I shall turn your most craving desire into a vivid fantasy..."
    $ renpy.pause(.5, hard=True)
    scene whitescreen with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "A light breeze sweeps through my body..."
    "However, the wind was not cold, but warm..."
    "A burning sensation fills my loins..."
    "Is this the magic of the Lady of the Lake?"
    $ renpy.pause(.5, hard=True)
    show story 001-54 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "A graphic image starts to unravel before my eyes..."
    "The scenario was the same as the porn I saw on MagiHub, not too long ago..."
    "But in the place of the busty blondes staring back at me..."
    "...there were two other girls, whom I knew all too well..."
    $ renpy.pause(.5, hard=True)
    show story 001-55 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 001-56 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    with vpunch
    mc "..."
    mc "W-What is this...?"
    show story 001-57 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    silv "Oh [mc], honey..."
    silv "Would you be a dear and take off your pants already?"
    silv "Don't you know it's rude to keep a woman waiting?"
    show story 001-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Yeah, [mc]..."
    este "Isn't this what you always wanted?"
    este "As long as it's warm, wet, and slippery, a virgin like you doesn't care whose hole you get to fill up, right?"
    este "...even if it belongs to your little [sil]."
    show story 001-56 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "N-No way..."
    mc "I'd never fantasize about... these two like this..."
    mc "Lady of the Lake, this is your doing, isn't it?"
    mv "..."
    mv "[mc], what you are currently experiencing is your own deepest fantasy..."
    mv "I simply used my magic to bring out your {i}true desire{/i} into the light..."
    mv "In the darkest depths of your heart, this is what you secretly yearn for..."
    mc "I-Impossible..."
    mc "I'd never... do that to [mil!c] or my [sil]..."
    mc "That's just... wrong..."
    mv "..."
    mv "Continue to deny it all you like, [mc]..."
    mv "...but your body's reaction from seeing these two in such a comprising position is clear."
    mv "What strikes me as odd are the chains wrapped around their necks..."
    mv "Could it be that your desire to save them isn't because you actually want to help them?"
    mv "Rather than have them serve someone else, you'd prefer that they serve {i}you{/i} as your own personal sex slaves, instead?"
    mv "Quite the male Valla mentality, if I do say so myself."
    mc "No... of course, not..."
    mc "I'm not... some sexual deviant..."
    mc "This is just a trick that you're pulling on me..."
    show story 001-58 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    este "Geez, [mc]..."
    este "Stop trying to act morally correct when your dick is throbbing like {i}that!{/i}"
    este "You really do want to fuck your little [sil], don't you?"
    este "...pervert."
    show story 001-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Mmhmm..."
    silv "[mc], you've grown into such a healthy young man..."
    silv "Which pussy would you like to use first?"
    show story 001-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Mines, mines!"
    este "Hurry up and tell her you want to use {i}mines{/i}, [mc]!"
    show story 001-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Aw, do you prefer younger pussy, [mc]?"
    silv "That makes me so sad..."
    silv "Well, if it's Estelle, I guess I don't mind sharing..."
    silv "After all, I love it when you two are lovey-dovey..."
    show story 001-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "How do you want me, [mc]?"
    este "From the front?"
    show story 001-59 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "Hehe..."
    este "Or would you prefer my ass, instead?"
    show story 001-60 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "My imagination was running wild..."
    "They didn't just look like [mil!c] and Estelle, but they sounded like them too..."
    "The stress and anxiety I was experiencing was clearly taking it's toll on me..."
    "My mind returned to the lake, and I could feel my dick ready to burst..."
    $ renpy.pause(.5, hard=True)
    show story 001-61 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 001-62 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "F-Fuck...!!!"
    mc "It's coming out!!!"
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play sound "audio/wind.mp3" volume 3
    $ renpy.pause(.5, hard=True)
    $ renpy.movie_cutscene("images/videos/prologue_08_01.webm", delay=None, loops=0, stop_music=False)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop sound
    stop music fadeout 1.0
    play music "audio/azula.mp3"
    $ renpy.pause(1, hard=True)
    show story 001-63 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mv "Ahaha!"
    mv "As expected, my plan worked flawlessly!"
    show story 001-64 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv "...and it's all thanks to you, [mc]!"
    mv "Because of you, I now have my body back!"
    mv "You're my hero!"
    show story 001-65 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "I could hardly believe it..."
    "In front of me was the most beautiful woman I had ever seen..."
    "She truly was a Goddess, as she claimed to be..."
    show story 001-66 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mv "Eh?"
    mv "How droll..."
    mv "I can sense vulgar intentions emanating from you..."
    show story 001-67 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "She was staring directly at my twitching cock..."
    mc "..."
    with vpunch
    mc "Sorry about that!"
    mc "You're just... uh... so beautiful..."
    show story 001-64 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv "Ah..."
    mv "I can sense your embarassment now, but..."
    mv "In the future, I have a feeling that you'll be accustomed to the female anatomy."
    mv "...as is natural for a young male Valla."
    show story 001-63 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv "Very well, then..."
    mv "Before you try to attack and have your way with my voluptuous body..."
    mv "...I shall fix myself up to become more presentable!"
    show story 001-65 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "W-What!? I would never do that to..."
    scene whitescreen with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    "A blinding white light flashes before my eyes..."
    show story 001-68 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    with vpunch
    mv "There, good as new!"
    mc "..."
    mc "H-How'd you do that!?"
    show story 001-69 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv "Hah!"
    mv "As a pure-blooded Valla, my magical powers far surpass the bounds of a normal human being..."
    mv "At my prime, I was capable of drowning the entire country with water..."
    show story 001-70 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Okay, what exactly is a Valla and why did you call me one, earlier?"
    mc "I don't have any magical powers like you."
    show story 001-71 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv "Hmm..."
    mv "I do sense that your magical aura is on the weaker side..."
    mv "It's almost non-existent..."
    show story 001-69 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv "However, I'm absolutely certain that you and I share bloodlines."
    mv "After all, you would not have been able to awaken me if you were not a true Valla."
    show story 001-70 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Just who are you, exactly?"
    mc "I never even got your name..."
    show story 001-72 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv "Oh, my apologies..."
    mv "I should have given you a proper introduction sooner..."
    show story 001-73 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "My name is [yel]Azula{/color}, and I am the Valla Goddess who once ruled this land some milennias ago..."
    azul "Those who traveled nearby and heard my whispers occassionally referred to me as the 'Lady of the Lake'."
    azul "And you are [mc], my newfound male companion who has given me life through your essence."
    azul "I must sincerely thank you for that."
    show story 001-74 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    stop music fadeout 3.0
    mc "I see..."
    mc "Well, I'm pleased to meet you, Azula..."
    mc "Er, wait..."
    mc "You said that if I came here, you could help me save [mil!c] and Estelle from being sold off!"
    show story 001-75 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    play music "audio/sad.mp3"
    azul "Hmm..."
    azul "Yes, that is quite the predicament..."
    azul "The Scarlet law existed even during my time."
    azul "Unfortunately, as I am now, there is not much that I can do to help you."
    show story 001-76 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "What!?"
    mc "Are you kidding me!? You said that you could help!"
    show story 001-75 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "I did say that..."
    azul "...and I meant it when I said I'd stop the Scarlet Law."
    azul "However, in my current state, I do not possess the strength to do anything."
    azul "Even now, it feels as though I cannot leave this lake without disappearing again."
    azul "I've been revived by you, [mc], but I still require a greater deal of your essence in order to regain my true form."
    show story 001-76 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "Perhaps it wasn't the right time, but..."
    "My dick grew stiff at the thought of providing Azula with more of my essence."
    show story 001-77 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Hmm..."
    azul "You know, perhaps there is something else that you can do."
    show story 001-78 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Huh?"
    mc "W-What is it? Please tell me!"
    show story 001-77 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Well..."
    azul "You can try buying their Scarlet Contracts first..."
    azul "That way, you can protect them since they'll be under your ownership."
    show story 001-78 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Buy them... myself?"
    "If I bought both [mil!c] and Estelle..."
    "...they'd be {b}mine.{/b}"
    "They'd be my personal slaves, my property to do whatever I so well pleased."
    show story 001-75 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Er..."
    azul "It appears that you have a ridiculous grin on your face..."
    azul "Shall I go ahead and read your mind, and..."
    show story 001-76 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "T-That's okay!"
    mc "Even if I bought them, I definitely would {i}never{/i} do anything lewd to them!"
    mc "I mean, it's my [mil] and [sil] we're talking about!"
    mc "Those kinds of perversions only happen in fantasies, not real life!"
    show story 001-69 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Uh-huh..."
    azul "Well, I never said anything about doing lewd things with them..."
    azul "And don't worry, even though you're my male companion, I certainly don't mind sharing you with other girls."
    show story 001-70 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "That plan won't work, anyway..."
    mc "[mil!c] and Estelle's contracts have already been bought..."
    show story 001-69 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Ah..."
    azul "Now that's where you're wrong..."
    azul "I was able to grasp and assess the current situation after reading your mind..."
    azul "You see, the Scarlet Law is not perfect..."
    show story 001-68 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    azul "One might even say that there's a {b}FLAW{/b} in the {b}LAW{/b}!!"
    mc "..."
    show story 001-75 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Dang, too soon?"
    azul "A-Anyway, the Scarlet Contract states that a person does not have the right to refuse her buyer..."
    azul "However, if there is another who matches the price of the contract, the person in question has the right to {b}CHOOSE{/b} her master..."
    azul "Do you understand where I'm getting at, [mc]?"
    show story 001-76 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh..."
    mc "I think I get it, you're saying that if I match the price before their contracts get finalized, [mil!c] and Estelle will obviously choose me over the other buyer."
    show story 001-68 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Correct!"
    azul "And according to your [mil], the deal will not be finalized for another few weeks..."
    azul "I don't know much about money, but that should be enough time to raise the funds for their contracts, right?"
    show story 001-70 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "There's just one problem..."
    mc "...I don't have a job."
    mc "In fact, I've never had a job in my entire life."
    show story 001-75 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "That does pose a problem..."
    azul "Unfortunately, {i}working{/i} is not a skill within my repertoire."
    azul "Perhaps there is someone else that you know who is willing to assist you with that?"
    show story 001-76 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm..."
    mc "I could try asking Serena..."
    mc "She works at the local convenience store."
    mc "Maybe if she puts in a good word for me with her grandpa, I'll be hired quickly."
    show story 001-71 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Do it then, [mc]..."
    azul "Save your [mil] and [sil]... Be the hero of this story..."
    azul "Alas, I cannot leave this lake without disappearing again..."
    azul "Perhaps if you could return to me every so often and provide me with more of your essence, I'll recover some more of my lost power."
    show story 001-70 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Thank you, Azula..."
    mc "I promise I'll be back..."
    show story 001-68 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "I'll look forward to it."
    azul "Best of luck out there, [mc]."
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    $ renpy.end_replay()
    stop music fadeout 3.0
    $ azulmet = True
    $ disabled = False
    $ renpy.pause(1, hard=True)
    play sound "audio/ding.mp3" volume 3
    "[yel]Azula's Character Card has been added to the Relationship Screen."
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    play sound "audio/ding.mp3" volume 3
    show screen tutorialscreen_02 with Dissolve(1.5)
    while endgame != True:
        pause

label prologue_09:

    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "I rushed out of the park and back into the street..."
    "When I arrived, I was pleased to see that Serena was outside and working at her grandpa's store..."
    show story 001-79 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/serena.mp3"
    sere "..."
    show story 001-80 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hey there, [mc]..."
    sere "Back here already, huh?"
    show story 001-79 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Serena..."
    mc "I need you..."
    $ renpy.pause(.5, hard=True)
    show story 001-81 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play sound "audio/slam.mp3" volume 3
    with vpunch
    $ renpy.pause(.5, hard=True)
    sere "[mc]..."
    sere "W-What's gotten into you!?"
    show story 001-82 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Please, Serena..."
    mc "You're the only one who can help me..."
    show story 001-83 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I-I'm the only one...?"
    sere "[mc], a-are you confessing to me?"
    show story 001-84 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "(Ah, I don't think my heart is ready...)"
    show story 001-82 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yes, you're the only one who can help me..."
    mc "Could you please ask your grandpa to let me work at the store with you..."
    show story 001-85 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Eh?"
    sere "H-Haven't you heard? Grandpa is..."
    show story 001-83 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    sere "W-Wait... Y-You want to work here?"
    sere "...with {i}me?{/i}"
    show story 001-82 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Yes!"
    mc "I need money as soon as possible..."
    show story 001-85 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "..."
    sere "[mc], what's going on?"
    sere "You've been acting weird all day..."
    show story 001-82 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "It's [mil!c] and Estelle..."
    mc "Someone's activated their Scarlet Contracts..."
    mc "And in order to save them, I have to raise enough money to buy them before they're gone forever!"
    show story 001-86 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "N-No way..."
    sere "Your [mil] {i}and{/i} Estelle?"
    sere "That's too much..."
    show story 001-82 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "That's why I need a job here..."
    mc "Please, Serena, you're all I got..."
    show story 001-87 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I-I don't know..."
    sere "The store barely makes enough money to stay running as it is..."
    show story 001-82 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "Please, Serena..."
    mc "Can you at least try asking your grandpa for me?"
    show story 001-85 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "[mc]..."
    sere "We've been friends forever, but this is the first time I've ever seen you like this..."
    sere "In a way, I'm kind of jealous..."
    sere "I wish there was someone out there who would be willing to do the same for me..."
    show story 001-82 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Don't be ridiculous, Serena..."
    mc "You're just as important to me as my [mil] and [sil]."
    mc "I wouldn't hesitate to do the very same for you if you were in their shoes."
    show story 001-86 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "R-Really?"
    show story 001-84 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Er... I'll see what I can do..."
    sere "Um, I also wouldn't mind working with you too, [mc]..."
    show story 001-88 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    "Serena rushed into the store, likely to call her grandpa to ask for his permission..."
    "I waited patiently outside, pondering the freakish events of today..."
    "The news of losing both [mil!c] and Estelle..."
    "The meeting of the blue-haired Goddess..."
    "Learning that I was actually a Valla..."
    "And now I'm here, trying to raise enough money to buyout their Scarlet Contracts..."
    mc "..."
    mc "I'd probably still be sitting at home and wasting my time if none of this had ever happened..."
    mc "In a way, I'm glad to be here and doing something {i}meaningful{/i}..."
    mc "...even if it meant just sitting around a store all day."
    show story 001-80 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    sere "Hey, [mc]!"
    sere "Good news! I checked our finances and I think you can work here part-time!"
    show story 001-79 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "That's great!"
    mc "Wait, what does that mean?"
    show story 001-89 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "It means that you can come in whenever you want and be paid on the hour..."
    sere "Convienent, don't you think?"
    show story 001-79 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Awesome..."
    mc "When can I start?"
    show story 001-89 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Hehe..."
    sere "Business usually picks up around this time..."
    sere "...so how bout working right {i}now?{/i}"
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3.0



    call charwork ("serena")
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 001-90 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    sere "..."
    show story 001-91 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "You did a great job today, [mc]!"
    sere "Time really flew by!"
    show story 001-90 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Thanks, Serena..."
    mc "It was fun working with you, too."
    show story 001-94 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I really hope that you can get your [mil] and [sil] back..."
    sere "We're neighbors, so I practically see them every day."
    show story 001-93 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Me too..."
    mc "And I'm sure they'll be delighted to know how much you care."
    show story 001-92 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "By the way..."
    sere "How much money are their Scarlet Contracts?"
    sere "It can't be cheap, right?"
    show story 001-93 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm..."
    mc "That's a good question, I have no idea."
    mc "Do you know where I have to go to find out?"
    show story 001-94 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I think you have to go to [yel]City Hall{/color} and ask about it..."
    sere "That's where all of the business is conducted."
    show story 001-93 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Got it..."
    mc "I'm going to check on their contracts right now."
    show story 001-92 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "Eh?"
    sere "Are you sure you want to go out now?"
    sere "It's pretty late..."
    show story 001-93 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I need to do everything I can to save [mil!c] and Estelle..."
    mc "I can't afford to waste any time."
    show story 001-94 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    sere "I understand..."
    sere "Well, I'm going home, [mc]."
    sere "Be safe, okay?"
    mc "Thanks for everything, Serena..."
    mc "...and good night."
    $ renpy.pause(.5, hard=True)
    scene street01_night with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    mc "Serena said that I have to go to [yel]City Hall{/color} in order to see their contracts..."
    mc "It's really far from here..."
    mc "Will I be able to make it in time before they close?"
    $ timeofday = 4
    play sound "audio/ding.mp3" volume 3
    "[yel]City Hall has been added to the Map Screen."
    jump streetlabel_01

label prologue_10:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 001-95 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/relax.mp3"
    "It was getting dark, fast..."
    "Everywhere I looked, men and women were rushing home to be back with their families..."
    "I actually thought about returning myself..."
    "...but I pushed on, even though the chances of the building being open at this hour were slim to none."
    show story 001-96 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    "A chill ran through me as I continued down the concrete road..."
    "Besides the howling of the wind, the streets were eerily quiet..."
    "For some unknown reason, I could feel as though I was being watched..."
    scene whitescreen with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    azul "[mc], your intuition is on point..."
    azul "Two humans have been following you for quite some time now."
    show story 001-95 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "(Azula...)"
    mc "(What should I do?)"
    azul "Hmm..."
    azul "I don't sense any killing intent from either of them..."
    azul "However, they appear adamant on confronting you for hostile reasons..."
    mc "..."
    show story 001-97 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play sound "audio/footsteps.mp3" volume 3
    "I can hear footsteps from behind me..."
    "Perhaps they realized that I was on to them, and decided to act."
    mc "..."
    "To be honest, my body was trembling..."
    "I had never been in a situation like this before..."
    azul "..."
    azul "Do not be afraid, [mc]..."
    azul "For you have the blood of the Valla flowing with you..."
    azul "I'm only sorry that I can do nothing else to help..."
    mc "..."
    "Azula's voice grew weak..."
    "She used what little strength she had left to warn me."
    show story 001-98 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "*Sigh*"
    mc "(I better go see what they want...)"
    $ renpy.pause(1, hard=True)
    show story 001-99 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    mc "Who are you girls?"
    mc "And what the hell do you want from me?"
    show story 001-100 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mvalti "..."
    mvalti "I'm so sorry..."
    mvalti "Goddess, forgive us."
    show story 001-101 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvvier "..."
    mvvier "I won't waste any of your time."
    mvvier "We're from the [yel]Powder Girls{/color} and we're here to rob you for every penny you got."
    mvvier "You can make this easy..."
    mvvier "...or you can make this hard."
    mvvier "The least I can do is offer you that choice."
    show story 001-99 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "Are you fucking kidding me?"
    mc "After all the bullshit I've been through today..."
    mc "...I'm now about to be mugged by two girls straight out of magic academy!?"
    show story 001-102 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvalti "P-Please don't make this d-difficult..."
    mvalti "E-Everything will be end p-peacefully if you just hand over your w-wallet..."
    show story 001-101 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvvier "You heard her..."
    mvvier "Don't make this hard, or else I'll really have to hurt you."
    show story 001-99 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "SCREW YOU BITCHES!!!"
    mc "I'M NOT GIVING A SINGLE DIME TO YOU LITTLE CUNTS!!!"
    show story 001-100 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvalti "Oh, Goddess..."
    mvalti "I'm so sorry... P-Please forgive us..."
    show story 001-103 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvvier "Heh..."
    mvvier "I certainly admire your courage..."
    mvvier "But you just gave us the wrong answer..."
    mvvier "Now, I'm going to have to wreck your shit."
    $ renpy.pause(1, hard=True)
    show story 001-104 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "I rose my fist into the air, preparing myself for a fight..."
    "The pink-haired girl backed off, allowing the flat-chested girl to step in..."
    "I didn't know a thing about fighting..."
    "And clearly, the girl in front of me was well-trained..."
    mc "..."
    menu prologue_10_menu:
        set menuset
        "Attempt to strike her..." if True:
            $ renpy.fix_rollback()
            show story 001-105 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            with vpunch
            mc "Hah!"
            mvvier "..."
            "Each time I swung my fists, the flat-chested girl anticipated my movement and dodged me with ease."
            "Even more, there was a grace in each step she made, almost as though she were dancing as she fought..."
            $ renpy.pause(.5, hard=True)
            show story 001-104 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            jump prologue_10_menu
        "Attempt to defend yourself..." if True:
            $ renpy.fix_rollback()
            show story 001-106 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            with vpunch
            mc "Ugh..."
            mvvier "..."
            "She lashed out her leg, but I was able to block it with my arm..."
            "But even though her body appeared weak and slender, her kicks felt as though I was being hit by a boulder..."
            "The damage was staggering, and I could immediately tell that she wasn't even close to using her full strength..."
            $ renpy.pause(.5, hard=True)
            show story 001-104 with Dissolve(1)
            $ renpy.pause(1, hard=True)
            jump prologue_10_menu
    $ renpy.pause(.5, hard=True)
    show story 001-107 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvvier "..."
    mvvier "Are you ready to give up now?"
    mvvier "There's no shame in surrendering when the difference in our skill is clear."
    mvvier "Of course, we ain't leaving here without the money."
    show story 001-104 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "She was right, there was no way that I could win this fight..."
    "She was simply too strong for me..."
    "Maybe the money I had on me wasn't a lot..."
    "Maybe it wasn't worth risking my life over..."
    "But this money wasn't for me..."
    show story 001-108 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "This money is for [mil!c] and Estelle!!!"
    mc "That's why I won't let anyone take it from me!!!"
    show story 001-109 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvvier "Your [mil], huh?"
    mvvier "I understand how you feel, but how you're going about it is wrong."
    mvvier "Choosing to become an {b}Owner{/b} on the basis of {i}saving them{/i} is a common theme for them..."
    mvvier "That's why, I have to stop you here."
    show story 001-110 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "Does she know that I'm trying to buy their Scarlet Contracts?"
    "Was that the reason why I was targeted?"
    with vpunch
    "H-Hold on... her eyes are closed..."
    "This might be my chance to take her down!"
    mc "..."
    show story 001-108 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "CCCCHHHAAAARRRRRGGGGGGEEEE!!!"
    show story 001-114 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    $ renpy.movie_cutscene("images/videos/prologue_10_01.webm", delay=None, loops=0, stop_music=False)
    scene whitescreen with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play sound "audio/fall.mp3" volume 3
    show story 001-111 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Aargh..."
    show story 001-112 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    "My vision starts to blur..."
    "Her kick hit me squarely on my chin..."
    show story 001-113 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    "Every muscle in my body tries to force myself back on my feet..."
    "...but no matter how much I tried, my body refused to listen."
    "...was this the end for me?"
    show story 001-115 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mvvier "Quick, Atty..."
    mvvier "Check his pockets!"
    mvalti "Ah..."
    mvalti "R-Right..."
    show story 001-116 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mv2 "*Sigh*"
    mv2 "Powder Girls, huh?"
    mv2 "To me, you look like nothing more than trash on the street."
    mv2 "If you punks are looking for a fight, how about you try {i}me{/i} instead?"
    show story 001-115 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mvvier "S-Shit... It's {i}her{/i}!"
    mvvier "We have to run, Atty! She's way too strong!"
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3.0
    "The scrambled thugs dart in the opposite direction..."
    "For a moment, the street goes quiet..."
    play sound "audio/footsteps.mp3" volume 3
    "Then, I hear the footsteps of my savior approaching me..."
    "With what little strength I had left, I opened my eyes to try and thank her..."
    stop sound
    $ renpy.pause(1, hard=True)
    show story 001-117 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 001-118 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 001-119 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mc "...booty."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    mc "Ugh, my head hurts..."
    mc "Where am I?"
    mc "What... smells so good?"
    $ renpy.pause(1, hard=True)
    show story 001-120 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 001-121 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    "Laying beside me was an {b}angel{/b}..."
    "Was this... heaven?"
    show story 001-122 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mvlaur "..."
    mc "..."
    show story 001-123 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvlaur "Good evening..."
    mvlaur "How are you feeling?"
    mc "..."
    with vpunch
    mc "W-WHOA!!!"
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/laureate02.mp3"
    "Confused and bewildered, I rolled off the mattress and rose to my feet..."
    $ renpy.pause(1, hard=True)
    show story 001-124 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mvlaur "..."
    show story 001-125 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvlaur "Ooh..."
    mvlaur "It looks like my healing magic really did the trick!"
    mvlaur "Looks like you have the strength to stand on your own two feet now!!"
    show story 001-124 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "She was right..."
    "My body was no longer sore and in pain..."
    mc "I do feel much better..."
    mc "Did you... heal me?"
    show story 001-126 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvlaur "I certainly did!"
    mvlaur "After those thugs escaped, we brought you back to my suite."
    show story 001-127 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvlaur "You were in such bad shape..."
    mvlaur "...so I thought that, by cuddling up with you and sharing my warmth, you'd heal up faster."
    show story 001-128 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv "*Sigh*"
    mv "Your Highness, that is simply an old wives tale..."
    show story 001-124 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...I see."
    mc "And who are you two?"
    show story 001-129 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv "Such impudence..."
    mv "You are in the presence of Her Highness herself, [yel]Princess Laureate{/color}!"
    show story 001-124 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "S-She's the {i}princess{/i}!?"
    mc "But she looks younger than me!"
    show story 001-130 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mv "Your Highness..."
    mv "Now that his wounds have been treated, shall I dispose of this vermin?"
    show story 001-131 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Er..."
    laur "That won't be necessary."
    laur "I rarely make it my business to show myself in public..."
    laur "I'm not entirely surprised that he doesn't recognize me."
    show story 001-124 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Thank you for saving me earlier..."
    mc "Really, things could have been much worse without your help."
    show story 001-141 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Eh?"
    laur "Oh no, I can't take full credit for that..."
    laur "All I did was patch up your wounds."
    show story 001-125 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "The one you should thank is [yel]Ferry{/color} here..."
    laur "She's the one who picked you up and carried you back to my place."
    show story 001-124 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Thank you, Ferry."
    show story 001-129 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Hmm..."
    ferr "Don't mention it."
    ferr "The Powder Girls are nothing more than cowards."
    ferr "They were only lucky that I didn't show up sooner."
    show story 001-126 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Now that the introductions are out of the way..."
    laur "...what business do you have at City Hall, [mc]?"
    show story 001-124 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Huh?"
    mc "How do you know my name?"
    show story 001-125 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Hehe, surprised?"
    laur "My magic power allows me to briefly tap into one's mind..."
    laur "It's not perfect, but I could sense your urgency to come here."
    laur "Pretty neat, don't you think?"
    show story 001-130 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Your Highness..."
    ferr "I do believe that you checked his ID while he was unconscious, did you not?"
    show story 001-131 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Aww..."
    laur "Way to ruin my attempt to look cool, Ferry..."
    laur "But honestly, I had to see whether [mc] was {i}packing{/i} or not..."
    laur "You know, for safety reasons..."
    show story 001-124 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "Right, I came here for [mil!c] and Estelle!"
    mc "I need to know the price of their Scarlet Contracts!"
    show story 001-127 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "I-Impressive!"
    laur "You actually have enough to buyout a contract?"
    show story 001-133 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Er..."
    mc "No, I probably don't have enough yet..."
    mc "But I'm saving up! I have to buy them off within the month before they're gone forever!"
    show story 001-134 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Gone... forever?"
    show story 001-133 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah..."
    mc "You see, someone's trying to buy both my [mil] and little [sil]..."
    mc "And in order for me to save them, I have to buy their contracts before it's too late!"
    show story 001-135 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "I... see...."
    laur "Er, Ferry, if you would?"
    show story 001-136 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "Certainly, Your Highness."
    ferr "Give me just one moment."
    show story 001-137 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    stop music fadeout 3.0
    play sound "audio/keyboard.mp3" volume 3
    "Ferry begins tapping away at her laptop..."
    ferr "..."
    show story 001-138 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "The Scarlet Contracts in question belong to 'Silvia' and 'Estelle', correct?"
    ferr "Their purchase is currently pending..."
    show story 001-137 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Right..."
    show story 001-139 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    stop sound
    ferr "This here is the total fees of their contracts."
    show story 001-140 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    play music "audio/sad.mp3"
    mc "..."
    mc "This is... too much..."
    mc "How can anyone afford to pay this..."
    "As if the day couldn't get any worse..."
    "Just when my hopes were risen, reality had to drag me back down to the ground..."
    "I suddenly felt like fainting again... fainting, and never waking up from my desperate slumber."
    show story 001-134 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "..."
    laur "I'm sorry, [mc]..."
    laur "But that's just the way it is..."
    laur "The Scarlet law is a sacred tradition that has been going on since the founding of Scarlet."
    laur "Once a contract's clause has been triggered, a sale must be done."
    show story 001-133 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Please, Princess..."
    mc "I'm begging you here..."
    mc "Just this once, please don't let them take away my [mil] and [sil]..."
    mc "They mean... everything to me..."
    show story 001-142 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "..."
    laur "[mc], you really care about them, huh?"
    show story 001-143 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yes..."
    mc "They are the most important people in my life..."
    mc "For them, I'll do anything..."
    show story 001-141 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "[mc]..."
    laur "I cannot break the Scarlet Law..."
    laur "That law... wasn't created by man..."
    laur "It was created by the 'Goddess' who ruled over Scarlet..."
    laur "If I break this law, her wrath will certainly destroy this land..."
    laur "That's what I've been told, anyway..."
    show story 001-143 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 001-142 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "However..."
    laur "There is one thing that I can do for you..."
    laur "I am willing to front you the money for your [mil]..."
    laur "But in exchange, you'll have to pay me back, over time."
    show story 001-132 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "..."
    mc "..."
    with vpunch
    mc "Y-You're serious!?"
    show story 001-141 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Yes..."
    laur "I'll be willing to do that much."
    show story 001-143 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "But wait..."
    mc "Can you please save Estelle, too?"
    mc "She's just as important to me..."
    show story 001-144 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Unfortunately, I cannot."
    laur "Your [sil] is much younger and more {i}fertile{/i} than your [mil]..."
    laur "As such, she has much more {i}potential{/i}, resulting in a Scarlet Contract with significantly higher value than Silvia's."
    laur "A 39-year-old homemaker simply isn't as attractive to prospective buyers."
    show story 001-143 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "In a way, I could understand... even if it was messed up..."
    show story 001-142 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "So how about it?"
    laur "Are you willing to {i}give your life{/i} to me?"
    laur "In exchange, I will pay off Silvia's contract right now...."
    laur "...and pronounce you her owner."
    show story 001-143 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I'll do it."
    mc "But I won't give up on Estelle..."
    mc "I'll have her Scarlet Contract before she's sold off!"
    show story 001-134 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Hmm..."
    laur "That's very admirable of you, [mc]."
    laur "I do hope that you can keep your household together."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3.0
    "Laureate finalized the documents and made me sign some papers..."
    "In hindsight, I felt that it was incredibly strange for her to be helping out a total stranger like me..."
    "I guess she was truly a very caring princess..."
    "Of course, I didn't have the audacity to question her motives..."
    "I just wanted to save [mil!c]..."
    $ renpy.pause(.5, hard=True)
    show story 001-124 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/laureate.mp3"
    laur "..."
    show story 001-126 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "You're all set here, [mc]."
    laur "Congratulations on becoming an {b}owner{/b}."
    show story 001-125 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "I'm so happy for you."
    laur "We should definitely throw a party, hehe..."
    show story 001-124 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Thank you so much, Laureate..."
    mc "I couldn't have done this without you."
    show story 001-126 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "You're very welcome, [mc]."
    laur "But don't forget, you still owe me a debt."
    laur "Come see me after a while, and we'll talk more."
    show story 001-124 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Got it..."
    show story 001-145 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    laur "Oh, and one more thing..."
    laur "Since you're officially an owner now, you will now be sent a [yel]weekly bill every Saturday{/color}."
    show story 001-146 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "It's affectionately known as the [yel]'Waifu Tax'{/color}..."
    laur "If for any reason you cannot pay this tax, it's [red]GAME OVER{/color} for you."
    laur "So make sure that you always have funds available at the end of Saturday."
    laur "Consider it JYP's poor attempt of trying to balance money in the game."
    show story 001-124 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I-I see..."
    mc "And how much is this {i}Waifu Tax{/i}, exactly?"
    show story 001-145 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Well..."
    laur "There are a lot of lengthy, mathy, rocket sciency, Ellen Musky factors involved but it primarily depends on the number of girls you own and their personalties."
    laur "A frugal girl usually tallies a lower tax, while a lavish girl generally results in a higher tax."
    laur "Maintenance fees, such as food, water, etc. for the girls will also be billed that day, as well."
    laur "{size=22}...prices are subject to change without prior notice due to currency fluctuation, fuel prices, imported products, raw materials, and/or unforeseen economic circumstances, usually during the next update. JYP carefully checks pricing and bug specifications, but occasionally errors can occur, therefore he reserves the right to change both without notice. JYP is not responsible for gamer bug errors or game over screens. Some variations between picture and price may occur. Some bugs listed may be undescribed items or unfixable. For more information, please visit JYP's Patreon at [oj]https://www.patreon.com/jypgames"
    show story 001-146 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "But don't worry, I'm sure it'll be easy for you to manage as long as you have some money available every Saturday."
    laur "I mean, you're not trying to start some harem, right?"
    laur "You're just trying to save your [mil] and [sil]."
    show story 001-124 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 001-126 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Alrighty then..."
    laur "That concludes our business here..."
    laur "[mc], you may take your leave..."
    show story 001-124 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I will..."
    mc "Thank you, Princess. I didn't realize how nice of a person you are..."
    mc "In games, noble types like you are usually pretty {i}evil{/i}."
    show story 001-127 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Eh?"
    laur "T-Thank you, I guess..."
    laur "...even though you don't know my backstory yet."
    show story 001-124 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You too, Ferry."
    mc "I appreciate everything that you've done for me."
    show story 001-129 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "..."
    ferr "I was simply doing my job."
    ferr "It's nothing worthy of praise."
    show story 001-142 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Have a safe night, [mc]..."
    laur "And do try to be careful this time, alright?"
    laur "For the night is dark and full of terrors."
    laur "...or so I'm told."
    show story 001-124 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Right..."
    mc "Good night, you two."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    stop music fadeout 3.0
    "I ran back home as fast as I could..."
    "Thanks to Laureate's magic, my body was fully recovered..."
    "And with the good news in hand, I couldn't wait to get home and tell [mil!c] that I had freed her from her contract..."
    $ renpy.pause(.5, hard=True)
    play sound "audio/ding.mp3" volume 3
    "[yel]Ferry's Character Card has been added to the Relationship Screen."
    play sound "audio/ding.mp3" volume 3
    "[yel]Laureate's Character Card has been added to the Relationship Screen."
    $ renpy.pause(1.5, hard=True)
    show story 001-147 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    laur "*YAWN*"
    laur "Another tiring day as princess..."
    laur "Time for me to hit the hay."
    show story 001-148 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    ferr "..."
    ferr "That was very unlike you, Your Highness..."
    show story 001-149 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Eh?"
    laur "What do you mean?"
    show story 001-148 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "You know precisely what I mean."
    ferr "Girls are bought and sold here on a daily basis..."
    ferr "...many of them come to you, crying and begging for your help."
    ferr "So why would you go out of your way to help this one man?"
    show story 001-150 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Hehe..."
    laur "Ferry, couldn't you sense it?"
    laur "The flow of magic buried deep inside his body is special..."
    laur "I was able to confirm it when we shared the bed together, just now."
    show story 001-148 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "..."
    ferr "Your Highness, it is not my place to ask questions..."
    ferr "However, what are you looking to achieve by using him?"
    show story 001-149 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "..."
    laur "I hope to utilize that power of his for myself, someday..."
    laur "Maybe... he'll become my {b}savior{/b}..."
    show story 001-148 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    ferr "..."
    ferr "As you say, Your Highness..."
    ferr "I will be sure to monitor him closely."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    $ renpy.pause(1.5, hard=True)
    show story 001-151 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/silvia.mp3"
    silv "..."
    show story 001-152 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    silv "Just where have you been, [mc]!?"
    silv "You had us both worried sick!"
    show story 001-153 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Y-Yeah, [mc]..."
    este "We thought something happened to you!"
    este "You could have at least told us where you were going!"
    show story 001-151 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "[mil!c]... Estelle..."
    mc "I'm so happy to see you both..."
    mc "I managed to pull it off..."
    mc "I was able to get your contract paid off, [mil!c]..."
    show story 001-152 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Eh?"
    silv "What are you talking about, [mc]?"
    silv "Someone's already purchased my Scarlet Contract..."
    show story 001-151 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "No, [mil!c]..."
    mc "If another buyer matches the price of your contract, you have the right to decide which {i}owner{/i} you get to go to..."
    mc "In other words, you belong to me, [mil!c]..."
    mc "Unless, of course, you actually did want to leave Scarlet..."
    show story 001-152 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "[mc], I still don't understand..."
    silv "What's going on here?"
    show story 001-154 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Here..."
    mc "Take a look at this and see for yourself."
    show story 001-155 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Eh?"
    silv "What is this?"
    show story 001-156 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "..."
    este "..."
    "The two of them read the fine print of the contract in silence..."
    "Then slowly, tears began to erupt from [mil!c]'s eyes..."
    show story 001-157 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "[mc]..."
    silv "Is this... {i}real{/i}?"
    silv "I can stay here... with you?"
    show story 001-158 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yes, it's real..."
    mc "I had it notarized at City Hall, myself."
    show story 001-159 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "*Sniff* *Sniff*"
    silv "Oh, [mc]... Thank you!"
    show story 001-160 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    silv "You really did it!"
    silv "You saved me, [mc]! Thank you, thank you, thank you!"
    "She pressed herself against me for a hug... something she hadn't given me in years..."
    "I had to ask myself, when was the last time I've seen her like this?"
    "When was the last time 'I' made her this happy?"
    show story 001-161 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "A warm, tingly sensation surged through me..."
    "And it wasn't just from her fat tits being pressed against my chest..."
    "I felt good... I felt like a hero..."
    "It was a feeling that I wanted to experience again and again, in the future..."
    show story 001-162 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "I'm so glad..."
    silv "I promise that I'll work hard to be a good {b}slave{/b} for you, [mc]..."
    silv "You have my word!"
    show story 001-163 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "W-Whoa, what!?"
    mc "I know that I bought your contract, but..."
    mc "I-It's only because I want you to stay by my side!"
    show story 001-164 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Eh?"
    silv "But according to the Scarlet Law, it's my duty to serve my master..."
    silv "...in any way that I can."
    show story 001-163 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "T-That's okay!"
    mc "As your master, I want our relationship to be the same as before!"
    show story 001-164 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Aww..."
    silv "Okay then, if that's your wish..."
    show story 001-165 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    este "..."
    show story 001-166 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Hey, [mc]..."
    este "What about me? Did you manage to get ahold of my contract, too?"
    show story 001-151 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I'm sorry, Estelle..."
    show story 001-153 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "O-Oh..."
    este "You chose [mil!c] over me, huh?"
    este "I-I guess I understand..."
    este "W-We aren't as close as we used to be, after all..."
    show story 001-151 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Estelle, I have no intentions of giving up on you, too."
    mc "Even if I'm not the person you expected me to be..."
    mc "...you're still my little [sil], and I love you."
    show story 001-153 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    este "Eh!?"
    este "H-How can you say something like that with a straight face?"
    show story 001-167 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "It's the truth."
    mc "After everything that has happened today, I finally understand what I need to do."
    mc "The only reason why I wasn't able to get your contract was because yours is much more expensive than [mil!c]'s."
    mc "But I promise that I'll find a way to pay it off so that the three of us can be together."
    show story 001-168 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "O-Okay..."
    este "Thanks, [mc]..."
    show story 001-169 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "*Sigh*"
    silv "I'm such a fool..."
    silv "I just remembered that I have a fairly decent emergency fund saved up in my bank account..."
    silv "Maybe we can use it to pay off a good portion of Estelle's contract."
    show story 001-170 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "W-What!? Are you saying that we can save Estelle!?"
    show story 001-169 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Possibly..."
    silv "Though, I'm certain that we'll still be short a few thousand..."
    silv "I initially planned on giving the money to you after we left, [mc]..."
    silv "But if we just need to buy one contract, perhaps it can be done."
    show story 001-170 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm..."
    mc "I understand."
    mc "I just need to save up a few thousand and I'll be able to buyout Estelle's contract."
    show story 001-171 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Right."
    show story 001-172 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Ah..."
    este "That means that we can be together again..."
    show story 001-173 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Then please... [mc], buy my contract..."
    este "I-I'll be happy to be owned by you, rather than some creep I don't even know..."
    show story 001-174 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "Hearing that come out of Estelle, of all people, was oddly erotic..."
    mc "I'll do it..."
    mc "I want us all to be together..."
    show story 001-173 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    este "Okay..."
    este "I'm counting on you, [mc]..."
    $ renpy.pause(.5, hard=True)
    $ renpy.end_replay()
    jump prologue_11

label prologue_11:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "We spent a few more minutes talking before we decided it was time for bed..."
    "It had been a long day..."
    "With so many things happening, I easily closed my eyes and drifted off to sleep..."
    $ renpy.pause(1.5, hard=True)
    mv2 "..."
    mv2 "[mc]?"
    mv2 "[mc], honey, are you awake?"
    $ renpy.pause(1, hard=True)
    show story 001-175 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 001-176 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mc "Huh?"
    mc "[mil!c]? Why are you inside my..."
    show story 001-177 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "*GULP* W-Wow..."
    show story 001-178 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Shh..."
    silv "Not too loud..."
    silv "Or else we might wake up Estelle..."
    show story 001-177 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "[mil!c], w-what are you doing here?"
    mc "...and why are you dressed up like {i}that{/i}!?"
    show story 001-179 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hehe..."
    silv "I just wanted to show my appreciation..."
    silv "...to my new {i}owner{/i}."
    show story 001-177 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "This... isn't a dream... is it?"
    show story 001-179 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Is it? I'm not quite sure myself."
    show story 001-180 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    silv "Here..."
    silv "How about we find out together?"
    show story 001-181 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    "Her soft hand clutches the bulk of my meaty cock..."
    "On reaction, blood rushes to my lower half..."
    show story 001-182 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh god..."
    mc "Is this... really alright?"
    mc "I mean, you're my [mil]..."
    show story 001-183 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Mmm..."
    silv "Under normal circumstances, this would be wrong and illegal, but..."
    silv "According to the Scarlet Laws, this is fine..."
    silv "I have to service my master, no matter what!"
    silv "...and that includes physically, even if I am your [mil]."
    show story 001-184 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "More importantly..."
    silv "Isn't this what you wanted?"
    silv "When I caught you peeking at me earlier, I could see the lust written all over your face..."
    silv "For that brief moment, you didn't see me as your [mil]..."
    silv "You saw me as a {i}woman{/i}... a member of the opposite sex..."
    show story 001-182 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Y-You knew...?"
    show story 001-183 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Of course I knew, sweetheart."
    silv "Every woman develops a sixth sense when it comes to a man's true intentions..."
    silv "I could tell immediately that you wanted to slam me on my mattress and have your way with me..."
    silv "...you wanted to {i}fuck{/i} your own [mil], plain and simple."
    show story 001-182 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I'm sorry, [mil]..."
    mc "I shouldn't be looking at you like that... It's wrong, even if it is okay..."
    show story 001-184 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Don't be ashamed, [mc]..."
    silv "I'm not getting any younger, and I was honestly thrilled that a young man like you thought of me like that."
    silv "That's why I want to reward you... That's why I offer this body of mine to you, {b}my master{/b}..."
    show story 001-181 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "This was definitely not a dream..."
    "Her grip tightens around my aching cock..."
    "Various emotions brewed within me, emotions that no man should ever have for their [mil]..."
    show story 001-182 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah..."
    mc "I can't deny it..."
    mc "You're so sexy, [mil!c]... When I saw you like that, I wanted to walk inside your room and take you right then and there..."
    mc "Of course, I never thought of you as a sexual entity before, but now..."
    mc "I {i}really{/i} want to fuck you..."
    show story 001-183 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hehe..."
    silv "You certainly have potty mouth, young man..."
    silv "You really want that cock of yours inside my pussy? Pussy that hasn't had a dick in so many years?"
    show story 001-182 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "Hearing my own [mil] use such vulgar language was incredibly arousing..."
    "I don't think I've ever heard her swear in my entire life..."
    show story 001-185 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Here, let me help you out of these..."
    "[mil!c] pinches the hem of my shorts, and gently pulls them down..."
    show story 001-186 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    silv "Ah..."
    silv "This is certainly much bigger than what I remembered, [mc]..."
    show story 001-187 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "You've grown up so very well..."
    silv "Perhaps I should stop calling you my {i}'Little Man'{/i}... Hehe..."
    show story 001-188 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "[mil!c]..."
    mc "I want to see them, too."
    show story 001-187 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Oh?"
    silv "What does my master want to see?"
    show story 001-188 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Your tits..."
    mc "I need to see your tits again..."
    show story 001-187 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Geez..."
    silv "Didn't you already see them this morning?"
    show story 001-189 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Tsk, tsk... You're such a greedy young master..."
    silv "Very well, then..."
    silv "If tits are what you want, tits are what you shall get..."
    show story 001-190 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mc "Oh god..."
    mc "Those are some fucking udders!"
    show story 001-191 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Now then..."
    silv "Let me take care of this for you, [mc]..."
    silv "I'm sure you've had enough of me talking."
    show story 001-192 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    show prologue_11_01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    pause
    "The soft touch of her fingers was incredible..."
    "I continued to mutter to myself that this had to be a dream..."
    "And yet, here I was, having my dick jerked off by my own [mil]...."
    hide prologue_11_01
    show story 001-193 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    with vpunch
    silv "Eh?"
    silv "[mc]... you're touching my..."
    show story 001-194 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah..."
    mc "I don't care if they're my [mil]'s tits..."
    mc "I still want to play with them..."
    show story 001-195 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Oh, [mc]..."
    silv "I think there's something awakening inside of you..."
    show story 001-196 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hehe..."
    silv "Just don't squeeze them too hard, alright?"
    silv "Some women like it rough, but I prefer a gentleman..."
    show story 001-197 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    show prologue_11_02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    pause
    "I was surprised by how soft and heavy her breasts were..."
    "But more importantly, I couldn't believe that my first pair of tits belonged to my [mil]."
    "Whether that was sad or not, I didn't care..."
    "...because a swelling sensation filled my loins, causing me to forget all about my guilt."
    mc "F-Fuck, [mil!c]..."
    mc "I can't hold it back..."
    mc "I'm going to..."
    hide prologue_11_02
    show story 001-198 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    with vpunch
    mc "F-FUCK!!!"
    show story 001-199 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    silv "Ah..."
    silv "You got your gunk all over me..."
    show story 001-200 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    silv "Hehe..."
    silv "I suppose we should stop here for tonight, [mc]..."
    silv "I'll go get myself cleaned up and head to bed..."
    silv "Please continue taking care of Estelle and I in the future..."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "Shortly after that, I quickly succumbed to a deep slumber..."
    "There was some regret that I didn't request more from her, but..."
    "...I knew there would be plenty of opportunities in the future for more fun."
    "[yel]Silvia's Scarlet Contract has increased the weekly Waifu Tax."
    "[yel]Your relationship with Silvia has reached a new level."
    $ renpy.end_replay()
    $ renpy.pause(1.5, hard=True)
    show mcroom_day with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    call advanceday
    call respawn
    play music "audio/days.mp3"
    $ silvbought = True
    $ laurmet = True
    $ ferrmet = True
    $ silv_is_dead = False
    $ este_is_dead = False
    $ timeofday = 0
    mc "*YAWN*"
    mc "Man, last night was something else..."
    mc "Alright, no more sitting around my room playing video games..."
    mc "I'm going to save Estelle if it's the last thing I do..."
    $ renpy.pause(.5, hard=True)
    play sound "audio/ding.mp3" volume 3
    show screen tutorialscreen_03 with Dissolve(1.5)
    while endgame != True:
        pause

label mainquest_10:


    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 008-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "Good morning, Azula."
    mc "What's with the grouchy look on your face?"
    show story 008-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Geez, [mc]..."
    azul "Must you be so cruel?"
    show story 008-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Cruel?"
    mc "Did I do something wrong?"
    show story 008-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Eh?"
    azul "Don't tell me that you've already forgotten?"
    show story 008-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "You're going to have to fill me in here, Azula..."
    show story 008-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Didn't you promise to help fix me a room?"
    azul "Estelle's bed is much too small for a Goddess such as myself..."
    azul "And that snoring of hers is disrupting my beauty sleep..."
    show story 008-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Estelle snores, huh?"
    mc "I didn't know that..."
    show story 008-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Yes, so please..."
    with vpunch
    azul "Hurry up and fix my room already!"
    azul "...Before I lose my mind!"
    show story 008-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Right, right..."
    mc "I do seem to recall [mil!c] mentioning the [yel]Builders Guild{/color}..."
    mc "I'll go ahead and pay them a visit..."
    mc "...until then, continue to endure Estelle's snoring."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "I followed the directions on the MagiNet..."
    "According to [mil!c], the [yel]Komatsu Builders Guild{/color} is one of the most famous guilds in Scarlet..."
    "It was my first time here, however, and I wasn't sure whether or not I was at the right place..."
    $ renpy.pause(1.5, hard=True)
    show story 008-04 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    mc "(This has to be the place...)"
    mc "(...I think.)"
    show story 008-05 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "(Hmm, there are girls over there...)"
    mc "({b}Cute girls{/b}, actually...)"
    show story 008-06 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    menu:
        "Ask them for directions..." if True:
            $ renpy.fix_rollback()
            mc "(Wouldn't hurt to ask them if I'm at the right place or not...)"
        "Flirt with them..." if True:
            $ renpy.fix_rollback()
            mc "(Those uniforms are of [yel]Scarlet Magic Academy...)"
            mc "(In other words, they're all above the age of 18...)"
            mc "..."
            with vpunch
            mc "(A-Alright, I wasn't able to get a girlfriend in high school, but...)"
            mc "(...here's my second chance at a springtime of youth!)"
    show story 008-07 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "(Alright, [mc]...)"
    mc "(I gotta play it cool... Chicks dig confidence...)"
    show story 008-08 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "Excuse me, ladies..."
    mc "I was wondering if..."
    show story 008-09 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play music "audio/makoto.mp3"
    with vpunch
    mvtori "KYAAAAHHH~!!!"
    mvtori "HE'S SOOOOO CUTE~!!!"
    show story 008-10 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mvhana "...Don't forget omega {i}nyah{/i}-andsome~! Nyah~!"
    show story 008-11 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mvmizu "Hmm..."
    show story 008-12 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "(Huh?)"
    mc "(Who are they talking about?)"
    show story 008-13 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mvmako "Stand back girls!"
    mvmako "This can get messy!"
    show story 008-14 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mvmako "Oh, Pandy... Give me strength..."
    show story 008-15 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mvmako "HAAAAAAAAHHHH!!!"
    show story 008-16 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play sound "audio/explosion.mp3" volume 3
    with vpunch
    mc "W-Whoa!!!"
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(2, hard=True)
    show story 008-17 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mvmako "Whew..."
    show story 008-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvmako "Alright, all finished with the job."
    mvmako "Your books are all smashed up, just like you requested."
    show story 008-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "Oh, [yel]Makoto-kun{/color}..."
    mvtori "You can smash me with your hammer, anytime..."
    show story 008-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvhana "Nya~ Nya~"
    mvhana "Makoto-kun, do you have a girlfriend, nyah~?"
    show story 008-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvmako "Eh?"
    mvmako "N-No, you got it all wrong..."
    mvmako "First of all, I'm older than you girls..."
    mvmako "Secondly, I-I'm not a..."
    show story 008-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "Hehe..."
    mvtori "Look at him getting all flustered..."
    mvtori "He's soooo {i}kawaii{/i}~!"
    show story 008-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvhana "Nya~ Nya~"
    mvhana "Cute and strong, that's our Makoto-kun, nyah~!"
    show story 008-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvmizu "Hmm..."
    show story 008-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvmizu "Makoto-sama, it was a pleasure seeing you again..."
    mvmizu "...until next we meet."
    show story 008-26 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mvtori "..."
    mvhana "..."
    mvmako "..."
    show story 008-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "Well, we should probably get going, too..."
    mvtori "It was fun playing with you, Makoto-kun!"
    show story 008-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvmako "Ah..."
    mvmako "Don't forget to pick up your crushed books..."
    show story 008-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "My books?"
    mvtori "Oh, you mean my {b}homework{/b}..."
    show story 008-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvtori "You can just toss them in the bin, not like I did it anyway."
    mvtori "We only came here because we love watching you smash things, Makoto-kun."
    show story 008-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvhana "Nya~ Nya~"
    mvhana "Makoto smash, nyah~"
    show story 008-32 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mvmako "Geez, those girls..."
    mvmako "They were just teasing me again..."
    mvmako "The reputation of the Builders Guild has really fallen, huh?"
    show story 008-33 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "(Really? This fucking asshole has fangirls?)"
    mc "(Some bastards get all the luck...)"
    show story 008-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvmako "Er..."
    mvmako "Can I help you with something?"
    show story 008-35 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    with vpunch
    mc "(W-Wow, he really {i}is{/i} good looking from up close...)"
    mc "(N-Not that I'm into guys or anything...)"
    show story 008-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvmako "Er... Why are you staring at me like that?"
    mvmako "Is there something on my face?"
    show story 008-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh, uh..."
    mc "I was just wondering... is this the Komatsu Builders Guild?"
    show story 008-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mvmako "Sure is!"
    mvmako "The name's [yel]Komatsu Makoto{/color}..."
    show story 008-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "But you can just call me Makoto."
    mako "What kind of work do you need done by the guild?"
    show story 008-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I'm [mc]."
    mc "I'm planning on repairing a room inside my house..."
    mc "...but before I do, I want to get a quote to see how much it'll cost me."
    show story 008-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Oh, I think I can help you with that."
    mako "I'll just have to survey the room first in order to get an accurate estimate."
    show story 008-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Alright..."
    mc "Where should I go to schedule an appointment?"
    show story 008-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Hmm..."
    mako "Well, I'm not doing anything at the moment, so..."
    mako "...we can leave right now, if you'd like."
    show story 008-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "Wait, just you?"
    mc "Aren't you supposed to have a team or something?"
    mc "I was told that the Builders Guid is famous throughout Scarlet for its teamwork and work ethic..."
    show story 008-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Actually..."
    mako "I'm the only builder left ever since my father passed away."
    mako "Everyone else handed in their resignation slips not too long ago."
    show story 008-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh, I see..."
    mc "I'm sorry to hear that..."
    mc "(Hold on, that sounds awfully suspicious...)"
    mc "(There has to be a good reason why those builders left...)"
    show story 008-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I know what you're thinking..."
    mako "You're wondering why everyone quit the guild, right?"
    show story 008-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Y-Yeah..."
    mc "I don't mean to be rude but I think that it's important for me to know before I hire you for the job..."
    show story 008-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "After my father died, ownership of the guild went to me..."
    mako "And when that happened, the confidence within the guild plummeted..."
    mako "Not only did our most skilled builders leave to start their own businesses, there were also a lot less commissions compared to before."
    mako "Due to budget cuts and lack of faith in leadership, I'm the only builder left."
    show story 008-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 008-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "But don't worry though!"
    mako "I assure you that my building skills are top notch!"
    show story 008-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "And before long, I'll restore the Komatsu name back to its proper state!"
    mako "...even if I have to do it alone."
    show story 008-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "You know what, let's just do it."
    mc "I can see how important this is to you."
    show story 008-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Hehe, really?"
    mako "Excellent choice! I won't let you down!"
    show story 008-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Alright, let's get going..."
    mc "...{i}bro{/i}!"
    show story 008-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Eh?"
    mako "But I'm not a..."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 008-42 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mako "..."
    show story 008-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "So this is the place, huh?"
    mako "It doesn't look too bad, to be honest."
    show story 008-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah..."
    mc "Sorry that it's a little messy, though..."
    mc "I would have cleaned up if I knew you were coming."
    show story 008-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "That's okay..."
    mako "I'm used to a messy job..."
    show story 008-45 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mako "Welp, I guess I should go ahead and get to work..."
    mako "First thing I gotta do is the {i}inspection{/i}..."
    show story 008-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Oi, oi..."
    mc "Is that hammer really necessary?"
    show story 008-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Definitely!"
    mako "The Komatsu Clan's warhammer, '[yel]Pandoria{/color}', is the pride of the Builders Guild!"
    mako "I just need to smash a few walls to see what needs to be fixed..."
    show story 008-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Now stand aside..."
    mako "...and let a Komatsu get to work!"
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/glass.mp3"
    "The room was already in bad shape..."
    "And Makoto was making it worst by smashing his hammer all over the place..."
    "I screamed and shouted, but he couldn't hear me through the noise he was making..."
    "By the time he was done, there were over a dozen holes in the floor and walls..."
    stop music fadeout 3.0
    $ renpy.pause(3, hard=True)
    show story 008-48 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/makoto.mp3"
    mako "Whew..."
    mako "What a workout..."
    show story 008-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Alrighty, [mc]! We're all done here!"
    show story 008-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Makoto, what have you done!?"
    mc "All I wanted was an estimate!"
    mc "Now the room is completely wrecked!"
    show story 008-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Er, [mc], this is actually how the process works."
    mako "You see, Pandoria here is a [yel]Holy Relic{/color} imbued with magical properties."
    mako "It's connected with me both body and mind..."
    mako "...and right now, she's going to tell me how much it'll cost to fix the place."
    mako "...hopefully."
    show story 008-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Are you screwing with me!?"
    mc "What kind of bullshit is that!?"
    show story 008-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "B-But it's true!"
    mako "[yel]A Holy Relic is made from the soul of a God!"
    mako "Pandy can speak! I promise you that!"
    show story 008-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "*Sigh*"
    mc "Let's say for a minute that I actually believe what you're saying..."
    mc "...How much money does your hammer want to fix the place?"
    show story 008-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Er..."
    mako "A-Actually, I don't know..."
    show story 008-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "...What!?"
    show story 008-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Truth is, Pandy hasn't been speaking to me lately."
    mako "I think she's ignoring me..."
    show story 008-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Are you even trying to be serious!?"
    mc "You just thrashed my place, and now you're telling me that you can't fix it!?"
    show story 008-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I-I'm telling the truth!"
    mako "Ever since my father passed away, Pandy's stopped speaking with me!"
    show story 008-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "This is getting ridiculous..."
    mc "You're treating your hammer as if it were a real person..."
    show story 008-55 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Sorry, but Pandy and I are part of a {i}team{/i}."
    mako "Without her help, I can't get anything done."
    mako "Well, not a big project like this, anyway..."
    show story 008-56 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    show story 008-57 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mako "Eh?"
    mako "W-Where do you think you're touching!?"
    show story 008-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I want a word with your 'talking hammer'!"
    mc "If it won't speak to you, maybe it'll speak to me!"
    show story 008-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Y-You can't!"
    mako "Pandy will only speak to members of the Komatsu Clan!"
    show story 008-60 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "(...)"
    mc "(Hold on...)"
    mc "(W-Why does his chest feel so... {i}soft{/i}...?)"
    scene whitescreen with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3.0
    mc "Huh?"
    mc "What's going on...?"
    mv2 "How pitiful..."
    mv2 "To allow this mortal's filthy hands to tarnish the Komatsu family heirloom."
    mv2 "Truly, the noble bloodline has reached its end..."
    mc "W-What's this voice?"
    mc "So you can speak, after all?"
    mv2 "..."
    mv2 "Mortal, you can hear me?"
    mc "Yes! I can hear you loud and clear!"
    mc "Who are you?"
    mv2 "How quaint..."
    mv2 "The name's [yel]Pandoria{/color} and I am the spirit that occupies this warhammer."
    pand "You must possess a special power to be able to communicate with me and not be of Komatsu blood."
    mc "Special powers...?"
    mc "Wait, that's not important right now!"
    mc "I want to know why you're ignoring Makoto!"
    pand "..."
    pand "Isn't that obvious?"
    pand "{b}She{/b} is not worthy of inheriting the Komatsu name."
    pand "And I will only entrust my power to the one who can prove their worth..."
    mc "She?"
    mc "Who is 'she'?"
    with vpunch
    pand "Makoto, of course!"
    pand "Only a {b}MALE{/b} member of the Komatsu clan may inherit the Builders Guild!"
    pand "With her father having deceased, that bloodline is now lost!"
    pand "There is no longer any reason for me to help Makoto..."
    pand "If anything, she should quit being a builder and pursue a new career..."
    mc "..."
    mc "You're telling me that you refuse to speak with Makoto because she's a {i}girl{/i}?"
    mc "That's horrible!"
    pand "Be that as it may, the fact remains..."
    pand "The Builders Guild has always been managed by a male member of the Komatsu family."
    pand "Without one, the clan's future is lost."
    mc "..."
    mc "If you can speak, then you must be able to see and hear what Makoto's been doing, right?"
    pand "Yes, that's correct."
    mc "Then why can't you see how much she cares for you?"
    mc "After losing her father and the builders she's known for so long, how can you abandon her at a time like this?"
    pand "..."
    mc "..."
    mc "Makoto said that the two of you are part of a team..."
    mc "Don't you feel the same about her?"
    pand "..."
    pand "My feelings here are irrelevant."
    pand "I am but a spirit, created by the first head of the Komatsu Clan."
    pand "I cannot stray from my creator's wishes."
    mc "You're saying that you won't help Makoto anymore?"
    mc "...just because she was born a girl?"
    pand "As I said, only a male can inherit the Builders Guild..."
    pand "And the only way that Makoto can make up for it is if she..."
    pand "..."
    pand "Perhaps it would be better if I show you..."
    $ renpy.pause(1, hard=True)
    show story 008-61 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 008-62 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    mc "Mmm, Makoto..."
    mc "When you swing that heavy hammer around, everyone thinks you're a man..."
    mc "...but in the bedroom, only I know the truth."
    show story 008-63 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Ahh..."
    mako "[mc], d-don't stare so much... It's embarrassing..."
    show story 008-62 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Heh..."
    mc "There's no need to be shy, Makoto..."
    mc "We've been doing it for a while now, haven't we?"
    mc "I know how much you like it when I treat you like a woman..."
    show story 008-63 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "T-That's not true!"
    mako "I'm only doing this out of duty, okay!?"
    mako "S-So be more gentle with me..."
    show story 008-62 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Now why would I do that?"
    mc "You heard the hammer..."
    mc "The only way that you'll prove your worth to the Builders Guild is if you produce a proper heir for the Komatsu Clan!"
    mc "That means I gotta put my son into that sweet belly of yours!"
    show story 008-64 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mako "AHN!!!"
    show story 008-65 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Heh... I love those cute noises you make, Makoto..."
    mc "Can you feel my dick getting harder inside you?"
    show story 008-66 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "[mc]..."
    mako "W-We've been doing it every night..."
    mako "I need a... break, too... you know?"
    show story 008-65 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Sorry, no can do."
    mc "You belong to me now, Makoto."
    mc "And that means I get to fuck you anytime, anywhere."
    show mainquest_10_01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    pause
    mako "Ahn... ahn..."
    mako "So... rough..."
    mc "That's right..."
    mc "I love that lewd face of yours, Makoto..."
    mc "How many babies do you think we need before Pandoria is satisfied?"
    mako "Eh?"
    mako "W-What are you talking about? Aren't we stopping with just {i}one{/i}?"
    mc "Screw that!"
    mc "I ain't stopping until I put at least eight babies into you!"
    mc "You're going to start pumping them out, one after another!"
    mako "N-No way..."
    mako "I can't..."
    mc "Don't lie to me Makoto..."
    mc "Tell me how much you love my dick..."
    mako "N-Never..."
    mc "Come on... Admit the truth..."
    mako "I-I..."
    hide mainquest_10_01
    show story 008-67 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mako "I LOVE YOUR DICK, [mc!u]!!!"
    scene whitescreen with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 008-68 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "Ugh..."
    mc "...Where am I?"
    mc "Was that... a vision?"
    show story 008-69 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play music "audio/makoto.mp3"
    mc "..."
    mc "...Makoto?"
    show story 008-70 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "[mc]..."
    mako "Are you alright?"
    show story 008-69 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Y-Yeah..."
    show story 008-71 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Here, let me help you stand..."
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 008-72 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "Thanks for the help..."
    mc "What... happened to me?"
    show story 008-73 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "You looked like you were in a trance after you touched the hammer, [mc]..."
    mako "Did you... also speak to Pandy, too?"
    show story 008-72 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Y-Yeah... I did..."
    show story 008-74 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Amazing..."
    mako "I didn't think it was possible for anyone outside of the Komatsu Clan to speak with Pandy..."
    mako "You must have some incredible powers, [mc]."
    show story 008-72 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "She showed me... a vision..."
    mc "...of you being a {b}girl{/b}."
    show story 008-73 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Eh?"
    mako "Er, well, that's because I am... a girl..."
    show story 008-72 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Really!?"
    mc "How come you didn't say anything sooner?"
    show story 008-73 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "It's not that I try to hide it..."
    mako "I've been treated like a boy throughout my entire life..."
    mako "Most girls don't want to end up as builders, you see..."
    show story 008-75 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "And only a male can inherit the Builders Guild..."
    mako "Knowing that, my father raised me up as a boy since he didn't have a son."
    mako "I think he secretly hoped that I would still be able to inherit the family's name..."
    mako "But unfortunately, Pandoria and the rest of the builders didn't agree..."
    show story 008-72 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Your hammer actually mentioned that inside my vision..."
    show story 008-73 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Ah..."
    mako "Did Pandy say anything else about me?"
    show story 008-72 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Well, I asked Pandoria how the two of you could make up..."
    mc "And I think that she... is willing to speak to you again if you can produce a {b}true heir{/b}..."
    mc "In other words, she wants a son from you..."
    show story 008-76 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "..."
    mc "..."
    mc "Makoto, what's wrong?"
    show story 008-77 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Er..."
    mako "Pandy didn't happen to, uh, show you anything weird, did she?"
    mako "D-Definitely not anything lewd?"
    mako "...like me in bed with a guy who looks a lot like you?"
    show story 008-76 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "D-Did you see the same vision as me!?"
    show story 008-78 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "H-Hahahaha..."
    mako "That can't be right! I mean, we only just met!"
    show story 008-76 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Y-Yeah, you're right..."
    mc "It's not like your hammer can predict the future or anything..."
    show story 008-77 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "..."
    mako "So, [mc]... You aren't married or anything, right?"
    mako "Because if you aren't..."
    show story 008-76 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "I-I'm way too young to be married!"
    show story 008-79 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Figured as much..."
    mako "Do you think that maybe..."
    show story 008-78 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "...Nevermind."
    show story 008-80 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "What is it?"
    show story 008-77 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "If producing offspring is the only way for Pandy to speak to me again..."
    mako "Then I'll just have to do it..."
    mako "It's the only way I'll be able to restore my family's honor..."
    show story 008-76 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Makoto..."
    mc "You can't just have kids with anyone..."
    mc "That'd be awful for the child..."
    show story 008-79 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I know, but..."
    mako "What choice do I have here?"
    show story 008-78 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I'll probably have to get married to anyone who'll have me..."
    mako "And considering my looks, I doubt that it'll be easy..."
    show story 008-76 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Makoto, you're plenty attractive..."
    mc "I don't know how I didn't realize it before."
    show story 008-77 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Eh?"
    mako "Y-You mean that?"
    show story 008-76 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah..."
    mc "And you're pretty cute when you're blushing."
    show story 008-81 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "T-Then does that mean..."
    mako "...You'd be willing to marry me someday?"
    show story 008-80 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "What!?"
    mc "A-A marriage proposal, just like that!?"
    show story 008-77 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Oh, [mc]..."
    mako "I promise I'll be a good wife!"
    mako "I'll cook and clean... and I'll even work hard to pay all of the bills..."
    show story 008-78 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "...A-And we can do {i}it{/i} as often as you'd like."
    mako "I-I won't say no..."
    show story 008-80 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Sorry, Makoto..."
    mc "But that just wouldn't be right..."
    mc "I'm not ready for marriage yet..."
    show story 008-77 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Dang..."
    mako "Now what am I going to do?"
    show story 008-78 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "M-Maybe we can just do it for... you know... {i}fun{/i}..."
    mako "And I can get pregnant that way..."
    show story 008-82 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    pand "Ahem..."
    pand "Allow me to intervene..."
    show story 008-83 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mako "Eh!?"
    mako "Pandy, you're speaking to me again!?"
    pand "..."
    pand "[mc], it's clear to me that you are someone {i}special{/i}..."
    pand "To be able to speak to a Holy Relic such as myself must mean that you are no ordinary human being."
    mc "..."
    mc "(Could it be because of my Valla blood?)"
    pand "A bastard will never be accepted as a true heir..."
    pand "For a son to be legitimate, he must either be born through Makoto as your wife..."
    pand "...or as your {b}slave{/b}."
    mc "..."
    with vpunch
    mc "W-What!? You aren't trying to say that..."
    pand "Yes..."
    pand "If you trigger Makoto's Scarlet Contract and put a baby inside of her, I'll be willing to assist her again."
    mc "You're out of your mind..."
    mc "There's no way that she'd agree to that..."
    show story 008-75 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mako "Hmm..."
    mako "That's not really a bad idea..."
    show story 008-72 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Huh?"
    mc "Makoto, don't tell me that you're seriously thinking about doing this..."
    show story 008-73 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I mean, sure, it'll suck to be considered property and all, but..."
    mako "...if it means getting Pandy back, I'm willing to do anything."
    show story 008-72 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "You'd trade away your {i}freedom{/i} for the Builders Guild?"
    show story 008-74 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Of course..."
    with vpunch
    mako "I'd gladly stake my {b}life{/b} for the Komatsu Clan!"
    show story 008-72 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    "I can tell how serious she was from her words..."
    "Pandoria clearly wasn't just a hammer to her..."
    "She was also Makoto's friend... a friend she'd be willing to do anything to have back..."
    mc "..."
    mc "I understand..."
    mc "I can see that you're commited to this, Makoto..."
    mc "If that's the only way I can help you, I'll see what I can do about your Scarlet Contract."
    show story 008-81 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "R-Really, [mc]?"
    mako "Thank you..."
    show story 008-83 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    pand "Excellent..."
    pand "Now that that's settled, we can discuss terms for fixing this room..."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "Pandoria said that she would contact me on a later date with a quote for the room..."
    "Before they left, Makoto told me that I could visit her at the Builders Guild if I needed work..."
    "To buy Makoto's Scarlet Contract, I would first have to speak with Laureate..."
    $ renpy.end_replay()
    $ renpy.pause(1, hard=True)
    play sound "audio/ding.mp3" volume 3
    "[yel]Makoto's Character Card has been added to the Relationship Screen."
    play sound "audio/ding.mp3" volume 3
    "[yel]Builders Guild has been added to the Map Screen."
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump hallwaylabel_02

label mainquest_11:

    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 009-20 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/laureate.mp3"
    mc "Hey, Laureate..."
    mc "Do you have a moment?"
    mc "There's a Scarlet Contract that I'm interested in."
    show story 009-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Oh, I'd be delighted to help!"
    laur "If it's a Scarlet Contract you're concerned about, I'm the one to ask!"
    show story 009-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Er, yeah..."
    mc "Do you mind searching up a name so that I can see her price?"
    show story 009-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Heh..."
    laur "It appears that you're buying more girls, huh [mc]?"
    show story 009-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Not that I mind, of course."
    laur "Scarlet benefits immensely whenever a Scarlet Contract is sold."
    show story 009-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "T-This is a special case!"
    show story 009-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Sure, sure..."
    laur "Go on and tell me the name of this woman in question."
    show story 009-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Her name is, uh..."
    mc "Right! It's {b}Makoto Komatsu{/b}!"
    mc "She's from the..."
    show story 009-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "...Builders Guild, right?"
    show story 009-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah..."
    mc "Do you know her?"
    show story 009-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Of course I do..."
    laur "The Komatsu Clan is one of the most famous families in Scarlet."
    laur "This Makoto girl is a descendent from one of the [yel]{b}Six Heroes{/b}{/color}."
    show story 009-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Six Heroes?"
    mc "Who are they...?"
    show story 009-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Geez, [mc]..."
    laur "I'm going to assume that you didn't do very well in history class..."
    show story 009-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...No comment."
    show story 009-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "The [yel]Six Heroes{/color} were the most powerful warriors in Scarlet during the time of darkness..."
    laur "Though their names are lost in history, their sobriquets are remembered and honored to this very day."
    show story 009-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "[oj]The Beast, the Magician, the Angel, the Shepherd, the Berserker, and the Seer..."
    laur "(...names still pending.)"
    show story 009-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Together with their [yel]Holy Relics{/color}, the heroes banished the [yel]Evil Goddess{/color} who ruled over this land."
    show story 009-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "And it's thanks to these heroes that the people of Scarlet now live in peace."
    laur "...For the most part, anyway."
    show story 009-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(An Evil Goddess who {i}ruled{/i} over the land...)"
    mc "(That sounds... {i}unsettling{/i}...)"
    show story 009-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Hmm..."
    laur "[mc], a question, if I may."
    show story 009-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Yeah?"
    show story 009-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "How should I say this...?"
    show story 009-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "No one is '{i}pressuring{/i}' you into doing this, right?"
    show story 009-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "As in, no one is '{i}asking{/i}' you to try and buy this Makoto girl's contract?"
    show story 009-28-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Because if so, I think it would be in your best interest to tell me..."
    show story 009-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(I can't tell Laureate that I'm planning on buying Makoto's contract so that I can impregnate her on her request...)"
    show story 009-28-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "..."
    mc "..."
    with vpunch
    mc "O-Of course not! I'm just generally interested in her is all!"
    show story 009-28-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Heh..."
    laur "Is that right...?"
    show story 009-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Anyway, there's no rule forbidding you from buying her contract, even if she is considered a descendent of one of the [yel]Six Heroes{/color}."
    laur "Under the eyes of the Scarlet Laws, everyone is treated equally."
    show story 009-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "That's good news, I suppose."
    show story 009-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "That being said..."
    laur "I can already tell that her contract price will be astronomically high."
    laur "Purchasing this person's Scarlet Contract would likely prove to be impossible for you."
    show story 009-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Why is that?"
    show story 009-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "There are a lot Ellen Musky factors that goes into these things, but..."
    show story 009-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "For the most part, contracts are based on the value of the candidate."
    show story 009-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Due to her prestigious lineage, her price will easily be in the millions..."
    laur "You're going to need some crazy dev cheat codes in order to buyout her contract."
    show story 009-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 009-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Terribly sorry, [mc]..."
    laur "It's unfortunate that I couldn't be of more use."
    show story 009-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "That's okay, Princess."
    mc "I guess I'll have to tell her the news myself."
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/days.mp3"
    jump cityhalllabel_01

label mainquest_12:

    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 008-35 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/makoto.mp3"
    mc "Makoto...?"
    mc "Can I have a word?"
    show story 008-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Ah, [mc]..."
    mako "What brings you to the Builders Guild today?"
    show story 008-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "We need to talk..."
    mc "It's about what we discussed before."
    mc "Is Pandoria here?"
    show story 008-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "She's sleeping right now, so I'm only doing light work right now..."
    mako "Should I go ahead and wake her up?"
    show story 008-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Nah, don't bother."
    mc "We can talk without her."
    show story 008-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Hmm..."
    mako "It's about my Scarlet Contract, right?"
    show story 008-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Right..."
    mc "I had a word with the person who handles the contracts."
    show story 008-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "And...?"
    mako "What'd they say?"
    show story 008-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "It just isn't possible..."
    mc "Apparently, you're a descendent of one of the [yel]Six Heroes{/color}."
    mc "And because of that, your Scarlet Contract's price is... too high..."
    show story 008-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Are you sure?"
    mako "I mean, it's true that the Komatsu Clan are considered nobles in Scarlet, but..."
    mako "What's this 'Six Heroes' business?"
    show story 008-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "You don't even know the history behind your own clan!?"
    show story 008-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "It does sound a little familiar, but..."
    mako "I'm pretty sure that it's something that happened a long, long, long time ago, right?"
    show story 008-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "'{i}Live in the present, not in the past{/i}'. That's the Komatsu way."
    show story 008-41-01 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Makoto..."
    mc "I think I'd remember if my family had a hero in it or not..."
    show story 008-41-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Nah, my family has always been pretty humble about our origins..."
    mako "If anything, the clan is more obsessed with the builder's bloodline than being descended by some hero."
    show story 008-41-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Humble, huh?"
    mc "Yeah, I think that's a good word to describe you, Makoto."
    show story 008-41-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Eh?"
    mako "W-What do you mean?"
    show story 008-41-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I mean, you're apparently one of the most famous people in Scarlet..."
    mc "And yet, you're still here, working in the trenches like some common laborer..."
    mc "I can't say that I'd be willing to do the same in your position."
    show story 008-41-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Heh, thanks, [mc]!"
    mako "For me, it doesn't matter how high up you are in society..."
    mako "...a good work ethic is always respected, especially for a Komatsu!"
    show story 008-41-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I can't argue with that."
    show story 008-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Anyway..."
    mako "My Scarlet Contract's price is too expensive because of my name, huh?"
    show story 008-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "That's right..."
    mc "Even if I saved up for a hundred years, I still wouldn't be able to afford it."
    show story 008-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Darn..."
    mako "And here I thought my price would be really low since..."
    show story 008-41-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "...er, I'm n-not very feminine or good looking or anything."
    show story 008-41-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Don't say that, Makoto."
    mc "You're very charming in your own way."
    mc "I think you have a lot more fans than you realize."
    show story 008-41-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Er... T-Thanks, [mc]..."
    show story 008-41-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I'm sorry that I can't do more to help, Makoto."
    mc "But perhaps it's for the best. Maybe you should consider finding a new..."
    show story 008-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mako "W-Wait a second, [mc]..."
    mako "How about I... pay for the contract myself?"
    mako "That way, you can still become my owner."
    show story 008-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "P-Pay for your own Scarlet Contract!?"
    mc "Isn't that a little... too much?"
    show story 008-41-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "[mc]..."
    mako "Pandy was adamant that you were special..."
    mako "You're able to hear her voice, despite not being from the Komatsu Clan..."
    show story 008-41-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "That's why..."
    with vpunch
    mako "T-That's why I won't let anyone else impregnate me except you!!!"
    show story 008-41-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "..."
    mc "..."
    with vpunch
    mc "R-Regardless of what you want, the reality of the situation hasn't changed..."
    mc "Even if you sell the Builders Guild for top dollar, you still won't be able to afford your contract."
    show story 008-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "S-Sell the Builders Guild...?"
    mako "...No way."
    show story 008-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "T-That's just conjecture! I know you'd never do such a thing!"
    mc "I'm sure we'll think of something else..."
    show story 008-41-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Hmm..."
    mako "You know, that isn't a bad idea..."
    show story 008-41-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Alrighty [mc], leave it to me!"
    mako "A true Komatsu doesn't give up on her dreams!"
    mako "I'll make sure you become my master if it's the last thing I do!"
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "It seems that Makoto has a plan..."
    "All you can do now is continue on with your adventure..."
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    $ renpy.pause(1, hard=True)
    play music "audio/days.mp3"
    jump buildersguildlabel


label mainquest_13:

    call name_fix
    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/hammer.mp3" volume 2
    "After paying Makoto her fee, the two of us set off to fix Azula's room."
    "Makoto went to work while I occasionally helped out by handing her her supplies..."
    "From an outsider's point of view, it might have appeared strange that she was constantly muttering and giggling to herself..."
    "But I knew the truth... I knew that she was just speaking with Pandoria, her partner..."
    "And it was a beautiful sight to witness the relationship that the two of them shared..."
    stop music
    play sound "audio/coins.mp3" volume 3
    show love_mako at up_happy
    "[yel]You paid Makoto $1,000!"
    $ renpy.pause(1, hard=True)
    show story 013-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/makoto.mp3"
    mako "Whew..."
    mako "That just about wraps things up around here..."
    show story 013-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Wow, Makoto..."
    mc "The room looks better than it ever has!"
    mc "You Komatsu's really are geniuses at building!"
    show story 013-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Hehe... Thanks..."
    show story 013-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "We're just about finished here..."
    mako "All that's left to do is clean up and..."
    show story 013-05 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    stop music fadeout 1.0
    with vpunch
    mv2 "Heeeyyyyyyy!!!"
    mv2 "What's going on here!?"
    show story 013-06 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play music "audio/azula.mp3"
    azul "I've been hearing nothing but banging the whole day!"
    azul "What are you and your friend doing here, [mc]!?"
    show story 013-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh, hey there, Azula..."
    mc "Makoto and I are just fixing up your room."
    mc "What do you think? Does it look good?"
    show story 013-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Oh, wow! This room looks amazing now!"
    azul "The blue really brings out my hair, doesn't it?"
    show story 013-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Hehe..."
    azul "And here I thought the two of you were busy {b}breeding{/b} with one another..."
    azul "But seeing as your friend is a {i}boy{/i}, I guess I have nothing to worry about..."
    show story 013-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Er..."
    with vpunch
    azul "U-Unless you're into that sort of thing, [mc]..."
    azul "It {i}is{/i} [year], after all..."
    azul "And you zoomers never cease to amaze me..."
    show story 013-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Eh?"
    mako "B-But I'm not a..."
    show story 013-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "Azula, we're just here to fix your room..."
    mc "...Why would you ever compare the sound of loud banging to the sounds of sex!?"
    show story 013-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Eh?"
    azul "Didn't I tell you already? Male Vallas are incredibly aggressive in their pursuit for sex."
    azul "It's pretty normal for one to breed with his concubine until she's out in a coma..."
    show story 013-14 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "...and even then, they'll still continue the act until they are certain that there's a baby in their belly."
    azul "Naturally, one could only assume that the loud banging from earlier was the sound of you violently thrusting your penis up a sloppy hole."
    show story 013-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    azul "..."
    mako "..."
    show story 013-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Um... B-Breeding? Valla?"
    mako "What are you two talking about...?"
    mako "...and why does your friend have horns?"
    show story 013-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Ignore her, Makoto."
    mc "Azula can say some pretty weird things sometimes."
    show story 013-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    stop music fadeout 1.0
    azul "..."
    show story 013-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "That hammer you're holding..."
    azul "That is the great warhammer, 'Pandoria', is it not?"
    show story 013-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Eh?"
    mako "You know about Pandy?"
    show story 013-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "For you to be able to wield her..."
    azul "...I can only assume that you are the heir to the Komatsu Clan."
    show story 013-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Azula, is something wrong?"
    show story 013-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "..."
    show story 013-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Yeah, I'm fine..."
    azul "I should probably go..."
    show story 013-23 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play sound "audio/door.mp3" volume 3
    $ renpy.pause(2, hard=True)
    show story 013-24 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    mako "..."
    show story 013-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Hmm..."
    mako "I don't think she likes me very much..."
    mako "Did you see the way she was glaring at me?"
    show story 013-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "That's weird..."
    mc "Azula is usually friendly... She's the type of person who becomes friends with everyone she meets."
    show story 013-27 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    pand "How strange..."
    pand "For some reason, I feel as though I should know that blue-haired woman..."
    pand "...and yet, I can't remember her for the life of me."
    show story 013-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Pandy?"
    show story 013-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    pand "..."
    pand "Whatever the case, we're finished with the job."
    pand "The only thing left to do is clean up."
    show story 013-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Right."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "By the time we got done cleaning, it was already late in the evening..."
    "I thanked Makoto and Pandoria for their service, and waved them off as they marched back home to the Builders Guild."
    $ renpy.pause(1, hard=True)
    show story 013-30 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    show story 013-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "I hope Makoto gets home safely..."
    mc "Well, I doubt anyone would want to mess with her with Pandoria lugged over her shoulder..."
    show story 013-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Hey, [mc]?"
    azul "Can I have a word?"
    show story 013-33 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play music "audio/sad.mp3"
    mc "Huh? Azula?"
    mc "Were you watching Makoto leave?"
    show story 013-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "That person just now..."
    azul "Just how do you know him?"
    show story 013-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "You mean, Makoto?"
    mc "Shes the head of the Builders Guild..."
    mc "...and I commissioned her to fix your room."
    show story 013-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "...I see."
    show story 013-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Azula, what's wrong?"
    mc "You've been acting weird today."
    show story 013-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Oh, have I?"
    azul "...It's just that I was a little concerned is all."
    show story 013-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...Why?"
    show story 013-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Because Pandoria is a [yel]Holy Relic{/color}..."
    azul "And to us, a Holy Relic is a {b}human-made weapon{/b} specifically designed to hunt and kill Vallas."
    show story 013-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "In my day, they were known as the 'God Slayer' weapons."
    azul "...I was afraid that the boy had the intention of harming you with it earlier."
    show story 013-37 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Perhaps that {i}uneasiness{/i} is why I haven't been myself."
    show story 013-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "...Holy Relics are weapons designed to kill Vallas?"
    mc "So if I were to be hit by one, would I..."
    show story 013-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "For most Vallas, getting struck by a Holy Relic is instant death..."
    show story 013-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "If you ever plan on meeting him again, you should be on guard..."
    azul "...Humans have a tendency to betray those closest to them for their own personal gain."
    show story 013-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Makoto isn't like that at all!"
    mc "She won't harm us. She's a good person."
    show story 013-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Hmm..."
    azul "I wonder about that..."
    show story 013-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "And this {i}boy{/i} was a {i}girl{/i}, huh?"
    show story 013-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Y-Yeah..."
    mc "I also thought she was a boy at first, too."
    show story 013-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "I see..."
    azul "Well, if you say that you trust her..."
    show story 013-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "...Then I will too."
    show story 013-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "You are my male companion, after all..."
    azul "You are the one who resurrected me, thus our lives are bound together by fate."
    show story 013-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Thanks, Azula."
    show story 013-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    stop music fadeout 1.0
    azul "..."
    mc "..."
    mc "What's with that smirk, Azula? Is there something else wrong?"
    show story 013-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Well..."
    azul "I don't have to listen to Estelle's snoring anymore, thanks to you..."
    azul "And your [mil] and [sil] are both in their rooms..."
    show story 013-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "So how about you follow me so that I can give my hero a proper reward."
    show story 013-47 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "Azula and I tiptoed our way toward her newly furnished room..."
    "The last thing we wanted was for [mil!c] and Estelle to interrupt us..."
    $ renpy.pause(1, hard=True)
    show story 013-48 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    azul "..."
    show story 013-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "[mc], I sense that you're nervous..."
    show story 013-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "A little..."
    mc "I mean, I've always been raised with the idea of only having one mate..."
    mc "You know, like getting married and stuff."
    show story 013-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "I see..."
    azul "[mc], you have to understand that the circumstances have changed..."
    show story 013-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "You are a male Valla... thus, it is your duty to want to {i}spread{/i} your seed to as many girls as possible."
    show story 013-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "After all, that is the primitive nature of all creatures, is it not?"
    show story 013-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Azula, you wouldn't understand..."
    mc "Even if I am part-Valla, I was raised a human..."
    show story 013-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "Hehe..."
    azul "I think that it's cute of you to think that way."
    show story 013-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "To be honest, I'm mystified by what humans are capable of..."
    azul "Vallas like myself don't generally think about things like {i}philosophy{/i} or {i}empathy{/i}..."
    show story 013-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "We only do things that we consider to be {i}natural{/i}..."
    azul "I suppose you can say that we're {i}simple creatures{/i}..."
    show story 013-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "All we need in life is food, water..."
    show story 013-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "...and of course, {b}essence{/b}."
    show story 013-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    show mainquest_13_01
    pause
    mc "..."
    azul "How is that, [mc]?"
    azul "Do you enjoy the warmth of my touch?"
    mc "Yeah..."
    mc "Azula, you're so good at this..."
    hide mainquest_13_01
    show story 013-52 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    azul "..."
    show story 013-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "[mc], I understand that you're close, but..."
    azul "...As my male companion, you still have a job to do."
    show story 013-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "*GULP*"
    mc "And that is?"
    show story 013-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    show story 013-55 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    show story 013-56 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    show story 013-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    show story 013-59 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show story 013-58 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    azul "I'm going to need you to drive that cock of yours into my pussy."
    show story 013-59 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "I understand."
    mc "I want to fuck you, Azula."
    show story 013-60 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show mainquest_13_02
    pause
    azul "How is it, [mc]?"
    azul "Do you enjoy my wet and sloppy pussy?"
    mc "A-Azula..."
    mc "Shit, this feels too good...!"
    mc "...I'm getting close!"
    hide mainquest_13_02
    show story 013-61 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    azul "No, [mc]... You can't finish yet..."
    azul "I still require {i}more{/i}... {b}ESSENCE{/b}!!!"
    scene whitescreen with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 013-65 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    play music "audio/scary.mp3"
    azul "(...)"
    azul "(Am I... {i}alive{/i}?)"
    show mainquest_13_03 with Dissolve(.5)
    $ renpy.pause(3, hard=True)
    play sound "audio/footsteps.mp3" volume 3
    scene whitescreen with Dissolve(2)
    $ renpy.pause(1.5, hard=True)
    stop sound
    show mainquest_13_04 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    azul "..."
    azul "For you to have awakened me..."
    azul "...you must be an {b}extremely powerful Valla{/b}."
    mv2 "..."
    azul "But from you..."
    azul "...I can sense a deep darkness troubling your heart."
    azul "What is your purpose for having brought me back?"
    mv2 "..."
    azul "...Who are you?"
    show mainquest_13_05 with Dissolve(1)
    $ renpy.pause(2, hard=True)
    scene whitescreen with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)



    scene black with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    show story 013-62 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    show story 013-63 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "..."
    show story 013-64 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "(Azula's fast asleep...)"
    mc "(How long was I out?)"
    show story 013-66 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    mc "(And that dream just now... it felt so vivid...)"
    mc "(But who was that person with Azula?)"
    mc "(...Wasn't I the one to have awakened her?)"
    show story 013-63 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(I should probably leave before [mil!c] or Estelle finds us...)"
    $ renpy.pause(.5, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    $ renpy.end_replay()
    stop music fadeout 1.0
    play sound "audio/ding.mp3" volume 3
    "[yel]Azula's presence in the household has increased the weekly Waifu Tax."
    "[yel]Your relationship with Azula has reached a new level."
    play music "audio/days.mp3"
    jump mcroomlabel

label mainquest_14:

    hide screen status01
    stop music fadeout 3
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    "Having raised enough funds for her own Scarlet Contract, Makoto and I set off to City Hall to speak with Laureate..."
    "Though adamant in her decisions at first, I could sense Makoto growing increasingly anxious..."
    "After all, she had sacrificed so much in order to see this done... I knew I had to be with her until the very end."
    $ renpy.pause(1, hard=True)
    show story 017-01 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play music "audio/laureate.mp3"
    laur "..."
    show story 017-02 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Why hello there, [mc]..."
    show story 017-03 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "What brings you to my..."
    show story 017-04 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    laur "Oh?"
    laur "It appears you brought a friend..."
    show story 017-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Ah..."
    mako "H-Hi, Miss Highness... I mean, m'am... I mean, um..."
    show story 017-06 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Psst... [mc], how am I supposed to address a princess?"
    show story 017-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Hehe..."
    laur "There's no need to be so formal..."
    show story 017-08 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "The Komatsu Clan has been friends with the royal family for many generations."
    show story 017-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "So please be at ease. We are already well-acquainted with one another."
    show story 017-05 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "W-Well, that might be true, but..."
    show story 017-10 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "This is still my first time meeting a princess... I'm so nervous that I don't even know what to say..."
    show story 017-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Hehe..."
    laur "Our first time meeting? That's not quite true..."
    show story 017-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "We've actually met a few times before."
    show story 017-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Eh? We did?"
    show story 017-07 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Most certainly."
    show story 017-09 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "I even met you back when you were a little baby."
    show story 017-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Gosh, you were so adorable. I even cradled you in my arms."
    show story 017-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Er..."
    mc "Princess, how is that even possible?"
    mc "Aren't you supposed to be younger than Makoto?"
    show story 017-16 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    laur "Eh?"
    show story 017-14 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    laur "Ah, I suppose you're right..."
    show story 017-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "A slip of the tongue. I can be quite forgetful at times."
    show story 017-17 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mako "..."
    show story 017-18 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "A-Anyway..."
    laur "What is it that brought you here today, [mc]?"
    show story 017-19 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Oh, that's right..."
    mc "Makoto and I have business to discuss with you, Princess..."
    mc "We want to... er... buy her Scarlet Contract..."
    show story 017-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Hmm, is that so?"
    show story 017-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "How interesting... May I ask how the two of you are acquainted?"
    show story 017-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "(Damn, it's too embarassing to tell her the truth...)"
    show story 017-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mako "We're trying to buy my Scarlet Contract for the sake of the Builders Guild!"
    show story 017-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "You see, the only way it can be saved is if [mc] puts a baby inside me and gives my family a male heir!"
    show story 017-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "And since we're not married, the only way the baby will be considered legitimate is if he controls my Scarlet Contract!"
    show story 017-25 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Makoto..."
    mc "I can't believe you actually went ahead and said it..."
    show story 017-04 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Curious..."
    show story 017-26 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "I have heard that the Builders Guild has been struggling for business since your father's passing..."
    show story 017-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "However, I do pray that you're not making a grave mistake in trusting this man..."
    show story 017-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "After all, this is your life we're talking about. Who knows what sort of dastardly deeds [mc] could be planning once all of the papers are signed..."
    show story 017-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Hehe... Just kidding!"
    show story 017-22 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "P-Princess..."
    mc "Even if you're joking, words can still sting..."
    show story 017-23 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mako "...I trust him!"
    show story 017-24 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "[mc] wouldn't take advantage of me... He's not that type of person..."
    show story 017-27 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Hehe... I like your determination..."
    show story 017-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "But is saving the Builders Guild the primary reason why you wish to relinquish your freedom?"
    show story 017-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "...or could it be that you actually {b}love{/b} and want to be closer to [mc]."
    show story 017-12 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Don't bother trying to lie... I can read minds, hehe..."
    show story 017-29 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    mako "O-Of course not!"
    show story 017-11 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "The Builders Guild is the most important thing to me! Everything else is secondary!"
    show story 017-30 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "...I-Isn't that right, [mc]?"
    show story 017-31 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    laur "..."
    show story 017-32 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Hehe... I won't delve any further..."
    show story 017-15 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "A contract is a contract, after all. Each sale greatly benefits the future of Scarlet."
    show story 017-33 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Right!"
    mako "I have the money in my bank account as we speak! I've saved up everything just for this moment!"
    show story 017-34 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "So please! Let me buy my own Scarlet Contract for [mc]!"
    show story 017-35 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Eh?"
    laur "You mean to tell me that you raised the entirety of your contract on your own?"
    laur "...and [mc] didn't do a darn thing?"
    show story 017-36 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Well, yeah..."
    mc "It was her idea to have her Scarlet Contract bought in the first place..."
    mc "She just wants it under my name is all..."
    show story 017-37 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    with vpunch
    laur "[mc], how shameless...!"
    show story 017-38 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Huh?"
    mc "What do you mean?"
    show story 017-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "The lady doth protest too much, methinks!"
    show story 017-40 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Though this be madness, yet there is method in 't!"
    show story 017-39 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "O, woe is me! T' have seen what I have seen, see what I see!"
    show story 017-41 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "W-What are you talking about, Princess?"
    show story 017-42 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "What I'm trying to say is..."
    show story 017-43 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "You've allowed this fair maiden to do all of the grunt work by herself while you sat in the background, waiting to reap the rewards!?"
    show story 017-44 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "That's so cruel, [mc]! Chivalry might be dead, but this takes slavery to a whole 'nother level!"
    show story 017-45 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    with vpunch
    mc "WHAT!?"
    show story 017-29 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "H-Hold on a second!"
    mako "It's not [mc]'s fault... This was my idea in the first place..."
    show story 017-46 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "Wow, [mc]..."
    laur "So you've trained her so well that she'll come up with any lame excuse to defend you, huh?"
    show story 017-28 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "That sort of evil manipulation belongs only in the movies, y'know? Mao Mao would be ashamed..."
    show story 017-13 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    with vpunch
    mc "Oi, oi..."
    mc "Makoto's adamant on buying her Scarlet Contract... Nothing I say will change her mind."
    mc "What exactly do you propose I should do?"
    show story 017-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "The only honorable thing you can do, [mc]..."
    show story 017-21 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "You are going to pay up some of her contract with your own money."
    show story 017-20 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    laur "It's only fair, after all. You are a man of honor, are you not?"
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    stop music fadeout 3.0
    "After a long and strenuous lecture regarding the principles of knighthood and honor..."
    "...I agreed that I would return to Laureate and pay up a small portion of Makoto's Scarlet Contract."
    $ renpy.pause(1, hard=True)
    show story 017-47 with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    mc "..."
    mc "Something wrong, Makoto?"
    show story 017-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Nah, nothing really..."
    mako "It's just something the princess said is all..."
    show story 017-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "Hmm?"
    mc "What do you mean?"
    show story 017-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Well, she said that she's met me before, right?"
    show story 017-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I don't know why, but I think she's telling the truth..."
    show story 017-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Though I can't say I remember ever meeting her in person..."
    show story 017-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Are you sure you didn't just forget?"
    mc "Laureate also mentioned that her memory wasn't very good..."
    show story 017-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "I think I'd remember if I met a princess or not..."
    show story 017-51 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    show story 017-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "The reason why I think we've met before is because, well..."
    show story 017-50 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Y'see, people naturally assume that I'm a boy when they meet me..."
    show story 017-52 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "But the princess instantly recognized that I was a girl..."
    show story 017-48 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "That's why I have a feeling that she knows me personally..."
    show story 017-49 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "..."
    mc "Laureate has a good eye for these types of things..."
    mc "And we did mention that it was {i}your{/i} contract that we were after."
    mc "She probably looked up your details ahead of time and saw that you were a girl."
    show story 017-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Hmm, you're probably right..."
    mako "Maybe I'm just overthinking this... After all, she has no reason to lie, right?"
    show story 017-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Anyway, I'll leave the rest of my Scarlet Contract to you, [mc]."
    show story 017-55 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "How much did she say she wanted from you?"
    show story 017-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "[yel]$10,000{/color}..."
    show story 017-56 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Is that too much for you? Maybe I should just..."
    show story 017-54 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mc "No, no, no..."
    mc "Laureate is right. I can't honestly say that I'm helping you or the Builders Guild if I don't contribute in some way."
    show story 017-57 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Hehe... Thank you, [mc]..."
    mako "I think I made the right decision in trusting you."
    show story 017-53 with Dissolve(.5)
    $ renpy.pause(.5, hard=True)
    mako "Just don't forget about me, okay?"
    $ renpy.pause(1, hard=True)
    scene black with Dissolve(1.5)
    $ renpy.pause(1.5, hard=True)
    play sound "audio/ding.mp3" volume 3
    "[yel]Quest Log updated!"
    play music "audio/days.mp3"
    jump streetlabel_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
