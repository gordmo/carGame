import pygame
import os

WIDTH, HEIGHT = 1200, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game")

WHITE = (255, 255, 255)

FPS = 60

CAR = pygame.image.load(os.path.join("Assets", "car.png"))

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(CAR, (100, 100))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        draw_window()
    
    pygame.quit()

if __name__ == "__main__":
    main()