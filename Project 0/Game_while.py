import random

#The Game: the computer makes a guess and guesses the number
start_iter,finish_iter=0,1000 # start/finish of repetitions
count_dict=[] #list of attempts
while start_iter<finish_iter: # for restarting process
    start_iter+=1

    x,y=1,100 #the first/last of random number
    number=random.randint(x,y)
    count=0 #'start' value of total attempts
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
            count_dict.append(count)
            break

print('My algorithm guesses the number in an average of',\
      round(sum(count_dict)/finish_iter), 'attempts out of',finish_iter, 'repetitions')


