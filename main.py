import pygame
import random
import time

# Inicializar pygame
pygame.init()

# Dimensiones de la ventana del juego
WIDTH = 800
HEIGHT = 600

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 192, 203)

# Crear la ventana del juego
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game")

# Fuente para el texto
font = pygame.font.SysFont(None, 55)

# Cargar imágenes
heart_image = pygame.image.load("img/heart.png").convert_alpha()
arrow_image = pygame.image.load("img/arrow.png").convert_alpha()

# Clase para representar al jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(heart_image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
        
        # Mantener dentro de los límites de la ventana
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

# Clase para representar a los enemigos
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(arrow_image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(WIDTH, WIDTH + 100)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)
        self.speed_x = random.randint(1, 3)
    
    def update(self):
        self.rect.x -= self.speed_x
        if self.rect.right < 0:
            self.rect.x = random.randint(WIDTH, WIDTH + 100)
            self.rect.y = random.randint(0, HEIGHT - self.rect.height)
            self.speed_x = random.randint(1, 3)

# Función para mostrar texto en la pantalla
def draw_text(surface, text, size, x, y, color):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_surface, text_rect)

# Pantalla de bienvenida
def show_start_screen():
    window.fill(PINK)
    draw_text(window, "Bienvenida, ¿Podrá cupido flechar tu corazón? ", 55, WIDTH // 2, HEIGHT // 2 - 50, BLACK)
    draw_text(window, "Presiona ENTER para iniciar", 40, WIDTH // 2, HEIGHT // 2 + 50, BLACK)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

# Pantalla de pérdida
def show_game_over_screen(score):
    window.fill(PINK)
    draw_text(window, "Perdiste", 55, WIDTH // 2, HEIGHT // 2 - 50, BLACK)
    draw_text(window, f"Tiempo: {score} segundos", 40, WIDTH // 2, HEIGHT // 2, BLACK)
    draw_text(window, "Presiona SPACE para reiniciar", 40, WIDTH // 2, HEIGHT // 2 + 50, BLACK)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

# Crear grupos de sprites
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Crear jugador
player = Player()
all_sprites.add(player)

# Crear enemigos
for _ in range(5):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Variable para controlar el estado del juego
game_over = False
lives = 3
start_time = None

# Mostrar pantalla de inicio
show_start_screen()

# Bucle principal del juego
running = True
while running:
    if game_over:
        show_game_over_screen(int(time.time() - start_time))
        # Reiniciar el juego
        player.rect.center = (WIDTH // 2, HEIGHT // 2)
        for enemy in enemies:
            enemy.rect.x = random.randint(WIDTH, WIDTH + 100)
            enemy.rect.y = random.randint(0, HEIGHT - enemy.rect.height)
        lives = 3
        start_time = time.time()
        game_over = False

    if start_time is None:
        start_time = time.time()

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Actualizar
    all_sprites.update()

    # Comprobar colisiones del jugador con los enemigos
    if pygame.sprite.spritecollide(player, enemies, True):
        lives -= 1
        if lives == 0:
            game_over = True
        else:
            for _ in range(10 - len(enemies)):
                enemy = Enemy()
                all_sprites.add(enemy)
                enemies.add(enemy)

    # Calcular el tiempo de supervivencia
    survival_time = int(time.time() - start_time)

    # Dibujar
    window.fill(PINK)
    all_sprites.draw(window)
    draw_text(window, f"Vidas: {lives}", 30, WIDTH - 100, 10, BLACK)
    draw_text(window, f"Tiempo: {survival_time} segundos", 30, 150, 10, BLACK)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir del juego
pygame.quit()
