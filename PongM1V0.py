cimport pygame
import sys

# Initialize pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 256
SCREEN_HEIGHT = 240
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Retro PONG")
clock = pygame.time.Clock()

# Set up the ball
BALL_SIZE = 8
BALL_X = SCREEN_WIDTH // 2 - BALL_SIZE // 2
BALL_Y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
BALL_VEL_X = 3
BALL_VEL_Y = 3

# Set up the paddles
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
PADDLE_1_X = 16
PADDLE_1_Y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
PADDLE_2_X = SCREEN_WIDTH - PADDLE_WIDTH - 16
PADDLE_2_Y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2

# Set up the score
SCORE_1 = 0
SCORE_2 = 0
font = pygame.font.Font(None, 36)

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the ball's position
    BALL_X += BALL_VEL_X
    BALL_Y += BALL_VEL_Y

    # Check for collisions with the walls
    if BALL_Y <= 0 or BALL_Y >= SCREEN_HEIGHT - BALL_SIZE:
        BALL_VEL_Y *= -1

    # Check for collisions with the paddles
    if PADDLE_1_X < BALL_X < PADDLE_1_X + PADDLE_WIDTH and PADDLE_1_Y < BALL_Y < PADDLE_1_Y + PADDLE_HEIGHT:
        BALL_VEL_X *= -1
    elif PADDLE_2_X < BALL_X < PADDLE_2_X + PADDLE_WIDTH and PADDLE_2_Y < BALL_Y < PADDLE_2_Y + PADDLE_HEIGHT:
        BALL_VEL_X *= -1

    # Check for a score
    if BALL_X <= 0:
        SCORE_2 += 1
        BALL_X, BALL_Y = SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2
        BALL_VEL_X, BALL_VEL_Y = 3, 3

    if BALL_X >= SCREEN_WIDTH - BALL_SIZE:
        SCORE_1 += 1
        BALL_X, BALL_Y = SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2
        BALL_VEL_X, BALL_VEL_Y = -3, 3

    # Update the paddles' positions
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and PADDLE_1_Y > 0:
        PADDLE_1_Y -= 5
    if keys[pygame.K_s] and PADDLE_1_Y < SCREEN_HEIGHT - PADDLE_HEIGHT:
        PADDLE_1_Y += 5

    # Second paddle movement (AI)
    if PADDLE_2_Y + PADDLE_HEIGHT // 2 < BALL_Y:
        PADDLE_2_Y += 3
    elif PADDLE_2_Y + PADDLE_HEIGHT // 2 > BALL_Y:
        PADDLE_2_Y -= 3

    # Draw the game
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (BALL_X, BALL_Y, BALL_SIZE, BALL_SIZE))
    pygame.draw.rect(screen, (255, 255, 255), (PADDLE_1_X, PADDLE_1_Y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, (255, 255, 255), (PADDLE_2_X, PADDLE_2_Y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Draw the score
    text_1 = font.render(str(SCORE_1), True, (255, 255, 255))
    text_2 = font.render(str(SCORE_2), True, (255, 255, 255))
    screen.blit(text_1, (50, 20))
    screen.blit(text_2, (SCREEN_WIDTH - 70, 20))

    # Flip the display
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
