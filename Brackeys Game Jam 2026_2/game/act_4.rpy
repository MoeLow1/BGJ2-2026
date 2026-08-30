label act_04:





    #region fourth Act 

    play music out_of_body fadein 1.0

    # side of door next to pannel shot
    "the beast is also there, impatiantly waiting for you to open the door"
    "next to the pannel lies a partially melted key"
    "as you get closer to the control pannel the beast backs off giving you some space, inviting you to open the door"
    menu:
        "open the door":

            # open door to field shot
            narrator"You insert the key and give it a turn"
            
            if trust>=2:
                "The door begains to creak open, its jittering as it struggles to open for the first time in many years"
                "the beast sits patiently waiting for the rusted door to finish openeing before moving out, dragging its bloated body behind"
                "You wait a while till its fully out of view, and you are on your way home"
                "Its a long path but you make it back, The stolen goods sell well"
                "Deep within the forest, the creature remains hidden from sight. In time, rumors of the beast begin to spread, its existence slowly becoming an urban legend."
                jump trust_ending

            elif trust <2:
                "The door begains to creak open, its jittering as it struggles to open for the first time in many years"
                "You peak outside to see a an open field"
                "Before you can turn around the beast lunges at jaw open taking sinking its jaws into your guts"
                "A sudden shock of cold spreads aross the wound, radiating to your legs and chest, you collapse to the floor soon after"
                "Laying on the ground unable to move you bleed out, everything goes dark and you die" #beast slayed ending (betrayl)
                jump game_over

        "ready your weapon": #maybe an if statment here with a varriable to grab the better weaon or not
            "unconvinced with the space you were given, you ready your weapon and the beast backs away even more, now cornered to the wall"
            narrator"You insert the key and give it a turn"
            "The door begains to creak open, its jittering as it struggles to open for the first time in many years"
            "the creature rushs to the door, attempting to squeezing itself through the narrow gap"
            
            menu:

                "Fire":
                    # open field 
                    if weapon =="silver rifle":
                        "You steady your aim, the rifle lets out a metallic ring echoing in the open field, a small silver stake embeds itself in the back of the beasts skull, it collapses"
                        "Walking past the corpse you sense a foul smell, that of burning flesh, the metalic stake sizzling against the poor creatures skull"
                        "You can't wait to get home and wash your hands of this whole situation" #beast slayed ending (betrayl)
                        jump slay_beast_ending

                    elif weapon =="standered":
                        "a plume of smoke errupts from the gun, the bullet striking the creature in its back, it scrambles to escape only to later then collapes to the ground"
                        "after a breif moment of silence you make your back home, it is a long road"
                        "It is a long way home, you are followed home and get killed in the woods" #beast slayed ending (betrayl)
                        jump game_over


                "let it be":
                    "it everntaully forces its way through, "
                    "after arriving back you wake up to hear that a nearby village has been ravaged from an unknown creature, making its way to other towns"
                    jump SEMI_TRUST_ENDING

    # jump act_04
