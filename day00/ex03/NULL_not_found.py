def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {str(object.__class__)}")
    elif object.__class__ is float:
        print(f"Cheese: {object} {str(object.__class__)}")
    elif object.__class__ is int:
        print(f"Zero: {object} {str(object.__class__)}")
    elif object.__class__ is str and object == "":
        print(f"Empty: {object} {str(object.__class__)}")
    elif object.__class__ is bool:
        print(f"Fake: {object} {str(object.__class__)}")
    else:
        print("Type not found")
    return 1