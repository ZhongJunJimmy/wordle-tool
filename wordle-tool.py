#import nltk
import re

# download dictionary, when first run this program
# nltk.download('words')

# set console font color following wordle rule
class bcolors:
    UNEXIST = '\033[30m\033[100m'
    CURRECT = '\033[30m\033[102m'
    WrongPos = '\033[30m\033[43m'
    HINT = '\033[96m'
    INFO = '\033[92m'
    ERROR = '\033[91m'
    WARN = '\033[93m'
    ENDC = '\033[0m'
    
# validate the answer entering by user
def str_answer_validation(str_answer, word_length):
    if(len(str_answer) == word_length):
        for letter in str_answer:
            if(not letter.isalpha()):
                # print(letter)
                return 0
    else:
        return 0
    
    return 1

# validate the status entering by user form wordle result
def str_status_validation(str_status, word_length):
    if(len(str_status) == word_length):
        for letter in str_status:
            if(not letter.isdigit() or int(letter) > 2):
                # print(letter)
                # print(letter.isdigit())
                return 0
    else:
        return 0
    return 1

# input answer with validation
def input_answer(word_length):
    str_answer_validation_status = 0
    while True:
        print(bcolors.INFO + 'Please input your answer or -1 to quit, -2 to reset: ' + bcolors.ENDC)
        str_answer = input()
        if (str_answer_validation(str_answer, word_length) == 1 or str_answer == '-1' or str_answer == '-2'):
            return str_answer
        else:
            print(bcolors.ERROR + 'Error: The length of answer MUST equal ' + str(word_length) + ' and MUST be an alphabet Also you can enter -1 to quit, -2 to reset.' + bcolors.ENDC)
    
# input status with validation
def input_status(word_length):
    str_status_validation_status = 0
    while True:
        print(bcolors.INFO + 'Please input the wordle status or -1 to reset answer word: ' + bcolors.ENDC)
        print(bcolors.INFO + '(0: not exist, 1: current position, 2: exist but wrong position)' + bcolors.ENDC)
        str_status = input()
        if (str_status_validation(str_status, word_length) == 1 or str_status == '-1'):
            return str_status
        else:
            print(bcolors.ERROR + 'Error: The length of answer MUST equal ' + str(word_length) + ' and MUST be an digital. Also you can enter -1 to reset answer word' + bcolors.ENDC)

# show answer and status following wordle rules with user entering
def show_answer_status(data_answer_array):
    count = 0
    current_status = ""
    for data in data_answer_array:
        if (data[1] == 0) :
            current_status += bcolors.UNEXIST + data[0] + bcolors.ENDC
            count+=1
        elif (data[1] == 1) :
            current_status += bcolors.CURRECT + data[0] + bcolors.ENDC
            count+=1
        elif (data[1] == 2) :
            current_status += bcolors.WrongPos + data[0] + bcolors.ENDC
            count+=1
    print(current_status)

def sorted_by_wrong_pos_letter(wordlist, letterArray, word_length):
    str_reg_msg = ''
    str_match_msg = ''
    for i in range(0, len(letterArray)):
        str_match_msg += letterArray[i]
        if(i < len(letterArray)):
            str_match_msg += '|'
    str_word_len_reg = ''
    for i in range(0, word_length):
        for j in range(0,  word_length):
            str_word_len_reg += '.'
        temp_list_match_msg = list('^' + str_word_len_reg + '$')
        temp_list_match_msg[i+1] = str_match_msg
        str_reg_msg += ''.join(temp_list_match_msg)
        if(i < word_length):
            str_reg_msg += '|'

    return [w for w in wordlist if re.match("^"+str_reg_msg+"$", w)]


# compare and match by regex, return recommend list
def check_recommend(str_answer, str_status, data_answer_array, wordlist, word_length):
    letterArray = []
    str_match_correct_letter_reg = ''
    str_word_len_reg = ''
    for i in range(0, word_length):
        if data_answer_array[i][1] == 0:
            status = []
            for j in range(0,  word_length):
                status.append(0)

            for j in range(0, word_length):
                # print(data_answer_array[j][0])
                # print(data_answer_array[i][0])
                if data_answer_array[j][0] == data_answer_array[i][0]:
                    if data_answer_array[j][1] == 1:
                        status[j] = 1
                    elif data_answer_array[j][1] == 2:
                        status[j] = 2
            if 2 in status:
                for j in range(0,  word_length):
                    str_word_len_reg += '.'
                list_match_reg = list('^' + str_word_len_reg + '$')
                list_match_reg[i] = '[^'+data_answer_array[i][0]+']'
                str_match_reg = ''.join(list_match_reg)
                # print(str_match_reg)
                wordlist = [w for w in wordlist if re.match(str_match_reg, w)]
                str_word_len_reg = ''
                # print(wordlist)
            else:
                for j in range(0,  word_length):
                    str_word_len_reg += '.'
                list_match_reg = list('^' + str_word_len_reg + '$')
                for j in range(0, word_length):
                    if status[j] == 0:
                        list_match_reg[j+1] = '[^' + data_answer_array[i][0] + ']'
                    elif status[j] == 1:
                        list_match_reg[j+1] = data_answer_array[i][0]
                str_match_reg = ''.join(list_match_reg)
                # print(str_match_reg)
                wordlist = [w for w in wordlist if re.match(str_match_reg, w)]
                str_word_len_reg = ''
                # print(wordlist)

        elif data_answer_array[i][1] == 1:
            for j in range(0,  word_length):
                str_word_len_reg += '.'
            list_match_correct_letter_reg = list('^' + str_word_len_reg + '$')
            list_match_correct_letter_reg[i+1] = data_answer_array[i][0]
            str_match_correct_letter_reg = ''.join(list_match_correct_letter_reg)
            # print(str_match_correct_letter_reg)
            wordlist = [w for w in wordlist if re.match(str_match_correct_letter_reg, w)]
            str_word_len_reg = ''
            # print(wordlist)
            
        
        elif data_answer_array[i][1] == 2:
            letterArray.append(data_answer_array[i][0])
            for j in range(0,  word_length):
                str_word_len_reg += '.'
            list_match_reg = list('^' + str_word_len_reg + '$')
            list_match_reg[i+1] = '[^' + data_answer_array[i][0] + ']'
            str_match_reg = ''.join(list_match_reg)
            # print(str_match_reg)
            wordlist = [w for w in wordlist if re.match(str_match_reg, w)]
            str_word_len_reg = ''
            # print(wordlist)


        if(len(letterArray) != 0):
            wordlist = sorted_by_wrong_pos_letter(wordlist, letterArray, word_length)
            # print(wordlist)
    
    return wordlist # return top 20 result

# show recommend list by table
def show_recommend_word(result):
    print(bcolors.HINT + 'Recommend Answer: ' + bcolors.ENDC)
    count = 1
    for word in result[:20]:
        print(bcolors.HINT + str(count) + '\t' + word + bcolors.ENDC)
        count+=1

def checkQuestion(str_question):
    userAnswer = ''
    while (userAnswer != 'y' and userAnswer != 'Y' and userAnswer != 'n' and userAnswer != 'N'):
        print(bcolors.WARN + str_question+' (y/n)' + bcolors.ENDC)
        userAnswer = input()
    if(userAnswer == 'y' or userAnswer == 'Y'):
        return True
    return False

def getDictionary():
    words_file = open("words.txt", "r")

    list_of_word = []
    for word in words_file:
        stripped_word = word.strip()
        list_of_word.append(stripped_word)

    words_file.close()

    return list_of_word

def input_word_length():
    while True:
        print(bcolors.INFO + "Please enter the word length: " + bcolors.ENDC)
        word_length = input()
        if(word_length.isdigit()):
            print(bcolors.HINT + 'You set the word length to ' + word_length + '.' + bcolors.ENDC)
            return word_length
        print(bcolors.ERROR + 'Error: The word length MUST be a digital.' + bcolors.ENDC)
    

# main function
def main():
    word_length = input_word_length()

    #wordlist = nltk.corpus.words.words()
    wordlist = getDictionary()
    wordlist = [w for w in wordlist if re.match(r"^\w{" + word_length + "}$", w.lower())]
    #print(wordlist)
    # print([w for w in wordlist if re.search('^..a..', w)])

    while True:
        data_answer_array = []

        str_answer = input_answer(int(word_length))
        if str_answer == '-1':
            if(checkQuestion('Are you sure to quit the program?')):
                print(bcolors.INFO + 'See you' + bcolors.ENDC)
                break
        elif str_answer == '-2':
            if(checkQuestion('Are you sure to reset the dictionary?')):
                #wordlist = nltk.corpus.words.words()
                wordlist = getDictionary()
                wordlist = [w for w in wordlist if re.match(r"^\w{" + word_length + "}$", w.lower())]
                print(bcolors.HINT + 'The program\'s dictionary had been reset.' + bcolors.ENDC)
        else:
            str_status = input_status(int(word_length))
            if str_status == '-1':
                continue
            for i in range(0,int(word_length)):
                data_answer_array.append([str_answer[i], int(str_status[i])])
            show_answer_status(data_answer_array)
            wordlist = check_recommend(str_answer, str_status, data_answer_array, wordlist, int(word_length))
            show_recommend_word(wordlist)

# run main function
if __name__ == "__main__":

    main()