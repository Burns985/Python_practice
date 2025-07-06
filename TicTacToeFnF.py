import numpy as np
import random
import pickle


# Function to print the Tic-Tac-Toe board
def print_board(board):
    """
    Print the Tic-Tac-Toe board.

    Parameters:
        board (numpy.ndarray): The game board.
    """
    print("---------------------------")
    for row in board:
        print('  |  '.join(row))
        print('-' * (4 * len(row) - 1))


# Function to convert the board into a string
def board_to_string(board):
    """
    Convert the board into a string.

    Parameters:
        board (numpy.ndarray): The game board.

    Returns:
        str: The board represented as a string.
    """
    return ''.join(board.flatten())


# Function to choose the next action
def choose_action(board, exploration_rate, Q):
    """
    Choose the next action.

    Parameters:
        board (numpy.ndarray): The game board.
        exploration_rate (float): The exploration rate for choosing random actions.
        Q (dict): Q-values for states.

    Returns:
        tuple: The chosen action coordinates.
    """
    state = board_to_string(board)

    if random.uniform(0, 1) < exploration_rate or state not in Q:
        empty_cells = np.argwhere(board == '-')
        action = tuple(random.choice(empty_cells))
    else:
        q_values = Q[state]
        empty_cells = np.argwhere(board == '-')
        win_actions = []
        for cell in empty_cells:
            next_state = board_next_state(cell, 'O', board)
            next_state_string = board_to_string(next_state)
            if next_state_string in Q and np.max(Q[next_state_string]) > 0:
                win_actions.append((cell, np.max(Q[next_state_string])))
        if win_actions:
            action = tuple(max(win_actions))
        else:
            empty_q_values = [q_values[cell[0], cell[1]] for cell in empty_cells]
            max_q_value = max(empty_q_values)
            max_q_indices = [i for i in range(len(empty_cells)) if empty_q_values[i] == max_q_value]
            max_q_index = random.choice(max_q_indices)
            action = tuple(empty_cells[max_q_index])

    return action


# Function to check if the game is over
def is_game_over(board):
    """
    Check if the game is over.

    Parameters:
        board (numpy.ndarray): The game board.

    Returns:
        tuple: Boolean indicating game over and the winner if any.
    """
    size = len(board)
    for i in range(size):
        if len(set(board[i])) == 1 and board[i][0] != '-':
            return True, board[i][0]
        if len(set(board[:, i])) == 1 and board[0][i] != '-':
            return True, board[0][i]
    if len(set(np.diag(board))) == 1 and board[0][0] != '-':
        return True, board[0][0]
    if len(set(np.diag(np.fliplr(board)))) == 1 and board[0][-1] != '-':
        return True, board[0][-1]
    if '-' not in board:
        return True, 'draw'
    return False, None


# Function to get the next state of the board after a player's move
def board_next_state(cell, player, board):
    """
    Get the next state of the board after a player's move.

    Parameters:
        cell (tuple): The cell coordinates for the move.
        player (str): The player making the move.
        board (numpy.ndarray): The game board.

    Returns:
        numpy.ndarray: The next state of the board.
    """
    next_state = board.copy()
    next_state[cell[0], cell[1]] = player
    return next_state


# Function to train the Q-learning algorithm
def train_q_learning(board_size, num_episodes):
    """
    Train the Q-learning algorithm.

    Parameters:
        board_size (int): The size of the game board.
        num_episodes (int): The number of episodes to train for.

    Returns:
        dict: The trained Q-values.
    """
    global Q
    exploration_rate = 0.99
    win = 0
    draw = 0

    for episode in range(num_episodes):
        if episode % 1000 == 0:
            print("Rounds {}".format(episode))
        board = np.full((board_size, board_size), '-')
        current_player = player1
        game_over = False

        while not game_over:
            action = choose_action(board, exploration_rate, Q)
            row, col = action
            board[row, col] = current_player

            game_over, winner = is_game_over(board)

            if game_over:
                if winner == player1 or player2:
                    giveReward(win, draw, board)

            else:
                if current_player == player1:
                    current_player = player2
                else:
                    current_player = player1

        exploration_rate *= 0.99

    print("win ratio=", win / 10000)
    print("draw ratio=", draw / 10000)

    return Q


# Function to feed reward to the player's Q-values
def feedReward(player, reward):
    """
    Feed reward to the player's Q-values.

    Parameters:
        player (Player): The player object.
        reward (float): The reward value.
    """
    for st in reversed(player.q_states):
        if player.states_value.get(st) is None:
            player.states_value[st] = 0
        player.Q[st] += player.lr * (player.decay_gamma * reward - player.Q[st])
        reward = player.Q[st]


# Function to assign rewards to the players based on game outcome
def giveReward(win, draw, board):
    """
    Assign rewards to the players based on game outcome.

    Parameters:
        win (int): Number of wins.
        draw (int): Number of draws.
        board (numpy.ndarray): The game board.

    Returns:
        tuple: Updated win and draw counts.
    """
    gameOver, winner = is_game_over(board)
    if winner is player1:
        feedReward(player1, 1)
        feedReward(player2, 0)
        win += 1
    elif winner is player2:
        feedReward(player1, 0)
        feedReward(player2, 1)
    else:
        feedReward(player1, 0.1)
        feedReward(player2, 0.5)
        draw += 1
    return win, draw

def savePolicy(self):
    fw = open('policy', 'wb')
    pickle.dump(self, fw)
    fw.close()

def loadPolicy(file):
    fr = open(file, 'rb')
    self = pickle.load(fr)
    fr.close()

# Function to play a game against the trained agent
def play_game(board_size, trained_Q):
    """
    Play a game against the trained agent.

    Parameters:
        board_size (int): The size of the game board.
        trained_Q (dict): The trained Q-values.
    """
    board = np.full((board_size, board_size), '-')
    current_player = player1
    game_over = False

    while not game_over:
        if current_player == 'X':
            print_board(board)
            row = int(input(f"Enter the row (0-{board_size - 1}): "))
            col = int(input(f"Enter the column (0-{board_size - 1}): "))
            action = (row, col)
        else:
            action = choose_action(board, 0, trained_Q)

        row, col = action
        board[row, col] = current_player

        game_over, winner = is_game_over(board)

        if game_over:
            print_board(board)
            if winner == 'X':
                print("Human player wins!")
            elif winner == 'O':
                print("Agent wins!")
            else:
                print("It's a draw!")
        else:
            if current_player == player1:
                current_player = player2
            else:
                current_player = player1


# Initializations
player1 = 'O'
player2 = 'X'
learning_rate = 0.1
discount_factor = 0.9
num_episodes = 300000
q_States = []
Q = {}

# User input for board size
board_size = eval(input("Enter board size"))

# Training the Q-learning algorithm
print(f"Training for {board_size}x{board_size} board...")
trained_Q = train_q_learning(board_size, num_episodes)
print("Training completed!")

# Save the trained policy
savePolicy(Q)

# Play multiple games against the trained agent
i = 0
while i <= 5:
    loadPolicy('policy')
    play_game(board_size, Q)
