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