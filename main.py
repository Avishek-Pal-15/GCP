import random
import requests
import vlc
from contextlib import redirect_stdout
from io import StringIO
import time


def knowMore(word):
    response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/{}'.format(word))
    obj = response.json()
    url = obj[0]['phonetics'][0]['audio']
    p = vlc.MediaPlayer("https:{}".format(url))
    with redirect_stdout(StringIO()):
        p.play()
    time.sleep(2)
    print('Meaning:', obj[0]['meanings'][0]['definitions'][0]['definition'])
    try:
        print('Example in a sentence:', obj[0]['meanings'][0]['definitions'][0]['example'])
    except:
        print()
    print('Synonyms:', obj[0]['meanings'][0]['definitions'][0]['synonyms'])
    print('Antonyms:', obj[0]['meanings'][0]['definitions'][0]['antonyms'])
    # print("\n")


def pickWord():
    words = ['computer', 'science', 'random', 'book', 'student',
             'status', 'country', 'education', 'school',
             'apple', 'mango', 'orange', 'aeroplane']

    pickedWord = random.choice(words)

    return pickedWord


def shuffleWord(pickedWord):
    pickedWord = random.sample(pickedWord, len(pickedWord))
    jumbledWord = ''.join(pickedWord)
    return jumbledWord


score = 0


def play():
    global score
    pickedWord = pickWord()

    jumbledWord = shuffleWord(pickedWord)

    print("\nJumbled word is :", jumbledWord)

    ans = input("\nGuess the word or Press D to display solution or Press Q to quit: ")

    while 1:

        if ans == pickedWord:  # user guessed the word correctly
            score += 5
            print('\nCorrect answer. Score is', score,
                  '. Press K to know more about the word or Press P to play again or Press Q to quit: ')
            ans = input()

        elif ans == 'P':  # user wants to play again
            play()

        elif ans == 'D':  # user wants to display the answer
            score -= 1
            print('\nThe word was:', pickedWord, 'Score is:', score)
            print('\nPress K to know more about the word or Press P to play again or Press Q to quit: ')
            ans = input()

        elif ans == 'K':  # user wants to know more about the word
            knowMore(pickedWord)
            print('\nPress P to play again or Press Q to quit: ')
            ans = input()

        elif ans == 'Q':  # user wants to quit playing
            quit()

        else:  # user guessed incorrectly
            score -= 2
            print('\nWrong answer. Score is', score, 'Try again or press D to display solution or press Q to quit: ')
            ans = input()


# Driver code
if __name__ == '__main__':
    print('Welcome to my word guessing game.')
    print('You gain 5 points for every correct answer.')
    print('You lose 2 point for every wrong answer.')
    print('You lose 1 point for displaying answer.')
    print('Please ignore the PREFETCH STREAM MESSAGE.')
    play()
