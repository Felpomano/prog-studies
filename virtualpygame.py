import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 400, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Pygame Virtual Pet")
clock = pygame.time.Clock()

#COLORS
WHITE = (255, 255, 255)
GRAY = (240, 240, 240)
DARK_GRAY = (50, 50, 50)
GREEN = (46, 204, 113)
BLUE = (52, 152, 219)
RED = (231, 76, 60)

#FONTS
font = pygame.font.SysFont("Comic Sans", 20)

#PET CLASS
class VirtualPet:
    def __init__(self):
        #STATS START AT MAX 100
        self.hunger = 100.0
        self.happiness = 100.0
        self.status = "Happy"

        #DECAY RATES PER FRAME
        self.hunger_decay = 0.02
        self.happiness_decay = 0.015

    def update(self):
        #STATS NATURALLY DROPS OVER TIME
        self.hunger = max(0.0, self.hunger - self.hunger_decay)
        self.happiness = max(0.0, self.happiness - self.happiness_decay)

        #UPDATE EMOTIONAL STATUS BASED ON LEVELS
        if self.hunger < 30 or self.happiness < 30:
            self.status = "Miserable"
        elif self.hunger < 60 or self.happiness < 60:
            self.status = "Bored/Hungry"
        else:
            self.status = "Happy"
        #I WANT TO MAKE A MECHANIC THAT THE PET FUCKING DIES please don't forget me :( )
    
    def feed(self):
        self.hunger = min(100.0, self.hunger + 20)

    def play(self):
        self.happiness = min(100.0, self.happiness + 20)

#CREATE GAME OBJECTS
pet = VirtualPet()

#DEFINE UI BUTTONS (X, Y, WIDTH, HEIGHT)
feed_btn = pygame.Rect(50, 420, 120, 40)
play_btn = pygame.Rect(230, 420, 120, 40)

#MAIN GAME LOOP
running = True
while running:
    #EVENT HANDLING / function that teached me about how to detect a mouse in prog (and how for works)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #LEFT CLICK
                mouse_pos = pygame.mouse.get_pos()
                if feed_btn.collidepoint(mouse_pos):
                    pet.feed()
                elif play_btn.collidepoint(mouse_pos):
                    pet.play()

    #UPDATE PET STATES
    pet.update()

    #DRAW EVERYTHING
    screen.fill(WHITE)

    #DRAW UI BACKGROUND PANEL
    pygame.draw.rect(screen, GRAY, (0, 350, WIDTH, 150))

    #RENDER TEXT UI
    status_text = font.render(f"Mood: {pet.status}", True, DARK_GRAY)
    hunger_text = font.render(f"Hunger: {int(pet.hunger)}/100", True, DARK_GRAY)
    happy_text = font. render(f"Happiness: {int(pet.happiness)}/100", True, DARK_GRAY)

    screen.blit(status_text, (20, 20))
    screen.blit(hunger_text, (20, 60))
    screen.blit(happy_text, (20, 80))

    
    #DRAW PET (CHANGES COLOR BASED ON MOOD)
    pet_color = GREEN if pet.status == "Happy" else (BLUE if pet.status == "Bored/Hungry" else RED)
    pygame.draw.circle(screen, pet_color, (WIDTH // 2, HEIGHT // 2 - 40), 60) #BODY
    pygame.draw.circle(screen, DARK_GRAY, (WIDTH // 2 - 20, HEIGHT // 2 - 50), 6) #LEFT EYE
    pygame.draw.circle(screen, DARK_GRAY, (WIDTH // 2 + 20, HEIGHT // 2 - 50), 6) #RIGHT EYE
    pygame.draw.circle(screen, DARK_GRAY, (WIDTH // 2, HEIGHT // 2 - 25), 6) #mouth.
    #+ 40 / -25

    #DRAW INTERACTIVE BUTTONS
    pygame.draw.rect(screen, GREEN, feed_btn, border_radius=5)
    pygame.draw.rect(screen, BLUE, play_btn, border_radius=5)

    feed_label = font.render("Feed", True, WHITE)
    play_label = font.render("Play", True, WHITE)
    screen.blit(feed_label, (feed_btn.x + 40, feed_btn.y + 8))
    screen.blit(play_label, (play_btn.x + 40, play_btn.y + 8))

    # Refresh the display
    pygame.display.flip()
    clock.tick(60) #Lock framerate to 60 FPS

pygame.quit()
sys.exit()
