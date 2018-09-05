import re
from random import shuffle

SUBSTITUTOR = re.compile(r"(\[[a-z]+?\])")

def main():
    story = 'Be kind to your [noun]-footed [noun]. For a duck may be somebody`s [noun], Be kind to your [noun] in [place]. Where the weather is always [adjective]. You may think that this is the [noun], Well it is.'
    print(re.sub(SUBSTITUTOR, '___', story))
    word_dict = {t: [input("Enter a(n) {}: ".format(t[1:-1])) for _ in range(story.count(t))]
                 for t in set(re.findall(SUBSTITUTOR, story))}
    formatted_story = ''.join(word_dict[sec].pop(0) if sec in word_dict else sec
                              for sec in re.split(SUBSTITUTOR, story))
    for key in word_dict:
        shuffle(word_dict[key])

    print(formatted_story)

if __name__ == '__main__':
    main()
