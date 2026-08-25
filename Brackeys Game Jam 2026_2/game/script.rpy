# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


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

    show eileen happy #shows a character sprite

    # These display lines of dialogue.

    #e "You've created a new Ren'Py game."
    #e "Once you add a story, pictures, and music, you can release it to the world!"

    narrator "You arrive at the place" #I defined the narrator in the 'character set up' file
    narrator "It's dark and gloomy"
    
    #some code stuff needs some python so you have to call it... 
    #I often check the help when I need to do something extra...
    #this name prompt was in the example
    python:
        name = renpy.input("What's your name?")
        name = name.strip() or "Guy Shy" #saves the name into the var or go with a default if the player doesn't input anything

    define mc = Character ("[name]") #since we are using a variable to define a character, we let this declaration here
    mc "Today is the day! "
    
    
    narrator "You ponder if you should move forward or go back..."

    
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
    
    # This ends the game.

    return
