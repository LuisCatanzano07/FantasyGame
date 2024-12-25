### Modulo: Constantes
RUTA_ASSETS = "assets/"
RUTA_SPRITES = RUTA_ASSETS + "sprites/"
RUTA_SPRITES_JUGADOR = RUTA_SPRITES + "jugador/"
RUTA_SPRITES_ARMA = RUTA_SPRITES + "arma/"
RUTA_SPRITES_ENEMIGOS = RUTA_SPRITES + "enemigos/"

ESCALA_BASE_JUGADOR = 1.0
ESCALA_BASE_ENEMIGO = 1.5
ESCALA_SPRITES_JUGADOR = ESCALA_BASE_JUGADOR
ESCALA_SPRITES_ENEMIGO = ESCALA_BASE_ENEMIGO

FPS = 60
DANO_JUGADOR_ENEMIGO = 1
DANO_ENEMIGO_JUGADOR = 2
DANO_BALA_ENEMIGO = 10
FACTOR_SUERTE = 0.05
FACTOR_RESISTENCIA = 0.1

CARACTERISTICAS_BASE_JUGADOR = {
    "vida": 3,
    "salud": 100,
    "fuerza": 10,
    "velocidad": 200,
    "velocidad_ataque": 1.0,
    "resistencia": 5,
    "agilidad": 5,
    "suerte": 5,
    "precision": 80,
    "mana": 50,
    "nivel": 1,
}

CARACTERISTICAS_ENEMIGO = {
    "vida": 2,
    "salud": 100,
    "fuerza": 20,
    "velocidad": 100,
    "velocidad_ataque": 1.5,
    "resistencia": 5,
    "agilidad": 10,
    "suerte": 0,
    "precision": 60,
    "mana": 0,
}

def ajustar_escala(ancho_pantalla, alto_pantalla, resolucion_base=(800, 600)):
    global ESCALA_SPRITES_JUGADOR, ESCALA_SPRITES_ENEMIGO
    factor_ancho = ancho_pantalla / resolucion_base[0]
    factor_alto = alto_pantalla / resolucion_base[1]
    factor = min(factor_ancho, factor_alto)
    ESCALA_SPRITES_JUGADOR = ESCALA_BASE_JUGADOR * factor
    ESCALA_SPRITES_ENEMIGO = ESCALA_BASE_ENEMIGO * factor







