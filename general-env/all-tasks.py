
### -------- ACTIONS ---------- ###
def put(obj,des,loc):
    obs = "The {} is put on {} located inside {}".format(obj,des,loc)
    return obs

def go(obj):
    obs = "You are in the {}".format(obj, [obj["env"].keys()] )
    return obs



### -------- ROOMS -------- ###
hallway = {
                    "chamber-1" : "open",
                    "chamber-2" : "closed",
                    "ICU ward" : "closed",
                    "General ward" : "open",
                    "Nurse station" : "info",
                    "poster" : "Picture of a baby-child smiling",
                    "Reception" : "open"            }

chamber1 = {
                "doctor-table" : ["Computer", "Waste-paper", "Notebook", "pen-stand"],
                "doctor-chair" : "nothing", 
                "bed" : "nothing", 
                "bed-table" : "nothing",
                "bed-medical-equipment" : "nothing",
                "dustbin" : 70          }
                
chamber2 = {
                "doctor-table" : ["Computer", "note-pad"],  
                "doctor-chair" : "nothing", 
                "bed" : "nothing",  
                "bed table" : "nothing", 
                "sink" : "off",
                "cupboard" :  "closed", 
                "toilet" :  "closed",
                "floor" : "banana peel",
                "dustbin" : 30,
                "hallway" : "open"   }



### ----------- GAMEPLAY ------------- ###
ini_obj = list(hallway["env"].keys())
ini_action = ["go to OBJ", "examine OBJ", "look around", "inventory", "open OBJ", "close OBJ", "put OBJ on OBJ"]
ini_obs = "You are in the {}. In it, you see {}. Your available actions are : {}".format(hallway, ini_obj, ini_action)


action = input()