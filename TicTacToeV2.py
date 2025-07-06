while True:
    def printGrid(grid):
        i = 0
        for j in range(0, 3):
            if j != 0:
                print("---|---|---")
            print("", grid[1 + i], "|", grid[2 + i], "|", grid[3 + i])
            i += 3


    def input_taker():
        a = input("Please enter Co-ordinates to take: ")
        while True:
            if a.isdigit() and 0 < int(a) < 10:
                break
            else:
                print("Error! Please consider co-ordinates as values from 1-9")
                a = input("Please enter Co-ordinates to take: ")
        return a


    def turn(grid, curr, cor):
        if grid[int(cor)] == " ":
            grid[int(cor)] = curr
            return False
        else:
            print("Slot taken.")
            return True


    def won(grid):
        if grid[1] == grid[2] == grid[3] != " " \
                or grid[4] == grid[5] == grid[6] != " " \
                or grid[7] == grid[8] == grid[9] != " " \
                or grid[1] == grid[4] == grid[7] != " " \
                or grid[2] == grid[5] == grid[8] != " " \
                or grid[3] == grid[6] == grid[9] != " " \
                or grid[1] == grid[5] == grid[9] != " " \
                or grid[3] == grid[5] == grid[7] != " ":
            return True


    def play():
        player1 = "o"
        player2 = "x"
        curr = "o"
        grid_dict = {1: " ",
                     2: " ",
                     3: " ",
                     4: " ",
                     5: " ",
                     6: " ",
                     7: " ",
                     8: " ",
                     9: " ",
                     }
        print("Welcome\nPlayer1: o\tPlayer2: x")
        turns = 0

        while True:
            print(grid_dict)
            print("\nTurn", turns + 1, ":")
            printGrid(grid_dict)
            flag = True
            while flag:
                if curr == "o":
                    print("\n\nPlayer 1:")
                else:
                    print("\n\nPlayer 2:")
                co_ordinate = input_taker()
                flag = turn(grid_dict, curr, co_ordinate)
            if won(grid_dict):
                print("Player", curr, "wins!")
                printGrid(grid_dict)
                break
            turns += 1
            if turns == 9:
                print("It's a tie!")
                printGrid(grid_dict)
                break
            curr = player2 if curr == player1 else player1

    play()
    choice = input("Do you wish to play again Y/N? ")
    if choice == "N":
        break
