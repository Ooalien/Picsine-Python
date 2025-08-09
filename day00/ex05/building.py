import sys


def analyze_text(text):
    """Analyze the given text and print character statistics."""
    char_count = len(text)
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    punctuation_count = \
        sum(1 for char in text if char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    space_count = sum(1 for char in text if char.isspace())
    digit_count = sum(1 for char in text if char.isdigit())

    print(f"The text contains {char_count} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        # No arguments provided, prompt user for input
        print("What is the text to count?")
        input_text = sys.stdin.readline()
    elif len(sys.argv) == 2:
        # Exactly one argument provided
        input_text = sys.argv[1]
    else:
        # More than one argument provided
        raise AssertionError("more than one argument are provided")

    try:
        analyze_text(input_text)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
