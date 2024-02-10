### LIBRARY ###
import random
import json

### TASK Description ###
task =  "TASK : to clear all the waste products from all the doctors’ rooms. Take actions to find waste products in all the rooms. Next, focus on the waste item and collect the item according to its category."

### Create Action Space ###
def ActSpace(la,lo):
    act_space = []
    for act in la:
        for obj in lo:
            act_space.append(act + " " + obj)
    return act_space

### OBJECTS ###
inventory = {  "objects" : ["tissue-papers", "floor-wipe"],
               "waste" : []     }
dustbin1 = []
dustbin2 = ["food", "tissues"]
doctor_table1 = ["glass cup (empty)", "computer", "note-pad", "waste-paper"]
doctor_table2 = ["computer", "note-pad"]
toilet_door = "closed"

### Create a new JSON and append to it ###
file1 = 'task1_var1_play20.txt'
ini = {
        "obs" : "This room is called the hallway. In it, you see: a poster, a doctor, the agent, a nurse station. You also see:  A door to chamber1, A door to chamber2, A door to the ICU ward, A door to the general ward, A door to the common toilet, A staircase to go to 1st Floor. In your inventory, you see:  {}".format(inventory),
        "valid-actions" : ["go to", "examine"],
        "valid-objects" : ["poster", "doctor-1", "agent", "nurse station", "chamber-1", "chamber-2", "ICU ward", "general ward", "common toilet", "1st Floor" ]     }
act_space = ActSpace(ini["valid-actions"],ini["valid-objects"]) + ["inventory"]
d1 = { "ACTION" : "initialize",
      "OBSERVATION" : ini["obs"],
      "#Actions Used" : 0}
with open(file1, 'w') as file:
    file.write(json.dumps(d1) + '\n')

def appJSON(a,o,n):
    d2 = {   "ACTION" : a, 
             "OBSERVATION" : o,
            "#Actions Used" : n  }
    with open(file1, 'a') as file:
        file.write(json.dumps(d2) + '\n')

### Control Variables ###
collect = 0
num_act = 0

### Start Exploring ###
while num_act<50:
    
    act_space = ActSpace(ini["valid-actions"],ini["valid-objects"]) + ["inventory"]
    #print(act_space)
    #action = input("Enter your response (Number of actions used = {}) >>> ".format(num_act))
    action = random.choice(act_space)
    num_act+=1
    
    if action == "go to chamber-1" :
        env = { "obs" : "This room is called the chamber1. In it, you see:  a doctor table,  a doctor chair, a bed,  a bed table, a bed-medical-equipment, a sink (turned off), a cupboard (closed), a door to hallway , a dustbin-1",
                "valid-actions" : [ "go to", "examine", "close", "open"],
                "valid-objects" : [ "doctor table", "doctor chair", "bed", "bed table", "bed-medical-equipment", "sink", "cupboard", "hallway", "dustbin-1" ]   }
        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, env["obs"]))
        appJSON(action, env["obs"], num_act)
        act_space = ActSpace(env["valid-actions"],env["valid-objects"]) + ["inventory"]
        #print(act_space)
        
        while num_act<50:
            #action = input("Enter your response (Number of actions used = {}) >>> ".format(num_act))
            action = random.choice(act_space)
            num_act+=1
            
            if action == "go to doctor table":
                obs = "You are near the doctor table."
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue                
            elif action == "go to doctor chair":
                obs = "You are near the doctor chair."
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "go to bed":
                obs = "You are near the bed."
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "go to bed table":
                obs = "You are near the bed table."
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "go to bed-medical-equipment":
                obs = "You are near the bed-medical-equipment."
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "go to sink":
                obs = "You are near the sink."
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "go to cupboard":
                obs = "You are near the cupboard."
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "go to hallway":
                obs = "This room is called the hallway. In it, you see: a poster, a doctor, the agent, a nurse station. You also see:  A door to chamber1, A door to chamber2, A door to the ICU ward, A door to the general ward, A door to the common toilet, A staircase to go to 1st Floor. In your inventory, you see:  {}".format(inventory)
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                break
            elif action == "go to dustbin-1":
                obs = "You are near the dustbin."
                if inventory["waste"]:
                    obs += "You have waste products in your inventory. Clear it!!! But do remember to examine the dustbin first."
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "examine doctor table":
                env = { "obs" : "On the table is: {} ".format(doctor_table1),
                        "valid-actions" : [ "collect" ],
                        "valid-objects" : doctor_table1   }
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, env["obs"]))
                appJSON(action, env["obs"], num_act)
                act_space = ActSpace(env["valid-actions"],env["valid-objects"]) + ["inventory"]
                #print(act_space)
                
                while num_act<50:
                    #action = input("Enter your response (Number of actions used = {}) >>> ".format(num_act))
                    action = random.choice(act_space)
                    num_act+=1
                    
                    if action == "collect glass cup (empty)" or action =="collect computer" or action == "collect note-pad":
                        obs = "Collect a waste-product. Not other objects"
                        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                        appJSON(action, obs, num_act)
                        continue
                    elif action == "collect waste-paper":
                        doctor_table1.remove("waste-paper")
                        inventory["waste"].append("waste-paper")
                        obs = "Waste-paper is collected. Now dispose it accordingly!"
                        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                        appJSON(action, obs, num_act)
                        break
                    elif action == "inventory":
                        obs = "Your inventory includes : {}".format(inventory)
                        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                        appJSON(action, obs, num_act)
                        continue
                    else:
                        obs = "Focus on collecting the waste-product"
                        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                        appJSON(action, obs, num_act)
                        continue  
                continue                                              
            elif action == "examine doctor chair":
                obs = "On the chair is: nothing."
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "examine bed":
                obs = "On the bed is: nothing."
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "examine bed table":
                obs = "On the bed table is: a bowl (containing a banana, a potato, a red apple, an orange), a drawer. There are no waste products here. Keep exploring!"
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "examine bed-medical-equipment":
                obs = "This is a medical equipment attached to the bed. Your job is to find waste products. Take actions accordingly."
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "examine sink":
                obs = "This is the sink. Your job is to find waste products. Take actions accordingly."
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "examine cupboard":
                obs = "This is the cupboard. Your job is to find waste products. Take actions accordingly."
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
            elif action == "examine dustbin-1":                
                    if len(dustbin1)>=10:
                        obs = "The dustbin is full. Please look for other options."
                        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                        appJSON(action, obs, num_act)
                    else :
                        if inventory["waste"]:
                            env = { "obs" : "The dustbin contains {} items. It can only accomodate {} more items. You have waste products in your inventory.".format(len(dustbin1), 10-len(dustbin1)),
                                    "valid-actions" : [ "dispose" ],
                                    "valid-objects" : inventory["waste"]  }
                            print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, env["obs"]))
                            appJSON(action, env["obs"], num_act)
                            in_wastes = ", ".join(inventory["waste"])
                            act_space = ["dispose {}".format(in_wastes), "inventory"]
                            #print(act_space)
                            
                            while num_act<50:
                                #action = input("Enter your response (Number of actions used : {}) >>> ".format(num_act))
                                action = random.choice(act_space)
                                num_act+=1
                                if action == "dispose {}".format(in_wastes):
                                    obs = "You have sucessfully disposed of the garbage from the inventory"
                                    collect+=1
                                    inventory["waste"].remove(in_wastes)
                                    print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                                    appJSON(action, obs, num_act)
                                    break
                                elif action == "inventory":
                                    obs = "Your inventory includes : {}".format(inventory)
                                    print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                                    appJSON(action, obs, num_act)
                                    continue
                                else:   
                                    obs = "Please dispose off the waste materials!"
                                    print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                                    appJSON(action, obs, num_act)
                                    continue
                        else:
                            obs = "You donot have any waste products to dispose."
                            print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                            appJSON(action, obs, num_act)
                    continue
            elif action == "open sink":
                obs = "The sink is now open. Water is flowing out of it, donot forget to close!"
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "open cupboard":
                obs = "The cupboard is now open. There is nothing inside the cupboard!"
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "close sink":
                obs = "The sink is now closed."
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "close cupboard":
                obs = "The cupboard is now closed!"
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "inventory":
                obs = "Your inventory includes : {}".format(inventory)
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
            else : 
                obs = " Enter some valid action!!"
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue 
        continue                   
    elif action == "go to chamber-2":
        env = { "obs" : "This room is called the chamber-2. In it, you see: a doctor table,  a doctor chair, a bed,  a bed table, banana peel on the floor, a dustbin-2, a door to toilet (open), a door to hallway (open)",
                "valid-actions" : [ "go to", "examine", "collect"],
                "valid-objects" : [ "doctor table", "doctor chair", "bed", "bed table", "banana peel", "hallway", "dustbin-2", "toilet" ]   }
        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, env["obs"]))
        appJSON(action, env["obs"], num_act)
        act_space = ActSpace(env["valid-actions"],env["valid-objects"]) + ["inventory"]
        #print(act_space)
        
        while num_act<50:
            #action = input("Enter your response (Number of actions used = {}) >>> ".format(num_act))
            action = random.choice(act_space)
            num_act+=1
            
            if action == "go to doctor table":
                obs = "You are near the doctor table."
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue                
            elif action == "go to doctor chair":
                obs = "You are near the doctor chair."
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "go to bed":
                obs = "You are near the bed."
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "go to bed table":
                obs = "You are near the doctor table."
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "go to banana peel":
                obs = "You are near the banana peel"
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "go to hallway":
                obs = "This room is called the hallway. In it, you see: a poster, a doctor, the agent, a nurse station. You also see:  A door to chamber1, A door to chamber2, A door to the ICU ward, A door to the general ward, A door to the common toilet, A staircase to go to 1st Floor. In your inventory, you see:  {}".format(inventory)
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                break
            elif action == "go to dustbin-2":
                obs = "You are near the dustbin."
                if inventory["waste"]:
                    obs += "You have waste products in your inventory. Clear it!!! But do remember to examine the dustbin first."
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "go to toilet":
                obs = "You are inside the toilet now, there is nothing here"
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "examine doctor table":
                obs = "On the table is: {} . Continue your quest to explore waste products and not other products!".format(doctor_table2)
                print("Action : {} and Observation : {}".format(action,obs))
                appJSON(action, obs, num_act)
                continue                                              
            elif action == "examine doctor chair":
                obs = "On the chair is: nothing."
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "examine bed":
                obs = "On the bed is: nothing."
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "examine bed table":
                obs = "On the bed table is: a bowl (containing a banana, a potato, a red apple, an orange), a drawer. Continue your quest to explore waste products and not other products!"
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "examine banana peel":
                obs = "There is a banana peel lying on the floor."
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
            elif action == "examine dustbin-2":                
                    if len(dustbin2)>=10:
                        obs = "The dustbin is full. Please look for other options."
                        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                        appJSON(action, obs, num_act)
                    else :
                        if inventory["waste"]:
                            env = { "obs" : "The dustbin contains {} items. It can only accomodate {} more items. You have waste products in your inventory.".format(len(dustbin2), 10-len(dustbin2)),
                                    "valid-actions" : [ "dispose" ],
                                    "valid-objects" : inventory["waste"]  }
                            print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, env["obs"]))
                            appJSON(action, env["obs"], num_act)
                            in_wastes = ", ".join(inventory["waste"])
                            act_space = ["dispose {}".format(in_wastes), "inventory"]
                            #print(act_space)
                            
                            while num_act<50:
                                #action = input("Enter your response (Number of actions used : {}) >>> ".format(num_act))
                                action = random.choice(act_space)
                                num_act +=1
                                if action == "dispose {}".format(in_wastes):
                                    obs = "You have sucessfully disposed of the garbage from the inventory"
                                    collect+=1
                                    inventory["waste"].remove(in_wastes)
                                    print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                                    appJSON(action, obs, num_act)
                                    break
                                elif action == "inventory":
                                    obs = "Your inventory includes : {}".format(inventory)
                                    print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                                    appJSON(action, obs, num_act)
                                else:   
                                    obs = "Please dispose off the waste materials!"
                                    print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                                    appJSON(action, obs, num_act)
                                    continue
                        else:
                            obs = "You donot have any waste products to dispose."
                            print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                            appJSON(action, obs, num_act)
                    continue
            elif action == "collect banana peel":
                inventory["waste"].append("banana peel")
                obs = "The banana peel is collected in the inventory. Now dispose it accordingly!"
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
            elif action == "inventory":
                obs = "Your inventory includes : {}".format(inventory)
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
            else : 
                obs = " Enter some valid action!!"
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue                           
    elif action == "go to ICU ward":
        env = { "obs" : "This room is called the ICU ward. In it, you see: medical equipment, patient beds, a nurse station, the agent. You also see: A door to Patient Room 1 (open), A door to Patient Room 2 (open), A door to Patient Room 3 (open), A door to the hallway (open). Your job is to explore waste materials from doctors chambers. Take actions accordingly!",           
                "valid-actions" : ["go to"],
                "valid-objects" : ["hallway"]     }
        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, env["obs"]))
        appJSON(action, env["obs"], num_act)
        act_space = ActSpace(env["valid-actions"],env["valid-objects"]) + ["inventory"]
        #print(act_space)
        
        while num_act<50:
            #action = input("Enter your response (Number of actions used = {}) >>> ".format(num_act))
            action = random.choice(act_space)
            num_act+=1
            
            if action == "go to hallway" :
                break     
            elif action == "inventory":
                obs = "Your inventory includes : {}".format(inventory)
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act) 
            else : 
                obs = "Not valid. Try going back to exploring doctors chambers"
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue       
    elif action == "go to general ward":
        env = { "obs" : "This room is called the general ward. In it, you see: 20 patient beds, 20 bed-side table, medical equipment, a nurse's station, a door to the hallway (open). Your job is to explore waste materials from doctors chambers. Take actions accordingly!",
                "valid-actions" : ["go to"],
                "valid-objects" : ["hallway"]     }
        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, env["obs"]))
        appJSON(action, env["obs"], num_act)
        act_space = ActSpace(env["valid-actions"],env["valid-objects"]) + ["inventory"]
        #print(act_space)
        while num_act<50:
            #action = input("Enter your response (Number of actions used = {}) >>> ".format(num_act))
            action = random.choice(act_space)
            num_act+=1
            
            if action == "go to hallway" :
                obs = "This room is called the hallway. In it, you see: a poster, a doctor, the agent, a nurse station. You also see:  A door to chamber1, A door to chamber2, A door to the ICU ward, A door to the general ward, A door to the common toilet, A staircase to go to 1st Floor. In your inventory, you see:  {}".format(inventory)
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                break     
            elif action == "inventory":
                obs = "Your inventory includes : {}".format(inventory)
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act) 
            else : 
                obs = "Not valid. Try going back to exploring doctors chambers"
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
    elif action == "go to common toilet":
        env = { "obs" : "This room is called the common toilet. You also see: A door to gents section (closed), A door to ladies section (closed). Your job is to explore waste materials from doctors chambers. Take actions accordingly!",
                "valid-actions" : ["go to"],
                "valid-objects" : ["hallway"]     }
        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, env["obs"]))
        appJSON(action, env["obs"], num_act)
        act_space = ActSpace(env["valid-actions"],env["valid-objects"]) + ["inventory"]
        #print(act_space)
        while num_act<50:
            #action = input("Enter your response (Number of actions used = {}) >>> ".format(num_act))
            action = random.choice(act_space)
            num_act+=1
            
            if action == "go to hallway" :
                obs = "This room is called the hallway. In it, you see: a poster, a doctor, the agent, a nurse station. You also see:  A door to chamber1, A door to chamber2, A door to the ICU ward, A door to the general ward, A door to the common toilet, A staircase to go to 1st Floor. In your inventory, you see:  {}".format(inventory)
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                break     
            elif action == "inventory":
                obs = "Your inventory includes : {}".format(inventory)
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act) 
            else : 
                obs = "Not valid. Try going back to exploring doctors chambers"
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
    elif action == "go to nurse station":
        env = { "obs" : " This room is the nurse station. In it, you see computer stations, filing cabinets, and nurses at work. You are still in the hallway, but near the nurse station. Your job is to explore waste materials from doctors chambers. Take actions accordingly!",
                "valid-actions" : ["go to"],
                "valid-objects" : ["hallway"]     }
        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, env["obs"]))
        appJSON(action, env["obs"], num_act)
        act_space = ActSpace(env["valid-actions"],env["valid-objects"]) + ["inventory"]
        #print(act_space)
        
        while num_act<50:
            #action = input("Enter your response (Number of actions used = {}) >>> ".format(num_act))
            action = random.choice(act_space)
            num_act+=1
            
            if action == "go to hallway" :
                obs = "This room is called the hallway. In it, you see: a poster, a doctor, the agent, a nurse station. You also see:  A door to chamber1, A door to chamber2, A door to the ICU ward, A door to the general ward, A door to the common toilet, A staircase to go to 1st Floor. In your inventory, you see:  {}".format(inventory)
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                break     
            elif action == "inventory":
                obs = "Your inventory includes : {}".format(inventory)
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act) 
            else : 
                obs = "Not valid. Try going back to exploring doctors chambers"
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue
    elif action == "go to 1st Floor": 
        env = { "obs" : "You are now on the 1st Floor landing. In it, you see: a corridor with doors leading to various rooms, the staircase to go down. You also see: A staircase leading to the Ground Floor, A door to the general ward, A door to the staff room, A door to the linen storage room.  There are no doctors chambers in this floor. Go back and complete the task!",
                "valid-actions" : ["go to"],
                "valid-objects" : ["Ground Floor", "General ward", "Staff room", "linen storage room"]  }
        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, env["obs"]))
        appJSON(action, env["obs"], num_act)
        act_space = ActSpace(env["valid-actions"],env["valid-objects"]) + ["inventory"]
        #print(act_space)
        while num_act<50:
            #action = input("Enter your response (Number of actions used = {}) >>> ".format(num_act))
            action = random.choice(act_space)
            num_act+=1
            
            if action == "go to hallway" :
                obs = "This room is called the hallway. In it, you see: a poster, a doctor, the agent, a nurse station. You also see:  A door to chamber1, A door to chamber2, A door to the ICU ward, A door to the general ward, A door to the common toilet, A staircase to go to 1st Floor. In your inventory, you see:  {}".format(inventory)
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                break     
            elif action == "inventory":
                obs = "Your inventory includes : {}".format(inventory)
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act) 
            else : 
                obs = "Not valid. Try going back to exploring doctors chambers"
                print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
                appJSON(action, obs, num_act)
                continue   
    elif action == "go to poster":
        obs = "You are near the poster now."
        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
        appJSON(action, obs, num_act)
    elif action == "go to doctor-1":
        obs = "You are near doctor-1 now."
        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
        appJSON(action, obs, num_act)
    elif action == "examine poster": 
        obs = "This is a poster of a baby boy smiling. Your job is to clear waste materials. Take action accordingly!"                    
        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
        appJSON(action, obs, num_act)
    elif action == "examine doctor-1": 
        obs = "He is doctor Ram specializes in orthopedics. Go to nurse station to get more information about his schedule. Your job is to clear waste materials. Take action accordingly!"                    
        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
        appJSON(action, obs, num_act)
    elif action == "examine agent":
        obs = "You are the agent who needs to complete the task. Take actions accordingly"
        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))  
        appJSON(action, obs, num_act)
    elif action == "examine chamber-1":
        obs = "You cannot examine a room without going inside. Take actions accordingly"
        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
        appJSON(action, obs, num_act)
    elif action == "examine chamber-2":
        obs = "You cannot examine a room without going inside. Take actions accordingly"
        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
        appJSON(action, obs, num_act)
    elif action == "examine nurse station":
        obs = "You cannot examine a room without going inside. Take actions accordingly"
        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
        appJSON(action, obs, num_act)
    elif action == "examine ICU ward":
        obs = "You cannot examine a room without going inside. Take actions accordingly"
        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
        appJSON(action, obs, num_act)
    elif action == "examine general ward":
        obs = "You cannot examine a room without going inside. Take actions accordingly"
        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
        appJSON(action, obs, num_act)
    elif action == "examine common toilet":
        obs = "You cannot examine a room without going inside. Take actions accordingly"
        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
        appJSON(action, obs, num_act)
    elif action == "examine 1st Floor":
        obs = "You cannot examine a room without going inside. Take actions accordingly"
        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
        appJSON(action, obs, num_act)
    else:
        obs = "Not a valid action. Start again!"
        print("ACTION (#actions={}) : {} and OBSERVATION : {}".format(num_act,action, obs))
        appJSON(action, obs, num_act)


print(collect)
if collect >= 1:
    print("TASK IS COMPLETED SUCCESSFULLY!!!")
    label = 1
else:
    print("You have exited without completing the task.")       
    label = 0
