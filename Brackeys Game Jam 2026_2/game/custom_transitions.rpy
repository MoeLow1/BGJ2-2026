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

