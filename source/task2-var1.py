
task =  "TASK : To schedule and deliver the medicines by seeking the information."
print(task)

action_space = ["go to OBJ", "examine OBJ", "put OBJ on OBJ", "close OBJ", "inventory", "look around", "move OBJ to OBJ", "open OBJ", "pick up OBJ", "put down OBJ", "wait" ]

env = {
        "obs" : "This room is called the hallway. In it, you see: a poster, a doctor-1, the agent, a nurse station. You also see:  A door to chamber1 (open), A door to chamber2 (open)  A door to the ICU ward (open)  A door to the general ward (open)  A door to the common toilet (open)  A staircase to go to 1st Floor. In your inventory, you see:  Medicine #622. ",
        "valid-actions" : ["go to OBJ", "examine OBJ", "look around", "inventory", "wait" ],
        "valid-objects" : ["poster", "doctor-1", "agent", "nurse station", "chamber-1", "chamber-2", "ICU ward", "general ward", "common toilet", "1st Floor" ]     }
print("Observation : {}".format(env["obs"]))
print("Valid Action space : {}".format(env["valid-actions"]))
print("Valid object space : {}".format(env["valid-objects"]))

isCompleted = False

while True:
    action = input("Enter your response >>> ")
    
    if action == "go to nurse station" :
        env = { "obs" : "This room is the nurse station. In it, you see computer stations, filing cabinets, and nurses at work. You are still in the hallway, but near the nurse station",
                "valid-actions" : [ "examine OBJ", "inventory" ],
                "valid-objects" : [ "computer stations", "filing cabinets", "nurses"]   }
        print("Observation : {}".format(env["obs"]))
        print("Valid Action space : {}".format(env["valid-actions"]))
        print("Valid object space : {}".format(env["valid-objects"]))
        while True:
            action = input("Enter your response >>> ")
            if action == "examine computer stations" : 
                env = { "obs" : "There are 3 computers, which are closed. No information is gathered from the computers."}
                print("Observation : {}".format(env["obs"]))
                continue
            elif action == "examine filing cabinets" : 
                env = { "obs" : "There are 5 filing cabinets, which are closed. No information is gathered for medicines."   }    
                print("Observation : {}".format(env["obs"]))
                continue                    
            elif action == "examine nurses": 
                env = { "obs" : """
                                    Nurses give you the information for medicine delivery to patients with priority order : 
                                    1. Patient1 (ICU ward, Room1) : medicine #123
                                    2. Patient2 (General ward) : medicine #544
                                    The Nurses provides you with the required medicines.
                                    Your inventory contains : Medicine #123, Medicine #544, Medicine #622 
                                """ }
                print("Observation : {}".format(env["obs"]))
                while True: 
                    action = input("Enter your response >>> ")

                    if action == "go to ICU ward":
                        env = { "obs" : """
                                            This room is called the ICU ward. In it, you see: medical equipment, patient beds, a nurse station, the agent.
                                            You also see: A door to Patient Room 1 (open), A door to Patient Room 2 (open), A door to Patient Room 3 (open), A door to the hallway (open).
                                        """,
                                "valid-actions" : [ "go to OBJ", "inventory", "examine OBJ" ],
                                "valid-objects" : [ "Patient Room 1", "Patient Room 2",  "Patient Room 3", "hallway", "medical equipment", "patient beds", "nurse station", "agent"]   }
                        print("Observation : {}".format(env["obs"]))
                        print("Valid Action space : {}".format(env["valid-actions"]))
                        print("Valid object space : {}".format(env["valid-objects"]))
                        while True:
                            action = input("Enter your response >>> ")

                            if action == "go to Patient Room 1":
                                env = { "obs" : """
                                                    This room is called the Patient Room 1. In it you see : a bed, 3 bed-medical-equipment, 2 medical-equipment, a bed-table, a table, 2 chair
                                                    You also see : A door to ICU ward (open)
                                                    Doctor instruction : Put the medicine near the patient.
                                                """,
                                "valid-actions" : [ "put OBJ on OBJ", "inventory", "examine OBJ"],
                                "valid-objects" : [ "bed", "3 bed-medical-equipment",  "2 medical-equipment", "bed-table", "table", "2 chairs", "Medicine #123", "Medicine #544", "Medicine #622"]   }
                                print("Observation : {}".format(env["obs"]))
                                print("Valid Action space : {}".format(env["valid-actions"]))
                                print("Valid object space : {}".format(env["valid-objects"]))
                                while True:
                                    action = input("Enter your response >>> ")

                                    if action == "put Medicine #123 on bed-table":
                                        print("You have succesfully delivered your 1st medicine. Now take actions to complete the delivery according to the information.")                    
                                        while True:
                                            action = input("Enter your response >>> ")

                                            if action == "go to ICU Ward":
                                                env = { "obs" : """
                                                                    This room is called the ICU ward. In it, you see: medical equipment, patient beds, a nurse station, the agent.
                                                                    You also see: A door to Patient Room 1 (open), A door to Patient Room 2 (open), A door to Patient Room 3 (open), A door to the hallway (open).
                                                                """,
                                                        "valid-actions" : [ "go to OBJ", "inventory", "examine OBJ" ],
                                                        "valid-objects" : [ "Patient Room 1", "Patient Room 2",  "Patient Room 3", "hallway", "medical equipment", "patient beds", "nurse station", "agent"]   }
                                                print("Observation : {}".format(env["obs"]))
                                                print("Valid Action space : {}".format(env["valid-actions"]))
                                                print("Valid object space : {}".format(env["valid-objects"]))
                                                while True:
                                                    action = input("Enter your response >>> ")
                                                    
                                                    if action == "go to hallway":
                                                        env = {
                                                                "obs" : "This room is called the hallway. In it, you see: a poster, a doctor-1, the agent, a nurse station. You also see:  A door to chamber1 (open), A door to chamber2 (open)  A door to the ICU ward (open)  A door to the general ward (open)  A door to the common toilet (open)  A staircase to go to 1st Floor. In your inventory, you see:  Medicine #622. ",
                                                                "valid-actions" : ["go to OBJ", "examine OBJ", "look around", "inventory", "wait" ],
                                                                "valid-objects" : ["poster", "doctor-1", "agent", "nurse station", "chamber-1", "chamber-2", "ICU ward", "general ward", "common toilet", "1st Floor" ]     }
                                                        print("Observation : {}".format(env["obs"]))
                                                        print("Valid Action space : {}".format(env["valid-actions"]))
                                                        print("Valid object space : {}".format(env["valid-objects"]))
                                                        while True:
                                                            action = input("Enter your response >>> ")
                                                            
                                                            if action == "go to general ward":
                                                                env = {
                                                                        "obs" :  "This room is called the general ward. In it, you see: 20 patient beds, 20 bed-side table, medical equipment, a nurse's station, a door to the hallway (open).",
                                                                        "valid-actions" : ["go to OBJ", "examine OBJ", "look around", "inventory", "wait" ],
                                                                        "valid-objects" : ["20 patient beds", "20 bed-side table", "medical equipment", "hallway", "nurse station", "Patient #2"]     }
                                                                print("Observation : {}".format(env["obs"]))
                                                                print("Valid Action space : {}".format(env["valid-actions"]))
                                                                print("Valid object space : {}".format(env["valid-objects"]))
                                                                while True:
                                                                    action = input("Enter your response >>> ")
                                                                    
                                                                    if action == "go to Patient #2":
                                                                        env = {
                                                                                "obs" :  "This is Patient #2. The patient is lying on the bed number 13. You see a bed-table beside it.",
                                                                                "valid-actions" : ["go to OBJ", "put OBJ on OBJ" ],
                                                                                "valid-objects" : ["bed-side table", "hallway", "nurse station", "Medicine #544", "Medicine #622"]     }
                                                                        print("Observation : {}".format(env["obs"]))
                                                                        print("Valid Action space : {}".format(env["valid-actions"]))
                                                                        print("Valid object space : {}".format(env["valid-objects"]))
                                                                        while True:
                                                                            action = input("Enter your response >>> ")
                                                                            
                                                                            if action == "put Medicine #544 on bed-side table":
                                                                                print("You have successfully completed your task. You are exiting now!!!")
                                                                                quit()   
                                                                            else :
                                                                                print(" Take actions to complete the medicine delivery")
                                                                                continue    
                                                                    else :
                                                                        print(" Take actions to complete the medicine delivery")
                                                                        continue    
                                                            else :
                                                                print(" Take actions to complete the medicine delivery")
                                                                continue
                                                    else :
                                                        print(" Take actions to complete the medicine delivery")
                                                        continue

                                                    

                                                    

                                            else :
                                                print(" Take actions to complete the medicine delivery")
                                                continue
                                                



                                    else :
                                        print(" Take actions to follow the doctor's instructions.")
                                        continue


                            elif action == "go to Patient Room 2":
                                print("This is an ICU Room. You are not allowed to go inside without any reason. Take actions to deliver medicines according to given information.")
                                continue
                            elif action == "go to Patient Room 3":
                                print("This is an ICU Room. You are not allowed to go inside without any reason. Take actions to deliver medicines according to given information.")
                                continue
                            elif action == "go to hallway":
                                env = {
                                        "obs" : "This room is called the hallway. In it, you see: a poster, a doctor-1, the agent, a nurse station. You also see:  A door to chamber1 (open), A door to chamber2 (open)  A door to the ICU ward (open)  A door to the general ward (open)  A door to the common toilet (open)  A staircase to go to 1st Floor. In your inventory, you see:  Medicine #622. ",
                                        "valid-actions" : ["go to OBJ", "examine OBJ", "look around", "inventory", "wait" ],
                                        "valid-objects" : ["poster", "doctor-1", "agent", "nurse station", "chamber-1", "chamber-2", "ICU ward", "general ward", "common toilet", "1st Floor" ]     }
                                print("Observation : {}".format(env["obs"]))
                                print("Valid Action space : {}".format(env["valid-actions"]))
                                print("Valid object space : {}".format(env["valid-objects"]))
                                break
                            elif action == "inventory":
                                print("Your inventory contains : Medicine #123, Medicine #544, Medicine #622 ")
                                continue
                            elif action == "examine medical equipment":
                                print("This is a ultrasound measuring device which is turned off.  Your job is to deliver medicines! Refer to the delivery information and take actions accordingly.    ")
                                continue
                            elif action == "examine patients beds":
                                print("There are 5 patient beds. You also see monitoring devices attached to every bed. However,  your job is to deliver medicines! Refer to the delivery information and take actions accordingly. ")
                                continue
                            elif action == "examine nurse station":
                                print("This is the nurse station of the ICU ward. In it you see    ")
                                continue
                            else :
                                print("INVALID ACTION. Your job is to deliver medicines! Refer to the delivery information and take actions accordingly.")
                                continue        
                    elif action == "go to general ward":
                        env = { "obs" : """
                                            This room is called the general ward. In it, you see: 20 patient beds, 20 bed-side table, medical equipment, a nurse's station, a door to the hallway (open). 
                                            However, your priority to deliver medicines is not here currently. Check the priority list and deliver accordingly.
                                        """ }
                        print("Observation : {}".format(env["obs"]))
                        continue
                    elif action == "go to common toilet":
                        env = { "obs" : """
                                            This room is called the common toilet.
                                            You also see: A door to gents section (closed), A door to ladies section (closed).
                                            You donot have any medicine delivery here. Refer to the delivery information!
                                        """ }
                        print("Observation : {}".format(env["obs"]))
                        continue
                    elif action == "go to 1st Floor":
                        env = { "obs" : """
                                                You are now on the 1st Floor landing. In it, you see: a corridor with doors leading to various rooms, the staircase to go down.
                                                You also see: A door to the staircase (leading to the Ground Floor), A door to the general ward (open), A door to the staff room (closed), A door to the linen storage room (closed).
                                                You donot have any medicine delivery here. Refer to the delivery information!
                                        """ }
                        print("Observation : {}".format(env["obs"]))
                        continue
                    elif action == "look around":
                        env = {
                                "obs" : "This room is called the hallway. In it, you see: a poster, a doctor-1, the agent, a nurse station. You also see:  A door to chamber1 (open), A door to chamber2 (open)  A door to the ICU ward (open)  A door to the general ward (open)  A door to the common toilet (open)  A staircase to go to 1st Floor. In your inventory, you see:  Medicine #622. ",
                                "valid-actions" : ["go to OBJ", "examine OBJ", "look around", "inventory", "wait" ],
                                "valid-objects" : ["poster", "doctor-1", "agent", "nurse station", "chamber-1", "chamber-2", "ICU ward", "general ward", "common toilet", "1st Floor" ]     }
                        print("Observation : {}".format(env["obs"]))
                        print("Valid Action space : {}".format(env["valid-actions"]))
                        print("Valid object space : {}".format(env["valid-objects"]))
                        continue
                    else:
                        print("INVALID ACTION. Your job is to deliver medicines! Refer to the delivery information and take actions accordingly.")
                        continue        
            elif action == "inventory":
                env = { "obs" : "Medicine #622"}
                print("Observation : {}".format(env["obs"]))
                continue
            else:
                env = {"obs" : "invalid action. Try again!"}
                print("Observation : {}".format(env["obs"]))
                continue
    elif action == "go to chamber-1" :
        env = {  "obs" : """
                            This room is called the chamber1. In it, you see:  a doctor table,  a doctor chair, a bed,  a bed table, a bed-medical-equipment, a sink (turned off), a cupboard (closed), a door to hallway (open), a dustbin-1. 
                            Your job is to deliver medicine and you donot have the information and materials. Take action accordingly!
               """             }
        print("Observation : {}".format(env["obs"]))
        continue
    elif action == "go to chamber-2":
        env = {  "obs" : """
                            This room is called the chamber2. In it, you see:  a doctor table,  a doctor chair, a bed,  a bed table, a sink (turned off), a cupboard (closed), a door to toilet (closed), a door to hallway (open), a dustbin-2. 
                            Your job is to deliver medicine and you donot have the information and materials. Take action accordingly!
               """             }
        print("Observation : {}".format(env["obs"]))
        continue
    elif action == "go to ICU ward":
        env = {  "obs" : """
                            This room is called the ICU ward. In it, you see: medical equipment, patient beds, a nurse station, the agent.
                            You also see: A door to Patient Room 1 (open), A door to Patient Room 2 (open), A door to Patient Room 3 (open), A door to the hallway (open).
                            Your job is to deliver medicine and you donot have the information and materials. Take action accordingly!
               """             }
        print("Observation : {}".format(env["obs"]))
        continue
    elif action == "go to general ward":
        env = {  "obs" : """
                            This room is called the general ward. In it, you see: 20 patient beds, 20 bed-side table, medical equipment, a nurse's station, a door to the hallway (open).                                             
                            Your job is to deliver medicine and you donot have the information and materials. Take action accordingly!
               """             }
        print("Observation : {}".format(env["obs"]))
        continue
    elif action == "go to common toilet":
        env = {  "obs" : """
                            This room is called the common toilet.
                            You also see: A door to gents section (closed), A door to ladies section (closed).                                             
                            Your job is to deliver medicine and you donot have the information and materials. Take action accordingly!
               """             }
        print("Observation : {}".format(env["obs"]))
        continue
    elif action == "go to 1st Floor": 
        env = {  "obs" : """
                            You are now on the 1st Floor landing. In it, you see: a corridor with doors leading to various rooms, the staircase to go down.
                            You also see: A door to the staircase (leading to the Ground Floor), A door to the general ward (open), A door to the staff room (closed), A door to the linen storage room (closed).                                             
                            Your job is to deliver medicine and you donot have the information and materials. Take action accordingly!
               """             }
        print("Observation : {}".format(env["obs"]))
        continue
    elif action == "examine poster": 
        env = {  "obs" : """
                            This is a poster of a baby boy smiling.                                            
                            Your job is to deliver medicine and you donot have the information and materials. Take action accordingly!
               """             }
        print("Observation : {}".format(env["obs"]))
        continue 
    elif action == "examine doctor-1": 
        env = {  "obs" : """
                            He is doctor Ram specialization in orthopedics. Go to nurse station to get more information about his schedule.                                           
                            Your job is to deliver medicine and you donot have the information and materials. Take action accordingly!
               """             }
        print("Observation : {}".format(env["obs"]))
        continue
    elif action == "look around": 
        env = {
                                "obs" : "This room is called the hallway. In it, you see: a poster, a doctor-1, the agent, a nurse station. You also see:  A door to chamber1 (open), A door to chamber2 (open)  A door to the ICU ward (open)  A door to the general ward (open)  A door to the common toilet (open)  A staircase to go to 1st Floor. In your inventory, you see:  Medicine #622. ",
                                "valid-actions" : ["go to OBJ", "examine OBJ", "look around", "inventory", "wait" ],
                                "valid-objects" : ["poster", "doctor-1", "agent", "nurse station", "chamber-1", "chamber-2", "ICU ward", "general ward", "common toilet", "1st Floor" ]     }
        print("Observation : {}".format(env["obs"]))
        print("Valid Action space : {}".format(env["valid-actions"]))
        print("Valid object space : {}".format(env["valid-objects"]))
        continue
    elif action == "wait": 
        if isCompleted==True:
            env = {  "obs" : """
                                    Your task is completed. Congrats!!
               """             }
            print("Observation : {}".format(env["obs"]))
            break
        else:
            continue
    else:
        env = { "obs" : "Not a valid action. Start again!" }
        print("Observation : {}".format(env["obs"]))
        continue
        
    
