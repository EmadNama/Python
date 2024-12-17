class Suitcase:
    def __init__(self, owner, size):
        self.owner = owner
        self.weight = size

    def __repr__(self):
        return f"Suitcase Information:\nOwner: {self.owner.name}\nWeight: {self.weight}"