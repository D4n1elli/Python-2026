# Code made in 19/01/2026

# Input, validation and calculates the mult table
# Returns true or false (true: code is repeated, false: program finishes)
def run_mult_table():
    #inputs
    index = int(input("Index: "))
    if index == 0:
        return False
    
    start = int(input("Start: "))
    end = int(input("End: "))

    while start > end: # validation
        print("Start must be smaller than end.")
        start = int(input("Start: "))
        end = int(input("End: "))

    # calculating and printing the result
    while start <= end:
        print(f"{index} x {start} = {index*start}")
        start += 1
    return True



def main(): # main code
    print("\nDigit 3 numbers to calculate the multiplication table!")
    print("Digit 0 on the index number to finish the program.\n")

    again = run_mult_table() 
    while again: #loops until return 0
        again = run_mult_table()

main()