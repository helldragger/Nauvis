class PlannedEvent():

    def __init__(self, all_day, date, estimated_length, reminders, name, id,
                 occur, link):
        self.all_day = all_day
        self.date = date
        self.estimated_length = estimated_length
        self.reminders = reminders
        self.name = name
        self.id = id
        self.occur = occur
        self.link = link

    def __str__(self):
        return "**"+\
               self.date+\
               "\t - "+\
               self.name+\
               "**#"+\
               self.occur+\
               " \t 🔗 "+\
               self.link
