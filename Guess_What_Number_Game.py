from mimetypes import guess_type
import random

#Made a similar game in C++ but the computer guessed the user's number
print('----------------------------------------------------------------')
print('                  Guess that Number Game               ')
print('----------------------------------------------------------------')
print('')

the_number = random.randint(0,100) #random class has a method that will allow a number range
guess = -1

#print(guess_text, type(guess_text))
#print(guess, type(guess))
#We cannot compare two different data types, I wonder if we will learn about type casting.

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number: #The colon at the end of this statement represents the start of a new code block
        print('Too low')
    elif guess > the_number:
        print('Too high')
    else:
        print('You Win!')
        
#indentation is super important, if the items after the while loop or any loop are indented under the loop they are 
#automatically apart of the loop if the items after the loop are not indented then they are not considered apart of the
#loop 
    

