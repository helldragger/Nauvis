class PlannedEvent():

    def __init__(self, date, name, id, occur, link):
        self.date = date
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