label act_03:





    #region Thrid Act 

    scene bg cathedral_M with dissolve 
    narrator "{b}making your way through the hall all the doors apear to be bashed shut a labrynth of a complex reduced to a single path{/b}"
    "{b}leaving you with a narrow path to go through{/b}"
    "{b}you tred through the hallways overgrown by floar walls with faded paint and plants positioned sprouting where cracks of light apear{/b}"
    "{b} two doors apear to be untouched almost as though they were forgotten{/b}"
    menu:
    
        "left door (research room)":
            "{b}give the player more insight via some research papers, talks about the creature and the general perpose{/b}"
            "interrupted by a loud bashing of the other door so close that you can feel the ringing in your ears"
            "more info is given, behavoir, traits etc...mentioning the intelligence of the creature and how it emr"

        "right door (equipment )":
            "{b}gives more insight into the experements that took place, the original containment of the creature and other experments that took place{/b}"
            "interrupted again by a loud bashing of the other door so close that you can feel the ringing in your ears"
            "many broken painful looking tools can be found broken, a broken container hosting some dead testing rodents and looking through the cabins a weapon can be found with a silver bullet"

            menu: 
                "pick up weapon":
                    $ weapon = "silver rifle"

                "leave weapon":
                
                    $ trust+=1



    "{b} the player leaves the room to find the other one shut, with nothing better to do you move on{/b}"
    "{b}at the end of the path you come across another door, locked with a control pad next to it{/b}"
   
    jump act_04
