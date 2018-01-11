import sys
import nltk.data
import re


def main(script_filename, character_name):
    script = open(script_filename, 'r')

    character_words = []
    dude_line = False
    for l in script:
        line = l.strip()
        if not line:
            dude_line = False
        elif line == character_name:
            dude_line = True
            continue
        if dude_line:
            # print(line)
            cleaned_line = re.sub("[\(\[].*?[\)\]]", "", line).replace('--', ' ')
            character_words.append(cleaned_line + ' ')
            # dude_sentences.write(line + ' ')

    script.close()
    nltk.download()
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    for sentence in tokenizer.tokenize(''.join(character_words)):
        if sentence == '.':
            continue
        print(sentence)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write('Please, enter filename and character_name')
    main(sys.argv[1], sys.argv[2])
