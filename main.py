from world import createWorld

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
