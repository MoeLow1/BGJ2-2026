label wp_act_03:


    stop sound
    stop audio
    "You come to the conclusion that the creature killed these vermins for your sake!"
    "\"Is it on my side?!...\""
    "As you walk through the facility, you didn't realize how much of a maze it is"
    scene scene 6_hall way with dissolve
    "You are suddenly lost, but then you notice that some doors are open and some are shut.."
    "The creature might be making a path for me!"
    "You decide to trust your gut and follow it..."


    scene forest_eyes_bg 
    show looping_fog zorder 5: #the z order is so the fog appears above everything
        yalign 0.0
        
    show looping_fog_2 zorder 5: 
        yalign 0.0
    with dissolve
    "You both get outside the building, you relieved that you are not lost in the maze."
    "You slowly follow the creature behind it, it walks as if guiding you somewhere"
    "You hesitate, but follow the dark fur being"

    scene black with dissolve
    "At the end of the path you come across a big gate, located at the giant walls, locked with a control pad next to it"
    
    
    show beast idle with dissolve
    
    jump wp_act_04
    
    
    
    #--------------------------------
    #       Original plan 👇
    #--------------------------------

    #region Thrid Act 

    # antoher shot of the hallway
    narrator "{b}making your way through the hall all the doors apear to be bashed shut a labrynth of a complex reduced to a single path{/b}"
    "{b}leaving you with a narrow path to go through{/b}"
    "{b}you tred through the hallways overgrown by floar walls with faded paint and plants positioned sprouting where cracks of light apear{/b}"
    "{b} two doors apear to be untouched almost as though they were forgotten{/b}"

    # and antoher shot of the hallway with 2 doors visable
    menu:
    
        "left door (research room)":
            #a room with desks and papers of some sort
            "{b}give the player more insight via some research papers, talks about the creature and the general perpose{/b}"
            "interrupted by a loud bashing of the other door so close that you can feel the ringing in your ears"
            "more info is given, behavoir, traits etc...mentioning the intelligence of the creature and how it emr"

        "right door (equipment )":
            #a room with more tools or equipment laying around cathederal miiiiiight work here
            "{b}gives more insight into the experements that took place, the original containment of the creature and other experments that took place{/b}"
            "interrupted again by a loud bashing of the other door so close that you can feel the ringing in your ears"
            "many broken painful looking tools can be found broken, a broken container hosting some dead testing rodents and looking through the cabins a weapon can be found with a silver bullet"

            menu: 
                "pick up weapon":
                    $ weapon = "silver rifle"

                "leave weapon":
                
                    $ trust+=1


    #hall way out
    "{b} the player leaves the room to find the other one shut, with nothing better to do you move on{/b}"


    #a heavy door perferably with a control pannel near it
    "{b}at the end of the path you come across another door, locked with a control pad next to it{/b}"
   
    jump wp_act_04
