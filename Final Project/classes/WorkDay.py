class WorkDay:
    def __init__(self, day, month, work_hours):
        self.day = day
        self.month = month
        self.work_hours = work_hours

    def __repr__(self):
        return f"WorkDay Information:\nDate: {self.date}\nDescription: {self.description}"
