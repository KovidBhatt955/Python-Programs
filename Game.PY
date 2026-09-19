import random
import pygame

# --- CONFIGURATION & GAME WINDOW ---
pygame.init()

# Setup a clean standard gameplay window size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Sprite Chaser")

# Essential tracking tools
clock = pygame.time.Clock()
score_font = pygame.font.SysFont("Arial", 28)
score = 0


# --- GAME OBJECTS ---
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        # Simple blue square for our player
        self.image = pygame.Surface((40, 40))
        self.image.fill((50, 120, 255))
        self.rect = self.image.get_rect()

        # Start right in the middle of the screen
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5

    def update(self):
        # Support both WASD and traditional Arrow keys naturally
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        # Stop the player from running off the edges of the window
        self.rect.clamp_ip(screen.get_rect())


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        # Simple red square for enemies
        self.image = pygame.Surface((30, 30))
        self.image.fill((230, 50, 50))
        self.rect = self.image.get_rect()
        self.randomize_position()

    def randomize_position(self):
        # Throw the enemy to a completely random spot on the active screen
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)


# --- INITIAL SETUP ---
# Creating our groups to manage drawing and updates easily
all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

# Spawn player
player = Player()
all_sprites.add(player)

# Spawn our 7 required enemies randomly across the screen
for _ in range(7):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemy_group.add(enemy)


# --- MAIN ENGINE LOOP ---
game_running = True
while game_running:

    # 1. Listen for user system events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # 2. Update object coordinates
    all_sprites.update()

    # 3. Collision Engine
    # Check if the player collides with any sprite in the enemy group
    hits = pygame.sprite.spritecollide(player, enemy_group, False)

    for hit_enemy in hits:
        score += 1  # Award a point on impact
        hit_enemy.randomize_position()  # Teleport the hit enemy somewhere new

    # 4. Rendering Pipeline
    screen.fill((240, 240, 240))  # Clear frame with a nice light grey background
    all_sprites.draw(screen)  # Draw player and enemies seamlessly

    # Draw the persistent score counter text in the upper left corner
    score_surface = score_font.render(f"Score: {score}", True, (50, 50, 50))
    screen.blit(score_surface, (20, 20))

    # Push updates directly to the visual monitor layer
    pygame.display.flip()

    # Cap performance at a comfortable, smooth 60 frames per second
    clock.tick(60)

pygame.quit()
