label wp_act_01:
        

    #I made a 'background set up' file, where we can declare background images. In renpy it's a good practice to keep declarations organized on their own type
    
    #the 'scene' command shows a background image, the 'with dissolve' calls a transition effect
    
    # play music "horror_plague.ogg"

    #region First Act 


    #region A1 [wall]
    

    scene scene 1 wall
    show looping_fog: 
        yalign 0.0
    show looping_fog_2: 
        yalign 0.0
    with dissolve
    play music unsolved fadein 0.5
    play ambience_bgm night_loop fadein 0.5
    queue sound [rope, rope, rope,]
    narrator "Hanging from a rope, making your way down a colossal wall, you think to yourself:"
    "\"What I'm doing here?!!\""
    "You were always told that the walls you saw from outside guards an abandoned reseach center." 
    queue sound [rope, rope, rope,]
    "You took a chance, and prepared to climb. \nIt wasn't an easy ride up..."
    "Now, on your way down, your hands are sweaty and bruised."
    narrator "The wall is crumbling and weathered, stained black by years of rain and neglect..."
    queue sound [rope, rope, rope,]
    narrator "Several hours have passed since you started your journey" 
    "\"Whatever is here must be valuble...\nBut even then this all seems a little too excessive\""
    

    menu:
        "Observe below":
            scene bg research_b 
            show looping_fog: 
                yalign 0.5
            show looping_fog_2 
            with dissolve
            narrator "Thick fog and trees make it difficult to see but you can make out the faint outline of a set of industrial buildings"
            "Large cilinders poke through the heavy foliage." 
            "\"It must be some sort of a power plant\""
            "All of it seemingly in no better condition that the wall you are climbing down"
            

        "What is this place?":
            narrator "Not much is known about this place...\nLocal rumors have it that it was part of a long initiave to find a cure to death..."
            "But nothing came out of it and it was quitely discontined, \nlost to time..."

    scene scene 1 wall 
    show looping_fog: 
        yalign 0.0
    show looping_fog_2: 
        yalign 0.0
    with dissolve
    queue sound [rope, rope, rope,]
    narrator "Nearing the bottom, you feel your rope slowly giving away as one by one the strands begin to flay until..."

    show layer master at weak_vpunch
    play audio gasp volume 2
    play sound snap
    with flashwhite
    narrator "Snap!!!"
    "The remaining threads fail to carry your weight any longer, and you are sent into free fall!"
    play sound fall_scream
    show layer master      at bg_zoom_in_more
    pause 1.0
    stop sound fadeout 2.0
    
    show black with dissolve
    pause 1




    #region A1 [first encounter]



    
    

    scene scene 2 ground 
    
    show looping_fog: 
        yalign 0.0
    show looping_fog_2: 
        yalign 0.0
    with dissolve
    
    play sound fall_grass volume 4.0
    play audio simple_pain
    show layer master at slam_floor
    with flashwhite
    narrator "Not long before you slam into the ground, you start to feel pain..." 
    "Your leg absorbed most of the impact is now too injured to walk straight."
    narrator "Exhausted from the day long journey and with nothing better to do, you limp your way to the nearest building in the hopes to find a place to rest for the upcoming night"

    show layer master at bg_zoom_in_right
    queue sound [step_grass_a,step_grass_b,step_grass_a] volume 3.0
    pause 1.5

    #scene scene 3 with dissolve 
    scene forest_eyes_bg with dissolve
    show looping_fog zorder 5: #the z order is so the fog appears above everything
        yalign 0.0
        
    show looping_fog_2 zorder 5: 
        yalign 0.0
        
    narrator "The silence is haunting..." 
    show forest_eyes_one_eye with dissolve #I figured it's best to keep in the scene and just show the sprite on top of the bg, this way the fog keeps playing

    "Looking around, you suddenly spot a pale light pointed at you from between the trees!!"

  
    menu:
        "Stare back":
          

            narrator "You hold still, gazing back carefully at the light."
            show forest_eyes_withsprite with dissolve
            play sound heartbeat
            "Eventually it blinks and moves to reveal another light next to it. \nThese lights do not seem belong to anything mechanical"
            "its silloute is hard to make out, but the potential size of it alone is enough to make your stomach tighten!"

            hide forest_eyes_withsprite
            hide forest_eyes_one_eye
            with dissolve
            stop sound fadeout 0.5

            "Luckly it turns around and fades into the fog of the woods"
            "Likewise you turn around and continue on... \n{p}You feel a drop of cold sweat running down your face."
            queue sound [step_grass_a,step_grass_b,step_grass_a] volume 1.0
            pause 1.5

        "Move along":

            narrator "\"Best to focus on finding a shelter first!!\""  # MoeNote: could use some more words here
            "Wasting no time you press on"
            queue sound [step_grass_a,step_grass_b,step_grass_a] volume 1.0
            pause 1.5



    
    
    #some code stuff needs some python so you have to call it... 
    #I often check the help when I need to do something extra...
    #this name prompt was in the example
    # python:
        # name = renpy.input("What's your name?")
        # name = name.strip() or "Guy Shy" #saves the name into the var or go with a default if the player doesn't input anything

# MoeNote: shift e and shift r are very useful

  

    
    scene scene 4 rusted door 
    show looping_fog 
    show looping_fog_2 
    with dissolve

    narrator "Walking up to one of the ruined buildings, you brush aside some vines covering a rusted door."
    
    show layer master      at bg_zoom_in


    queue sound [step_grass_a,step_grass_b,step_grass_a] volume 1.0
    pause 1.5
    "With significant effort, you push it open as it creaks loudly."
    play sound effort_a
    scene scene 5 open door with dissolve
    stop ambience_bgm fadeout 0.5
    
    #play ambience_bgm hollow_corridor fadein 0.5 volume 0.5
    narrator  "Inside, the air is stale and stagnant. \n{w}Who knows when someone last entered this place."
    narrator "Light filters through the now-open door, illuminating broken machinery and faded papers."
    narrator "Each step you take echoes through the lifeless interior,\n{w}the sound travelling far into the darkness beyond."

   



    #region A1 [Enter Building]





    
    #here is a simple choice menu. ident the choices with the choice text, followed by a ' : '
    #the 'jump' command moves the code to the specified 'label' line of code (can also redirect to another rpy file)
    #we should also have files for 'act 1, act 2 and act 3', so the progress is not in one giant block of code

    # MoeNote: for now i think the regeions are good enough, is it possible to string multiple code files together?

    scene scene 6_hall way with dissolve
    narrator "You wander through the compound, checking the rooms for a place to rest."
    show layer master at bg_zoom_in
    queue sound [step_grass_a,step_grass_b,step_grass_a] volume 3.0
    pause 1.5

    scene scene 7_hall way2 with dissolve
    "it is not too long till you come across a medical ward"
    "You drag yourself to the nearest bed. \n{w}Its surface covered in a fine layer of dust"
    play sound making_bed
    "Too tierd to wipe it away, you accept it as it is and gently lay yourself on it..."
    
    play audio gun_reload_trim
    "Before shutting your eyes, you make sure to keep your firearm near you, just in case"
    
    "Despite the creaking metal and the rough mattress, you shut your eyes...\n{w}and rest"


    # MoeNote: transition here of closing eyes to a black screen
    scene black with dissolve
    pause 3
    stop music fadeout 1.0

    # MoeNote: transition here of closing eyes to a black screen





    jump wp_act_02
    # jump to the next chapter






