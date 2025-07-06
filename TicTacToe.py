while True:
    def updated_board(grid):
        for g in grid:
            if g != [" ", 1, 2, 3]:
                print()
            for i in g:
                print(i, end=" ")


    def turn(grid, curr, cor):
        x = list(cor)
        flag = False
        for g in grid:
            if x[0] in g:
                if g[int(x[1])] == ".":
                    g[int(x[1])] = curr
                else:
                    print("Slot taken")
                    flag = True
                break
        return flag


    def won(grid):
        for i in range(1, 4):
            if grid[i][1] == grid[i][2] == grid[i][3] != ".":
                return True
        for i in range(1, 4):
            if grid[1][i] == grid[2][i] == grid[3][i] != ".":
                return True
        if grid[1][3] == grid[2][2] == grid[3][1] != "." or grid[1][1] == grid[2][2] == grid[3][3] != ".":
            return True


    def input_taker():
        a =  input("Please enter Co-ordinates to take: ")
        while True:
            if len(a) == 2 and a[0].isupper() and a[0] in ["A", "B", "C"] and a[1].isdigit() and a[1] in ["1", "2", "3"]:
                break
            else:
                print("Please write values provided on grid borders i.e. A1")
                a = input("Please enter Co-ordinates to take: ")
        return a


    def play():
        player1 = "o"
        player2 = "x"
        curr = "o"
        grid = [[" ", 1, 2, 3], ["A", ".", ".", "."], ["B", ".", ".", "."], ["C", ".", ".", "."]]

        print("Welcome\nPlayer1: o\tPlayer2: x")
        turns = 0

        while True:
            print("\nTurn", turns + 1, ":")
            updated_board(grid)
            flag = True
            while flag:
                if curr == "o":
                    print("\n\nPlayer 1:")
                else:
                    print("\n\nPlayer 2:")
                co_ordinate = input_taker()
                flag = turn(grid, curr, co_ordinate)
            if won(grid):
                print("Player", curr, "wins!")
                updated_board(grid)
                break
            turns += 1
            if turns == 9:
                print("It's a tie!")
                updated_board(grid)
                break
            curr = player2 if curr == player1 else player1


    play()
    choice = input("Do you wish to play again Y/N? ")
    if choice == "N":
        break
