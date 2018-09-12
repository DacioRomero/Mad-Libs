#!/usr/bin/env python3

import re
from random import shuffle

# Used to find substrings in the format [abc]
SUBSTITUTOR = re.compile(r"(\[[a-z]+?\])")

def mad_libs(story):
    print(re.sub(SUBSTITUTOR, '___', story))

    # Find all unique subsititours, and create a dictionary of lists of words
    word_dict = {t: [input_word("Enter a(n) {}: ".format(t[1:-1])) for _ in range(story.count(t))]
                 for t in set(re.findall(SUBSTITUTOR, story))}

    for key in word_dict:
        shuffle(word_dict[key])

    # Split string into pieces based on and including substitutor
    # and replace substitutor with word in dictionary to create completed story
    formatted_story = ''.join(word_dict[sec].pop(0) if sec in word_dict else sec
                              for sec in re.split(SUBSTITUTOR, story))

    print('-' * 32)
    print(formatted_story)

def input_word(prompt):
    word = input(prompt)

    while not word or not all(c.isalpha() or c.isspace() for c in word):
        print('Invalid input')
        word = input(prompt)

    return word

if __name__ == '__main__':
    mad_libs('''Be kind to your [noun]-footed [noun].
For a duck may be somebody\'s [noun],
Be kind to your [noun] in [place].
Where the weather is always [adjective].
You may think that this is the [noun],
Well it is.''')
