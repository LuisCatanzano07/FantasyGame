import pygame
from Constantes import (
    DANO_JUGADOR_ENEMIGO, DANO_ENEMIGO_JUGADOR, DANO_BALA_ENEMIGO,
    FACTOR_RESISTENCIA, FACTOR_SUERTE
)

def verificar_colision_jugador_enemigo(personaje, enemigo):
    if personaje.rect.colliderect(enemigo.rect):
        dano_recibido_jugador = max(0, DANO_JUGADOR_ENEMIGO - personaje.resistencia * FACTOR_RESISTENCIA)
        dano_recibido_jugador *= (1 - personaje.suerte * FACTOR_SUERTE)

        dano_recibido_enemigo = max(0, DANO_ENEMIGO_JUGADOR - enemigo.resistencia * FACTOR_RESISTENCIA)

        personaje.health -= dano_recibido_jugador
        enemigo.health -= dano_recibido_enemigo

        if personaje.health <= 0:
            personaje.vida -= 1
            if personaje.vida > 0:
                personaje.regenerar()
            else:
                print("Derrota: El personaje ha perdido todas las vidas.")

        if enemigo.health <= 0:
            enemigo.vida -= 1
            if enemigo.vida > 0:
                enemigo.regenerar()
            else:
                print("Enemigo derrotado definitivamente.")

def verificar_colision_balas_enemigo(personaje, enemigo):
    for bala in personaje.arma.balas[:]:
        if bala.rect.colliderect(enemigo.rect):
            dano_recibido_enemigo = max(0, DANO_BALA_ENEMIGO - enemigo.resistencia * FACTOR_RESISTENCIA)
            enemigo.health -= dano_recibido_enemigo

            if enemigo.health <= 0:
                enemigo.vida -= 1
                if enemigo.vida > 0:
                    enemigo.regenerar()
                else:
                    print("Enemigo derrotado definitivamente.")

            personaje.arma.remover_bala(bala)

def verificar_colisiones(personaje, enemigos):
    for enemigo in enemigos:
        verificar_colision_jugador_enemigo(personaje, enemigo)
    for enemigo in enemigos:
        verificar_colision_balas_enemigo(personaje, enemigo)
    ancho_pantalla = pygame.display.get_surface().get_width()
    alto_pantalla = pygame.display.get_surface().get_height()
    for bala in personaje.arma.balas[:]:
        if (bala.rect.x < 0 or bala.rect.x > ancho_pantalla or
                bala.rect.y < 0 or bala.rect.y > alto_pantalla):
            personaje.arma.remover_bala(bala)











