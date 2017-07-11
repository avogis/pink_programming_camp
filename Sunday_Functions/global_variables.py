def read_global():
    print("From inside the scope of read_global(), value is: ", value)


def shadow_global():
    value = -10  # Same variable name as global variable name. This is called shadowing.
    print("From inside the scope of shadow_global(), value is: ", value)


def change_global():
    global value  # This is how you ask for permission to change a global variable.
    value = -10
    print("From inside the scope of change_global(), value is: ", value)

# main
value = 10
read_global()
print("In the global scope, value is: ", value)
shadow_global()
print("In the global scope, value is: ", value)
change_global()
print("In the global scope, value is: ", value)

