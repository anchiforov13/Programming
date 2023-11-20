import copy

class SnapShot:
    def __init__(self, state):
        self.state = copy.deepcopy(state)
 
    def get_state(self):
        return self.state