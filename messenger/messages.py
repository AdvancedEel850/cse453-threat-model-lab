########################################################################
# COMPONENT:
#    MESSAGES
# Author:
#    Br. Helfrich, Kyle Mueller, Br. Phillips
# Summary: 
#    This class stores the notion of a collection of messages
########################################################################

import message
import control

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
        self._control_object = control.Control()

    ##################################################
    # MESSAGES :: DISPLAY
    # Display the list of messages
    ################################################## 
    def display(self, control):
        for m in self._messages:
            if self._control_object.read_access(control, m): 
                m.display_properties()

    ##################################################
    # MESSAGES :: SHOW
    # Show a single message
    ################################################## 
    def show(self, id, control, exe):
        for m in self._messages:
            if m.get_id() == id and exe(control, m):
                m.display_text()
                return True
        return False


    ##################################################
    # MESSAGES :: UPDATE
    # Update a single message
    ################################################## 
    def update(self, id, text, control):
        for m in self._messages:
            if m.get_id() == id and self._control_object.write_access(control, m):
                m.update_text(text)
            elif m.get_id() == id and not self._control_object.write_access(control, m):
                print("Not Accessible.")

    ##################################################
    # MESSAGES :: REMOVE
    # Remove a single message
    ################################################## 
    def remove(self, id, control):
        for m in self._messages:
            if m.get_id() == id and self._control_object.write_access(control, m):
                m.clear()

    ##################################################
    # MESSAGES :: ADD
    # Add a new message
    ################################################## 
    def add(self, text, author, date, control):
        m = message.Message(text, author, date, control)
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
                    self.add(text.rstrip('\r\n'), author, date, text_control)

        except FileNotFoundError:
            print(f"ERROR! Unable to open file \"{filename}\"")
            return
