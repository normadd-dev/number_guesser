import random # import a module called randam

top_of_range = input('type a number: ') # a variable that takes input from the user and stores it in a variable called top_of_range

if top_of_range.isdigit():# check if the input is a digit
    top_of_range = int(top_of_range) # convert the input to an integer

    if top_of_range <= 0: # check if the input is less than or equal to 0
        print('please type a number larger than 0 next time.')
        quit()
else:
    print('please type a number next time.')  
    quit()        

random_number = random.randrange(0, top_of_range) # generate a random number between 0 and the top_of_range variable
guesses = 0

print(random_number) # print the random number to the console
while True: # create an infinite loop
    guesses += 1 # increment the guesses variable by 1
    user_guess = input('make a guess: ') # take input from the user and store it in a variable called user_guess
    if user_guess.isdigit(): # check if the input is a digit
        user_guess = int(user_guess) #  convert the input to an integer
    else:
        print('please type a number next time.')
        continue 

    if user_guess == random_number: # check if the user_guess is equal to the random_number
        print('you got it!')
        break # exit the loop
    else:
        if user_guess > random_number: # check if the user_guess is greater than the random_number
            print('you were above the number!')
        else:
            print('you were below the number!')    


print('you got it in', guesses, 'guesses') # print the number of guesses it took the user to guess the random number     
