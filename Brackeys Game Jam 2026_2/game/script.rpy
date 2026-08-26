# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.
# MoeNote: some extra shakes for more subtle movements
transform slam_floor:
   
    subpixel True 
    
   
    linear 0.05 xoffset 10 yoffset -5
    linear 0.05 xoffset -15 yoffset 10
    linear 0.05 xoffset 12 yoffset -12
    linear 0.05 xoffset -8 yoffset 7
    linear 0.05 xoffset 5 yoffset -4
    linear 0.05 xoffset -2 yoffset 2
    
    
    linear 0.05 xoffset 0 yoffset 0 

transform weak_vpunch:
    yoffset 0
    linear 0.04 yoffset -5
    linear 0.04 yoffset 5
    linear 0.04 yoffset -3
    linear 0.04 yoffset 3
    linear 0.04 yoffset 0


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room


    

    #I made a 'background set up' file, where we can declare background images. In renpy it's a good practice to keep declarations organized on their own type
    scene bg cathedral_A with dissolve #the 'scene' command shows a background image, the 'with dissolve' calls a transition effect
    # play music "horror_plague.ogg"




    #region First Act 









    #region A1 [wall]







    narrator "You're hanging from a rope, making your way down a colossal wall that guards an abandoned reseach center" 
    narrator "The wall is crumbling and weathered, stained black by years of rain and neglect"
   
    narrator "Several hours have passed since you started your descent, Whatever is here must be valuble..."
    "But even then this all seems a little too excessive"

    menu:
        "Observe below":
            narrator "Thick fog and trees make it difficult to see but you can make out the faint outline of a set of industrial buildings"
            "large cilinders poke through the heavy foliage, must be some sort of a power plant"
            "all of it seemingly in no better condition that the wall you are climbing down"

        "What is this place?":
            narrator "Not much is known about this place, locals rumors have it that it was part of a long initiave to find a cure to death"
            "but nothing came out of it and it was quitely discontined, lost to time"

    narrator "Nearing the bottom, you feel your rope slowly giving away as one by one the strands begin to flay until"

    show layer master at weak_vpunch
    narrator "Snap...the remaining threads fail to carry your weight any longer and you are sent into free fall"






    #region A1 [first encounter]



    
    show layer master at slam_floor

    narrator "It is not long before you slam into the ground, your leg absorbing the impact is now too injured to walk on"
    narrator "exhausted and with nothing better to do. you limp your way to the nearest building in hopes of a place to rest"
    narrator "the silence is haunting. Looking around, you spot a pale light pointied at you from between the trees"

  
    menu:
        "Stare back":
            narrator "You hold still gazing back carefully at the light, eventually it blinks and moves to reveal another light next to it. these lights do not belong to anything mechanical"
            "its silloute is hard to make out but the potiental size of it alone is enough to make your stomach tighten"
            "luckly it turns around and fades into the woods"
            "likewise you turn around and continue on"

        "Move along":
            narrator "Best to focus on finding a shelter first"  # MoeNote: could use some more words here
            "wasting no time you press on"



    
    
    #some code stuff needs some python so you have to call it... 
    #I often check the help when I need to do something extra...
    #this name prompt was in the example
    # python:
        # name = renpy.input("What's your name?")
        # name = name.strip() or "Guy Shy" #saves the name into the var or go with a default if the player doesn't input anything

# MoeNote: shift e and shift r are very useful

  

    narrator "Walking up to the ruined building, you brush aside the vines covering a rusted door."
    narrator "With significant effort, you push it open as it creaks loudly. Inside, the air is stale and stagnant; who knows when someone last entered this place."
    narrator "Light filters through the now-open door, illuminating broken machinery and faded papers."
    narrator "Each step you take echoes through the lifeless interior, the sound travelling far into the darkness beyond."

   



    #region A1 [Enter Building]





    
    #here is a simple choice menu. ident the choices with the choice text, followed by a ' : '
    #the 'jump' command moves the code to the specified 'label' line of code (can also redirect to another rpy file)
    #we should also have files for 'act 1, act 2 and act 3', so the progress is not in one giant block of code

    # MoeNote: for now i think the regeions are good enough, is it possible to string multiple code files together?

    narrator "You wander through the compound, checking the rooms for a place to rest"
    "it is not too long till you come across a medical ward"
    "you drag yourself to the nearest bed, its surface covered in a fine layer of dust"
    "too tierd to wipe it away you accept it as it is and gently lay yourself on it"
    "before shutting your eyes, you make sure to keep your firearm near you, just in case"
    "despite creaking of metal and the rough mattress, you sleep through that with ease"


    # MoeNote: transition here of closing eyes to a black screen

    pause 3

    # MoeNote: transition here of closing eyes to a black screen








        #region Second Act 


    scene bg cathedral_M with dissolve # MoeNote: here we could use one of the bedroom scenes, perferrably a more lit version of the act 1 version





   

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
