import pygame

class AudioManager:
    def __init__(self):
        pygame.mixer.init()

    def reproducir_musica(self, ruta):
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.play(-1)

    def reproducir_sonido(self, sonido):
        sonido.play()
