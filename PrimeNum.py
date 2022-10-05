# Name: Alan Ingersoll
# Description: Simple program that determines whether a number given by user
#               is a prime number.

# determines whether number is prime or not
def is_prime(n):
    i = 2
    while i < n/2:
        if (n % i) == 0:
            return False
        i = i + 1
    return True


# begin loop for taking input from user
loop = True
while loop:

    # take in input from user  to receive number
    number = input("\nEnter number greater than 0: ")

    # Start a loop to check if number is greater than 0
    # Take in another number if not
    numBad = True
    while numBad:
        if int(number) > 0:
            numBad = False
        else:
            number = input("That number is not greater than 0! Try again: ")

    # check if number is divisible by any number from 2 to number/2
    if is_prime(int(number)):
        print(number, " is prime!")
    else:
        print(number, " is NOT prime!")

    # Ask user if they would like to see if another number is prime
    again = input("Another one? (Y/N): ")
    inp = True

    # Loop while asking for another number
    while inp:
        if again == 'Y' or again == 'y':
            inp = False
        elif again == 'N' or again == 'n':
            inp = False
            print("Okay! Goodbye!")
            loop = False
        else:
            again = input("I don't understand that! Try again (Y/N): ")
