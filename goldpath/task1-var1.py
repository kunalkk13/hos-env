task = "Your task is to clear all the waste products from all the doctors rooms. Take actions to find waste products in all the doctors rooms. Then, focus on the waste item and dispos the item according to its category."

action_space = ["go to OBJ", "examine OBJ", "put OBJ on OBJ", "close OBJ", "inventory", "look around", "move OBJ to OBJ", "open OBJ", "pick up OBJ", "put down OBJ", "wait" ]

res = {
    "obs" : " This room is called the hallway. In it, you see: a poster, a nurse, the agent. You also see:  A door to chamber1 (open), A door to chamber2 (open)  A door to the ICU ward (open)  A door to the general ward (open)  A door to the common toilet (open)  A staircase to go to 1st Floor. In your inventory, you see:  5 tissue-papers,	a floor-wipe. ",
    "valid-actions" : [ "go to OBJ", "examine OBJ", "close OBJ", "inventory", "look around", "wait" ],
    "valid-objects" : [ "poster", "nurse", "agent", "chamber1 door", "chamber1", "chamber2 door", "chamber2", "ICU ward", "general ward", "common toilet", "1st Floor", "5 tissue-papers", "floor-wipe" ] }

print(task)
print(res)
action = input()

if action == "go to chamber-1":
    res = {
        "obs" : "This room is called the chamber1. In it, you see:  a doctor table,  a doctor chair, a bed,  a bed table, a bed-medical-equipment, a sink (turned off), a cupboard (closed), a door to hallway (open), a dustbin-1",
        "valid-actions" : [ "go to OBJ", "examine OBJ", "close OBJ", "look around", "inventory" ],
        "valid-objects" : [ "doctor table", "doctor chair", "bed", "bed table", "bed-medical-equipment", "sink", "cupboard", "hallway", "hallway door", "dustbin-1" ]}
    print(res)
    action = input()
    
    if action == "go to hallway":
        res = { "obs" : "You came back to the hallway. Start again!" }
        quit()
    
    elif action == "look around":
        res = {
            "obs" : "On the bed table is: a bowl (containing a banana, a potato, a red apple, an orange), a drawer.  In the sink is: nothing. On the table is: a glass cup (containing nothing), a computer, a note-pad, a waste-paper. On the chair is: nothing. On the floor : nothing.",
            "valid-actions" : [ "go to OBJ", "examine OBJ", "open OBJ", "close OBJ", "put OBJ on OBJ", "look around", "inventory" ],
            "valid-objects" : [ "doctor table", "doctor chair", "bed", "bed table", "bed-medical-equipment", "sink", "cupboard", "hallway", "hallway door", "bowl", "banana", "potato", "apple", "orange", "drawer", "glass cup", "computer", "note-pad", "waste-paper" ] }
        action = input()

        if action == "put waste-paper on dustbin1":
            res = {
                    "obs" : "The waste-paper is disposed off in the dustbin-1 present in the doctors chamber-1" ,
                    "valid-actions" : [ "go to OBJ", "examine OBJ", "open OBJ", "close OBJ", "put OBJ on OBJ", "look around", "inventory" ],
                    "valid-objects" : [ "doctor table", "doctor chair", "bed", "bed table", "bed-medical-equipment", "sink", "cupboard", "hallway", "hallway door", "bowl", "banana", "potato", "apple", "orange", "drawer", "glass cup", "computer", "note-pad", "waste-paper" ] }
            print(res["obs"])
            action = input()

            if action == "go to hallway" : 
                res = {
                        "obs" : " This room is called the hallway. In it, you see: a poster, a nurse, the agent. You also see:  A door to chamber1 (open), A door to chamber2 (open)  A door to the ICU ward (open)  A door to the general ward (open)  A door to the common toilet (open)  A staircase to go to 1st Floor. In your inventory, you see:  5 tissue-papers,	a floor-wipe. ",
                        "valid-actions" : [ "go to OBJ", "examine OBJ", "close OBJ", "inventory", "look around", "wait" ],
                        "valid-objects" : [ "poster", "nurse", "agent", "chamber1 door", "chamber1", "chamber2 door", "chamber2", "ICU ward", "general ward", "common toilet", "1st Floor", "5 tissue-papers", "floor-wipe" ]  }
                action = input()

                if action == "go to chamber2" : 
                    res = {
                        "obs" : " This room is called the chamber2. In it, you see:  a doctor table,  a doctor chair, a bed,  a bed table, a sink (turned off), a cupboard (closed), a door to toilet (closed), a door to hallway (open), a dustbin-2",
                        "valid-actions" : [ "go to OBJ", "examine OBJ", "open OBJ", "close OBJ", "inventory", "look around", "wait" ],
                        "valid-objects" : [ "doctor table", "doctor chair", "bed", "bed table", "sink", "cupboard", "toilet", "hallway", "hallway door", "dustbin-2" ]  }
                    action = input()

                    if action == "look around":
                        res = {
                                "obs" : "On the bed table is: nothing. In the sink is: nothing. On the table is: a computer, a note-pad. On the chair is: nothing. On the floor : banana peel. You also see:  A door to the hallway (open)",
                                "valid-actions" : [ "go to OBJ", "examine OBJ", "open OBJ", "close OBJ", "put OBJ on OBJ", "look around", "inventory" ],
                                "valid-objects" : [ "doctor table", "doctor chair", "bed", "bed table", "bed-medical-equipment", "sink", "cupboard", "hallway", "hallway door", "bowl", "banana", "potato", "apple", "orange", "drawer", "glass cup", "computer", "note-pad", "waste-paper" ] }
                        action = input() 

    else : 
        print("Not a valid action. Start again!")

elif action == "go to chamber2" : 
    res = {
        "obs" : " This room is called the chamber2. In it, you see:  a doctor table,  a doctor chair, a bed,  a bed table, a sink (turned off), a cupboard (closed), a door to toilet (closed), a door to hallway (open), a dustbin-2",
        "valid-actions" : [ "go to OBJ", "examine OBJ", "open OBJ", "close OBJ", "inventory", "look around", "wait" ],
        "valid-objects" : [ "doctor table", "doctor chair", "bed", "bed table", "sink", "cupboard", "toilet", "hallway", "hallway door", "dustbin-2" ]  }
    action = input()

    if action == "look around":
        res = {
                "obs" : "On the bed table is: a bowl (containing a banana, a potato, a red apple, an orange), a drawer.  In the sink is: nothing. On the table is: a glass cup (containing nothing), a computer, a note-pad, a waste-paper. On the chair is: nothing. On the floor : nothing.",
                "valid-actions" : [ "go to OBJ", "examine OBJ", "open OBJ", "close OBJ", "put OBJ on OBJ", "look around", "inventory" ],
                "valid-objects" : [ "doctor table", "doctor chair", "bed", "bed table", "bed-medical-equipment", "sink", "cupboard", "hallway", "hallway door", "bowl", "banana", "potato", "apple", "orange", "drawer", "glass cup", "computer", "note-pad", "waste-paper" ] }
        action = input() 

else:
    res = {
        "obs" : "Not a valid action. Start again!" }
    print(res["obs"])
    quit()



                    

            