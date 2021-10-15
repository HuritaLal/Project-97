import random
number = random.randint(1, 9)
chanceCount = 0
while (chanceCount < 5):
    introString = int(input("Enter a number between 1 and 9: "))
    if (introString > number):
        print("Your guess was too large")
    elif (introString == number):
        print("Congratulation! You guessed it correct.")
    else :
        print("Your guess was too low.")
    chanceCount = chanceCount + 1
if (chanceCount > 5):
    print("Oops!! You are out of chances.")
