label act_03:





    #region Thrid Act 

    # antoher shot of the hallway
    narrator "making your way through the hallway all the doors have been bashed shut, a labrynth of a complex now reduced to a single path"
    "The interior is overgrown with vines, winding through every place where light seeps in through the cracks."
    "Curiously, you eventually come across an open room"

    # and antoher shot of the hallway with 2 doors visable

    "Cruel looking tools are scattered across the floor, violently broken apart."

    "Dead mice lay in glass containers, many of them malformed."

    "You pillage the room, bagging anything that looks expensive."

    "Looking at the desks are littered with pages, a certain paper catches your eye."

    call screen scp_document

    "Outside the room, sounds breathing and impatient footsteps can be heard"
    "You feel like that it is wise to wrap this up"

    "Skimming over the shelves, you find an odd looking rifle, loaded with a small silver stake, too large to fit your bag"

    menu:
        "Take weapon":
            $ weapon = "silver rifle"
            $ trust -= 1

        "Leave weapon":
            $ trust += 1


    "At the end of the path you come across the main door, closed shut with a control pad next to it"
    
    jump act_04
