import pygame  # librería principal para hacer el juego
import sys     # para cerrar el programa limpiamente


# ── CONFIGURACIÓN ──
WIDTH, HEIGHT = 800, 600  # tamaño de la ventana en píxeles (ancho x alto)
FPS = 60                  # fotogramas por segundo que corre el juego
TITLE = "Estrella Caída"  # texto que aparece en la barra de la ventana

# Colores en formato RGB (Rojo, Verde, Azul) — placeholders hasta que Zoe ponga los assets
BLACK = (0,   0,   0)    # negro puro
WHITE = (255, 255, 255)  # blanco puro
GRAY  = (40,  40,  40)   # gris oscuro


# ── ESCENAS ──
# Variables que identifican cada pantalla del juego
SCENE_MENU     = "menu"      # pantalla del menú principal
SCENE_GAME     = "game"      # pantalla del gameplay
SCENE_GAMEOVER = "gameover"  # pantalla de game over


def scene_menu(screen, font, events):
    # screen = la ventana | font = fuente de texto | events = lista de inputs del frame
    
    screen.fill(BLACK)  # limpia la pantalla pintándola de negro

    title  = font.render("ESTRELLA CAÍDA", True, WHITE)        # convierte el texto a imagen dibujable
    prompt = font.render("Presiona ENTER para jugar", True, GRAY)  # mismo pero para el texto de instrucción

    screen.blit(title,  title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40)))   # dibuja el título centrado, un poco arriba del centro
    screen.blit(prompt, prompt.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))  # dibuja el prompt centrado, un poco abajo del centro

    for event in events:  # revisa todos los inputs de este frame
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  # si presionó Enter
            return SCENE_GAME  # cambia a la escena del juego

    return SCENE_MENU  # si no presionó nada, se queda en el menú


def scene_game(screen, font, events):
    # Placeholder del gameplay
    # Aquí Jose mete físicas/input y JP + Genaro meten cámara/enemigos

    screen.fill((10, 10, 30))  # fondo azul muy oscuro, tono cósmico provisional

    label = font.render("[ GAMEPLAY — en construcción ]", True, WHITE)  # texto placeholder
    screen.blit(label, label.get_rect(center=(WIDTH // 2, HEIGHT // 2)))  # lo dibuja al centro de la pantalla

    for event in events:  # revisa inputs
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # si presionó ESC
            return SCENE_GAMEOVER  # cambia a game over (para probar el flujo)

    return SCENE_GAME  # si no pasó nada, se queda en el gameplay


def scene_gameover(screen, font, events):
    screen.fill(BLACK)  # limpia la pantalla de negro

    title  = font.render("GAME OVER", True, WHITE)                          # texto principal
    prompt = font.render("R — reintentar   |   ESC — salir", True, GRAY)   # instrucciones

    screen.blit(title,  title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40)))  # dibuja título arriba del centro
    screen.blit(prompt, prompt.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))) # dibuja instrucciones abajo del centro

    for event in events:  # revisa inputs
        if event.type == pygame.KEYDOWN:  # si presionó alguna tecla
            if event.key == pygame.K_r:       # si fue la R
                return SCENE_GAME             # regresa al gameplay
            if event.key == pygame.K_ESCAPE:  # si fue ESC
                return None                   # regresa None = señal para cerrar el juego

    return SCENE_GAMEOVER  # si no presionó nada, se queda en game over


# ── LOOP PRINCIPAL ──

def main():
    pygame.init()  # enciende todos los módulos de pygame, siempre va primero

    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # crea la ventana con el tamaño definido arriba
    pygame.display.set_caption(TITLE)                  # pone el título en la barra de la ventana
    clock  = pygame.time.Clock()                       # objeto que controla los FPS
    font   = pygame.font.SysFont("Arial", 32)          # carga la fuente Arial tamaño 32

    current_scene = SCENE_MENU  # el juego siempre arranca en el menú

    while True:  # loop infinito — corre cada frame hasta que se cierre el juego
        dt = clock.tick(FPS) / 1000.0  # limita a 60 FPS y calcula el tiempo entre frames en segundos (delta time)

        events = pygame.event.get()    # recolecta todos los inputs/eventos de este frame
        for event in events:
            if event.type == pygame.QUIT:  # si el usuario cierra la ventana con la X
                pygame.quit()  # apaga pygame
                sys.exit()     # cierra el programa

        # llama la función de la escena activa y guarda a cuál escena ir después
        if current_scene == SCENE_MENU:
            next_scene = scene_menu(screen, font, events)
        elif current_scene == SCENE_GAME:
            next_scene = scene_game(screen, font, events)
        elif current_scene == SCENE_GAMEOVER:
            next_scene = scene_gameover(screen, font, events)
        else:
            next_scene = None  # escena desconocida — cierra el juego

        if next_scene is None:  # si alguna escena regresó None
            pygame.quit()  # apaga pygame
            sys.exit()     # cierra el programa

        current_scene = next_scene  # actualiza la escena activa para el siguiente frame
        pygame.display.flip()       # muestra en pantalla todo lo que se dibujó en este frame


if __name__ == "__main__":  # solo corre main() si ejecutas este archivo directamente
    main()