label act_04:





    #region fourth Act 

    
    "{b}the beast is also there, impatiantly waiting for you to open the door{/b}"
    "as you get closer to the control pannel the beast makes room for you as a way to encorage you to open the door"
    menu:
        "open the door":
            $ trust +=1
            "depending unless you have shown no hostility prior, the beast will either attack you after the door is open or leave you be in the full trust ending"
            if trust==2:
                narrator"you both sit patenily waiting for the rusted door to finish openeing"
                "the beast moves out, akwardly dragging its bloated body behind before"
                "likewise you make your way back following the path you once took to get here"
                "the creature still remains in the forest eternal, well hidden out of sight and becomes some sort of an urban legend"  #trust No.1 ending

            elif trust <2:
                "the door begains to creak open, its jittering as it struggles to open for the first time in many years"
                "you peak outside to see a an open field"
                "before you can turn around the beast lunges at jaw open taking sinking its jaws into your guts"
                "a sudden shock of cold spreads aross the wound, radiating to your legs and chest, you collapse to the floor soo after"
                "laying on the cold floor you bleed out, everything goes dark and you die" #beast slayed ending (betrayl)


        "ready your weapon (slighly changes depending on if you got the weapon or not)": #maybe an if statment here with a varriable to grab the better weaon or not
            "not convinced by the space you were give you pull out your weapon as a security messure and the beast backs off even more cornered to the wall"
            "upon opening the door the creature rushing to the door squeezing itself between the now opened crack"
            "{b} you are given another option here fire at it or let it be {/b}"
            menu:

                "fire":
                    if weapon =="silver rifle":
                        "you steady your aim, the rifle lets out a metallic ring echoing in the open field,a small silver stake embeds itself in the back of the beasts skull, it collapses"
                        "walking past the corpse you sense a foul smell, that of burning flesh, the metalic stake sizzling against the poor creatures skull"
                        "{b} continue along the field home and thats an ending {/b}" #beast slayed ending (betrayl)

                    if weapon =="standered":
                        "you steady your aim and hold your breath, a plume of smoke errupts from the gun, the buttet striking the creature in its back, it scrambles to escape only to later then collapes to the ground"
                        "after a breif moment of silence you make your back home, it is a long road"
                        "{b}you are followed home and get killed in the woods{/b}" #beast slayed ending (betrayl)


                "let it be":
                    "{b} here the besat leaves you in peace and you too depart your way after it as long disapeared making sure to take the long way back {/b}"
                    "after arriving back you wake up to hear that a nearby village has been ravaged from an unknown creature, making its way to other towns"

    # jump act_04
