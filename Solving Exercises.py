# Exercise 1
import random

fruits = ['banana', 'apple', 'orange', 'blueberry', 'grapefruit', 'lemon', 'raspberry', 'pawpaw', 'blackberry', 'strawberry']

print(f"Make your guess based on the inside of this fruit: {fruits}")

for _ in range(0, len(fruits)):
    Random_selection = random.choice(fruits)
    print(f"Was that your guess? {Random_selection}")
    Reviewing_the_answer = input("(yes/no): ")

    if Reviewing_the_answer == "yes":
        print("It was guessed.")
        break

    elif Reviewing_the_answer == "no":
        fruits.remove(Random_selection)
# -------------------------------------------------------------------------------------------------------
# Exercise 2
Age = int(input("Enter your age: "))

if Age >= 18:
    Income = int(input("Enter your income($)(Per month): "))

    if Income >= 2000:
        print("You are eligible for the loan.")

    else:
        print("You are not eligible for the loan.")

else:
    print("Your age is not suitable for the loan.")
# -------------------------------------------------------------------------------------------------------
# Exercise 3
Sides = []

for _ in range(3):
    Side = input("Sides of a triangle: ")
    Sides.append(int(Side))

Sides = sorted(Sides)

if Sides[0] > 0 and Sides[0] + Sides[1] > Sides[2]:

    if (Sides[2] ** 2) == (Sides[0] ** 2) + (Sides[1] ** 2):
        print("Right-angled triangle")

    if Sides[2] == Sides[1] == Sides[0]:
        print("Equilateral triangle")

    if Sides[2] == Sides[1] or Sides[2] == Sides[0] or Sides[1] == Sides[0]:
        print("Isosceles triangle")

    if Sides[2] != Sides[1] != Sides[0]:
        print("Scalene triangle")

else:
    print("No triangle with these sides was found.")
# -------------------------------------------------------------------------------------------------------
# Exercise 4
char = input("Enter a character: ")

if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
    print("Your character is an English letter.")

elif 48 <= ord(char) <= 57:
    print("Your character is a number.")

else:
    print("The character is another symbol.")
# -------------------------------------------------------------------------------------------------------
# Exercise 5
N = []
s = input("Enter your number: ")
while True:
    su_m = 0
    for i in range(len(s)):
        su_m += int(s[i]) ** 2
    if su_m == 1:
        print("True")
        break
    s = str(su_m)
    if s in N:
        print("False")
        break
    N.append(s)
# -------------------------------------------------------------------------------------------------------
# Exercise 6
words = input("Enter words separated by space: ").split()

letters = []

for i in range(min(len(word) for word in words)):
    if all(word[i] == words[0][i] for word in words):
        letters.append(words[0][i])
    else:
        break

for letter in letters:
    print(letter, end="")
# -------------------------------------------------------------------------------------------------------
# Exercise 6
