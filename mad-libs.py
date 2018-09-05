import re

SUBSTITUTOR = re.compile(r"(\[[a-z]+?\])")

def main():
    story = 'There was once a(n) [noun] that had a(n) [verb].'
    word_dict = {t: [input("Enter a(n) {}: ".format(t[1:-1])) for _ in range(story.count(t))]
                 for t in set(re.findall(SUBSTITUTOR, story))}
    formatted_story = ''.join(word_dict[sec].pop(0) if sec in word_dict else sec
                              for sec in re.split(SUBSTITUTOR, story))
    print(formatted_story)

if __name__ == '__main__':
    main()
