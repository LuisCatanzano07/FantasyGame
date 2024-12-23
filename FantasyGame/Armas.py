import pygame
import os
from Municiones import Bala
import math

class Arma:
    def __init__(self, sprite, bala_sprite):
        self.original_image = sprite
        self.image = sprite
        self.rect = self.image.get_rect()
        self.angulo = 0
        self.bala_sprite = bala_sprite
        self.balas = []
        self.facing_left = False

    def set_direccion(self, facing_left):
        self.facing_left = facing_left
        if self.facing_left:
            self.image = pygame.transform.flip(self.original_image, True, False)
        else:
            self.image = self.original_image

    def set_angulo(self, angulo):
        self.angulo = angulo
        rotated_image = pygame.transform.rotate(self.original_image, -self.angulo)
        if self.facing_left:
            self.image = pygame.transform.flip(rotated_image, True, False)
        else:
            self.image = rotated_image
        self.rect = self.image.get_rect(center=self.rect.center)

    def disparar(self, mouse_pos):
        dx = mouse_pos[0] - self.rect.centerx
        dy = mouse_pos[1] - self.rect.centery
        distancia = math.hypot(dx, dy)  # Uso de math.hypot
        if distancia != 0:
            dx /= distancia
            dy /= distancia
        velocidad_bala = 300
        nueva_bala = Bala(
            self.rect.centerx,
            self.rect.centery,
            dx * velocidad_bala,
            dy * velocidad_bala,
            self.bala_sprite
        )
        self.balas.append(nueva_bala)

    def actualizar(self, pos_personaje, dt):
        offset_x = -10 if self.facing_left else 10
        self.rect.center = (pos_personaje[0] + offset_x, pos_personaje[1])
        for bala in self.balas[:]:
            bala.actualizar(dt)
            pantalla_rect = pygame.display.get_surface().get_rect()
            if not pantalla_rect.contains(bala.rect):
                self.balas.remove(bala)

    def remover_bala(self, bala):
        if bala in self.balas:
            self.balas.remove(bala)

    def dibujar(self, superficie):
        superficie.blit(self.image, self.rect)
        for bala in self.balas:
            bala.dibujar(superficie)

### Implementación de carga de sprites para el arma con manejo de errores ###
def cargar_sprite_arma():
    try:
        return pygame.image.load("assets/sprites/armas/Pistola.png").convert_alpha()
    except FileNotFoundError as e:
        print(f"Error: {e}. Creando un sprite temporal para el arma.")
        sprite = pygame.Surface((30, 10))
        sprite.fill((255, 0, 0))  # Sprite temporal en rojo
        return sprite

def cargar_sprite_bala():
    try:
        return pygame.image.load("assets/sprites/armas/Bala.png").convert_alpha()
    except FileNotFoundError as e:
        print(f"Error: {e}. Creando un sprite temporal para la bala.")
        sprite = pygame.Surface((5, 5))
        sprite.fill((0, 255, 0))  # Sprite temporal en verde
        return sprite

if __name__ == "__main__":
    print(f"Directorio actual: {os.getcwd()}")










