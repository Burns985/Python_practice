import numpy as np
import random
import pickle




def print_board(board):
    # player1: O  p2: X
    for i in range(0, board_size):
        print('-------------')
        out = '| '
        for j in range(0, board_size):
            if board[i, j] == 1:
                symbol = 'o'
            if board[i, j] == -1:
                symbol = 'x'
            if board[i, j] == 0:
                symbol = ' '
            out += symbol + ' | '
        print(out)
    print('-------------')
# def print_board(board):
#     print("---------------------------")
#     for row in board:
#         print('  |  '.join(row))
#         print(' ' * (4 * len(row) - 1))

def board_to_string(board):
    boardValue = str(board.reshape(board_size * board_size))
    return boardValue

def emptyCells(board):
    cells = []
    for i in range(board_size):
        for j in range(board_size):
            if board[i, j] == 0:
                cells.append((i, j))  # need to be tuple
    return cells
def choose_action(board, exploration_rate, Q,player,empty_cells):
    state = board_to_string(board)

    if np.random.uniform(0, 1) < exploration_rate:
        action = empty_cells[np.random.choice(len(empty_cells))]
    else:
        # q_values = Q[state]
        # empty_cells = np.argwhere(board == 0)
        maxValue=-999

        # Prioritize actions leading to win states
        win_actions = []
        for cell in empty_cells:
            # next_state = board.copy()
            # next_state[cell] = player
            # next_state_string = board_to_string(next_state)
            next_state = board_next_state(cell, player, board)
            next_state_string = board_to_string(next_state)
            value=0 if Q.get(next_state_string) is None else Q.get(next_state_string)
            if value >= maxValue:
                maxValue = value

                # win_actions.append(cell)
                action=cell

        # if win_actions:
        #     action = tuple(random.choice(win_actions))
        #     else:
        #         empty_q_values = [q_values[cell[0], cell[1]] for cell in empty_cells]
        #         max_q_value = max(empty_q_values)
        #         max_q_indices = [i for i in range(len(empty_cells)) if empty_q_values[i] == max_q_value]
        #         max_q_index = random.choice(max_q_indices)
        #         action = tuple(empty_cells[max_q_index])

    return action


def is_game_over(board):
    size = len(board)

    # Check rows and columns
    for i in range(size):
        if len(set(board[i])) == 1 and board[i][0] != 0:
            return True, board[i][0]
        if len(set(board[:, i])) == 1 and board[0][i] != 0:
            return True, board[0][i]

    # Check diagonals
    if len(set(np.diag(board))) == 1 and board[0][0] != 0:
        return True, board[0][0]
    if len(set(np.diag(np.fliplr(board)))) == 1 and board[0][-1] != 0:
        return True, board[0][-1]

    # Check if the board is full
    if 0 not in board:
        return True, 'draw'

    return False, None

def board_next_state(cell, player, board):
    next_state = board.copy()
    next_state[cell] = player
    return next_state

# def update_q_table(state, action, next_state, reward,Q):
#     q_values = Q.get(state, np.zeros((board_size, board_size)))
#
#     next_q_values = Q.get(board_to_string(next_state), np.zeros((board_size, board_size)))
#     max_next_q_value = np.max(next_q_values)
#
#     q_values[action[0], action[1]] += learning_rate * (reward + discount_factor * max_next_q_value - q_values[action[0], action[1]])
#
#     Q[state] = q_values

def feedReward(Q,reward,q_states):
    for st in reversed(q_states):
        if Q.get(st) is None:
            Q[st] = 0
        Q[st] += learning_rate * (discount_factor * reward - Q[st])
        reward = Q[st]

# Main Q-learning algorithm
def train_q_learning(board_size, num_episodes):
    global Qplayer1,Qplayer2


    exploration_rate = 0.99
    win=0
    draw=0
    lose=0

    for episode in range(num_episodes):
        print("Round",episode)
        if episode % 100 == 0:
            print("Rounds {}".format(episode))
        board = np.full((board_size, board_size), 0)
        current_player = player1
        empty_cells=emptyCells(board)
        game_over = False


        while not game_over:
            if current_player == player1:
                action = choose_action(board, exploration_rate, Qplayer1,player1,empty_cells)
                row, col = action
                board[row, col] = current_player
                current_player = player2

            else :
                action = choose_action(board, exploration_rate, Qplayer2,player2,empty_cells)
                row, col = action
                board[row, col] = current_player
                current_player = player1

            # row, col = action
            # board[row, col] = current_player
            #
            # if current_player == player1:
            #     current_player = player2
            # else:
            #     current_player = player1

            game_over, winner = is_game_over(board)

            if game_over:
                if winner == player1:
                    giveReward(board)
                    win +=1
                    print_board(board)
                elif winner == player2:
                    giveReward(board)
                    lose +=1
                else:
                    draw +=1

            # if not game_over:
            #     if current_player == player1:
            #         next_state = board_next_state(action, current_player, board)
            #         update_q_table(board_to_string(board), action, next_state, 0,Qplayer1)
            #
            #     else:
            #         next_state = board_next_state(action, current_player, board)
            #         update_q_table(board_to_string(board), action, next_state, 0,Qplayer2)





        exploration_rate *= 0.99

    print("win ratio=",win)
    print("draw ratio=",draw)

    return Qplayer1,Qplayer2




def giveReward(board):

    gameOver, winner = is_game_over(board)
    # backpropagate reward
    if winner is player1:
        feedReward(Qplayer1,1,q_states1)
        feedReward(Qplayer2, 0,q_states2)

    elif winner is player2:
        feedReward(Qplayer1,0,q_states1)
        feedReward(Qplayer2, 1,q_states2)
    else:
        feedReward(Qplayer1,0.1,q_states1)
        feedReward(Qplayer2, 0.5,q_states2)


def savePolicy(self):
    fw = open('policy', 'wb')
    pickle.dump(self, fw)
    fw.close()

def loadPolicy(file):
    fr = open(file, 'rb')
    self = pickle.load(fr)
    fr.close()

# Play against the trained agent
def play_game(board_size,trained_Q):
    board = np.full((board_size, board_size), 0)
    empty_cells=emptyCells(board)
    current_player = player1
    game_over = False

    while not game_over:
        if current_player == player2:
            print_board(board)
            row = int(input(f"Enter the row (0-{board_size - 1}): "))
            col = int(input(f"Enter the column (0-{board_size - 1}): "))
            action = (row, col)
        else:
            action = choose_action(board, 0, trained_Q,player1,empty_cells)

        row, col = action
        board[row, col] = current_player

        game_over, winner = is_game_over(board)

        if game_over:
            print_board(board)
            if winner == player2:
                print("Human player wins!")
            elif winner == player1:
                print("Agent wins!")
            else:
                print("It's a draw!")
        else:
            if current_player == player1:
                current_player = player2
            else:
                current_player = player1
# Main

player1= 1   #O
player2= -1  #X
learning_rate = 0.2
discount_factor = 0.9
num_episodes = 10000
q_states1=[]
q_states2=[]

Qplayer1 = {}
Qplayer2={}





# for board_size in board_sizes:
board_size = eval(input("Enter board size"))

print(f"Training for {board_size}x{board_size} board...")
trained_Q = train_q_learning(board_size, num_episodes)
print("Training completed!")
savePolicy(Qplayer1)

loadPolicy('policy')
play_game(board_size, Qplayer1)

loadPolicy('policy')
play_game(board_size, Qplayer1)

loadPolicy('policy')
play_game(board_size, Qplayer1)

loadPolicy('policy')
play_game(board_size, Qplayer1)


loadPolicy('policy')
play_game(board_size, Qplayer1)