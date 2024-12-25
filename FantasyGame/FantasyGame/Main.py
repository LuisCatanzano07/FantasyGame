import pygame
import os
from Constantes import ajustar_escala, FPS, RUTA_SPRITES_ARMA, RUTA_SPRITES_JUGADOR, RUTA_SPRITES_ENEMIGOS
from Personaje import Personaje
from Armas import Arma
from Enemigos import Esqueleton
from Colisiones import verificar_colisiones

def cargar_assets():
    """
    Carga los assets necesarios para el juego. Si un archivo no se encuentra, genera un error.
    """
    try:
        assets = {
            "Pistola": pygame.image.load(os.path.join(RUTA_SPRITES_ARMA, "Pistola.png")).convert_alpha(),
            "Bala": pygame.image.load(os.path.join(RUTA_SPRITES_ARMA, "Bala.png")).convert_alpha(),
            "Player": [
                pygame.image.load(os.path.join(RUTA_SPRITES_JUGADOR, f"Player_{i}.png")).convert_alpha() for i in range(7)
            ],
            "Esqueleton": [
                pygame.image.load(os.path.join(RUTA_SPRITES_ENEMIGOS, f"Esqueleton_{i}.png")).convert_alpha() for i in range(10)
            ],
        }
        print("Assets cargados correctamente.")
        return assets
    except FileNotFoundError as e:
        print(f"Error al cargar assets: {e}")
        raise

def main():
    pygame.init()
    infoObject = pygame.display.Info()
    ANCHO_PANTALLA = infoObject.current_w
    ALTO_PANTALLA = infoObject.current_h
    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA), pygame.FULLSCREEN)
    pygame.display.set_caption("Mi Juego Adaptable")
    clock = pygame.time.Clock()

    ajustar_escala(ANCHO_PANTALLA, ALTO_PANTALLA)

    # Cargar assets
    assets = cargar_assets()

    arma = Arma(assets["Pistola"], assets["Bala"])
    personaje = Personaje(assets["Player"], arma, (100, ALTO_PANTALLA // 2))
    enemigos = [
        Esqueleton(assets["Esqueleton"], (ANCHO_PANTALLA - 100, ALTO_PANTALLA // 2)),
        Esqueleton(assets["Esqueleton"], (ANCHO_PANTALLA - 300, ALTO_PANTALLA // 3)),
    ]

    corriendo = True
    en_pausa = False
    ventana_reducida = False

    while corriendo:
        dt = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    # Alternar pausa y ajuste de ventana
                    en_pausa = not en_pausa
                    if en_pausa and not ventana_reducida:
                        pantalla = pygame.display.set_mode((ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2))
                        ventana_reducida = True
                    elif not en_pausa and ventana_reducida:
                        pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA), pygame.FULLSCREEN)
                        ventana_reducida = False
                elif event.key == pygame.K_f:
                    # Alternar dirección del personaje y el arma
                    personaje.toggle_direction()
                    personaje.arma.set_direccion(personaje.facing_left)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not en_pausa:
                    personaje.arma.disparar(pygame.mouse.get_pos())

        if en_pausa:
            continue  # No actualizar lógica si está en pausa

        teclas = pygame.key.get_pressed()
        personaje.manejar_entrada(teclas)
        personaje.apuntar_arma(pygame.mouse.get_pos())
        personaje.actualizar(dt)

        for enemigo in enemigos:
            enemigo.actualizar(dt, personaje.rect.center)

        verificar_colisiones(personaje, enemigos)

        pantalla.fill((30, 30, 30))
        personaje.dibujar(pantalla)
        for enemigo in enemigos:
            enemigo.dibujar(pantalla)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()





















