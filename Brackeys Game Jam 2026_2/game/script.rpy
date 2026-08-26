# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    

    #I made a 'background set up' file, where we can declare background images. In renpy it's a good practice to keep declarations organized on their own type
    scene bg cathedral_A with dissolve #the 'scene' command shows a background image, the 'with dissolve' calls a transition effect

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy #shows a character sprite

    # These display lines of dialogue.

    #e "You've created a new Ren'Py game."
    #e "Once you add a story, pictures, and music, you can release it to the world!"

    narrator "You arrive at the place" #I defined the narrator in the 'character set up' file
    narrator "It's dark and gloomy"
    
    #some code stuff needs some python so you have to call it... 
    #I often check the help when I need to do something extra...
    #this name prompt was in the example
    # python:
        # name = renpy.input("What's your name?")
        # name = name.strip() or "Guy Shy" #saves the name into the var or go with a default if the player doesn't input anything

    # define mc = Character ("[name]") #since we are using a variable to define a character, we let this declaration here

    narrator "Walking up to the ruined building, you brush aside the vines covering a rusted door. "
    narrator "With significant effort, you push it open as it creaks loudly. Inside, the air is stale and stagnant; who knows when someone last entered this place."
    narrator "Light filters through the now-open door, illuminating broken machinery and faded papers."
    narrator "Each step you take echoes through the lifeless interior, the sound travelling far into the darkness beyond."
    
    #here is a simple choice menu. ident the choices with the choice text, followed by a ' : '
    #the 'jump' command moves the code to the specified 'label' line of code (can also redirect to another rpy file)
    #we should also have files for 'act 1, act 2 and act 3', so the progress is not in one giant block of code
    menu:
        "I'm already here, I should go!":
            $ courage_flag = True #turns on a flag switch that we can use later
            jump choice_move_forward
        
        "I'm having doubts...":
            jump choice_have_doubts

    label choice_move_forward: #if first choice, executes this code
        scene bg cathedral_B with dissolve
        narrator "The walls are big, but you can see the building behind them"
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
                jump choice_climb

    label choice_climb:

        scene   bg cathedral_D with dissolve

        #I forgot you can call the narrator character without the tag, just text inside a quote
        "As you go down, the rope breaks in the middle"
        with vpunch #vertical camera shake
        pause 1.0
        "The loud thud of your fall echoed through the forest"
        "Maybe someone heard it... \n{p} or something..." # \n breakes the line and {p} forces a 'wait for click' command
        "\" I shouldn't be here\", you think to yourself" #the \' is to acually use quotes on the dialoge
        "You brush any weird thoughts aside and rush to get back on your feet."
        pause 1.0
        "But then the pain comes"
        "\"A sprayed ankle, nice!...\""
        "It's getting late and you can't even try to climb back."
        "You decide your best option is to get shelter in the building"
        "it's your ONLY option, it seems."
        

    scene bg cathedral_E with dissolve
    "The fog is thicker as you go." 
    "You feel a cold sensation running through your spine"
    "You climb the broken old stairs"
    "Your confidence starts to waver at each unsteady step"
    "The trust on the tip you got to come here now sounds like a scam..."

    scene bg cathedral_F with dissolve

    "There is something eerie with this place."
    "You feel watched..."
    "The wind blows hard and you feel a goosebump."
    "It gave you a chill down the spine, but then,... {p}\n you freeze.."
    "You feel something sharp and cold sliding down your back!"
    with vpunch

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

    return
