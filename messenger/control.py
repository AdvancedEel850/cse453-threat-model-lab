

class Control:
    def __init__(self):
        self._control = ["Public", "Confidential", "Privileged", "Secret"]

    def get_control(self):
        return self._control
    
    ##################################################
    # MESSAGES :: ACCESS
    # Determine if a user has access to a message.
    ##################################################
    def read_access(self, control, message):
        return self._control.index(message) <= self._control.index(control)
    
    def write_access(self, control, message):
        return self._control.index(message) >= self._control.index(control)
