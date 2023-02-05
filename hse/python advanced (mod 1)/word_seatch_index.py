def solve(input_words):
    final_dictionary = {}
    for word in input_words:
        final_dictionary.setdefault(word[0], {}).setdefault(word[:2], []).append(word)
    for value in final_dictionary.values():
        for item_list in value.values():
            item_list.sort()
    return final_dictionary
