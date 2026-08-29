transform bg_zoom_in:
    zoom 1.0 #starting zoom
    xalign 0.5  #pivot point, 0.5 is in the middle (1 = 100%)
    yalign 0.5
    
    ease 2.0 zoom 1.5 xalign 0.5 yalign 0.5 #ease for X seconds the following: makes the zoom 150%, and keep the pivot in the center

transform bg_zoom_in_right:
    zoom 1.0 #starting zoom
    xalign 0.5  #pivot point, 0.5 is in the middle (1 = 100%)
    yalign 0.5
    
    ease 2.0 zoom 1.5 xalign 0.7 yalign 0.5 #ease for X seconds the following: makes the zoom 150%, and pivots slight to the right


transform bg_zoom_in_more:
    zoom 1.0 #starting zoom
    xalign 0.5  #pivot point, 0.5 is in the middle (1 = 100%)
    yalign 0.5
    
    ease 1.5 zoom 3.5 xalign 0.5 yalign 0.5 #ease for X seconds the following: makes the zoom 150%, and keep the pivot in the center


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

define flashwhite = Fade(0.2, 0.0, 0.6, color = 'ffff')

define flash_punch = ComposeTransition (flashwhite, after = vpunch) #combines 2 transitions in this case... we can add a 3rd more with 'before = XXXX'

define flashred = Fade(0.1, 0.0, 0.1, color = "#b41f1f")

transform tint_red:
        matrixcolor TintMatrix("#df4242")

#----------------------------
# ATL for scrolling screen object. In this case, credits roll.
## Speed is the time for object to move up from initial ypos to finish ypos.
define scroll_speed = 30

transform credits_scroll(scroll_speed):
    ypos 720
    linear scroll_speed ypos -720

## Credits screen.

screen credits():
    style_prefix "credits"

    # add "#ad3b3b"

    frame at credits_scroll(scroll_speed):
        background None
        xalign 0.5

        vbox:
            label "Credits"

            null height 20

            hbox:
                text "Game Design"
                text "MoeLow"
            
            null height 20

            hbox:
                text "Story"
                text "MoeLow"

            null height 20

            hbox:
                text "Character art and 2D animation"
                text "MoeLow"
            
            null height 20

            hbox:
                text "Background art/Pixel art/3D art"
                text "Bullstorm"
            
            null height 20

            hbox:
                text "Game Programming"
                text "Bullstorm / MoeLow"
            
            null height 20

            hbox:
                text "Audio"
                text "Bullstorm / MoeLow"

            null height 50
            
            label "Thank you for playing!"

            timer scroll_speed action Return()

style credits_hbox:
    spacing 40
    ysize 30
    xalign 0.5

style credits_label:
    xalign 0.5

style credits_text:
    xalign 0.5

#------------------

# transform fade_screen:
#     on hide:
#         ease 0.0 alpha 1.0