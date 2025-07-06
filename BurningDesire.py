import pygame
import sys

# Initialize Pygame
pygame.init()

# Define screen dimensions
screen_width = 1000
screen_height = 750

# Define colors (RGB format)
white = (255, 255, 255)
black = (0, 0, 0)

# Define player character attributes
player_width = 30  # Reduced player size
player_height = 30  # Reduced player size
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height - 10
player_speed = 0.6  # 20% of the original speed
jump_height = 2  # 20% of the original jump height
jumping = False  # Flag to track jumping
jump_count = 10  # Jump countdown

# Define wall and platform attributes
wall_width = 20
wall_height = 200
platform_width = 200
platform_height = 20

# Create the screen in a windowed mode
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the window title
pygame.display.set_caption("Burning Desire Prototype")

# Create the player character
player = pygame.Surface((player_width, player_height))
player.fill(color='darkgrey')

# Create the walls and platform
wall1 = pygame.Surface((wall_width, wall_height))
wall1.fill(white)
wall1_x = 100
wall1_y = screen_height - wall_height - 50

wall2 = pygame.Surface((wall_width, wall_height))
wall2.fill(white)
wall2_x = screen_width - wall_width - 100
wall2_y = screen_height - wall_height - 50

platform = pygame.Surface((platform_width, platform_height))
platform.fill(white)
platform_x = (screen_width - platform_width) // 2
platform_y = screen_height - platform_height - 150

# Track the current screen mode (0 for windowed, 1 for full-screen)
screen_mode = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exit the loop when the window is closed
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                # Toggle between full-screen and windowed mode when F11 is pressed
                if screen_mode == 0:
                    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
                    screen_mode = 1
                else:
                    screen = pygame.display.set_mode((screen_width, screen_height))
                    screen_mode = 0
            elif event.key == pygame.K_RETURN:
                # Toggle full-screen mode when Enter is pressed (with Alt)
                if pygame.key.get_mods() & pygame.KMOD_ALT:
                    if screen_mode == 0:
                        screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
                        screen_mode = 1
                    else:
                        screen = pygame.display.set_mode((screen_width, screen_height))
                        screen_mode = 0

    # Check for collisions with walls and platform
    if player_x < wall1_x + wall_width and player_x + player_width > wall1_x:
        if player_y + player_height > wall1_y:
            # Player hit the left wall
            # Handle the collision by stopping the player's movement to the left
            player_x = wall1_x + wall_width

    if player_x < wall2_x + wall_width and player_x + player_width > wall2_x:
        if player_y + player_height > wall2_y:
            # Player hit the right wall
            # Handle the collision by stopping the player's movement to the right
            player_x = wall2_x - player_width

    if player_x < platform_x + platform_width and player_x + player_width > platform_x:
        if player_y + player_height > platform_y:
            # Player is on the platform
            # Reset the jump_count to allow jumping when on the platform
            jump_count = 10
            # Ensure the player stays on top of the platform
            player_y = platform_y - player_height

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Boundary checking to keep the player on the screen
    player_x = max(0, min(player_x, screen_width - player_width))

    # Jumping logic
    if not jumping:
        if keys[pygame.K_SPACE]:
            jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg * jump_height
            jump_count -= 1
        else:
            jumping = False
            jump_count = 10

    # Fill the screen with black
    screen.fill(black)
    # Fill the screen with black
    screen.fill(black)

    # Draw the player character
    screen.blit(player, (player_x, player_y))

    # Draw the walls and platform
    screen.blit(wall1, (wall1_x, wall1_y))
    screen.blit(wall2, (wall2_x, wall2_y))
    screen.blit(platform, (platform_x, platform_y))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
