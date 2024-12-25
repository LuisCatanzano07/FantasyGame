import pygame
import math
from Constantes import CARACTERISTICAS_BASE_JUGADOR, ESCALA_SPRITES_JUGADOR

class Personaje:
    def __init__(self, lista_sprites, arma, posicion_inicial=(100, 100)):
        self.sprites = [
            pygame.transform.scale(sprite, (int(sprite.get_width() * ESCALA_SPRITES_JUGADOR),
                                            int(sprite.get_height() * ESCALA_SPRITES_JUGADOR)))
            for sprite in lista_sprites
        ]
        self.frame_actual = 0
        self.tiempo_anim = 0
        self.tiempo_por_frame = 0.1
        self.image = self.sprites[self.frame_actual]
        self.rect = self.image.get_rect(center=posicion_inicial)

        self.vel_x = 0
        self.vel_y = 0
        self.facing_left = False

        self.vida = CARACTERISTICAS_BASE_JUGADOR['vida']
        self.max_health = CARACTERISTICAS_BASE_JUGADOR['salud']
        self.health = self.max_health
        self.fuerza = CARACTERISTICAS_BASE_JUGADOR['fuerza']
        self.velocidad = CARACTERISTICAS_BASE_JUGADOR['velocidad']
        self.velocidad_ataque = CARACTERISTICAS_BASE_JUGADOR['velocidad_ataque']
        self.resistencia = CARACTERISTICAS_BASE_JUGADOR['resistencia']
        self.agilidad = CARACTERISTICAS_BASE_JUGADOR['agilidad']
        self.suerte = CARACTERISTICAS_BASE_JUGADOR['suerte']
        self.precision = CARACTERISTICAS_BASE_JUGADOR['precision']
        self.mana = CARACTERISTICAS_BASE_JUGADOR['mana']
        self.nivel = CARACTERISTICAS_BASE_JUGADOR['nivel']

        self.arma = arma
        self.scale = ESCALA_SPRITES_JUGADOR
        self.original_position = posicion_inicial

    def manejar_entrada(self, teclas):
        self.vel_x = 0
        self.vel_y = 0
        if teclas[pygame.K_w]:
            self.vel_y = -self.velocidad
        if teclas[pygame.K_s]:
            self.vel_y = self.velocidad
        if teclas[pygame.K_a]:
            self.vel_x = -self.velocidad
        if teclas[pygame.K_d]:
            self.vel_x = self.velocidad

    def toggle_direction(self):
        self.facing_left = not self.facing_left
        self.arma.set_direccion(self.facing_left)

    def apuntar_arma(self, mouse_pos):
        dx = mouse_pos[0] - self.rect.centerx
        dy = mouse_pos[1] - self.rect.centery
        angulo = math.degrees(math.atan2(dy, dx))
        self.arma.set_angulo(angulo)

    def actualizar(self, dt):
        self.rect.x += self.vel_x * dt
        self.rect.y += self.vel_y * dt

        pantalla_rect = pygame.display.get_surface().get_rect()
        self.rect.clamp_ip(pantalla_rect)

        self.actualizar_animacion(dt)
        self.arma.actualizar(self.rect.center, dt)

    def actualizar_animacion(self, dt):
        if self.vel_x != 0 or self.vel_y != 0:
            self.tiempo_anim += dt
            if self.tiempo_anim >= self.tiempo_por_frame:
                self.tiempo_anim = 0
                self.frame_actual = (self.frame_actual + 1) % len(self.sprites)
        else:
            self.frame_actual = 0
        self.image = self.sprites[self.frame_actual]

    def regenerar(self):
        """
        Restaura la salud del personaje y su posición inicial.
        Si se queda sin "vida", reinicia las vidas y la salud para un nuevo inicio.
        """
        self.vida -= 1
        if self.vida > 0:
            self.health = self.max_health
            self.rect.center = self.original_position
        else:
            print("¡Derrota! El personaje ha perdido todas las vidas.")
            self.health = self.max_health  # Restablecer salud
            self.vida = CARACTERISTICAS_BASE_JUGADOR['vida']  # Reiniciar vidas
            self.rect.center = self.original_position

    def dibujar(self, superficie):
        if self.facing_left:
            imagen_volteada = pygame.transform.flip(self.image, True, False)
            superficie.blit(imagen_volteada, self.rect)
        else:
            superficie.blit(self.image, self.rect)
        self.dibujar_barra_salud(superficie)
        self.arma.dibujar(superficie)

    def dibujar_barra_salud(self, superficie):
        bar_width = int(50 * self.scale)
        bar_height = int(5 * self.scale)
        health_frac = max(0, min(1, self.health / self.max_health))

        if health_frac > 0.75:
            color_barra = (0, 255, 0)
        elif health_frac > 0.5:
            color_barra = (255, 255, 0)
        elif health_frac > 0.25:
            color_barra = (255, 140, 0)
        else:
            color_barra = (255, 0, 0)

        color_fondo = (50, 50, 50)
        current_bar_width = int(bar_width * health_frac)

        x = self.rect.centerx - bar_width // 2
        y = self.rect.top - (bar_height + 10)

        pygame.draw.rect(superficie, color_fondo, (x, y, bar_width, bar_height))
        pygame.draw.rect(superficie, color_barra, (x, y, current_bar_width, bar_height))

### Implementación de carga de sprites ###
def cargar_sprites_personaje():
    try:
        return [
            pygame.image.load("assets/sprites/jugador/Player_0.png").convert_alpha(),
            pygame.image.load("assets/sprites/jugador/Player_1.png").convert_alpha(),
            pygame.image.load("assets/sprites/jugador/Player_2.png").convert_alpha(),
            pygame.image.load("assets/sprites/jugador/Player_3.png").convert_alpha(),
            pygame.image.load("assets/sprites/jugador/Player_4.png").convert_alpha(),
            pygame.image.load("assets/sprites/jugador/Player_5.png").convert_alpha(),
            pygame.image.load("assets/sprites/jugador/Player_6.png").convert_alpha()
        ]
    except pygame.error as e:
        print(f"Error al cargar los sprites del personaje: {e}")
        raise













