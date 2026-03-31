from collections import deque

# challenge: check if a string is a palindrome using deque library

# check if parameter is a palindrom, return true or false
def palindrome_check(word):
    chars_reversed = deque([]) # will store the reversed characters

    # loop to reverse characters
    for char in word:
        chars_reversed.appendleft(char)

    # join elements to a single string
    reversed_word = "".join(chars_reversed)

    # prints
    print(f"\nOriginal word: {word}")
    print(f"Reversed word: {reversed_word}\n")

    # returns
    if reversed_word == word:
        return True
    else:
        return False

# ask user for string. Quit if len is 1, else give it to palindrom_check()
def string_input():
    while True:
        user_word = input("Word: ")

        if len(user_word) == 1:
            return
        else:
            # call function to check if is palindrome or not
            is_palindrome = palindrome_check(user_word)

            # prints
            if is_palindrome:
                print("Yes, the reversed version of this word is equal to the original.\n")
            else:
                print("No, the reversed version of this word is different than the original.\n")

# main
def main():
    print("\nPlease type a word to check if it is a palindrome")
    print("Type a single letter to quit\n\n")

    # calls function to ask for string until user wants to quit
    string_input()

    print("Quitting...\n\n")


main()