import nltk
import re

# download dictionary, when first run this program
# nltk.download('words')

# set console font color following wordle rule
class bcolors:
    UNEXIST = '\033[30m\033[100m'
    CURRECT = '\033[30m\033[102m'
    WrongPos = '\033[30m\033[43m'
    ENDC = '\033[0m'
    
# validate the answer entering by user
def str_answer_validation(str_answer):
    if(len(str_answer) == 5):
        for letter in str_answer:
            if(not letter.isalpha()):
                # print(letter)
                return 0
    else:
        return 0
    
    return 1

# validate the status entering by user form wordle result
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

# input answer with validation
def input_answer():
    str_answer_validation_status = 0
    while True:
        print('Please input your answer: ')
        str_answer = input()
        if (str_answer_validation(str_answer) == 1):
            return str_answer
        else:
            print('The length of answer MUST equal 5 and MUST be an alphabet.')
    
# input status with validation
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

# show answer and status following wordle rules with user entering
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

def sorted_by_wrong_pos_letter(wordlist, letterArray):
    str_reg_msg = ''
    str_match_msg = ''
    for i in range(0, len(letterArray)):
        str_match_msg += letterArray[i]
        if(i < len(letterArray)):
            str_match_msg += '|'
    temp_str_match_msg = ''
    for i in range(0, 5):
        temp_list_match_msg = list('^.....$')
        temp_list_match_msg[i+1] = str_match_msg
        str_reg_msg += ''.join(temp_list_match_msg)
        if(i < 5):
            str_reg_msg += '|'

    return [w for w in wordlist if re.match("^"+str_reg_msg+"$", w.lower())]


# compare and match by regex, return recommand list
def check_recommand(str_answer, str_status, wordlist):
    letterArray = []
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
            letterArray.append(str_answer[count])
            list_match_reg = list('^.....$')
            list_match_reg[count+1] = '[^'+str_answer[count]+']'
            str_match_reg = ''.join(list_match_reg)
            # print(str_match_reg)
            # print(wordlist)
            wordlist = [w for w in wordlist if re.search(str_match_reg, w.lower())]
            # print(wordlist)
            count+=1
    
    str_regex_current = ''.join(list_regex_current)
    # print(str_regex_current)
    # print(str_regex_wrongPos)
    if(len(letterArray) != 0):
        wordlist = sorted_by_wrong_pos_letter(wordlist, letterArray)
    if(str_regex_current != '^.....$'):
        # print(str_regex_current)
        # print(wordlist[:20])
        wordlist = [w for w in wordlist if re.match(str_regex_current, w.lower())]
        # print(wordlist[:20])
    #print(wordlist)
    #sort_by_rule(str_answer, str_status, wordlist)
    #print(wordlist)
    return wordlist # return top 20 result

# show recommand list by table
def show_recommand_word(result):
    print('Recommand Answer: ')
    count = 1
    for word in result[:20]:
        print(str(count) + '\t' + word)
        count+=1

# main function
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

# run main function
if __name__ == "__main__":
    main()