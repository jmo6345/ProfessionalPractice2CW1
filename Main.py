#this is the main file for the program, it will hold the core features
import time
word = "hello"

def typetime():
    start = time.time()
    said = input('Type the word: '+ word)
    while said != word:
        print('Incorrect word typed, try again.')
        said = input('Type the word: '+ word)
    end = time.time()
    return end-start, said
#this function measures the time taken for a user to type a specific word


timetaken, userword = typetime()
print('You typed: ' + userword + ' in ' + str(timetaken) + ' seconds')
if (timetaken < 5):
    print('Great job you win!')
else:
    print('Too slow, you lose!')
#this function shows what word a user typed and how long it took them, and tells them if they win or lose based on their time
