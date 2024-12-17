class Suitcase:
    def __init__(self, owner, weight):
        self.owner = owner
        self.weight = weight

    def __repr__(self):
        return f"Suitcase Information:\nOwner: {self.owner.name}\nWeight: {self.weight}"