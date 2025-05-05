
def list_names():
    name = ""
    in_name = ""
    while in_name != "END":
        in_name = input("please enter a name:")
        if in_name != "END":
            name+=in_name
            name += ","
        else:
            name

    print("Names:"+name)

list_names()


