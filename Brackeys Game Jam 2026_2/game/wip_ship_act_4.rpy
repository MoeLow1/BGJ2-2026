label wp_act_04:





    #region fourth Act 

    play music out_of_body fadein 1.0

    # side of door next to pannel shot
    "The beast is also there, impatiantly waiting for you to open the door"
    "As you get closer to the control pannel the beast makes room for you as a way to encorage you to open the door..."
    menu:
        "open the door":

            # open door to field shot


            $ trust +=1
            #scene forest_eyes_bg with dissolve
            #show beast idle

            #"depending unless you have shown no hostility prior, the beast will either attack you after the door is open or leave you be in the full trust ending"
            if trust==2:
                narrator"you both sit patiently waiting for the rusted door to finish opening"
                "The beast moves out, akwardly dragging its bloated body"# behind before"
                "likewise you make your way back to the outside world" #following the path you once took to get here"
                #"The creature still remains in the forest eternal, well hidden out of sight"
                "You hesitate for a minute, thinking it would be best to shoot it, but then decide not to..."
                show beast idle at bg_zoom_out
                pause 2
                hide beast idle
                
                "Years to come, it becomes some sort of an urban legend, with many people reporting seeing a dark fur creature around"  #trust No.1 ending
                pause 2
                jump credit_scene

            elif trust <2:
                "The door begains to creak open, its jittering as it struggles to open for the first time in many years"
                "You peak outside to see a an open field"
                hide beast idle
                show bitesprite 
                play audio alien_beast volume 1.5
                show layer master at tint_red
                with flashred
                with flashred
                play audio bite_flesh volume 1.5
                
                with vpunch
                "Before you can turn around, the beast lunges at jaw open taking sinking its jaws into your guts"
                play sound death
                "a sudden shock of cold spreads aross the wound, radiating to your legs and chest"
                "You collapse to the floor soon after"
                hide bitesprite with dissolve
                scene black with dissolve
                stop audio
                stop sound
                "Laying on the cold floor you bleed out, everything goes dark ..." #beast slayed ending (betrayl)
                
                jump game_over


        "ready your weapon": 
            #(slighly changes depending on if you got the weapon or not): #maybe an if statment here with a varriable to grab the better weaon or not
            "Not convinced by the space you were give, you pull out your weapon as a security messure"
            play audio gun_reload_trim
            pause 0.8
            "The beast backs off even more cornered to the wall"
            hide beast idle
            show beast fear
            play audio zombie_growl
            "Upon opening the door, the creature rushes to it, squeezing itself between the now opened crack"
            "You ready your aim"
            #"{b} you are given another option here fire at it or let it be {/b}"
            menu:

                "fire":
                    # open field 
                    # if weapon =="silver rifle":
                    #     "you steady your aim, the rifle lets out a metallic ring echoing in the open field,a small silver stake embeds itself in the back of the beasts skull, it collapses"
                    #     "walking past the corpse you sense a foul smell, that of burning flesh, the metalic stake sizzling against the poor creatures skull"
                    #     "{b} continue along the field home and thats an ending {/b}" #beast slayed ending (betrayl)

                    # if weapon =="standered":
                        "you steady your aim and hold your breath"
                        play audio pistol volume 1.5
                        show beast shot
                        with flash_punch #custom transition, combines a flash with a vpunc
                        "A plume of smoke errupts from the gun, the buttet striking the creature in its back, it scrambles to escape only to later then collapse to the ground"
                        hide beast shot with dissolve
                        play sound breath_a
                        "After a breif moment of silence you make your back home."
                        
                        "It was a long road..."
                        scene black with dissolve
                        "As you walk your way home, tired and limping, but relieved, you stop to stare at the walls one last time."
                        "As you marvel at the adventure you just had, you didn't realize something crawling behind your back..."
                        show bitesprite 
                        play audio alien_beast volume 1.5
                        show layer master at tint_red
                        with flashred
                        with flashred
                        play audio bite_flesh volume 1.5
                        "The creature still had strength to lunge at you!"
                        "You feel deep regret for being hostile to it, as you feel your life wasting away..."
                        jump game_over
                        #"{b}you are followed home and get killed in the woods{/b}" #beast slayed ending (betrayl)



                "let it be":
                    "You hesitate for a minute, but then decide to not shoot it."
                    show beast fear at bg_zoom_out
                    pause 2
                    hide beast fear
                    "The beast vanishes in the free world, leaving you to be..."
                    pause 2
                    #"{b} here the besat leaves you in peace and you too depart your way after it as long disapeared making sure to take the long way back {/b}"
                    "After arriving back, you decide it's best to not tell everyone else about it..."
                    "One day, you wake up to the news that a nearby city has been ravaged by an unknown creature..."
                    "Feeling regret, you just wish it doesn't come to your own town, or at least hope it recognizes you, if it does..."
                    scene black
                    pause 2

                    jump credit_scene

    # jump act_04
