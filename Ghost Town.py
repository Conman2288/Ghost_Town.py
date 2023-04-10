#################################################################
# Name: Dominic Rosario, Connor Heard, Lee Saucier
# Date: 4/7/23
# Description: Room Adventure - Revolutions, Ghost Town
#################################################################
from tkinter import *

# the room class
class Room:

# the constructor
    def __init__(self, name, image):
        # rooms have a name, an image (the name of a file),
        # exits (e.g., south), exit locations
        # (e.g., to the south is room n), items (e.g., table),
        # item descriptions (for each item), and grabbables
        # (things that can be taken into inventory)
        self.name = name
        self.image = image
        self.exits = {}
        self.items = {}
        self.grabbables = []
        # getters and setters for the instance variables

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value
        # adds an exit to the room
        # the exit is a string (e.g., north)
        # the room is an instance of a room

    def addExit(self, exit, room):
        # append the exit and room to the appropriate
        # dictionary
        self._exits[exit] = room
        # adds an item to the room
        # the item is a string (e.g., table)
        # the desc is a string that describes the item (e.g., it is
        # made of wood)

    def addItem(self, item, desc):
        # append the item and description to the appropriate
        # dictionary
        self._items[item] = desc
        # adds a grabbable item to the room
        # the item is a string (e.g., key)

    def addGrabbable(self, item):
        # append the item to the list
        self._grabbables.append(item)
        # removes a grabbable item from the room
        # the item is a string (e.g., key)

    def delGrabbable(self, item):
        # remove the item from the list
        self._grabbables.remove(item)
        # returns a string description of the room

    def __str__(self):
        # first, the room name
        s = "You are in {}.\n".format(self.name)
        # next, the items in the room
        s += "You see: "
        for item in self.items.keys():
            s += item + ", "
            
        # next, the exits from the room
        s += "\n"
        s += "Exits: "

        for exit in self.exits.keys():
            s += exit + " "
        return s

# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
    # the constructor
    def __init__(self, parent):
        # call the constructor in the superclass
        Frame.__init__(self, parent)
        # creates the rooms

    def createRooms(self):
        # r1 through r4 are the four rooms in the mansion
        # currentRoom is the room the player is currently in (which
        # can be one of r1 through r4)
        # create the rooms and give them meaningful names and an
        # image in the current directory
        r1 = Room("The Post Office", "post.png")
        r2 = Room("The Saloon", "saloon.png")
        r3 = Room("The General Store", "store.png")
        r4 = Room("The Stable", "stable.png")
        r5 = Room("The Factory", "factory.png")

        # add exits to room 1
        r1.addExit("saloon", r2) # to the east of room 1 is room 2
        r1.addExit("general_store", r3)
        r1.addExit("factory", r5)
        # add grabbables to room 1
        r1.addGrabbable("revolver")
        # add items to room 1
        r1.addItem("wall", "It has tens of empty wooden boxes, likey where mail would end up if there was anyone left to mail anything to")
        r1.addItem("desk", "It is made of wood, old and rotted to the point its malluable like putty, your golden revolver is sunk into the center of the desk")
        r1.addItem("room", "Old and dusty, galss is shrewn around from a moment ago when you crashed through the window.")

        # add exits to room 2
        r2.addExit("post_office", r1)
        r2.addExit("stable", r4)
        r2.addExit("factory", r5)
        # add items to room 2
        r2.addItem("stairs", "It likely heads upstairs to the hotel rooms, but I wouldnt trust those staris as much as i would trust a job to go right")
        r2.addItem("bar", "All the Alcohol is gone, not suprised.")

        # add exits to room 3
        r3.addExit("post_office", r1)
        r3.addExit("stable", r4)
        r3.addExit("factory", r5)
        # add grabbables to room 3
        r3.addGrabbable("stash")
        # add items to room 3
        r3.addItem("bookshelves", "They are some small books left, however id bet they're so matted opening one would destroy it")
        r3.addItem("counter", "You see that the window next to the counter is shattered, taking a peak behind it.... ITS THERE! THE STASH!!")
        r3.addItem("medicine_cabnet", "Just about empty, whatever is left is bound to do the opposite of what its supposed to")

        # add exits to room 4
        r4.addExit("factory", r5)
        r4.addExit("saloon", r2)
        r4.addExit("general_store", r3)
        r4.addExit("horse?", None) # DEATH!
        # add items to room 4
        r4.addItem("wooden_stable","It looks like the only thing thats lasted the test of time, theres some grass growing.")
        r4.addItem("horse", "Its your horse! he came back for you, his pitch black tone standing as a contrast to the setting sun in the horizon")
        
        # add exits to room 5
        r5.addExit("post_office", r1)
        r5.addExit("stable", r4)
        r5.addExit("general_store", r3)
        r5.addExit("saloon", r2)
        # add items to room 5
        r5.addItem("interior", "In the center of town its old and rusted, this factory has long run out of purpose other than as an unstable shelter")
        r5.addItem("well", "Its all run out of water")
        r5.addItem("doors", "The town is quite split up with few trails leading from place to place, but the factory has a trail leading to all of the different locations")
        
        # set room 1 as the current room at the beginning of the
        # game
        Game.currentRoom = r1
        # initialize the player's inventory
        Game.inventory = []

    # sets up the GUI
    def setupGUI(self):
        # organize the GUI
        self.pack(fill=BOTH, expand=1)
        # setup the player input at the bottom of the GUI
        # the widget is a Tkinter Entry
        # set its background to white and bind the return key to the
        # function process in the class
        # push it to the bottom of the GUI and let it fill
        # horizontally
        # give it focus so the player doesn't have to click on it
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()
        # setup the image to the left of the GUI
        # the widget is a Tkinter Label
        # don't let the image control the widget's size
        img = None
        Game.image = Label(self, width=WIDTH // 2, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)
        # setup the text to the right of the GUI
        # first, the frame in which the text will be placed
        text_frame = Frame(self, width=WIDTH // 2)
        # the widget is a Tkinter Text
        # disable it by default
        # don't let the widget control the frame's size
        Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)


    # set the current room image
    def setRoomImage(self):
        if (Game.currentRoom == None):
            if ("stash" in self.inventory):
                Game.img = PhotoImage(file="win.png")
            else:
                if("revolver" in self.inventory):
                    Game.img = PhotoImage(file="shootout.png")
                else:
                    Game.img = PhotoImage(file="lose.png")
            Game.image.config(image=Game.img)
            Game.image.image = Game.img
        else:
            # otherwise grab the image for the current room
            Game.img = PhotoImage(file=Game.currentRoom.image)
            # display the image on the left of the GUI
            Game.image.config(image=Game.img)
            Game.image.image = Game.img


    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
        # enable the text widget, clear it, set it, and disabled it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom == None):
            if ("stash" in self.inventory):
                Game.text.insert(END, "You have left town on your horse, The stash resting on the back of the horse gleaming off the setting sun, You return to camp a hero!")
            else:
                if("revolver" in self.inventory):
                    Game.text.insert(END, "You have left town on your horse leaving behind the stash. On your return to the camp your fellow outlaws attempt to shoot you and a intense shootout ocurrs where you come out on top. You escape on your horse with all the gold in the camp")
                else:
                    Game.text.insert(END, "You have left town on your horse leaving behind the stash. You are shot when returnign to camp empty handed.")          
      
        else:
            # otherwise, display the appropriate status
            Game.text.insert(END, str(Game.currentRoom) + "\nYou are carrying: " + str(Game.inventory) + "\n\n" + status)
        Game.text.config(state=DISABLED)

    # play the game
    def play(self):
        # add the rooms to the game
        self.createRooms()
        # configure the GUI
        self.setupGUI()
        # set the current room
        self.setRoomImage()
        # set the current status
        self.setStatus("""The Old West is a place of almost infinite wealth surrounded by immense danger. You and your crew  just pulled off your biggest heist yet, robbing 4 high values trains all at the same time. After reconveining the law is hot on your trail and you flee to a nearby ghost town. BUT! as you approach the town a rival gang attacks sending you off your horse. While flying through the air you glimpse the stash of money fly off the horse as well and go into the town. Crashing into a building you hear your horse run off and the screams of gang members, lawmen, and your crew slowly drift off into the horizon FIND THE MONEY, GET OUT OF TOWN!!""")




    # processes the player's input
    def process(self, event):
        # grab the player's input from the input at the bottom of
        # the GUI
        action = Game.player_input.get()
        # set the user's input to lowercase to make it easier to
        # compare the verb and noun to known values
        action = action.lower()
        # set a default response
        response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"
        # exit the game if the player wants to leave (supports quit,
        # exit, and bye)

        if(action == "quit" or action == "exit" or action == "bye" or action == "sionara!" or action == "lets delta!"):
            exit(0)
        # if the player is dead if goes/went south from room 4

        if (Game.currentRoom == None):
            # clear the player's input
            Game.player_input.delete(0, END)
            return
        
        # split the user input into words (words are separated by
        # spaces) and store the words in a list
        words = action.split()
        # the game only understands two word inputs

        if (len(words) == 2):
            # isolate the verb and noun
            verb = words[0]
            noun = words[1]

            # the verb is: go
            if (verb == "go"):
                # set a default response
                response = "Invalid exit."
                # check for valid exits in the current room
                if (noun in Game.currentRoom.exits):
                    # if one is found, change the current room to
                    # the one that is associated with the
                    # specified exit
                    Game.currentRoom =\
                    Game.currentRoom.exits[noun]
                    # set the response (success)
                    response = "Room changed."
            # the verb is: look
            elif (verb == "look"):
                # set a default response
                response = "I don't see that item."
                # check for valid items in the current room
                if (noun in Game.currentRoom.items):
                # if one is found, set the response to the
                # item's description
                    response = Game.currentRoom.items[noun]
                        
            # the verb is: take
            elif (verb == "take"):
                # set a default response
                response = "I don't see that item."
                # check for valid grabbable items in the current
                # room
                for grabbable in Game.currentRoom.grabbables:
                    # a valid grabbable item is found
                    if (noun == grabbable):
                        # add the grabbable item to the player's
                        # inventory
                        Game.inventory.append(grabbable)
                        # remove the grabbable item from the
                        # room
                        Game.currentRoom.delGrabbable(grabbable)
                        # set the response (success)
                        response = "Item grabbed."
                        # no need to check any more grabbable
                        # items
                    break
                
        # display the response on the right of the GUI
        # display the room's image on the left of the GUI
        # clear the player's input
        self.setStatus(response)
        self.setRoomImage()
        Game.player_input.delete(0, END)

##########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600
# create the window
window = Tk()
window.title("Room Adventure")
# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()
# wait for the window to close
window.mainloop()
