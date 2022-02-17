import re

def readDictionary():
    words_file = open("words.txt", "r")

    list_of_word = []
    for word in words_file:
        stripped_word = word.strip()
        list_of_word.append(stripped_word)

    words_file.close()

    return list_of_word

def writeDictionary(list_of_word):
    f = open("words.txt", "w")
    for word in list_of_word:
        f.write(word.lower())
        f.write('\n')
    f.close()

def main():
    wordlist = readDictionary()
    wordlist = [w for w in wordlist if len(w) == 5]
    print("5 letter: " + str(len(wordlist)))
    str_match_reg = '^[^\'|\.][^\'|\.][^\'|\.][^\'|v][^\'|\.]$'
    wordlist = [w for w in wordlist if re.match(str_match_reg, w.lower())]
    print("remove symbol: " + str(len(wordlist)))
    writeDictionary(wordlist)

# run main function
if __name__ == "__main__":
    main()
