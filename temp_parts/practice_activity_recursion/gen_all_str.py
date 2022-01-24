def gen_all_str(word):
    temp_list = ['']
    alphabet = [letter for letter in word]
    if len(word) == 1:
        temp_list.append(word[0])
        return temp_list
    else:
        for index in range(len(word)):
            elements_remain = alphabet[:index] + alphabet[index + 1:]
            perms = gen_all_str(elements_remain)
            for perm in perms:
                temp_list.append(alphabet[index] + str(perm))
    return temp_list


# print(gen_all_str('abc'))
print(gen_all_str('abc'))
