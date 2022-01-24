"""
Student code for Word Wrangler game
"""

import urllib3
import SimpleGUICS2Pygame.codeskulptor as codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    sorted_list = list(list1)
    for index in range(len(list1))[1:]:
        if list1[index - 1] == list1[index]:
            sorted_list.remove(list1[index])
        else:
            continue
    return sorted_list


def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    if list1 == [] or list2 == []:
        return []
    elif list1[0] < list2[0]:
        return intersect(list1[1:], list2)
    elif list1[0] == list2[0]:
        return [list1[0]] + intersect(list1[1:], list2[1:])
    else:
        return intersect(list1, list2[1:])


# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """
    if list1 == [] and list2 == []:
        return []
    temp_list1 = list(list1)
    temp_list2 = list(list2)
    temp_list = []
    if list1[-1] <= list2[0]:
        return list1 + list2
    else:
        if list1[0] >= list2[-1]:
            return list2 + list1
        else:
            while len(temp_list1) != 0 and len(temp_list2) != 0:
                if temp_list1[0] < temp_list2[0]:
                    temp_list.append(temp_list1[0])
                    temp_list1.pop(0)
                elif temp_list1[0] > temp_list2[0]:
                    temp_list.append(temp_list2[0])
                    temp_list2.pop(0)
                else:
                    temp_list.append(temp_list1[0])
                    temp_list.append(temp_list2[0])
                    temp_list1.pop(0)
                    temp_list2.pop(0)
            if temp_list1:
                return temp_list + temp_list1
            else:
                return temp_list + temp_list2


def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    list1 = list(list1)
    if not list1:
        return []
    for index in range(len(list1))[1:]:
        if list1[index] < list1[0]:
            temp_var = list1[0]
            list1[0] = list1[index]
            list1[index] = temp_var
    return [list1[0]] + merge_sort(list1[1:])


# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    temp_list = ['']
    alphabet = [letter for letter in word]
    if len(word) == 1:
        temp_list.append(word[0])
        return temp_list
    else:
        for index in range(len(word)):
            elements_remain = alphabet[:index] + alphabet[index + 1:]
            perms = gen_all_strings(elements_remain)
            for perm in perms:
                temp_list.append(alphabet[index] + str(perm))
    return temp_list


# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []


def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)


# Uncomment when you are ready to try the game
# run()

# print(remove_duplicates([8,8]))
# print(merge([3, 4, 5, 6, 7, 9, 11], [3, 4, 5, 13]))
# print(intersect([0,2,3,5,8], [1, 2, 4, 5, 7, 8, 10]))
# print(merge_sort([9, 3, 5, 1]))
print(gen_all_strings('ab'))