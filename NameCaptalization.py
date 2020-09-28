# Capitalize any string

name = input("enter your name")
if (name.isupper()):
    print(f"string in lower case is {name[0:].lower()}")
elif (name.islower()):
    print(f"string in UPPER case is {name[0:].upper()}")
else:
    print("miDcase condition arrived")

         