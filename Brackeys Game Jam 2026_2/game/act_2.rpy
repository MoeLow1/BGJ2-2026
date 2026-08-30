label act_02:





    #region Second Act 


    scene scene 8_bed wake up with dissolve # MoeNote: here we could use one of the bedroom scenes, perferrably a more lit version of the act 1 version
    play ambience_bgm hollow_corridor fadein 1 volume 0.2
    
    narrator" You sluggishly awake from your rest, still unsure of where you are"
    "The aching in your body now fully realized, the weight of exhaustion clinging on from yesterday"
    "It isn't long before the faint sound of breathing startle you fully awake"
    pause 0.5
    play music haunted fadein 1.0
    play audio whispers
    play sound heartbeat loop 
    show beast idle:
        xpos -0.01 #offset, so the paw aligns with the BG
    with flashwhite #custom transition
    "The beast lays across the room, motionless its eyes fixed on to you"
    pause 0.2

    menu:
      
        "Pull out the gun":
            show handgun_aim
            play audio gun_reload_trim
            pause 0.8
            play audio zombie_growl
            play sound zombie_growl
            show beast fear:
                xpos -0.02
            "Your arm springs out pointing the barrel towards the head of the beast"
            "It reacts with a mix of fear and frustration hesitantly shifting forward and back, it is familiar with the gun"
            "The beast gaze is now fixed on the gun, you need to make a choice"
            menu:
                    "Fire":
                        hide handgun_aim
                        
                        show handgun_fire
                        play audio void_scream volume 1.5
                        play audio pistol volume 1.5
                        play sound void_scream volume 1
                        show beast shot:
                            xpos -0.01
                        
                        with flash_punch #custom transition, combines a flash with a vpunch
                        
                        "the beast swerves anticipating your shot, the bullet landing in its body"
                        "it lets out a blood curdling screech before rushing towards you"
                        "The beast swerves anticipating your shot, the bullet landing in its body"
                        "It lets out a blood curdling screech before rushing towards you"
                        
                        
                        play audio gun_reload_trim
                        
                        "You rush to line up for another shot"
                        
                        show layer master at weak_vpunch
                        hide beast shot
                        show bitesprite 
                        hide handgun_fire
                        play audio alien_beast volume 1.5
                        show layer master at tint_red
                        play sound alien_beast volume 1
                        with flashred
                        with flashred
                        play audio bite_flesh volume 1.5
                        with vpunch
                        toptext "but the beast reaches you first, its jaws sunk deep into your guts"
                        play sound death
                        show layer master at tint_red
                        toptext "But the beast reaches you first, its jaws sunk deep into your guts"
                        
                        scene black with dissolve
                        "It is not long before you bleed out, and you die"
                        stop sound fadeout 0.5
                        
                        jump game_over

                    "Wait":
                        $ trust-=1
                        stop audio fadeout 0.5
                        "The beast's eyes dart between your hands the door as it awkwardly moves towards the exit, its back pressed against the wall"
                        "Upon reaching the door it rushes out, and you are left alone"
                        stop sound fadeout 0.5
                        hide handgun_aim

                    "Lower the gun":
                        hide handgun_aim
                        # trust uneffected (cancels out)
                        stop audio fadeout 0.5
                        $ trust+=1
                        "it takes a while but the beast calms down, still weary of your hands it slowly moves towards the door before bolting out"
                        stop sound fadeout 0.5
            


        "stay put":
            $ trust+=1
            
            "you steady your breathing and try to calm down"
            "its fur is a pitch black tone and its eyes and mouth emitting a faint light"
            "a crude metal canister is attached to its back, containing what could only be blood"
            "torn tubes dangle from the bottom of the canister with lumps of clotted blood keeping it shut"
            stop sound fadeout 0.5

            "A minute passes and the beast calmly makes its way out off the door"


    scene bedroom_door_out with dissolve
    narrator "Feeling homesick already, you haul yourself of the bed and leave in search for an exit"

    #bedroom door walk out
    "As you are making your way out you notice something odd on the floor"

    # a shot of the floor outside it, a screenshot would do
    scene vermin_floor with dissolve
    "On the ground, vermin lay violently splattered and torn on the ground, they were not there before"
    scene vermin_floor2 with dissolve
    show rat idle
    menu:
            "Inspect it":
                "The dead vermon seems to share a much in common with the beast"
                "Its body lies bloated and swollen, its eyes faintly glowing beneath a dark coat of fur."
                "Yet, unlike the beast, its form appears somewhat more natural. Patches of its body remain untouched, retaining the creature's original appearance."


            "Touch it":
                show rat jaw
                show layer master at weak_vpunch
                "Your hand recoils instinctively, fingers curling as a sharp chill races through them"
                "As you clench your hand in pain you notice the decapitated rat's head being to subtly twitch"
                "its jaws opening and closing in an eerie way, as it struggles to move towards you"

                
    show layer master at weak_vpunch
    play audio doorbash volume 0.8
    pause 0.75
    play audio doorbash volume 0.6
    pause 0.3
    play audio doorbash volume 0.4
    pause 0.75
    play audio doorbash volume 0.2
    "Your train of thought is interrupted by a loud sound of clattering metal, with each crash becoming more and more distant"
    "You feel like it's a good idea to move along"
    scene scene 7_hall way2 with dissolve

    jump act_03
