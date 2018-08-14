import itertools
import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)


draw = ['T', 'I', 'I', 'G', 'T', 'T','L']

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""

    draw_strings = _get_permutations_draw(draw)

    draw_words = []

    for ds in draw_strings:
        if ds.lower() in dictionary:
            draw_words.append(ds.lower())

    return draw_words


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""

    perm_tuples = []

    for i in range(1,len(draw)):
        perm_tuples.extend(list(itertools.permutations(draw, r=i)))

    perm_strings = []

    for pt in perm_tuples:
        perm_strings.append(''.join(pt))

    return perm_strings


if __name__ == '__main__':
    get_possible_dict_words(draw)