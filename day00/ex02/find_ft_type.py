def is_inst(value, classinfo):
    if (value.__class__) == classinfo:
        return True
    else:
        return False
    
def all_thing_is_obj(object: any) -> int:
    if is_inst(object, tuple):
        print(f"Tuple: {(object.__class__)}")
    elif is_inst(object, set):
        print(f"Set: {(object.__class__)}")
    elif is_inst(object, dict):
        print(f"Dict: {(object.__class__)}")
    elif is_inst(object, list):
        print(f"List: {(object.__class__)}")
    elif is_inst(object, str):
        print(f"{object} is in the kitchen: {(object.__class__)}")
    else:
        print("Type not found")
    return 42