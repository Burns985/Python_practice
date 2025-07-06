import tkinter as tk
import random

# Set up the game window
window = tk.Tk()
window.title("Snake Game")

# Set up the game canvas
canvas_width = 400
canvas_height = 400
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="black")
canvas.pack()


# Define the Snake class
class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]  # Initial snake body
        self.direction = "Right"  # Initial direction

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == "Up":
            new_head = (head_x, head_y - 10)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 10)
        elif self.direction == "Left":
            new_head = (head_x - 10, head_y)
        elif self.direction == "Right":
            new_head = (head_x + 10, head_y)
        self.body.insert(0, new_head)
        self.body.pop()

    def change_direction(self, new_direction):
        if new_direction == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif new_direction == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif new_direction == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif new_direction == "Right" and self.direction != "Left":
            self.direction = "Right"

    def draw(self):
        canvas.delete("snake")
        for x, y in self.body:
            canvas.create_rectangle(
                x, y, x + 10, y + 10, fill="blue", outline="green", tags="snake"
            )

    def check_collision(self):
        head = self.body[0]
        if (
                head in self.body[1:]
                or head[0] < 0
                or head[0] >= canvas_width
                or head[1] < 0
                or head[1] >= canvas_height
        ):
            return True
        return False


# Define the Food class
class Food:
    def __init__(self):
        self.position = self.generate_food_position

    @property
    def generate_food_position(self):
        x = random.randint(0, (canvas_width - 10) // 10) * 10
        y = random.randint(0, (canvas_height - 10) // 10) * 10
        return x, y

    def draw(self):
        x, y = self.position
        canvas.create_oval(
            x,
            y,
            x + 10,
            y + 10,
            fill="green",
            outline="green",
            tags="food"
        )

    def check_collision(self, snake):
        if snake.body[0] == self.position:
            snake.body.append((0, 0))  # Extend the snake body
            canvas.delete("food")  # Remove the food from the canvas
            self.position = self.generate_food_position


# Initialize the snake and food
snake = Snake()
food = Food()


# Define key bindings
def handle_key(event):
    if event.keysym == "Up":
        snake.change_direction("Up")
    elif event.keysym == "Down":
        snake.change_direction("Down")
    elif event.keysym == "Left":
        snake.change_direction("Left")
    elif event.keysym == "Right":
        snake.change_direction("Right")


window.bind("<KeyPress>", handle_key)


# Define the restart function
def restart_game():
    canvas.delete("snake")
    canvas.delete("food")
    canvas.delete("gameover")  # Remove the "Game Over" text from the canvas
    snake.body = [(100, 100), (90, 100), (80, 100)]
    snake.direction = "Right"
    food.position = food.generate_food_position
    game_loop()


# Create a restart button
restart_button = tk.Button(window, text="Restart", command=restart_game)
restart_button.pack(anchor="n")  # Place the restart button in the top


# Game loop
def game_loop():
    if snake.check_collision():
        canvas.create_text(
            canvas_width // 2,
            canvas_height // 2,
            text="Game Over",
            fill="white",
            font=("Arial", 24),
            tags="gameover"
        )
        return

    snake.move()
    snake.draw()
    food.draw()
    food.check_collision(snake)

    window.after(100, game_loop)  # Run the game loop again after 100 milliseconds


# Start the game loop
game_loop()

window.mainloop()
