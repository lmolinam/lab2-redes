import sys
from os.path import dirname, join, abspath

import utils

PATH_INPUT = join(dirname(dirname(abspath(__file__))), "inputs", "codificacion")
PATH_OUTPUT = join(dirname(dirname(abspath(__file__))), "outputs", "codificacion")
ARCHIVO_ENTRADA = 'mensaje.txt'
ARCHIVO_SALIDA = 'codificación-enviada.txt'

def rellenar_byte(byte):
    while len(byte) < 8:
        byte = f"0{byte}"
    
    return byte

def mensaje_a_binario(nombre_archivo):
    data = utils.leer_archivo(PATH_INPUT, nombre_archivo)
    binary_data = [rellenar_byte(bin(ord(char))[2:])  for char in data]

    return binary_data

def binario_a_palabra(mensaje_binario):
    coded_data = ""
    for byte in mensaje_binario:
        byte_iterator = iter(byte)
        for bit in byte_iterator :
            next_bit = next(byte_iterator)
            if bit == "0" and next_bit == "0":
                coded_data = f"{coded_data}00100"
            elif bit == "0" and next_bit == "1":
                coded_data = f"{coded_data}01011"
            elif bit == "1" and next_bit == "0":
                coded_data = f"{coded_data}10110"
            elif bit == "1" and next_bit == "1":
                coded_data = f"{coded_data}11001"
    print(coded_data)
    utils.escribir_archivo(PATH_OUTPUT, ARCHIVO_SALIDA, coded_data)


if len(sys.argv) < 2:
    print("No se dió como argumento nombre de txt utilizado como input para proceso")
    print("ej: python src/codificacion.py archivo.txt")
    print(f"Se intetará tomar nombre default '{ARCHIVO_ENTRADA}'")
else:
    ARCHIVO_ENTRADA = sys.argv[1]

mensaje_binario = mensaje_a_binario(ARCHIVO_ENTRADA)
binario_a_palabra(mensaje_binario)