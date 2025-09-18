def NULL_not_found(object: any) -> int:
    obj_type = str(object.__class__)

    if object is None:
        print("Nothing: None <class 'NoneType'>")
        return 0
    elif obj_type == "<class 'float'>" and str(object) == 'nan':
        print("Cheese: nan <class 'float'>")
        return 0
    elif obj_type == "<class 'int'>" and object == 0:
        print("Zero: 0 <class 'int'>")
        return 0
    elif obj_type == "<class 'str'>" and object == "":
        print("Empty: <class 'str'>")
        return 0
    elif obj_type == "<class 'bool'>" and object is False:
        print("Fake: False <class 'bool'>")
        return 0
    else:
        print("Type not Found")
        return 1
