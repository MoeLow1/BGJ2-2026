label act_02:





    #region Second Act 


    scene scene 8_bed wake up with dissolve # MoeNote: here we could use one of the bedroom scenes, perferrably a more lit version of the act 1 version
    play ambience_bgm hollow_corridor fadein 1 volume 0.2
    
    narrator"you sluggishly awake from your rest, still unsure of where you are"
    "the aching in your body now fully realized, the weight of exhaustion clinging on from yesterday"
    "it isnt long before the faint sound of breathing startles you fully awake"
    pause 0.5
    play music haunted fadein 1.0
    play audio whispers
    play sound heartbeat loop 
    show beast idle:
        xpos -0.01 #offset, so the paw aligns with the BG
    with flashwhite #custom transition
    "the beast lays across the room, motionless its eyes fixed on to you"
    pause 0.2
    menu:
        "pull out the gun":
            play sound zombie_growl
            show beast fear:
                xpos -0.02
            "your arm springs out pointing the barrel towards the head of the beast"
            "it reacts with a mix of fear and frustration hesitantly shifting forward and back, it is familar with the gun"
            "the beast gaze is now fixed on the gun, you need to make a choice"
            menu:
                    "Fire":
                        play sound void_scream volume 1.5
                        play audio pistol volume 1.5
                        show beast shot:
                            xpos -0.01
                        
                        with flash_punch #custom transition, combines a flash with a vpunch
                        
                        "the beast swerves anticipating your shot, the bullet landing in its body"
                        "it lets out a blood curdling screech before rushing towards you"
                        
                        
                        
                        "you rush to line up for another shot"
                        
                        show layer master at weak_vpunch
                        hide beast shot
                        show bitesprite 
                        play sound alien_beast volume 1.5
                        
                        show layer master at tint_red
                        with flashred
                        with flashred
                        play audio bite_flesh volume 1.5
                        with vpunch
                        toptext "but the beast reaches you first, its jaws sunk deep into your guts"
                        play sound death
                        scene black with dissolve
                        "it is not long before you bleed out, and you die"
                        stop sound fadeout 0.5
                        
                        jump game_over

                    "Wait":
                        $ trust-=1
                        "also leaves"
                        stop sound fadeout 0.5

                    "Lower the gun":
                        # trust uneffected (cancels out)
                        "leaves"
                        stop sound fadeout 0.5
            


        "stay put":
            $ trust+=1
            
            "you hold your breath and try to calm down"
            "it's fur is a pitch black tone and it's eyes and mouth emitting a faint light"
            "a bronze canister is attached to its back, cointainting what could only be blood"
            "torn tubes dangle from the bottom of the canister with blotches clotted blood keeping it shut"
            stop sound fadeout 0.5


    narrator "{b}if the player is still alive we continue on with the beast leaving the room{/b}"

    #bedroom door walk out
    scene bedroom_door_out with dissolve
    "{b}the player walks out of the ward{/b}"

    # a shot of the floor outside it, a screenshot would do
    scene vermin_floor with dissolve
    "{b}on the ground lay vermin violently splattered across the ground that were not there before{/b}"
    "{b}continued description of the dead creatures and the similaritioes with the beast{/b}"
    "{b} untill it is intteruptted with a sound of metal being bashed, repeating becoming more distant as it goes on{/b}"

    jump act_03
