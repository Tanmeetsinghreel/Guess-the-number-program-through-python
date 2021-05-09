#Build a number guessing game in which a winning number is set to some integer value
#the program should take input to the user and if the entered number is less than the
#winning number,a message should display that the number is smaller and vice versa

#instructions:-
# the number of guesses should be limited i.e.(5or9)
#print the number of guesses left
#print the number of guesses he took to win the game
#game over message should display if the number of guesses becomes equal to 0

print("welcome to number guessing game----\n")
print("you have 6 guesses\n")
winning_number = 15
number_of_guesses = 6
while(True):
    print("number of gases left to win the game: ", number_of_guesses)
    number_of_guesses = number_of_guesses - 1
    inpnum = int(input("Guess any number between 1 to 15\n"))
    if number_of_guesses <= 0:
        print("Game over baby!!")
        break
    elif inpnum == 15:
         print("yayy you got it! number of gueses left is",number_of_guesses)
         break
    elif inpnum < 15:
         print("you have entered a small number try again!!\n")
    elif inpnum > 15:
         print("you have entered a greater number try again!!\n")
    else:
        print("invalid input")