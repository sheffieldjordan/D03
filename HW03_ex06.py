#!/usr/bin/env python
# HW03_ex06
# (1) Please comment your code.
# (2) Please be thoughtful when naming your variables.
# (3) Please remove development code before submitting.
###############################################################################
# Exercise 6.2
# See 6.1: "write a compare function takes two values, x and y, and returns 1
# if x > y, 0 if x == y, and -1 if x < y."
# When you submit only include your final function: compare
def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    return -1 #Technically no need to write an if statement here because there's only one other comparison to make




###############################################################################
# Exercise 6.2
# See 6.2: "use incremental development to write a function called hypotenuse
# that returns the length of the hypotenuse of a right triangle given the
# lengths of the other two legs as arguments."
# When you submit only include your final function: hypotenuse
# Do develop incrementally. Do not share in your final push your incremental
# work.
import math
def hypotenuse(leg1, leg2):
    #a squared plus b squared equals c squared, 3**3 + 4**4 = 5**5
    sq1 = leg1*leg1
    sq2 = leg2*leg2
    return math.sqrt(sq1+sq2)



###############################################################################
# Exercise 6.4
# See 6.4: "write a function is_between(x, y, z) that returns True if x ≤ y ≤ z
# or False otherwise"
# When you submit only include your final function: is_between
def is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False



###############################################################################
# Exercise 3.2
# See "Exercise 3, part 2": "Write a function called is_palindrome that takes a
# string argument and returns True if it is a palindrome and False otherwise.
# Remember that you can use the built-in function len to check the length of a
# string."
# When you submit only include your final function: is_palindrome
def is_palindrome(word):
    x = len(word) #figures out the length of the word
    if x > 2: #Checks if the word has more than two letters,    
        if word[0] == word[-1]: #and if the first letter is equal to the last letter,
            word = word[1:-1] #then it shortens the word by cutting off the first and last letters
            return is_palindrome(word) #and then re-reruns the function to check the new value of "word"
        else: #if at any time the first and last letters don't match, it will return False
            return False
    elif word[0] == word[-1]: #if the word has two letters, it compares the first and last
        return True 
    elif x == 1: #if the word has one letter, it's a palindrome
        return True
    else:  #if the word is two letters and the first and last letters don't match, it's not a palindrom
        return False





###############################################################################
# Exercise 4
# See "Exercise 4": "A number, a, is a power of b if it is divisible by b and
# a/b is a power of b. Write a function called is_power that takes parameters a
# and b and returns True if a is a power of b. Note: you will have to think
# about the base case."
# Note: Please use the provided definition and only plan for positive integers
# (whole numbers not including zero)
# When you submit only include your final function: is_power
def is_power(a,b):
    if a == 1: 
        return True
    elif a%b == 0 and is_power(a/b, b) == True:
        return True
    else:
        return False




###############################################################################
def main():
    """Your functions will be called within this function."""
    ###########################################################################
    # Use this space temporarily to call functions in development:
    print("Hello World!")






    ###########################################################################
    # # Uncomment the below to test and before commiting:
    # # Exercise 1
    print(compare(1, 1))
    print(compare(1, 2))
    print(compare(2, 1))
    # # # Exercise 2
    print(hypotenuse(1, 1))
    print(hypotenuse(3, 4))
    print(hypotenuse(1.2, 12))
    # # # Exercise 3
    print(is_between(1, 2, 3))
    print(is_between(2, 1, 3))
    print(is_between(3, 1, 2))
    print(is_between(1, 1, 2))
    # # # Exercise 6
    print(is_palindrome("Python"))
    print(is_palindrome("evitative"))
    print(is_palindrome("sememes"))
    print(is_palindrome("oooooooooooo"))
    # # # Exercise 7
    print(is_power(28, 3))
    print(is_power(27, 3))
    print(is_power(248832, 12))
    print(is_power(248844, 12))


if __name__ == "__main__":
    main()
