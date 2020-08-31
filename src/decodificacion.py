import sys
from os.path import dirname, join, abspath

import utils

PATH_INPUT = join(dirname(dirname(abspath(__file__))), "inputs", "decodificacion")
PATH_OUTPUT = join(dirname(dirname(abspath(__file__))), "outputs", "decodificacion")
ARCHIVO_ENTRADA = 'codificación-recibida.txt'
ARCHIVO_SALIDA = 'salida.txt'

def contar_diferencias(palabra_real, palabra_esperada):
    if palabra_real == palabra_esperada:
        return 0
    
    return sum(1 for a, b in zip(palabra_real, palabra_esperada) if a != b) + abs(len(palabra_real) - len(palabra_esperada))

def determinar_mas_cercano(palabra):
    mas_cercano = ""
    dif_00 = contar_diferencias(palabra, utils.MAPEO_00)
    dif_01 = contar_diferencias(palabra, utils.MAPEO_01)
    dif_10 = contar_diferencias(palabra, utils.MAPEO_10)
    dif_11 = contar_diferencias(palabra, utils.MAPEO_11)

    dif_minima = min([dif_00, dif_01, dif_10, dif_11])

    if dif_00 == dif_minima:
        mas_cercano = "00"
    elif dif_01 == dif_minima:
        mas_cercano = "01"
    elif dif_10 == dif_minima:
        mas_cercano = "10"
    elif dif_11 == dif_minima:
        mas_cercano = "11"

    
    return mas_cercano


def corregir_error(palabra):
    if palabra == utils.MAPEO_00:
        return "00"
    elif palabra == utils.MAPEO_01:
        return "01"
    elif palabra == utils.MAPEO_10:
        return "10"
    elif palabra == utils.MAPEO_11:
        return "11"
    else:
        return determinar_mas_cercano(palabra)

def decodificar_mensaje(mensaje_recibido):
    largo_mapeo = 5
    contador = 0
    palabra = ""
    decoded_data = ""
    for bit in mensaje_recibido:
        contador = contador + 1
        palabra = f"{palabra}{bit}"
        if contador == largo_mapeo:
            decoded_data = f"{decoded_data}{corregir_error(palabra)}"
            contador = 0
            palabra = ""

    return decoded_data

def obtener_caracteres(mensaje_binario):
    largo_byte = 8
    contador = 0
    bits_caracter = ""
    mensaje = ""
    for bit in mensaje_binario:
        contador = contador + 1
        bits_caracter = f"{bits_caracter}{bit}"
        if contador == largo_byte:
            mensaje = f"{mensaje}{chr(int(bits_caracter, base=2))}"
            contador = 0
            bits_caracter = ""


    return mensaje


if len(sys.argv) < 2:
    print("No se dió como argumento nombre de txt utilizado como salida para proceso")
    print("ej: python src/decodificacion.py resultado.txt")
    print(f"Se intetará tomar nombre default '{ARCHIVO_SALIDA}'")
else:
    ARCHIVO_SALIDA = sys.argv[1]

mensaje_recibido = utils.leer_archivo(PATH_INPUT, ARCHIVO_ENTRADA)
mensaje_decodificado = decodificar_mensaje(mensaje_recibido)
mensaje_final = obtener_caracteres(mensaje_decodificado)
utils.escribir_archivo(PATH_OUTPUT, ARCHIVO_SALIDA, mensaje_final)