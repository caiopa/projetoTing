import os
import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith('.txt'):
            print(f"Formato inválido", file=sys.stderr)
        else:
            with open(path_file, 'r') as file:
                return file.read().split("\n")    
    except:
       print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
