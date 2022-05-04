label chargift(char):
    menu:
        "Give Magical Flower... [red](Current: [inventory_magicflower])" if (inventory_magicflower > 0 and inventory_magicflower < 4):
            $ inventory_magicflower -= 1
            $ givegift = True
            if (char == "silvia"):
                "[yel]You handed [char!c] a Magical Flower..."
                call charaff ("silvia")
            elif (char == "estelle"):
                "[yel]You handed [char!c] a Magical Flower..."
                call charaff ("estelle")
            elif (char == "azula"):
                "[yel]You handed [char!c] a Magical Flower..."
                call charaff ("azula")
            return
        "Give Parfait... [red](Current: [inventory_parfait])" if (inventory_parfait > 0 and inventory_parfait < 4):
            $ inventory_magicflower -= 1
            $ givegift = True
            if (char == "silvia"):
                "[yel]You handed [char!c] a Parfait..."
                call charaff ("silvia")
            elif (char == "estelle"):
                "[yel]You handed [char!c] a Parfait..."
                call charaff ("estelle")
            elif (char == "azula"):
                "[yel]You handed [char!c] a Parfait..."
                call charaff ("azula")
            return
        "Give Plushie... [red](Current: [inventory_plushie])" if (inventory_plushie > 0 and inventory_plushie < 4):
            $ inventory_magicflower -= 1
            $ givegift = True
            if (char == "silvia"):
                "[yel]You handed [char!c] a Plushie..."
                call charaff ("silvia")
            elif (char == "estelle"):
                "[yel]You handed [char!c] a Plushie..."
                call charaff ("estelle")
            elif (char == "azula"):
                "[yel]You handed [char!c] a Plushie..."
                call charaff ("azula")
            return
        "Give Book... [red](Current: [inventory_book])" if (inventory_book > 0 and inventory_book < 4):
            $ inventory_magicflower -= 1
            $ givegift = True
            if (char == "silvia"):
                "[yel]You handed [char!c] a Book..."
                call charaff ("silvia")
            elif (char == "estelle"):
                "[yel]You handed [char!c] a Book..."
                call charaff ("estelle")
            elif (char == "azula"):
                "[yel]You handed [char!c] a Book..."
                call charaff ("azula")
            return
        "Nevermind..." if True:
            return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
