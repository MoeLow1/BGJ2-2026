# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.
# MoeNote: some extra shakes for more subtle movements

label start:
    default trust = 0
    default weapon = "standered"
    
    jump act_01
    
    # when the project is big, Renpy works best if we split the scenes into different files
    # I made an act_1 and act_2 files and we navigate through them through the 'jump / label' statements
    # It's kinda of a weird way not having things processing in parallel though, haha! but for the nature of visual novel, it works...
   

#  ------------------------------------------------------------------
# code below is ignored, since we are going to jump form file to file

    label choice_move_forward: #if first choice, executes this codeE
        scene bg cathedral_B with dissolve
        narrator "The walls are big, but you can see the building behind them"
        show bg cathedral_B at bg_zoom_in_right
        queue sound [step_grass_a,step_grass_b,step_grass_a] volume 1.0
        pause 1.5
        jump first_choice_done
    
    label choice_have_doubts:
        scene bg cathedral_M with dissolve
        narrator "you turn around to the forest"
        narrator "you think it's too late to back down"
        scene bg cathedral_A with dissolve
        narrator "it's now or never!"
        jump choice_move_forward

    label first_choice_done:
    
        scene bg cathedral_C with dissolve

        narrator    "The wall extends through all the area..."
        narrator "It's clear they don't want people going there"
        narrator "At some point, you see an opening between the stones"
        narrator "They tried to block it with a fence, but there is enough room for one person"

        menu:
            "Use the rope you brought to climb":
                show bg cathedral_C at bg_zoom_in
                pause 0.5
                jump choice_climb

    label choice_climb:

        scene   bg cathedral_D with dissolve

        #I forgot you can call the narrator character without the tag, just text inside a quote
        "As you go down, the rope breaks in the middle"
        play sound fall_grass volume 4.0
        with vpunch #vertical camera shake
        pause 1.0
        "The loud thud of your fall echoed through the forest"
        "Maybe someone heard it... \n{p} or something..." # \n breakes the line and {p} forces a 'wait for click' command
        "\" I shouldn't be here\", you think to yourself" #the \' is to acually use quotes on the dialoge
        "You brush any weird thoughts aside and rush to get back on your feet."
        pause 1.0
        play sound simple_pain
        "But then the pain comes"
        "\"A sprayed ankle, nice!...\""
        play sound sigh_a
        "It's getting late and you can't even try to climb back."
        "You decide your best option is to get shelter in the building"
        "it's your ONLY option, it seems."
        show bg cathedral_D at bg_zoom_in
        queue sound [step_grass_a,step_grass_b,step_grass_a] volume 3.0
        pause 1.5
        

    scene bg cathedral_E with dissolve
    "The fog is thicker as you go." 
    "You feel a cold sensation running through your spine"
    "You climb the broken old stairs"
    "Your confidence starts to waver at each unsteady step"
    "The trust on the tip you got to come here now sounds like a scam..."
    show bg cathedral_E at bg_zoom_in


    scene bg cathedral_F with dissolve

    "There is something eerie with this place."
    "You feel watched..."
    "The wind blows hard and you feel a goosebump."
    stop music fadeout 1
    
    "It gave you a chill down the spine, but then,..." #{p}\n you freeze.."

    play music "behind_heaven.ogg"
    play audio gasp volume 5.0 #I'm using the audio channel so it can play multiple sounds at the same time here
    play sound heartbeat_loud loop
    #play ambience_bgm heartbeat_loud loop
    
    #with vpunch
    $ renpy.transition(vpunch) #I'm not using "with vpunch" here because it hides the dialogue box, so I'm calling the python directly
    play audio breath_b volume 2.0
    "...you freeze!"
    
    
    
    pause 1.5

    "You feel something sharp and cold sliding down your back!"
    
    pause 1

    menu:
            "Stay still":
                jump choice_stay_still
            
            "Run inside":
                jump choice_run_inside
            
            "Turn back to see":
                jump choice_turn_your_back

    label choice_stay_still:
    
        "There is just not mental energy to move"
        "You stay still and close your eyes, certain of your demise..."
        scene black with dissolve
        "The previous cold skin now burns with the adrenaline"
        pause 1.0
        
        stop ambience_bgm fadeout 1.0
        stop audio fadeout 1.0 
        stop sound fadeout 1.0
        stop music fadeout 1.0
        "then nothing..."
        scene bg cathedral_F with dissolve
        jump end_of_monster_scare

    label choice_run_inside:
        
        "Your mind can't process anything else around you"
        "The only possible action is to run inside."
        "You don't even care that it's dark there. It feels safer inside than outside"
        "Limping your way as fast as you can, you stumble on door frame but gets inside."
        "looking back is NOT an option"
        jump end_of_monster_scare
    
    label choice_turn_your_back:

        "And then you see it"
        pause 1.0
        "Something you haven't imagined before!"
        "Your mind is still processing what exactly were you looking at"
        "\"Is it animal? is it alien?\" {p} You didn't have words to describe the...{p}thing... "
        jump end_of_monster_scare

    # This ends the game.

    label end_of_monster_scare:
        "This is just so the game doesn't shut down fast"

    return
