from collections import deque

'''
    This code is an example on how to use the main deque library commands
    I first saw it as I was learning about queues data structure, and decided
    to create this folder to practice using this library, which is faster and more
    efficient to do operations with a list.
'''

def main():
    # start
    dq = deque([1, 2, 3])
    print(f"\nStart: {dq}\n")


    # APPEND: add an element
    dq.append(4)
    dq.appendleft(0)

    print("4 joined the dq in the end. 0 joined the dq in the start.")
    print(f"Current dq: {dq}\n")



    # EXTEND: used to add multiple elements at once
    dq.extend([5, 6])
    dq.extendleft([-1, -2]) #the order written gets reversed, -1, -2 becomes -2, -1

    print("2 new numbers joined the dq on both sides")
    print(f"Current dq: {dq}\n")


    # REMOVE: remove a specific element
    # if the value isn't found, it errors, so always check if number is in the dq
    if 3 in dq:
        dq.remove(3)
        print("3 was removed.")
        print(f"Current dq: {dq}\n")


    # POP: remove from the right and returns
    removed_r = dq.pop()
    removed_l = dq.popleft()

    print(f"{removed_r} and {removed_l} were removed.")
    print(f"Current dq: {dq}\n")

    
    # CLEAR: clear the list, removing every element
    dq.clear()
    print("Dq was cleared.\n")
    print(f"Current queue: {dq}\n")



main()