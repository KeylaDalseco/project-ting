from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for item in instance._data:
        if item['nome_do_arquivo'] == path_file:
            sys.stderr.write(f"O arquivo {path_file}"
                             "já foi processado anteriormente.\n")
            return

    lines = txt_importer(path_file)

    if lines is None:
        return
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }

    instance.enqueue(data)
    print(data)


def remove(instance):
    if len(instance) > 0:
        remove = instance.dequeue()
        print(
            f'Arquivo {remove["nome_do_arquivo"]} removido com sucesso',
            file=sys.stdout,
            )
    else:
        print("Não há elementos")


def file_metadata(instance, position):
    try:
        file_data = instance.search(position)
        print(file_data, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
