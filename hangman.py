import random

import pyglet

music = pyglet.resource.media('OldTownRoad.mp3')
music.play()

f = open('wordlist.txt', 'r')
words = f.readlines()

english_alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def play():
    players_dict={}
    results=[]
    num_of_players=int(input('Give number of players: '))
    for i in range(1,num_of_players+1):
        a=input('Give name of Player {}: '.format(i))
        players_dict['Player {}'.format(i)]=a
    for i in range(1,num_of_players+1):
        print(players_dict['Player {}'.format(i)])
        r=hangman()
        if r:
            results.append(True)
        else:
            results.append(False)
    while results.count(True)>1:
        for i in range(len(results)):
            if results[i]==True:
                print(players_dict['Player {}'.format(i+1)])
                a=hangman()
                if a:
                    results[i]=True
                else:
                    results[i]=False
    if results.count(True)==1:
        b=results.index(True)+1
        print('And the winner is:',players_dict['Player {}'.format(b)]+'!')
    else:
        print('Nobody won.')
                

def shape(incorrect_guesses=6):
    if incorrect_guesses==1:
        print('|----------|')
        print('|          O')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
    elif incorrect_guesses==2:
        print('|----------|')
        print('|          O')
        print('|         /|\\')
        print('|')
        print('|')
        print('|')
        print('|') 
    elif incorrect_guesses==3:
        print('|----------|')
        print('|          O')
        print('|         /|\\')
        print('|          |')
        print('|')
        print('|')
        print('|')
    elif incorrect_guesses==4:
        print('|----------|')
        print('|          O')
        print('|         /|\\')
        print('|          |')
        print('|        _/ \\_')
        print('|')
        print('|')
    elif incorrect_guesses==5:
        print('|----------|')
        print('|          O')
        print('|         /|\\')
        print('|          |')
        print('|        _/ \\_')
        print('|        ## ##')
        print('|')
    else:
        print('|----------|')
        print('|          O')
        print('|         /|\\')
        print('|          |')
        print('|        _/ \\_')
        print('|        ## ##')
        print('|         fire')

def get_word(random_word,new_word,letter):
    for i in range(len(random_word)):
        if random_word[i]==letter and new_word[i]=='_':
            new_word=list(new_word)
            new_word[i]=letter
            new_word=''.join(new_word)
    return new_word

def found_word(random_word,new_word):
    if new_word==random_word:
        return True
        
def hangman():
    found=False
    random_word=random.choice(words)
    words.remove(random_word)
    used_letters=[]
    incorrect_guesses=0
    new_word=len(random_word)*'_'
    print('You can make up to 5 mistakes.')
    print('The 6th mistake will put you out of the game.')
    print('The word you have to guess is:',new_word,'which has',len(random_word),'letters.')
    while not found and incorrect_guesses<=5:
        letter=input('Give letter: ')
        if letter in random_word and letter not in used_letters:
            used_letters.append(letter)
            print('The word you have to guess is:',get_word(random_word,new_word,letter))
            new_word=get_word(random_word,new_word,letter)
            if found_word(random_word,new_word):
                print('Congratulations! You found the word!')
                found=True
        elif letter not in english_alphabet:
            print('You did not give a letter. Please try again.')
        elif letter in used_letters:
            print('This letter has already been used.')
        else:
            used_letters.append(letter)
            incorrect_guesses+=1
            shape(incorrect_guesses)
            if incorrect_guesses==6:
                break
            else:
                if incorrect_guesses!=5:
                    print('You still have ',5-incorrect_guesses,'lives.')
                else:
                    print('You lost your 5 lives. The next mistake will put you out of the game.')
                print('The word you have to guess is:',get_word(random_word,new_word,letter))
                new_word=get_word(random_word,new_word,letter)                
    if not found:
        print('You did not manage to find the word.')
        print('The word we were looking for was:',random_word)
        return False
    else:
        return True

play()

pyglet.app.run()
