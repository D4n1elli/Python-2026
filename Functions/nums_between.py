# Back to learning Python
# Starting with learning how to write functions

# Made in 16/01/2026, a re-make of "nums_between.cpp" from my 2025 cpp repository

def evens_counter(s, e): # returns how many evens between start and end
    evens_amount = 0
    for i in range(s+1, e):
        if(i%2 == 0):
            evens_amount += 1
    return evens_amount

def sum_counter(s, e): # returns the sum of all the numbers between
    total = 0
    for i in range(s+1, e):
        total += i
    return total

def negatives_counter(s, e):
    if (s>0):
        return 0
    else:
        negatives = 0
        for i in range(s+1, e):
            if(i < 0):
                negatives += 1
        return negatives

def main():
    start = int(input("Start: ")) #inputs
    end = int(input("End: "))
    if(start == 0 and end == 0): # Finishing check
        return False

    while(start > end or start+1 == end): #validation
        if(start > end):
            print("Start must be smaller than end.")
        elif(start+1 == end):
            print("Numbers must be at least 2 apart.")

        start = int(input("Start: "))
        end = int(input("End: "))

    total_between = end - start - 1
    total_sum = sum_counter(start, end)
    total_average = total_sum/total_between
    negatives_between = negatives_counter(start, end)
    positives_between = total_between - negatives_between
    evens_between = evens_counter(start, end)
    odds_between = total_between - evens_between

    print(f"Between {start} and {end}, there are {total_between} numbers")
    print(f"The sum of them all is {total_sum}")
    print(f"The average is {total_average}")
    print(f"There are {negatives_between} negatives and {positives_between} positives")
    print(f"{evens_between} are evens, {odds_between} are odds")
    return True



print("In Between Info")
print("Rules: start must be smaller than end")
print("Numbers must be at least 2 apart")
print("Type 0 in both inputs to finish the program.")

again = main() # looping the code and leaving when both are 0
while again:
    again = main()


