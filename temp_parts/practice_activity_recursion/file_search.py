import os
from os.path import isfile, join


def search(full_path: str, filename: str):
    print('checking:', full_path)
    if filename in full_path:
        print("Found " + filename + ' in ' + full_path)
        return True
    if isfile(full_path):
        return
    for file in os.listdir(full_path):
        if search(join(full_path, file), filename):
            return

search('C:\\Users\Home\Documents', '1.nip')
