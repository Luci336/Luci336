screen questscreen():
    modal True
    hbox xalign 0.5 yalign 0.8:
        imagebutton:
            idle "screens_update/blank_screen.webp"
    hbox xalign 0.5 yalign 0.05:
        text "{size=200}Quests" outlines [ (absolute(2), "#000", absolute(0), absolute(1)) ] color "#FFF" font "Timeless.ttf" xalign 0.5
    hbox xalign 0.97 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_relations.webp" hover "icons_update/icon_relations_hover.webp" action [Show("statusscreen"), Hide("questscreen")]
    hbox xalign 0.91 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_map.webp" hover "icons_update/icon_map_hover.webp" action [Show("mapscreen"), Hide("questscreen")]
    hbox xalign 0.85 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_quest.webp" hover "icons_update/icon_quest_hover.webp" action [Show("status01"), Hide("questscreen")]
    hbox xalign 0.79 yalign 0.03:
        imagebutton:
            idle "icons_update/icon_bag.webp" hover "icons_update/icon_bag_hover.webp" action [Show("inventoryscreen"), Hide("questscreen")]

    vbox xalign 0.5 yalign 0.5:

        if (mainquest == 0):
            text "- Navigate and find the bathroom [yel](Main Quest)" style "questfont"
        if (mainquest == 1):
            text "- Speak with Silvia in the living room. [yel](Main Quest)" style "questfont"
        if (mainquest == 2):
            text "- Find Silvia around the house. [yel](Main Quest)" style "questfont"
        if (mainquest == 3):
            text "- Wait for Silvia in the living room. [yel](Main Quest)" style "questfont"
        if (mainquest == 4 or mainquest == 5 or mainquest == 6):
            text "- Seek out the Lady of the Lake at Scarlet Park. [yel](Main Quest)" style "questfont"
        if (mainquest == 7):
            text "- Speak with Serena to inquire a job. [yel](Main Quest)" style "questfont"
        if (mainquest == 8):
            text "- Head to City Hall to view Silvia and Estelle's Scarlet Contracts. [yel](Main Quest)" style "questfont"
        if (mainquest == 9 and estebought == False):
            text "- Purchase Estelle's Scarlet Contract at City Hall for $5,000. [yel](Main Quest)" style "questfont"
        if (mainquest == 9 and azulevents == 4 and sidequest >= 5 and estebought):
            text "- Visit the living room during the morning. [yel](Main Quest)" style "questfont"
        if (mainquest == 10):
            text "- Speak to Laureate regarding Makoto's Scarlet Contract. [yel](Main Quest)" style "questfont"
        if (mainquest == 11):
            text "- Tell Makoto the bad news. [yel](Main Quest)" style "questfont"
        if (mainquest == 12 and makoevents >= 2 and azulbought == False):
            text "- Pay Makoto $1,000 to fix a room for Azula. [yel](Main Quest)" style "questfont"
        if (mainquest == 13 and makoevents >= 6 and azulbought):
            text "- Speak to Laureate regarding Makoto's Scarlet Contract. [yel](Main Quest)" style "questfont"
        if (mainquest == 14 and makobought == False):
            text "- Purchase Makoto's Scarlet Contract at City Hall for $10,000. [yel](Main Quest)" style "questfont"


        if (sidequest == 17 and mainquest == 14 and makobought == True and serebought == True):
            hbox xalign 0.5 yalign 0.5:
                text "[yel]You've reached the end of this current update." style "questfont"


        if (silvevents == 0 and silvaff < 5 and mainquest >= 9):
            hbox xalign 0.5 yalign 0.5:
                text "- Raise Silvia's Affection." style "questfont"
        if (silvevents == 0 and silvaff == 5 and silvquest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Visit the living room during the evening. [pur](Silvia)" style "questfont"
        if (silvevents == 1 and silvaff == 5 and silvquest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Find the Flower Girl at the street at either evening or night. [pur](Silvia)" style "questfont"
        if (silvevents == 2 and silvaff == 5 and silvquest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Return to Silvia's bedroom with a magical flower during the evening. [pur](Silvia)" style "questfont"

        if (silvevents == 3 and silvaff < 10):
            hbox xalign 0.5 yalign 0.5:
                text "- Raise Silvia's Affection." style "questfont"
        if (silvevents == 3 and silvaff == 10 and silvquest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Visit the living room during the evening. [pur](Silvia)" style "questfont"
        if (silvevents == 4 and silvaff == 10 and silvquest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Visit the living room during the morning. [pur](Silvia)" style "questfont"


        if (esteevents == 0 and esteaff < 4 and mainquest >= 9 and estebought == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Raise Estelle's Affection." style "questfont"
        if (esteevents == 0 and esteaff == 4 and estequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Visit your bedroom in the evening. [pur](Estelle)" style "questfont"
        if (esteevents == 1 and esteaff == 4 and estequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Look around the house to find Estelle and apologize (Evening). [pur](Estelle)" style "questfont"
        if (esteevents == 2 and esteaff == 4 and estequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Seek out Estelle at the park (Evening). [pur](Estelle)" style "questfont"

        if (esteevents == 3 and esteaff < 8):
            hbox xalign 0.5 yalign 0.5:
                text "- Raise Estelle's Affection." style "questfont"
        if (esteevents == 3 and esteaff == 8 and estequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Visit the living room during the evening. [pur](Estelle)" style "questfont"
        if (esteevents == 4 and esteaff == 8 and estequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Pick up Estelle's textbook from Serena at the store [pur](Estelle)" style "questfont"
        if (esteevents == 5 and esteaff == 8 and estequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Speak with Estelle during the afternoon inside her room. [pur](Estelle)" style "questfont"

        if (esteevents == 6 and esteaff < 13 and serebought and makobought):
            hbox xalign 0.5 yalign 0.5:
                text "- Raise Estelle's Affection." style "questfont"
        if (esteevents == 6 and esteaff == 13 and estequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Head to the living room during the morning. [pur](Estelle)" style "questfont"
        if (esteevents == 7 and esteaff == 13 and estequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Visit City Hall to pick up your package during the morning. [pur](Estelle)" style "questfont"
        if (esteevents == 8 and esteaff == 13 and estequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Return to your bedroom at noon. [pur](Estelle)" style "questfont"


        if (azulevents == 0 and azulaff < 4 and mainquest >= 9):
            hbox xalign 0.5 yalign 0.5:
                text "- Raise Azula's Affection." style "questfont"
        if (azulevents == 0 and azulaff == 4 and azulquest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Visit the living room during the morning. [pur](Azula)" style "questfont"
        if (azulevents == 1 and azulaff == 4 and azulquest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Visit Azula at the park during the morning. [pur](Azula)" style "questfont"

        if (azulevents == 2 and azulaff < 9):
            hbox xalign 0.5 yalign 0.5:
                text "- Raise Azula's Affection." style "questfont"
        if (azulevents == 2 and azulaff == 9 and azulquest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Visit Azula at the park during the morning. [pur](Azula)" style "questfont"
        if (azulevents == 3 and azulaff == 9 and azulquest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Check out the hallway at midnight. [pur](Azula)" style "questfont"


        if (laurevents == 0 and lauraff < 4 and mainquest >= 9):
            hbox xalign 0.5 yalign 0.5:
                text "- Raise Laureate's Affection." style "questfont"
        if (laurevents == 0 and lauraff == 4 and laurquest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Visit the living room during the morning. [pur](Laureate)" style "questfont"
        if (laurevents == 1 and lauraff == 4 and laurquest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Laureate has requested that you meet her at midnight. [pur](Laureate)" style "questfont"
        if (laurevents == 2 and lauraff == 4 and laurquest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Meet your personal trainer at the park during evenings and nights. [pur](Laureate)" style "questfont"


        if (makoevents == 0 and makoaff < 4 and mainquest >= 12):
            hbox xalign 0.5 yalign 0.5:
                text "- Raise Makoto's Affection." style "questfont"
        if (makoevents == 0 and makoaff == 4 and makoquest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Visit the living room at night. [pur](Makoto)" style "questfont"
        if (makoevents == 1 and makoaff == 4 and makoquest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Head to the street during the evening. [pur](Makoto)" style "questfont"

        if (makoevents == 2 and makoaff < 8):
            hbox xalign 0.5 yalign 0.5:
                text "- Raise Makoto's Affection." style "questfont"
        if (makoevents == 2 and makoaff == 8 and makoquest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Visit the living room during the morning. [pur](Makoto)" style "questfont"
        if (makoevents == 3 and makoaff == 8 and makoquest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Purchase swim trunks from Serena at the store. [pur](Makoto)" style "questfont"
        if (makoevents == 4 and makoaff == 8 and makoquest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Head to the beach at noon. [pur](Makoto)" style "questfont"
        if (makoevents == 5 and makoaff == 8 and makoquest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Explore the beach at noon. [pur](Makoto)" style "questfont"


        if (ferrevents == 0 and ferraff < 5 and laurevents >= 3):
            hbox xalign 0.5 yalign 0.5:
                text "- Raise Ferry's Affection." style "questfont"
        if (ferrevents == 0 and ferraff == 5 and ferrquest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Visit the park during the evening. [pur](Ferry)" style "questfont"


        if (sereevents == 0 and sereaff < 5 and mainquest >= 9):
            hbox xalign 0.5 yalign 0.5:
                text "- Raise Serena's Affection." style "questfont"
        if (sereevents == 0 and sereaff == 5 and serequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Visit the living room during the evening. [pur](Serena)" style "questfont"
        if (sereevents == 1 and sereaff == 5 and serequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Speak with Serena during the morning. [pur](Serena)" style "questfont"

        if (sereevents == 2 and sereaff < 9):
            hbox xalign 0.5 yalign 0.5:
                text "- Raise Serena's Affection." style "questfont"
        if (sereevents == 2 and sereaff == 9 and serequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Visit the street during the morning. [pur](Serena)" style "questfont"
        if (sereevents == 3 and sereaff == 9 and serequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Speak with Silvia during the afternoon. [pur](Serena)" style "questfont"
        if (sereevents == 4 and sereaff == 9 and serequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "-Take Serena to Evergarden Cafe during the afternoon. [pur](Serena)" style "questfont"

        if (sereevents == 5 and sereaff < 14 and estebought):
            hbox xalign 0.5 yalign 0.5:
                text "- Raise Serena's Affection." style "questfont"
        if (sereevents == 5 and sereaff == 14 and serequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Visit the street during the morning. [pur](Serena)" style "questfont"
        if (sereevents == 6 and sereaff == 14 and serequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Stay in your bedroom during night. [pur](Serena)" style "questfont"


        if (sereevents == 7 and sereaff == 14 and sidequest >= 6):
            hbox xalign 0.5 yalign 0.5:
                text "- Speak with Serena during the afternoon." style "questfont"
        if (sereevents == 8 and sereaff == 14 and sidequest >= 6):
            hbox xalign 0.5 yalign 0.5:
                text "- Visit the living room at night. [pur](Serena)" style "questfont"
        if (sereevents == 9 and sereaff == 14 and serebought == False):
            hbox xalign 0.5 yalign 0.5:
                text "- Purchase Serena's Scarlet Contract at City Hall for $10,000. [pur](Serena)" style "questfont"


        if (sereevents == 9 and sereaff < 19 and serebought and makobought):
            hbox xalign 0.5 yalign 0.5:
                text "- Raise Serena's Affection." style "questfont"
        if (sereevents == 9 and sereaff == 19 and serequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- On a weekday, visit the living room during the morning. [pur](Serena)" style "questfont"
        if (sereevents == 10 and sereaff == 19 and serequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Find Celestia at the street during the night. [pur](Serena)" style "questfont"


        if (celeevents == 0 and celeaff < 3 and celemet):
            hbox xalign 0.5 yalign 0.5:
                text "- Raise Celestia's Affection." style "questfont"
        if (celeevents == 0 and celeaff == 3 and celemet and celequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Speak with Celestia during the night. [pur](Celestia)" style "questfont"
        if (celeevents == 1 and celetreasure == 0 and celeaff == 3 and celequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Search the streets for 'treasure' (Midnight). [oj](0/2) [pur](Celestia)" style "questfont"
        if (celeevents == 2 and celetreasure == 1 and celeaff == 3 and celequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Search the streets for 'treasure' (Midnight). [oj](1/2) [pur](Celestia)" style "questfont"
        if (celeevents == 3 and celetreasure == 2 and celeaff == 3 and celequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Report back to Celestia with your results (Midnight). [pur](Celestia)" style "questfont"
        if (celeevents == 4 and celeaff == 3 and celequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Find Celestia at the Park (Midnight). [pur](Celestia)" style "questfont"

        if (celeevents == 5 and celeaff < 6 and celemet):
            hbox xalign 0.5 yalign 0.5:
                text "- Raise Celestia's Affection." style "questfont"
        if (celeevents == 5 and celeaff == 6 and celemet and celequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Speak with Celestia (Night). [pur](Celestia)" style "questfont"
        if (celeevents == 6 and celeaff == 6 and celemet and celequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Head to City Hall (Midnight). [pur](Celestia)" style "questfont"
        if (celeevents == 7 and celeaff == 6 and celemet and celequest == True):
            hbox xalign 0.5 yalign 0.5:
                text "- Find Celestia at her usual spot (Midnight). [pur](Celestia)" style "questfont"


        if (goldenticket and goldenticketevents == 0):
            hbox xalign 0.5 yalign 0.5:
                text "- Find someone interested in the Golden Ticket... [red](Unavailable)" style "questfont"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
