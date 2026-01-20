import random

def difficulty_selection(): # returns difficulty determined by the user
    difficulty = int(input("Difficulty: "))

    while difficulty < 0 or difficulty > 4: # validation
        print("Please insert valid difficulty")
        difficulty = int(input("Difficulty: "))
    return difficulty

def game_run(max_number): # The 3 difficulties said in the menu
    print(f"Guess a random number between 1 and {max_number}!")

    answer = random.randint(1,max_number) #game answer
    
    attempts = 1
    while True: # loops until user guess the number
        guess = int(input(f"{attempts} Guess: "))

        if guess == answer:
            break
        else:
            if guess < 1 or guess > max_number:
                print(f"Try staying between 1 and {max_number}")
            elif guess > answer:
                print("Try a lower number")
            elif guess < answer:
                print("Try a higher number")
            attempts += 1
    #final print
    print(f"Congratulations! You guessed it with {attempts} attempts!")
    print("Type 0 if you want to stop playing or the number of the difficulty you want now")

def custom_game_run(): # User can custom their game
    start = int(input("Start of the intervail: "))
    end = int(input("End of the intervail: "))

    while start >= end: #validation
        print("Start must be smaller than end")
        start = int(input("Start of the interval: "))
        end = int(input("End of the interval: "))

    answer = random.randint(start, end) #game answer
    
    attempts = 1
    while True: # loops until user guess the number
        guess = int(input(f"{attempts} Guess: "))

        if guess == answer:
            break
        else:
            if guess < start or guess > end:
                print(f"Try staying between {start} and {end}")
            elif guess > answer:
                print("Try a lower number")
            elif guess < answer:
                print("Try a higher number")
            attempts += 1
    #Final print
    print(f"Congratulations! You guessed it with {attempts} attempts!")
    print("Type 0 if you want to stop playing or the number of the difficulty you want now")


# introduction print
print("\n--Guess a random number game!--")
print("There are 3 difficulties:")
print("1 - Easy: between 1-20.   2 - Medium: 1-100   3 - Hard: 1-1000. 4 - custom your game!")
print("Type 0 if you want to stop playing")
print("Which one would you like?")

dif = difficulty_selection()
while dif != 0:
    if dif == 1:
        print("\n-Easy-")
        game_run(20)
    elif dif == 2:
        print("\n-Medium-")
        game_run(100)
    elif dif == 3:
        print("\n-Hard-")
        game_run(1000)
    elif dif == 4:
        print("\n-Custom your game-")
        custom_game_run()
    dif = difficulty_selection()