def hash_function(key):
    return sum(index * ord(character) for index, character in enumerate(repr(key).lstrip("'"), start=1))

print(hash_function('abc'))
print(hash_function('bac'))
print(hash_function('bbb'))

print(hash_function(3.14))
print(hash_function('3.14'))

print(ord('c'))