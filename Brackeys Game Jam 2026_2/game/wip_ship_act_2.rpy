label wp_act_02:





    #region Second Act 


    scene scene 8_bed wake up with dissolve # MoeNote: here we could use one of the bedroom scenes, perferrably a more lit version of the act 1 version
    play ambience_bgm hollow_corridor fadein 1 volume 0.2
    
    narrator"You sluggishly awake from your rest, still unsure of where you are"
    "The aching in your body now fully realized, the weight of exhaustion clinging on from yesterday..."
    "It isnt long before the faint sound of breathing startles you fully awake!"
    pause 0.5
    play music haunted fadein 1.0
    play audio whispers
    play sound heartbeat loop 
    show beast idle:
        xpos -0.01 #offset, so the paw aligns with the BG
    with flashwhite #custom transition
    "A beast lays across the room, motionless, its eyes fixed on to you"
    "Your heart beats fast, the adrenaline rushing through your veins..."
    "You can't exactly recognize what is in front of you"
    "\"Is it going to attack me?!\""
    pause 0.2
    menu:
        "pull out the gun":
            play audio gun_reload_trim
            pause 0.8
            play audio zombie_growl
            show beast fear:
                xpos -0.02
            "Your arm springs out pointing the barrel towards the head of the beast"
            "It reacts with a mix of fear and frustration, hesitantly shifting forward and back.\n{w}It is familar with the gun..."
            "The beast's gaze is now fixed on the gun.\n{p}you need to make a choice"
            menu:
                    "Fire":
                        
                        "The beast swerves anticipating your shot, the bullet landing in its body"
                        play audio void_scream volume 1.5
                        play audio pistol volume 1.5
                        show beast shot:
                            xpos -0.01
                        
                        with flash_punch #custom transition, combines a flash with a vpunch
                        
                        
                        "It lets out a blood curdling screech before rushing towards you"
                        
                        
                        play audio gun_reload_trim
                        "You rush to line up for another shot..."
                        
                        show layer master at weak_vpunch
                        hide beast shot
                        show bitesprite 
                        play audio alien_beast volume 1.5
                        
                        show layer master at tint_red
                        with flashred
                        with flashred
                        play audio bite_flesh volume 1.5
                        with vpunch
                        toptext "But the beast reaches you first!\n{w}Its jaws sunk deep into your guts"
                        play sound death
                        scene black with dissolve
                        "It is not long before you bleed out, and starts to lose consciousness"
                        stop sound fadeout 0.5
                        "\"Was I wrong? Was I too hasty?\"{w} \nwere your last thoughts before your mind drifts and fades into darkness..."
                        
                        jump game_over

                    "Wait":
                        $ trust-=1
                        "As you stay still, you can see the creature stiffness fading a bit, while you are trembling in doubt"
                        "It seems to not like the gun pointed at it..."
                        "You are not sure, but feels that the creature is giving you a disappointed look..."
                        "After a few seconds of this stalemate, the creature springs outside the door and vanishes, leaving you there, with your gun still pointed at that direction."
                        #"also leaves"
                        stop audio fadeout 0.5
                        stop sound fadeout 0.5
                        hide beast idle with Dissolve (0.2)
                        pause 2
                        jump survived_1st_meet

                    "Lower the gun":
                        # trust uneffected (cancels out)
                        "You are scared, but the creature seems to be scared too..."
                        "\"If it wanted to attack me, it would have already!\""
                        stop sound fadeout 0.5
                        play audio gun_reload_trim volume 0.5
                        "You slowly lower your gun, while making a 'stop' sign with the other hand"
                        "It feels the creature seems to relax a little bit..."
                        "Suddenly, it sprints out of the room, leaving you there startled"
                        hide beast idle with Dissolve (0.2)
                        pause 2
                        "\"What the hell is going on??!\""
                        #"leaves"
                        stop audio fadeout 0.5
                        jump survived_1st_meet
            


        "stay put":
            $ trust+=1
            
            "You hold your breath and try to calm down, despite the intense fear"
            "You stay still while analyzing what's in front of you..."
            "The creature's fur is of a pitch black tone and it's eyes and mouth emitt a faint light..."
            "A bronze canister is attached to its back, cointainting what could only be blood"
            "Torn tubes dangle from the bottom of the canister with blotches of clotted blood keeping it shut"
            stop sound fadeout 0.5
            "You have a glimpse of how much it must have suffered..."
            pause 1.0
            "After a few seconds, the creature seems to relax a bit"
            "Suddenly, it springs outside, looking at you as if calling you to follow."
            hide beast idle with Dissolve (0.2)
            pause 1
            "\"What a crazy idea!\""
            jump survived_1st_meet

    label survived_1st_meet:

    #narrator "{b}if the player is still alive we continue on with the beast leaving the room{/b}"

    #bedroom door walk out
    scene bedroom_door_out with dissolve
    #"{b}the player walks out of the ward{/b}"
    "You get up from the bed, still feeling the pain and fear."
    "You realize you can't rest until you are out of this place"
    "The rewards don't even matter anymore!"
    "You slowly walk to the door, carefully looking for signs of danger..."

    # a shot of the floor outside it, a screenshot would do
    scene vermin_floor with dissolve
    "You look down, and suddenly see something you didn't expect!"
    "Right there on the floor, lay dozens of giant size vermin, violently splattered"
    "These vermin were not there before you came inside!"
    "As you get closer and poked one with a metal bar, you see that these vermin resembled the beast"
    "The remains of some sort of artificial appendages were attached to them, like those you see on sci-fi movies"
    pause 1.0
    "You then suddenly hear metal sounds across the hallways"
    "You ready yourself, but then you notice that these seem to be door sounds"
    "Someone,... \n{w}...or something...\n{w}is shutting and opening doors on the facility..."
    # "{b}on the ground lay vermin violently splattered across the ground that were not there before{/b}"
    # "{b}continued description of the dead creatures and the similaritioes with the beast{/b}"
    # "{b} untill it is intteruptted with a sound of metal being bashed, repeating becoming more distant as it goes on{/b}"

    jump wp_act_03
