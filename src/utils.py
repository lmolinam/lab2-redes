from os.path import join

def leer_archivo(path, file_name):
    with open(join(path, file_name), 'r') as txt_file:
        data = list(txt_file.read())
    
    return data

def escribir_archivo(path, file_name, data):
    with open(join(path, file_name), 'w') as txt_file:
        txt_file.write(data)