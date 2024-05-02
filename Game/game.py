import pygame
import random

pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Character Movement")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# karakter
class Character:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.width = 50
        self.height = 50
        self.speed = 5

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def update_position(self):
        # Batasi pergerakan karakter di dalam bingkai layar
        self.x = max(0, min(WIDTH - self.width, self.x))
        self.y = max(0, min(HEIGHT - self.height, self.y))

# musuh
class Enemy:
    def __init__(self, x, y, color, target):
        self.x = x
        self.y = y
        self.color = color
        self.width = 50
        self.height = 50
        self.speed = 3
        self.target = target

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def follow_target(self):
        if self.x < self.target.x:
            self.x += self.speed
        elif self.x > self.target.x:
            self.x -= self.speed

        if self.y < self.target.y:
            self.y += self.speed
        elif self.y > self.target.y:
            self.y -= self.speed

        # agar tidak keluar layar /frame
        self.x = max(0, min(WIDTH - self.width, self.x))
        self.y = max(0, min(HEIGHT - self.height, self.y))

# Fungsi utama
def main():
    clock = pygame.time.Clock()

    # Buat karakter dan musuh
    player = Character(50, 50, WHITE)
    enemy = Enemy(200, 200, RED, player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= player.speed
        if keys[pygame.K_RIGHT]:
            player.x += player.speed
        if keys[pygame.K_UP]:
            player.y -= player.speed
        if keys[pygame.K_DOWN]:
            player.y += player.speed

        # posisi krakter update
        player.update_position()

        # bersihin layar
        screen.fill(BLACK)

        # Gambar karakter dan musuh
        player.draw()
        enemy.draw()
        enemy.follow_target()

        # Perbarui layar
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
