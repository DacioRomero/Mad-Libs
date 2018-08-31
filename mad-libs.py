import re

def print_story(story, vars=[]):
    new_format = ''.join('underscore' if c.isdigit() and int(c) >= len(vars) else c for c in story)
    print(new_format.format(*vars, underscore="___"))

def main():
    story = "There was once a {0} that had a {1}."
    print_story(story)

    vars = []
    for _ in range(story.count('{')):
        vars.append(input("Enter a word: "))
        print_story(story, vars)

if __name__ == '__main__':
    main()
