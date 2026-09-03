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

plant = input()

if (plant == "banana" or "apple" or "grapes" or "kiwi"):
    print(plant + " is a fruit")
    print("Is it true?")
    answer = input()
    if not answer == "yes":
        print("It is true!!")
elif (plant == "cucumber" or "carrot" or "pepper" or "brocolli"):
    print(plant + " is a vegetable")
elif (plant == "tomato" or "tomato"):
    print(plant + " is a vegetable")
    print("is it true?")
    answer1 = input()
    if not answer1 == "no":
        print("It is not true! tomato is a fruit!")
else:
    print("Unknown")