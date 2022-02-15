import nltk
import re
# nltk.download('words')
class bcolors:
    UNEXIST = '\033[30m\033[100m'
    CURRECT = '\033[30m\033[102m'
    WrongPos = '\033[30m\033[43m'
    ENDC = '\033[0m'
    

def str_answer_validation(str_answer):
    if(len(str_answer) == 5):
        for letter in str_answer:
            if(not letter.isalpha()):
                # print(letter)
                return 0
    else:
        return 0
    
    return 1

def str_status_validation(str_status):
    if(len(str_status) == 5):
        for letter in str_status:
            if(not letter.isdigit() or int(letter) > 2):
                # print(letter)
                print(letter.isdigit())
                return 0
    else:
        return 0
    return 1

def input_answer():
    str_answer_validation_status = 0
    while True:
        print('Please input your answer: ')
        str_answer = input()
        if (str_answer_validation(str_answer) == 1):
            return str_answer
        else:
            print('The length of answer MUST equal 5 and MUST be an alphabet.')
    

def input_status():
    str_status_validation_status = 0
    while True:
        print('Please input the wordle status: ')
        print('(0: not exist, 1: current position, 2: exist but wrong position)')
        str_status = input()
        if (str_status_validation(str_status) == 1):
            return str_status
        else:
            print('The length of answer MUST equal 5 and MUST be an digital.')

def show_answer_status(str_answer, str_status):
    count = 0
    current_status = ""
    for status in str_status:
        if int(status) == 0 :
            current_status += bcolors.UNEXIST + str_answer[count] + bcolors.ENDC
            count+=1
        elif int(status) == 1 :
            current_status += bcolors.CURRECT + str_answer[count] + bcolors.ENDC
            count+=1
        elif int(status) == 2 :
            current_status += bcolors.WrongPos + str_answer[count] + bcolors.ENDC
            count+=1
    print(current_status)


def check_recommand(str_answer, str_status, wordlist):
    list_regex_current = list('^.....$')

    
    count = 0
    current_status = ""
    for status in str_status:
        if int(status) == 0 :
            list_match_reg = list('^.....$')
            list_match_reg[count+1] = '[^'+str_answer[count]+']'
            str_match_reg = ''.join(list_match_reg)
            wordlist = [w for w in wordlist if re.match(str_match_reg, w.lower())]
            
            count+=1
        elif int(status) == 1 :
            list_regex_current[count+1] = str_answer[count]
            count+=1
        elif int(status) == 2 :
            list_match_reg = list('^.....$')
            list_match_reg[count+1] = '[^'+str_answer[count]+']'
            str_match_reg = ''.join(list_match_reg)
            print(str_match_reg)
            print(wordlist)
            wordlist = [w for w in wordlist if re.search(str_match_reg, w.lower())]
            print(wordlist)
            count+=1
    
    str_regex_current = ''.join(list_regex_current)
    # print(str_regex_current)
    # print(str_regex_wrongPos)
    if(str_regex_current != '^.....$'):
        print(str_regex_current)
        print(wordlist[:20])
        wordlist = [w for w in wordlist if re.match(str_regex_current, w.lower())]
        print(wordlist[:20])
    #print(wordlist)
    #sort_by_rule(str_answer, str_status, wordlist)
    #print(wordlist)
    return wordlist # return top 20 result

def show_recommand_word(result):
    print('Recommand Answer: ')
    count = 1
    for word in result[:20]:
        print(str(count) + '\t' + word)
        count+=1


def main():
    wordlist = nltk.corpus.words.words()
    wordlist = [w for w in wordlist if len(w) == 5]
    # print(wordlist)
    # print([w for w in wordlist if re.search('^..a..', w)])

    while True:
        str_answer = input_answer()
        str_status = input_status()
        show_answer_status(str_answer, str_status)
        wordlist = check_recommand(str_answer, str_status, wordlist)
        show_recommand_word(wordlist)

if __name__ == "__main__":
    main()

    




    

    



                