#### IMPORTS ####
import re
import random
import json


#### JSON FILE APPEND FUNCTION ####
file1 = 'task1_var1_play30.json'
def write_json(action,obs,num):
    d2 = {   "ACTION" : action, 
             "OBSERVATION" : obs,
            "#Actions Used" : num  }
    with open(file1, 'a') as file:
        file.write(json.dumps(d2) + '\n')



###########################################################     CLASSES      ###############################################################

#### ROOM CLASS ####
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connected_rooms = []
        self.items = []
        self.item_names = {}
        self.actions = []
        self.connected_room_names = {}
        

    def connect_room(self, room):
        if room not in self.connected_rooms:
            self.connected_rooms.append(room)
            room.connected_rooms.append(self)  # Bidirectional connection
            self.connected_room_names[room.name] = room

    def get_details(self):
        obs = self.description
        rooms = [i.name for i in self.connected_rooms]
        obs += f"The rooms that we can go from here are : {', '.join(rooms)}. "
        items = [i.name for i in self.items]
        obs += f"The room contains : {', '.join(items)}."
        return obs
    
    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:  # First, try to remove the item directly from the room
                self.items.remove(item)
            
            elif item.contains:
                for i in item.contains:
                    if i.name == item_name:
                        item.contains.remove(i)        # If not found, check if the item is nested within another item

    def add_item(self, item):
        self.items.append(item)
        self.item_names[item.name] = item

    def add_action(self, action_name):
        self.actions.append(action_name)

    def get_actions(self):
        action_space = ["inventory"]
        for action in self.actions:
            if action == "examine":
                for item in self.items:
                    action_space.append(f"examine {item.name}")
            elif action == "go to":
                for room in self.connected_rooms:
                    action_space.append(f"go to {room.name}")
            elif action == "collect":
                for item in self.items:
                    if item.is_static==False:  # Check for movable objects
                        action_space.append(f"collect {item.name}")
            else:
                action_space.append(action)
        
        return action_space
        
        

    def perform_action(self, action_name, game):
        if action_name in self.actions:
            self.actions[action_name](game)
        else:
            print("Action not available.")


#### ITEM CLASS ####
class Item:
    def __init__(self, name, description, action=None, is_static=True):
        self.name = name
        self.description = description
        self.action = action
        self.is_static = is_static
        self.contains = []  # List of items contained by this item

    def add_desc(self, desc):
        self.description += desc

    def describe(self):
        obs = f"{self.description}. "
        items = [i.name for i in self.contains]
        if self.contains:
            obs += f"It contains: {', '.join(items)}. "
        return obs

    def add_item(self, item):
        self.contains.append(item)

    def remove_item(self, item_name):
        for item in self.contains:
            if item.name == item_name:
                self.contains.remove(item)
                return item
        return None



#### GAME CLASS ####
class Game:
    def __init__(self, starting_room):
        self.current_room = starting_room
        obs = f"You are in the {self.current_room.name}. "
        obs += self.current_room.get_details()
        print(f"ACTION : <initialize> and OBSERVATION : {obs}")
        ini = { "ACTION" : "<initialize>",
                "OBSERVATION" : obs,
                "#Actions Used" : 0}
        with open(file1, 'w') as file:
            file.write(json.dumps(ini) + '\n')
        self.inventory = []
        self.waste_info = ["waste paper", "banana peel"]
        self.flag=False
        self.num_actions=0
    
    #### Action Functions ####
    
    def add_to_inventory(self, item_name):
        for i in self.current_room.items:
            if i.name == item_name:         # Find item from current room items
                item = i
            elif i.contains:
                for a in i.contains:
                    if a.name == item_name:     # Find item from nested items.
                        item = a
            else:
                obs = f"{item_name} not found in the room. "
        if item:
            if item.is_static==True:
                obs = f"{item_name} cannot be collected. "
            elif item.is_static == False:
                self.inventory.append(item)
                obs = f"{item_name} added to inventory. "
        return obs

    def put_item(self, item_name, target_name):
        # Use an item from the inventory on a target item in the room
        if item_name in [item.name for item in self.inventory]:
            for item in self.current_room.items:
                if item.name == target_name:
                    target_item = item
            if target_item:
                target_item.add_item(self.remove_from_inventory(item_name))
                obs = f"{item_name} placed on {target_name}."
            else:
                obs = f"{target_name} not found in the room."
        else:
            obs = f"{item_name} is not in your inventory."
        return obs

    def remove_from_inventory(self, item_name):
        # Remove and return an item from the inventory
        item = next(item for item in self.inventory if item.name == item_name)
        self.inventory.remove(item)
        return item

   
    #### Game Loop ####
    
    def start(self):
        while self.num_actions!=30:
            
            
            print(f"Action Space : {list(set(self.current_room.get_actions()))}")
            
            
            choice = input("\nAction choice (HUMAN or RANDOM) >>> ").lower()
            if choice == "human":
                command = input("Action >>> ").lower()
                self.num_actions+=1
            elif choice == "random":
                command = random.choice(self.current_room.get_actions())
                self.num_actions+=1
            else : 
                print("Invalid Choice. Try again!")
                continue


            if command.startswith("go to"):
                room_name = command[len("go to "):]
                for room in self.current_room.connected_rooms:
                    if room.name == room_name:
                        self.current_room = room
                        obs = self.current_room.get_details()
                        break
                    else:
                        obs = "Room not found"
                print(f"ACTION : {command} and OBSERVATION : {obs}")
                write_json(command, obs, self.num_actions)
            
            elif command.startswith("collect"):
                item_name = command[len("collect "):]
                obs = self.add_to_inventory(item_name)
                self.current_room.remove_item(item_name)
                print(f"ACTION : {command} and OBSERVATION : {obs}")
                write_json(command, obs, self.num_actions)

            elif command.startswith("put"):
                pattern = r"^put\s+(.*?)\s+on\s+(.*)$"
                match = re.search(pattern, command)
                if match:
                    item_name = match.group(1)  # The first capturing group (item name)
                    target_name = match.group(2)
                obs = self.put_item(item_name, target_name)
                print(f"ACTION : {command} and OBSERVATION : {obs}")
                write_json(command, obs, self.num_actions)

                # Check for dustbin status
                if bin1.contains or bin2.contains:
                    items = [i.name for i in bin1.contains] + [j.name for j in bin2.contains]
                    if(all(x in items for x in self.waste_info)):
                        self.flag = True
                        break
            
            elif command.startswith("examine"):
                item_name = command[len("examine "):]
                for item in self.current_room.items:
                    if item.name == item_name:
                        obs = item.describe()
                        if item.contains:
                            for i in item.contains:
                                self.current_room.add_item(i)
                        break
                    else:
                        obs = "Invalid Item"
                print(f"ACTION : {command} and OBSERVATION : {obs}")
                write_json(command, obs, self.num_actions)

            elif command == "inventory":
                items = [i.name for i in self.inventory]
                obs = f"Your inventory includes : {','.join(items)}. "
                print(f"ACTION : {command} and OBSERVATION : {obs}")
                write_json(command, obs, self.num_actions)
            
            else:
                print("Invalid action. Try again!")
    



###########################################################    ROOMS     ###############################################################


### ROOMS ###
hall = Room("hallway", "This room is called the hallway. This is the main corridor in the ground floor from which we can go to other rooms. ")
ch1 = Room("doctor chamber #1", "This is the doctor chamber #1. Doctors in OPD diagnose patients here. ")
ch2 = Room("doctor chamber #2", "This is the doctor chamber #2. Doctors in OPD diagnose patients here. ")
gen_ward = Room("general ward", "This is the general ward. There are a total of 5 beds with a nurse station who carries the information of the patients. ")
icu_ward = Room("icu ward", "This is the icu ward. There are a total of 3 patient rooms attached with medical equipments and a nurse station who carries the information of the patients. ")
comm_toilet = Room("common toilet", "This is the common toilet in the hallway. This has single occupancy. ")
nurse_station1 = Room("nurse station", "This is the nurse station. You see nurses at work here. You can get information from the nurse station.")
nurse_station2 = Room("nurse station", "This is the nurse station. You see nurses at work here. You can get information from the nurse station.")
icu_nurse_st = Room("nurse station", "This is the nurse station. You see nurses at work here. You can get information from the nurse station.")


### CONNECT ROOMS ###
hall.connect_room(ch1)
hall.connect_room(ch2)
hall.connect_room(gen_ward)
hall.connect_room(icu_ward)
hall.connect_room(comm_toilet)
hall.connect_room(nurse_station1)
gen_ward.connect_room(nurse_station2)
icu_ward.connect_room(icu_nurse_st)

#### Adding Actions to Rooms ####
hall.add_action("go to")
ch1.add_action("go to")
ch2.add_action("go to")
gen_ward.add_action("go to")
icu_ward.add_action("go to")
comm_toilet.add_action("go to")
nurse_station1.add_action("go to")
nurse_station2.add_action("go to")
icu_nurse_st.add_action("go to")



###########################################################     ITEMS     ###############################################################

#### HALLWAY ITEMS ####
poster = Item("wall poster", "This is a poster comprising a picture of a baby boy smiling. ")
doctor1 = Item("doctor #1", "He is doctor Ram specializes in orthopedics. ")
agent = Item("agent", "You are the agent. Your job is to complete the tasks. ")

hall.add_item(poster)
hall.add_item(doctor1)
hall.add_item(agent)

hall.add_action("examine")


### CHAMBER-1 ITEMS ###
doc_table1 = Item("doctor table", "This table belongs to the doctor who keeps his belongings. ")
doc_chair1 = Item("doctor chair", "This chair belongs to the doctor. It is near the doctor table. ")
doc_bed1 = Item("patient bed", "This bed in the doctor chamber is used to diagnose OPD patients by the doctor. ")
doc_bedtable1 = Item("patient bed table", "This bed table is beside the patient bed. ")
bin1 = Item("dustbin", "A dustbin for disposing waste materials")

book1 = Item("book", "An old leather-bound book.", is_static=False)
lamp1 = Item("lamp", "A small electric lamp.", is_static=False)
waste_paper1 = Item("waste paper", "A paper to be thrown", is_static=False)
note_pad1 = Item("note pad", "A notebook for the doctor to write notes", is_static=False)

doc_table1.add_item(book1)
doc_table1.add_item(lamp1)
doc_table1.add_item(waste_paper1)
doc_table1.add_item(note_pad1)

ch1.add_item(doc_table1)
ch1.add_item(doc_chair1)
ch1.add_item(doc_bed1)
ch1.add_item(doc_bedtable1)
ch1.add_item(bin1)

ch1.add_action("examine")
ch1.add_action("collect")



#### CHAMBER-2 ITEMS ####
doc_table2 = Item("doctor table", "This table belongs to the doctor who keeps his belongings. ")
doc_chair2 = Item("doctor chair", "This chair belongs to the doctor. It is near the doctor table. ")
doc_bed2 = Item("patient bed", "This bed in the doctor chamber is used to diagnose OPD patients by the doctor. ")
doc_bedtable2 = Item("patient bed table", "This bed table is beside the patient bed. ")
peel = Item("banana peel", "A banana peel is lying on the ground of the room", is_static=False)
bin2 = Item("dustbin", "A dustbin for disposing waste materials")

book2 = Item("book", "An old leather-bound book.", is_static=False)
lamp2 = Item("lamp", "A small electric lamp.", is_static=False)
note_pad2 = Item("note pad", "A notebook for the doctor to write notes", is_static=False)

doc_table2.add_item(book2)
doc_table2.add_item(lamp2)
doc_table2.add_item(note_pad2)

ch2.add_item(doc_table2)
ch2.add_item(doc_chair2)
ch2.add_item(doc_bed2)
ch2.add_item(doc_bedtable2)
ch2.add_item(peel)
ch2.add_item(bin2)

ch2.add_action("examine")
ch2.add_action("collect")



#### GENERAL WARD ITEMS ####
nurse1 = Item("nurse", "This is a nurse. This nurse have information about where to collect waste information. ")
pat_bed1 = Item("patient bed", "This bed belongs to patient #1. ")
pat_bed2 = Item("patient bed", "This bed belongs to patient #2. ")
pat_bed3 = Item("patient bed", "This bed belongs to patient #3. ")
pat_bed4 = Item("patient bed", "This bed belongs to patient #4. ")
pat_bed5 = Item("patient bed", "This bed belongs to patient #5. ")

gen_ward.add_item(pat_bed1)
gen_ward.add_item(pat_bed2)
gen_ward.add_item(pat_bed3)
gen_ward.add_item(pat_bed4)
gen_ward.add_item(pat_bed5)
gen_ward.add_item(nurse1)

gen_ward.add_action("examine")




#### NURSE STATION (HALLWAY) ITEMS ###
comp_station = Item("computer station", "This is a computer station comprising of 3 computers. These are used for extracting information and registration. Can only be accessed by the nurses. ")
files = Item("filing cabinet", "This is the filing cabinet comprising of different patient files used during treatment by the doctors and nurses. ")

nurse_station1.add_item(comp_station)
nurse_station1.add_item(files)

nurse_station1.add_action("examine")


#### ICU WARD ITEMS ###
med_equip1 = Item("medical equipment", "This is a Ultrasonograph measuring device. It can be only operated by nurses and doctors. ")
icu_bed1 = Item("patient bed", "This bed belongs to patient #1. ")
icu_bed2 = Item("patient bed", "This bed belongs to patient #2. ")


icu_ward.add_item(med_equip1)
icu_ward.add_item(icu_bed1)
icu_ward.add_item(icu_bed2)

gen_ward.add_action("examine")



# Initialize game with the starting room
game = Game(hall)

# Start the game
game.start()
print(f"Status : {game.flag} with Number of actions taken : {game.num_actions}")

#### Write the success label to the JSON file ####
if game.flag == True:
    label = 1
elif game.flag == False:
    label = 0
res = {
        "success" : label,
        "Number of actions taken" : game.num_actions
    }
with open(file1, 'a') as file:
    file.write(json.dumps(res) + '\n')


