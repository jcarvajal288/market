class Town:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def addNeighbor(self, neighbor, distance):
        self.neighbors[neighbor] = distance


class World:
    def __init__(self):
        self.towns = {}

    def addTown(self, name):
        self.towns[name] = Town(name)

    def addRoad(self, startTown, endTown, distance):
        if startTown not in self.towns:
            self.addTown(startTown)
        if endTown not in self.towns:
            self.addTown(endTown)
        self.towns[startTown].addNeighbor(endTown, distance)
        self.towns[endTown].addNeighbor(startTown, distance)

    def getTown(self, name):
        return self.towns[name]


def createWorld():
    world = World()
    world.addTown("Yoitsu")
    world.addTown("Parovo")
    world.addTown("Conovon")

    world.addRoad("Yoitsu", "Parovo", 5)
    world.addRoad("Yoitsu", "Conovon", 9)
    world.addRoad("Parovo", "Conovon", 7)
    return world

def refreshScreen(currentTown):
    print(f"Current town: {currentTown.name}")
    print("")
    print("Next town:")
    for neighbor in currentTown.neighbors.keys():
        print(f"\t{neighbor}")


def main():
    world = createWorld()
    currentTown = world.getTown("Yoitsu")
    while True:
        refreshScreen(currentTown)
        selection = input(">")
        if selection in currentTown.neighbors.keys():
            currentTown = world.getTown(selection)
        else:
            print("Invalid town name")
        

if __name__ == '__main__':
    main()

