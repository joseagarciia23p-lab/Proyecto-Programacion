import pygame
import sys


#  CONFIGURACIÓN
WIDTH, HEIGHT = 800, 600
FPS = 60
TITLE = "Estrella Caída"

# Colores default para que Zoe ponga atributos
BLACK  = (0,   0,   0)
WHITE  = (255, 255, 255)
GRAY   = (40,  40,  40)


#  ESCENAS
SCENE_MENU     = "menu"
SCENE_GAME     = "game"
SCENE_GAMEOVER = "gameover"


def scene_menu(screen, font, events):
    """Retorna la siguiente escena o None para quedarse."""
    screen.fill(BLACK)

    title  = font.render("ESTRELLA CAÍDA", True, WHITE)
    prompt = font.render("Presiona ENTER para jugar", True, GRAY)

    screen.blit(title,  title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40)))
    screen.blit(prompt, prompt.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))

    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return SCENE_GAME

    return SCENE_MENU


def scene_game(screen, font, events):
    """
    Placeholder del gameplay.
    Aquí es donde Jose mete físicas/input
     JP + Genaro meten cámara/enemigos.
    """
    screen.fill((10, 10, 30))  # fondo oscuro cósmico provisional

    label = font.render("[ GAMEPLAY — en construcción ]", True, WHITE)
    screen.blit(label, label.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

    for event in events:
        # Tecla ESC = Game Over (para probar el flujo)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return SCENE_GAMEOVER

    return SCENE_GAME


def scene_gameover(screen, font, events):
    """Retorna la siguiente escena o None para quedarse."""
    screen.fill(BLACK)

    title  = font.render("GAME OVER", True, WHITE)
    prompt = font.render("R — reintentar   |   ESC — salir", True, GRAY)

    screen.blit(title,  title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40)))
    screen.blit(prompt, prompt.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                return SCENE_GAME
            if event.key == pygame.K_ESCAPE:
                return None  # señal de salir

    return SCENE_GAMEOVER


#  LOOP PRINCIPAL

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock  = pygame.time.Clock()
    font   = pygame.font.SysFont("Arial", 32)

    current_scene = SCENE_MENU

    while True:
        dt = clock.tick(FPS) / 1000.0  # delta time en segundos (útil pa físicas)

        # ── Eventos ──
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Escenas
        if current_scene == SCENE_MENU:
            next_scene = scene_menu(screen, font, events)
        elif current_scene == SCENE_GAME:
            next_scene = scene_game(screen, font, events)
        elif current_scene == SCENE_GAMEOVER:
            next_scene = scene_gameover(screen, font, events)
        else:
            next_scene = None

        if next_scene is None:
            pygame.quit()
            sys.exit()

        current_scene = next_scene
        pygame.display.flip()


if __name__ == "__main__":
    main()