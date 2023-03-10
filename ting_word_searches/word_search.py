from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    results = []

    for item in instance.items:
        occurrences = [
            {"linha": i + 1}
            for i, line in enumerate(item["linhas_do_arquivo"])
            if word.lower() in line.lower()
        ]
        if occurrences:
            results.append({
                "palavra": word.lower(),
                "arquivo": item["nome_do_arquivo"],
                "ocorrencias": occurrences
            })

    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
