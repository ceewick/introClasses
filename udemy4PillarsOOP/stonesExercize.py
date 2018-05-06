'''
Write an object oriented program to create a precious stone.
Not more than 5 precious stones can be held in possession at a
given point of time. If there are more than 5 precious stones,
delete the first stone and store the new one.
'''

class PreciousStone():
    def __init__(self, listOfStones):
        self.listOfStones = listOfStones
    
    def printStones(self):
        print(self.listOfStones)
    
    def addStones(self, stoneAdded):
        if len(self.listOfStones) == 5:
            self.listOfStones.remove(self.listOfStones[0])
            self.listOfStones.append(stoneAdded)
        else:
            self.listOfStones.append(stoneAdded)
        
stones = PreciousStone(['rew','bra','green','diamond','crystal'])
stones.printStones()
stones.addStones('Ruby')
stones.printStones()
stones.addStones('granite')
stones.printStones()