a = True
b = True
c = False
d = True

result = a and b and c and d #stops checking after false because of and!

def print1():
    print(result)

print("Would you like to see the result?")

answer = input()

if answer == "yes":
    print1()
elif answer == "no":
    print("Result won't be shown")
else:
    print("Enter a valid response")

print("Enter a random plant, system will determine what it is.")

plant = input().lower()

if plant in ("banana", "apple", "grapes", "kiwi"):
    print(plant + " is a fruit")
    print("Is it true?")
    answer = input().lower()

    if answer != "yes":
        print("It is true!!")

elif plant in ("cucumber", "carrot", "pepper", "broccoli"):
    print(plant + " is a vegetable")

elif plant == "tomato":
    print(plant + " is a vegetable")
    print("Is it true?")
    answer1 = input().lower()

    if answer1 != "no":
        print("It is not true! Tomato is a fruit!")

else:
    print("Unknown")