class Games:
    # ? potentially change rounds to a class variable ?
    # each game has a title, brief description, 
    #total number of rounds and a farewell message
    def __init__(self, title, description, rounds, total_points = 0):
        self.title = title
        self.description = description
        self.rounds = rounds
        self.total_points = total_points

    # prints title, description
    def welcomeMessage(self):
        return 'Welcome to {}\n{}\n'.format(self.title,self.description)
    
    #prints farewell message
    def goodbyeMessage(self):
        return 'Thank you for playing {}\n'.format(self.title)

    def play(self):
        pass



#testing
game1 = Games('Title', 'Description','5')


print(game1.welcomeMessage())
print(game1.goodbyeMessage())




