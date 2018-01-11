import sys
import re


BETWEEN_BRACKETS = re.compile('[\(\[\*].*?[\)\]\*]')
UNWANTED_SYMBOLS = ['…']


def parse(character, script_file):
    regex = re.compile('^{}: (.*)'.format(character), flags=re.IGNORECASE)
    for i, raw_line in enumerate(script_file):
        if not raw_line:
            continue
        is_hero_phrase = regex.match(raw_line.strip())
        if is_hero_phrase:
            # Remove reactions/actions
            line = BETWEEN_BRACKETS.sub('', is_hero_phrase.group(1))
            cleaned_line = ' '.join(line.replace('…', '').split())
            yield cleaned_line


def main():
    if len(sys.argv) < 3:
        print('Specify character and at least one file')
    character = sys.argv[1]
    file_names = sys.argv[2:]
    lines = []
    for file_name in file_names:
        with open(file_name) as script_file:
            for line in parse(character, script_file):
                lines.append(line)
    for l in lines:
        print(l)


if __name__ == '__main__':
    main()
