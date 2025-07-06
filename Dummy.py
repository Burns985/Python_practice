import pygame
import random
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doodle Jump")

# Player settings
player_x = WIDTH // 2
player_y = HEIGHT - 100  # Initialize player_y here
player_jump = 10
player_jump_height = 100
player_is_jumping = False

# Platform settings
platform_width = 80
platform_height = 10
platform_x = random.randint(0, WIDTH - platform_width)
platform_y = HEIGHT - 20

# Genetic Algorithm Parameters
population_size = 20
mutation_rate = 0.1

def initialize_population():
    population = []
    for _ in range(population_size):
        genome = {
            'weights': np.random.rand(2),
            'score': 0
        }
        population.append(genome)
    return population

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1['weights']))
    child = {
        'weights': np.concatenate((parent1['weights'][:crossover_point], parent2['weights'][crossover_point:])),
        'score': 0
    }
    return child

def mutate(child):
    for i in range(len(child['weights'])):
        if random.random() < mutation_rate:
            child['weights'][i] = np.random.rand()
    return child

def run_game(agent):
    player_x = WIDTH // 2  # Reset player_x
    player_y = HEIGHT - 100  # Reset player_y

    player_jump = 10
    player_is_jumping = False

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Your genetic algorithm code here to make decisions for the agent
        agent_decision = agent['weights'].dot(np.array([platform_x, player_y]))

        if agent_decision > 0:
            player_x += 5
        else:
            player_x -= 5

        # Jumping logic
        if player_is_jumping:
            player_y -= player_jump
            player_jump -= 1

            if player_jump < -player_jump_height:
                player_jump = 10
                player_is_jumping = False

        # Gravity
        if not player_is_jumping:
            player_y += 5

        # Check if the player has landed on the platform
        if player_y > platform_y:
            player_y = platform_y
            if platform_x - platform_width // 2 < player_x < platform_x + platform_width // 2:
                player_is_jumping = True

        # Draw everything
        screen.fill(WHITE)
        pygame.draw.rect(screen, (0, 0, 255), (platform_x, platform_y, platform_width, platform_height))
        pygame.draw.circle(screen, (255, 0, 0), (player_x, player_y), 20)  # Red circle as the player

        pygame.display.update()

    return player_x

# Main genetic algorithm loop
generations = 10
population = initialize_population()

for generation in range(generations):
    for agent in population:
        agent['score'] = run_game(agent)

    # Sort population by score
    population.sort(key=lambda x: x['score'], reverse=True)

    # Select the top-performing agents to be parents
    parents = population[:population_size // 2]

    # Create a new population through crossover and mutation
    new_population = []
    while len(new_population) < population_size:
        parent1, parent2 = random.sample(parents, 2)
        child = crossover(parent1, parent2)
        child = mutate(child)
        new_population.append(child)

    population = new_population

# Get the best agent
best_agent = max(population, key=lambda x: x['score'])
print(f"Best agent's score: {best_agent['score']}")

# Quit the game
pygame.quit()
