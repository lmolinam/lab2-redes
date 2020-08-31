from os.path import join

MAPEO_00 = "00100"
MAPEO_01 = "01011"
MAPEO_10 = "10110"
MAPEO_11 = "11001"

def leer_archivo_como_lista(path, file_name):
    with open(join(path, file_name), 'r') as txt_file:
        data = list(txt_file.read())
    
    return data

def leer_archivo(path, file_name):
    with open(join(path, file_name), 'r') as txt_file:
        data = txt_file.read()
    
    return data

def escribir_archivo(path, file_name, data):
    with open(join(path, file_name), 'w', encoding="utf-8") as txt_file:
        txt_file.write(data)