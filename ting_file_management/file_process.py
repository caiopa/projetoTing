from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for item in range(len(instance)):
        if instance.search(item)["nome_do_arquivo"] == path_file:
            return None

    file = txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }
    instance.enqueue(data)
    print(data, file=sys.stdout)


def remove(instance):
    if (len(instance) == 0):
        print("Não há elementos", file=sys.stdout)
        return None
    removed = instance.dequeue()
    file_name = removed["nome_do_arquivo"]

    print(f"Arquivo {file_name} removido com sucesso")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        print(file, file=sys.stdout)
    except IndexError:
        return sys.stderr.write("Posição inválida")
