import pygame
from Constantes import RUTA_SPRITES_JUGADOR, RUTA_SPRITES_ARMA, RUTA_SPRITES_ENEMIGOS, ESCALA_SPRITES_JUGADOR, ESCALA_SPRITES_ENEMIGO

def cargar_y_escalar_imagen(ruta, escala):
    """
    Carga una imagen desde el disco y la escala según el factor proporcionado.

    Args:
        ruta (str): Ruta de la imagen.
        escala (float): Factor de escala.

    Returns:
        Surface: Imagen escalada.
    """
    try:
        img = pygame.image.load(ruta).convert_alpha()
        ancho = int(img.get_width() * escala)
        alto = int(img.get_height() * escala)
        return pygame.transform.scale(img, (ancho, alto))
    except pygame.error as e:
        print(f"Error cargando la imagen: {ruta} -> {e}")
        return None

def cargar_y_escalar_varias(ruta_base, nombres, escala):
    """
    Carga y escala múltiples imágenes desde una ruta base y una lista de nombres.

    Args:
        ruta_base (str): Ruta base donde se encuentran las imágenes.
        nombres (list): Lista de nombres de archivos.
        escala (float): Factor de escala.

    Returns:
        list: Lista de imágenes escaladas.
    """
    imagenes = []
    for nombre in nombres:
        ruta = ruta_base + nombre
        img = cargar_y_escalar_imagen(ruta, escala)
        if img:
            imagenes.append(img)
        else:
            print(f"Imagen no encontrada o fallida: {ruta}")
    return imagenes

def cargar_assets():
    """
    Carga y escala todos los recursos necesarios para el juego.

    Returns:
        dict: Diccionario con los recursos cargados.
    """
    assets = {}

    # Cargar sprites del jugador
    nombres_jugador = [f"Player_{i}.png" for i in range(7)]
    assets["jugador_walk"] = cargar_y_escalar_varias(RUTA_SPRITES_JUGADOR, nombres_jugador, ESCALA_SPRITES_JUGADOR)

    # Cargar arma y balas
    assets["pistola"] = cargar_y_escalar_imagen(RUTA_SPRITES_ARMA + "Pistola.png", ESCALA_SPRITES_JUGADOR)
    assets["bala"] = cargar_y_escalar_imagen(RUTA_SPRITES_ARMA + "Bala.png", ESCALA_SPRITES_JUGADOR)

    # Cargar sprites del enemigo
    nombres_esqueleto = [f"Esqueleton_{i}.png" for i in range(10)]
    assets["esqueleton_walk"] = cargar_y_escalar_varias(RUTA_SPRITES_ENEMIGOS, nombres_esqueleto, ESCALA_SPRITES_ENEMIGO)

    return assets

def dibujar_texto(superficie, texto, x, y, fuente, color=(255, 255, 255)):
    """
    Dibuja texto en la superficie proporcionada.

    Args:
        superficie (Surface): Superficie donde se dibuja el texto.
        texto (str): Texto a mostrar.
        x (int): Posición X del texto.
        y (int): Posición Y del texto.
        fuente (Font): Fuente utilizada para el texto.
        color (tuple): Color del texto en formato RGB (por defecto blanco).
    """
    try:
        imagen_texto = fuente.render(texto, True, color)
        superficie.blit(imagen_texto, (x, y))
    except Exception as e:
        print(f"Error al dibujar texto '{texto}': {e}")




