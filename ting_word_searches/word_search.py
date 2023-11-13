def exists_word(word, instance):
    result = []

    for i in range(len(instance)):
        file_data = instance.search(i)
        file_name = file_data['nome_do_arquivo']
        occurrences = []

        for line_number, line in enumerate(file_data['linhas_do_arquivo'],
                                           start=1):
            if word.lower() in line.lower():
                occurrences.append({"linha": line_number})

        if occurrences:
            word_info = {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences
            }
            result.append(word_info)

    return result


def search_by_word(word, instance):
    result = []

    for i in range(len(instance)):
        file_data = instance.search(i)
        file_name = file_data['nome_do_arquivo']
        occurrences = []

        for line_number, line in enumerate(file_data['linhas_do_arquivo'],
                                           start=1):
            if word.lower() in line.lower():
                occurrences.append({"linha": line_number, "conteudo": line})

        if occurrences:
            word_info = {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences
            }
            result.append(word_info)

    return result
