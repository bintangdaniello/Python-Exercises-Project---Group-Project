### Grid Based Exploration Game ###
def main():
    started = False

    # 3x3 Grid of Rooms
    rooms = [["Forest", "Riverbank", "Cave Entrance"],
             ["Village", "Town Square", "Marketplace"],
             ["Beach", "Cliffside", "Abandoned Hut"]]

    # Player Start Position (1, 1)
    px = 1
    py = 1

    # Title + Instructions
    print("EXPLORATION GAME")
    print("Type north, south, east, west to move. Type Quit to Exit")

    # Starts the game
    begin = input("TYPE START TO BEGIN: ").lower()
    if begin == "start":
        started = True

    # Game Loop
    while started == True:
        print("\nYou are currently at:", rooms[py][px]) # Gives current player location
        move = input("Move (north/south/east/west) or quit: ").lower() # Movement Input

        # Uses movement input
        if move == "north":
            if py > 0:
                py -= 1
            else:
                print("I seem to have hit a wall!")

        elif move == "south":
            if py < 2:
                py += 1
            else:
                print("I seem to have hit a wall!")

        elif move == "east":
            if px < 2:
                px += 1
            else:
                print("I seem to have hit a wall!")

        elif move == "west":
            if px > 0:
                px -= 1
            else:
                print("I seem to have hit a wall!")

        elif move == "quit":
            print("Thanks for playing!")
            started = False

        else:
            print("Invalid Input")

main()