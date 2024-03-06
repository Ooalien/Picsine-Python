import sys

list_of_arguments = sys.argv

if len(list_of_arguments) > 2:
    print("AssertionError: more than one argument is provided")
    exit()
elif len(list_of_arguments) == 1:
    exit()
try:
    if int(list_of_arguments[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except ValueError:
    print("AssertionError: argument is not an integer")