def is_member(word_list, elem):
    if not word_list:
        return False
    else:
        if word_list[0] == elem:
            return True
        else:
            return is_member(word_list[1:], elem)

print(is_member(['c','a','t'], 'c'))