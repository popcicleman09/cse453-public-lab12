########################################################################
# COMPONENT:
#    INTERACT
# Author:
#    Br. Helfrich, Kyle Mueller, Jack Deller
# Summary: 
#    This class allows one user to interact with the system
########################################################################

import messages, control

###############################################################
# USER
# User has a name and a password
###############################################################
class User:
    def __init__(self, name, password, control_level):
        self.name = name
        self.password = password
        self.control_level = control_level

userlist = [
   [ "AdmiralAbe",     "password", control.Control.SECRET ],  
   [ "CaptainCharlie", "password", control.Control.PRIVILEGED ], 
   [ "SeamanSam",      "password", control.Control.CONFIDENTIAL ],
   [ "SeamanSue",      "password", control.Control.CONFIDENTIAL ],
   [ "SeamanSly",      "password", control.Control.CONFIDENTIAL ]
]

###############################################################
# USERS
# All the users currently in the system
###############################################################
users = [*map(lambda u: User(*u), userlist)]

ID_INVALID = -1

######################################################
# INTERACT
# One user interacting with the system
######################################################
class Interact:

    ##################################################
    # INTERACT CONSTRUCTOR
    # Authenticate the user and get him/her all set up
    ##################################################
    def __init__(self, username, password, messages):
        self._authenticate(username, password)
        self._username = username
        self._p_messages = messages

    ##################################################
    # INTERACT :: SHOW
    # Show a single message
    ##################################################
    def show(self):
        id_ = self._prompt_for_id("display")
        if not self._p_messages.show(id_,self._control_level):
            print(f"ERROR! Message ID \'{id_}\' does not exist")
        print()

    ##################################################
    # INTERACT :: DISPLAY
    # Display the set of messages
    ################################################## 
    def display(self):
        print("Messages:")
        self._p_messages.display(self._control_level)
        print()

    ##################################################
    # INTERACT :: ADD
    # Add a single message
    ################################################## 
    def add(self):
        self._p_messages.add(self._prompt_for_line("message"),
                             self._username,
                             self._prompt_for_line("date"),
                             self._control_level)

    ##################################################
    # INTERACT :: UPDATE
    # Update a single message
    ################################################## 
    def update(self):
        id_ = self._prompt_for_id("update")
        if not self._p_messages.show(id_,self._control_level):
            print(f"ERROR! Message ID \'{id_}\' does not exist\n")
            return
        self._p_messages.update(id_, self._prompt_for_line("message"),self._control_level)
        print()
            
    ##################################################
    # INTERACT :: REMOVE
    # Remove one message from the list
    ################################################## 
    def remove(self):
        self._p_messages.remove(self._prompt_for_id("delete"),self._control_level)

    ##################################################
    # INTERACT :: PROMPT FOR LINE
    # Prompt for a line of input
    ################################################## 
    def _prompt_for_line(self, verb):
        return input(f"Please provide a {verb}: ")

    ##################################################
    # INTERACT :: PROMPT FOR ID
    # Prompt for a message ID
    ################################################## 
    def _prompt_for_id(self, verb):
        return int(input(f"Select the message ID to {verb}: "))

    ##################################################
    # INTERACT :: AUTHENTICATE
    # Authenticate the user: find their control level
    ################################################## 
    def _authenticate(self, username, password):
        id_ = self._id_from_user(username)
        if ID_INVALID != id_ and password == users[id_].password:
            self._control_level = users[id_].control_level  # actual user's clearance
            return True
        else:
            self._control_level = control.Control.PUBLIC  # fallback default
            return False

    ##################################################
    # INTERACT :: ID FROM USER
    # Find the ID of a given user
    ################################################## 
    def _id_from_user(self, username):
        for id_user in range(len(users)):
            if username == users[id_user].name:
                return id_user
        return ID_INVALID

#####################################################
# INTERACT :: DISPLAY USERS
# Display the set of users in the system
#####################################################
def display_users():
    for user in users:
        print(f"\t{user.name}")
