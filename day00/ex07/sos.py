import sys

if __name__ == '__main__':
    """Convert a string to Morse code."""
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        exit(1)
    NESTED_MORSE = {
        " ": "/ ", "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
        "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ",
        "J": ".--- ", "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ",
        "O": "--- ", "P": ".--. ", "Q": "--.- ", "R": ".-. ",
        "S": "... ", "T": "- ", "U": "..- ", "V": "...- ", "W": ".-- ",
        "X": "-..- ", "Y": "-.-- ", "Z": "--.. ",
        "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
        "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
        "8": "---.. ", "9": "----. "
    }

    my_input = sys.argv[1].upper()
    check = sys.argv[1].replace(" ", "")
    if not check.isalnum():
        print("AssertionError: the arguments are bad")
        exit(1)
    my_output = ""
    for c in my_input:
        my_output += NESTED_MORSE[c]
        my_output += " "
    print(my_output[:-2])
