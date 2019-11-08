from world import createWorld
from player import Player

def refreshScreen(world, player):
    currentTown = player.currentTown
    print(f"Current town: {currentTown.name}")
    print(f"Current date: {world.date}")
    print("")
    print("Next town:")
    for neighbor in currentTown.neighbors.keys():
        print(f"\t{neighbor}")


def main():
    world = createWorld()
    player = Player(world.getTown("Yoitsu"))
    while True:
        refreshScreen(world, player)
        selection = input(">")
        if selection in player.currentTown.neighbors.keys():
            newTown = world.getTown(selection)
            daysToTown = player.currentTown.neighbors[newTown.name]
            player.currentTown = newTown
            world.date += daysToTown
        else:
            print("Invalid town name")
        

if __name__ == '__main__':
    main()
