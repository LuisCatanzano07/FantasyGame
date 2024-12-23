import pygame
import random
import math
from Constantes import ESCALA_SPRITES_ENEMIGO, CARACTERISTICAS_ENEMIGO

class Esqueleton:
    def __init__(self, lista_sprites, posicion_inicial):
        self.sprites = [
            pygame.transform.scale(sprite, (int(sprite.get_width() * ESCALA_SPRITES_ENEMIGO),
                                            int(sprite.get_height() * ESCALA_SPRITES_ENEMIGO)))
            for sprite in lista_sprites
        ]
        self.frame_actual = 0
        self.tiempo_anim = 0
        self.tiempo_por_frame = 0.1
        self.image = self.sprites[self.frame_actual]
        self.rect = self.image.get_rect(center=posicion_inicial)

        self.vida = CARACTERISTICAS_ENEMIGO["vida"]
        self.max_health = CARACTERISTICAS_ENEMIGO["salud"]
        self.health = self.max_health
        self.fuerza = CARACTERISTICAS_ENEMIGO["fuerza"]
        self.velocidad = CARACTERISTICAS_ENEMIGO["velocidad"]
        self.resistencia = CARACTERISTICAS_ENEMIGO["resistencia"]
        self.agilidad = CARACTERISTICAS_ENEMIGO["agilidad"]
        self.suerte = CARACTERISTICAS_ENEMIGO["suerte"]
        self.precision = CARACTERISTICAS_ENEMIGO["precision"]
        self.mana = CARACTERISTICAS_ENEMIGO["mana"]

        self.facing_left = False

    def set_direction(self, facing_left):
        self.facing_left = facing_left
        if self.facing_left:
            self.sprites = [pygame.transform.flip(sprite, True, False) for sprite in self.sprites]
        else:
            self.sprites = [pygame.transform.flip(sprite, False, False) for sprite in self.sprites]

    def actualizar(self, dt, posicion_jugador):
        self.tiempo_anim += dt
        if self.tiempo_anim >= self.tiempo_por_frame:
            self.tiempo_anim = 0
            self.frame_actual = (self.frame_actual + 1) % len(self.sprites)
        self.image = self.sprites[self.frame_actual]

        if self.health <= 0:
            self.regenerar()

        dx = posicion_jugador[0] - self.rect.centerx
        dy = posicion_jugador[1] - self.rect.centery
        distancia = math.hypot(dx, dy)
        if distancia > 0:
            self.rect.centerx += (dx / distancia) * self.velocidad * dt
            self.rect.centery += (dy / distancia) * self.velocidad * dt

        if dx < 0 and not self.facing_left:
            self.set_direction(True)
        elif dx > 0 and self.facing_left:
            self.set_direction(False)

    def regenerar(self):
        """
        Regenera al enemigo, restableciendo su salud y colocándolo en una nueva posición.
        Si se queda sin "vida", reinicia sus valores para un nuevo inicio.
        """
        self.vida -= 1
        if self.vida > 0:
            self.health = self.max_health
            self.rect.center = (
                random.randint(600, 800),
                random.randint(100, 500)
            )
        else:
            print("Enemigo eliminado definitivamente.")
            self.health = self.max_health  # Restablecer salud
            self.vida = CARACTERISTICAS_ENEMIGO["vida"]  # Reiniciar vidas
            self.rect.center = (
                random.randint(600, 800),
                random.randint(100, 500)
            )

    def dibujar_barra_salud(self, superficie):
        bar_width = 50
        bar_height = 5
        health_frac = max(0, min(1, self.health / self.max_health))

        if health_frac > 0.75:
            color_barra = (0, 255, 0)
        elif health_frac > 0.5:
            color_barra = (255, 255, 0)
        elif health_frac > 0.25:
            color_barra = (255, 165, 0)
        else:
            color_barra = (255, 0, 0)

        color_fondo = (50, 50, 50)
        current_bar_width = int(bar_width * health_frac)

        x = self.rect.centerx - bar_width // 2
        y = self.rect.top - 10

        pygame.draw.rect(superficie, color_fondo, (x, y, bar_width, bar_height))
        pygame.draw.rect(superficie, color_barra, (x, y, current_bar_width, bar_height))

    def dibujar(self, superficie):
        superficie.blit(self.image, self.rect)
        self.dibujar_barra_salud(superficie)

### Implementación de carga de sprites ###
def cargar_sprites_esqueleton():
    try:
        return [
                pygame.image.load("assets/enemigos/Esqueleton_0.png").convert_alpha(),
                pygame.image.load("assets/enemigos/Esqueleton_1.png").convert_alpha(),
                pygame.image.load("assets/enemigos/Esqueleton_2.png").convert_alpha(),
                pygame.image.load("assets/enemigos/Esqueleton_3.png").convert_alpha(),
                pygame.image.load("assets/enemigos/Esqueleton_4.png").convert_alpha(),
                pygame.image.load("assets/enemigos/Esqueleton_5.png").convert_alpha(),
                pygame.image.load("assets/enemigos/Esqueleton_6.png").convert_alpha(),
                pygame.image.load("assets/enemigos/Esqueleton_7.png").convert_alpha(),
                pygame.image.load("assets/enemigos/Esqueleton_8.png").convert_alpha(),
                pygame.image.load("assets/enemigos/Esqueleton_9.png").convert_alpha(),
        ]
    except pygame.error as e:
        print(f"Error al cargar los sprites del esqueleton: {e}")
        raise










