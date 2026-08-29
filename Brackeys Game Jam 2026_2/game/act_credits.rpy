


label credit_scene:

    play music sundowner
    scene forest_eyes_withsprite
    show looping_fog zorder 5: #the z order is so the fog appears above everything
        yalign 0.0
            
    show looping_fog_2 zorder 5: 
        yalign 0.0
    with dissolve

    #'call' forces the code to wait for the subroutine to finish before going for the next line. clicks are not allowed
    #'show' triggers and keeps running the code below, that's why the 'pause', so the player can wait OR click to skip
    
    #call screen credits
    show screen credits

    pause scroll_speed

    hide screen credits #at fade_screen
        
    
    scene black with dissolve
    pause 0.5

    $ renpy.full_restart()
