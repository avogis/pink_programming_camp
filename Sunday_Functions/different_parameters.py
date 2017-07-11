# Positional parameters
def birthday_wishes(name, age):
    print("Happy birthday, " + name + "!" + " You're " + age + " today.\n")


# Parameters with default values
def birthday_wishes2(name="Julia", age="25"):
    print("Happy birthday, " + name + "!" + " You're " + age + " today.\n")



print("birthday_wishes")
# birthday_wishes()
birthday_wishes("Carol", "30")
birthday_wishes("30", "Carol")
birthday_wishes(name="Carol", age="30")
birthday_wishes(age="30", name="Carol")

print("birthday_wishes2")
birthday_wishes2()
birthday_wishes2(name="Klara")
birthday_wishes2(age="27")
birthday_wishes2(name="Klara", age="27")
birthday_wishes2("Klara", "27")
birthday_wishes2("Klara")