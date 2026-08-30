effectlabel act_01:
        

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
   
    narrator "You're hanging from a rope, making your way down a colossal wall that guards an abandoned research center" 
   
    narrator "The wall is crumbling and weathered, stained black by years of rain and neglect"
    
   
    narrator "Several hours have passed since you started your descent, Whatever is here must be valuable..."
    "But even then this all seems a little too excessive"

    menu:
        "Observe below":
            scene bg research_b 
            show looping_fog: 
                yalign 0.5
            show looping_fog_2 
            with dissolve
            narrator "Thick fog and trees make it difficult to see but you can make out the faint outline of a set of industrial buildings"
            "large cylinders poke through the heavy foliage, must be some sort of a power plant"
            "all of it seemingly in no better condition than the wall you are climbing down"
            

        "What is this place?":
            narrator "Not much is known about this place, locals rumors have it that it was part of a long initiative to find a cure to death"
            "but nothing came out of it and it was quitely discontinued, lost to time"

    scene scene 1 wall 
    show looping_fog: 
        yalign 0.0
    show looping_fog_2: 
        yalign 0.0
    with dissolve
    queue sound [rope]

    narrator "Nearing the bottom, you feel your rope slowly giving away as one by one the strands begin to fray until"

    show layer master at weak_vpunch
    play audio gasp volume 2
    play sound snap
    narrator "Snap...the remaining threads fail to carry your weight any longer and you are sent into free fall"
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
    narrator "It is not long before you slam into the ground, your leg absorbing the impact is now too injured to walk on"
    narrator "exhausted and with nothing better to do. you limp your way to the nearest building in hopes of a place to rest"

    show layer master at bg_zoom_in_right
    queue sound [step_grass_a,step_grass_b,step_grass_a] volume 3.0
    pause 1.5

    #scene scene 3 with dissolve 
    scene forest_eyes_bg with dissolve
    show looping_fog zorder 5: #the z order is so the fog appears above everything
        yalign 0.0
        
    show looping_fog_2 zorder 5: 
        yalign 0.0
        
    narrator "the silence is haunting." 
    show forest_eyes_one_eye with dissolve #I figured it's best to keep in the scene and just show the sprite on top of the bg, this way the fog keeps playing

    "Looking around, you spot a pale light pointed at you from between the trees"

  
    menu:
        "Stare back":
            show forest_eyes_withsprite with dissolve
            play sound heartbeat

            narrator "You hold still gazing back carefully at the light, eventually it blinks and moves to reveal another light next to it. these lights do not belong to anything mechanical"
            "its silhouette is hard to make out but the potential size of it alone is enough to make your stomach tighten"

            hide forest_eyes_withsprite
            hide forest_eyes_one_eye
            with dissolve
            stop sound fadeout 0.5

            "luckily it turns around and fades into the woods"
            "likewise you turn around and continue on"
            queue sound [step_grass_a,step_grass_b,step_grass_a] volume 1.0
            pause 1.5

        "Move along":

            narrator "Best to focus on finding a shelter first"  # MoeNote: could use some more words here
            "wasting no time you press on"
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

    narrator "Walking up to the ruined building, you brush aside the vines covering a rusted door."
    
    show layer master      at bg_zoom_in


    queue sound [step_grass_a,step_grass_b,step_grass_a] volume 1.0
    pause 1.5
    "With significant effort, you push it open as it creaks loudly."
    play sound effort_a
    play sound effort_a volume 0.4
    scene scene 5 open door with dissolve
    stop ambience_bgm fadeout 0.5
    
    #play ambience_bgm hollow_corridor fadein 0.5 volume 0.5
    narrator  "Inside, the air is stale and stagnant; who knows when someone last entered this place."
    narrator "Light filters through the now-open door, illuminating broken machinery and faded papers."
    narrator "Each step you take echoes through the lifeless interior, the sound travelling far into the darkness beyond."

   



    #region A1 [Enter Building]





    
    #here is a simple choice menu. ident the choices with the choice text, followed by a ' : '
    #the 'jump' command moves the code to the specified 'label' line of code (can also redirect to another rpy file)
    #we should also have files for 'act 1, act 2 and act 3', so the progress is not in one giant block of code

    # MoeNote: for now i think the regeions are good enough, is it possible to string multiple code files together?

    scene scene 6_hall way with dissolve
    narrator "You wander through the compound, checking the rooms for a place to rest"
    show layer master at bg_zoom_in
    queue sound [step_grass_a,step_grass_b,step_grass_a] volume 3.0
    pause 1.5

   
    scene testing bg with dissolve
    "it is not too long till you come across a medical ward"

    scene beds2 with dissolve
    "you drag yourself to the nearest bed, its surface covered in a fine layer of dust"
    play sound making_bed
    "too tired to wipe it away you accept it as it is and gently lay yourself on it"
    "before shutting your eyes, you make sure to keep your firearm near you, just in case"
    "despite creaking of metal and the rough mattress, you shut your eyes...and rest"


    # MoeNote: transition here of closing eyes to a black screen
    scene black with dissolve
    pause 3
    stop music fadeout 1.0

    # MoeNote: transition here of closing eyes to a black screen





    jump act_02
    # jump to the next chapter






