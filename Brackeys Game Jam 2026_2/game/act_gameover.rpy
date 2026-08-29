label game_over:
    
    scene black 
    play music arrhythmia fadein 0.3 volume 2
    pause 0.5
    show game_over_title with dissolve
    pause 1.0
    show game_over_title at bg_zoom_in
    pause 1.0
    scene black 
    with Dissolve (0.5)
    pause 1.0
    stop music fadeout 0.4
    pause 0.5

    jump credit_scene 
    
    $ renpy.full_restart()
    
