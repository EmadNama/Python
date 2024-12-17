class WorkDay:
    def __init__(self, date, description):
        self.date = date
        self.description = description

    def __repr__(self):
        return f"WorkDay Information:\nDate: {self.date}\nDescription: {self.description}"
