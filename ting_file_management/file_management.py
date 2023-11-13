import sys
extensao = '.txt'


def txt_importer(path_file):
    try:
        if extensao in path_file:
            with open(path_file, 'r', encoding='utf-8') as file:
                lines = file.read().split('\n')
            return lines
        else:
            sys.stderr.write("Formato inválido\n")
            return None
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        return None
