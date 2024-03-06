import sys

def analyze_text(text):
    char_count = len(text)
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    punctuation_count = sum(1 for char in text if char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    space_count = text.count(' ')
    digit_count = sum(1 for char in text if char.isdigit())

    print(f"The text contains {char_count} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python building.py \"Your text here\"")
        sys.exit(1)

    input_text = sys.argv[1]
    analyze_text(input_text)