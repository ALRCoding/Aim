import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Aim Trainer")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the game clock
clock = pygame.time.Clock()

# Set up the target
target_radius = 20
target_x = random.randint(target_radius, width - target_radius)
target_y = random.randint(target_radius, height - target_radius)

# Set up the score
score = 0
font = pygame.font.Font(None, 36)

# Set up the game states
START = 0
GAME = 1
END = 2
game_state = START

# Set up the clock
clock_font = pygame.font.Font(None, 48)
clock_time = 90
clock_text = clock_font.render("Time: " + str(clock_time), True, RED)
clock_rect = clock_text.get_rect(center=(width // 2, 50))

# Game loop
running = True
while running:
    display.fill(WHITE)

    if game_state == START:
        start_text = font.render("Click to Start", True, RED)
        start_rect = start_text.get_rect(center=(width // 2, height // 2))
        display.blit(start_text, start_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game_state = GAME

    elif game_state == GAME:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                distance = ((mouse_x - target_x) ** 2 + (mouse_y - target_y) ** 2) ** 0.5
                if distance <= target_radius:
                    score += 1
                    target_x = random.randint(target_radius, width - target_radius)
                    target_y = random.randint(target_radius, height - target_radius)

        # Draw the target
        pygame.draw.circle(display, RED, (target_x, target_y), target_radius)

        # Display the score
        score_text = font.render("Score: " + str(score), True, RED)
        display.blit(score_text, [10, 10])

        # Update the clock
        clock_time -= 1 / 60
        clock_text = clock_font.render("Time: " + str(int(clock_time)), True, RED)
        display.blit(clock_text, clock_rect)
        if clock_time <= 0:
            game_state = END

    elif game_state == END:
        end_text = font.render("Game Over", True, RED)
        end_rect = end_text.get_rect(center=(width // 2, height // 2))
        display.blit(end_text, end_rect)
        score_text = font.render("Score: " + str(score), True, RED)
        score_rect = score_text.get_rect(center=(width // 2, height // 2 + 50))
        display.blit(score_text, score_rect)
        restart_text = font.render("Press R to Restart", True, RED)
        restart_rect = restart_text.get_rect(center=(width // 2, height // 2 + 100))
        display.blit(restart_text, restart_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_state = START
                    score = 0
                    clock_time = 90

    pygame.display.update()
    clock.tick(60)

# Quit Pygame
pygame.quit()
