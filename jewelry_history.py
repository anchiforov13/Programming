class JewelryHistory:
    MAX_LENGTH = 100
 
    def __init__(self, jewelry):
        self.jewelry = jewelry
        self.history = []
 
    def save(self):
        snapshot = self.jewelry.save()
        self.history.append(snapshot)
        if len(self.history) > JewelryHistory.MAX_LENGTH:
            self.history.pop(0)

    def undo(self):
        if not self.history:
            print("This item has no history.")
        else:
            snapshot = self.history.pop()
            self.jewelry.restore(snapshot)
 
    def redo(self, ind):
        if not self.history:
            print("This item has no history.")
        elif ind > len(self.history):
            print("Version not found.")
        else:
            snapshot = self.history.pop(-1*ind)
            self.jewelry.restore(snapshot)