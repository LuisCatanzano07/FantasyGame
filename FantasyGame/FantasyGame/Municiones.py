class Bala:
    def __init__(self, x, y, vel_x, vel_y, sprite):
        self.image = sprite
        self.rect = self.image.get_rect(center=(x, y))
        self.vel_x = vel_x
        self.vel_y = vel_y

    def actualizar(self, dt):
        self.rect.x += self.vel_x * dt
        self.rect.y += self.vel_y * dt

    def dibujar(self, superficie):
        superficie.blit(self.image, self.rect)


