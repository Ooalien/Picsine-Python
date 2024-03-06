import sys

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    if (sys.argv[1].isnumeric()):
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    if (sys.argv[2].isalpha()):
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    res = []
    for w in sys.argv[1].split():
        res.append(w) if len(w) > int(sys.argv[2]) else None
        
    print(res)
    # print(filter(lambda x: x.isalpha(), sys.argv[1]))