########################################################################
# COMPONENT:
#    MESSAGES
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of a collection of messages
########################################################################

import control, message

##################################################
# MESSAGES
# The collection of high-tech messages
##################################################
class Messages:

    ##################################################
    # MESSAGES CONSTRUCTOR
    # Read a file to fill the messages
    ##################################################
    def __init__(self, filename):
        self._messages = []
        self._read_messages(filename)

    ##################################################
    # MESSAGES :: DISPLAY
    # Display the list of messages
    ################################################## 
    def display(self, subjectControl):
        for m in self._messages:
            if control.securityConditionRead(m._control_level,subjectControl):
                m.display_properties()

    ##################################################
    # MESSAGES :: SHOW
    # Show a single message
    ################################################## 
    def show(self, id, subjectControl):
        for m in self._messages:
            if m.get_id() == id and control.securityConditionRead(m._control_level,subjectControl):
                m.display_text()
                return True
        return False

    ##################################################
    # MESSAGES :: UPDATE
    # Update a single message
    ################################################## 
    def update(self, id, text, subjectControl):
        for m in self._messages:
            if m.get_id() == id and control.securityConditionWrite(m._control_level,subjectControl):
                m.update_text(text)

    ##################################################
    # MESSAGES :: REMOVE
    # Remove a single message
    ################################################## 
    def remove(self, id, subjectControl):
        for m in self._messages:
            if m.get_id() == id and control.securityConditionWrite(m._control_level,subjectControl):
                m.clear()

    ##################################################
    # MESSAGES :: ADD
    # Add a new message
    ################################################## 
    def add(self, text, author, date, control_level):
        m = message.Message(text, author, date, control_level)
        self._messages.append(m)

    ##################################################
    # MESSAGES :: READ MESSAGES
    # Read messages from a file
    ################################################## 
    def _read_messages(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    text_control, author, date, text = line.split('|')
                    text_control = control.Control[text_control.upper()]
                    self.add(text.rstrip('\r\n'), author, date, text_control)

        except FileNotFoundError:
            print(f"ERROR! Unable to open file \"{filename}\"")
            return
