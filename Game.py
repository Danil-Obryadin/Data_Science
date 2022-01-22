import random

#The Game: the computer makes a guess and guesses the number
def game_number():
    x,y=1,100# the first/last of random number
    number=random.randint(x,y)
    count=0 # the start value of total attempts
    while True:
        count += 1
        guess = random.randint(x,y)
        if guess < number:
            print('your number is less them random number')
            x = guess
        elif guess > number:
            print('your nunber is more them random number')
            y = guess
        else:
            print(f'Yes! The number is {number}, total attempts - {count}')
            break
    return count

# the function for finding the average value of attempts
def average_score():
    start_iter, finish_iter=0,1000 #
    count_dict=[] # list of attempts
    while start_iter<finish_iter: # for restarting process
        start_iter+=1
        game_number() # function start
        result=game_number()
        count_dict.append(result)

    print('My algorithm guesses the number in an average of',\
      round(sum(count_dict)/finish_iter), 'attempts out of',finish_iter, 'repetitions')

#game_number()
average_score()