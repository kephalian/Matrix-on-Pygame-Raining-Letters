
import pygame
import random

pygame.init()

# Set up display
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("Raining Letters")

# Define colors
black = (0, 0, 0)
fluorescent_green = (0, 255, 0)

# Define the font
font = pygame.font.SysFont(None, 30)

# Create a list of letters
letters = [chr(i) for i in range(65, 91)]  # A-Z

# Create a list to store letter positions and speeds
letter_positions = [{'x': random.randint(0, width), 'y': random.randint(-50, height), 'speed': random.randint(5, 20)} for _ in range(100)]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False  # Set running to False to end the while loop.

#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False

    # Update letter positions
    for letter in letter_positions:
        letter['y'] += letter['speed']
        if letter['y'] > height:
            letter['y'] = 0
            letter['x'] = random.randint(0, width)

    # Draw background
    screen.fill(black)

    # Draw letters
    for i, letter in enumerate(letter_positions):
        text = font.render(random.choice(letters), True, fluorescent_green)
        screen.blit(text, (letter['x'], letter['y']))

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
#```

#This version sets the display mode to fullscreen (`pygame.FULLSCREEN`) and changes the letter color to fluorescent green.