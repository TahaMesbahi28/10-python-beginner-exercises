# Exercise 1 — Name Guessing Game

We have a custom list of ten different names. Write a program that asks the user to think of one name, and then lets the computer try to guess which name the user has chosen.

After each guess, the program should ask the user whether the guess was correct or not. If the guess is incorrect, the computer should guess another name.

**Important:** The program must not guess a name that the user has already said is incorrect.

## Example

Suppose our list contains:

```python
["C", "B", "A"]
```

The user chooses **A** in their mind.

The program guesses **B** and asks:

> Did I guess correctly?

The user says **No**.

The program then guesses **A** and asks again:

> Did I guess correctly?

The user says **Yes**, and the program ends.

## Sample Code

You can use any list you like. In this example, we have used a list of 10 fruits as the initial data.

```python
fruits = ['banana', 'apple', 'orange', 'blueberry', 'grapefruit', 'lemon', 'raspberry', 'pawpaw', 'blackberry',
          'strawberry']
```

# Exercise 2 — Loan Eligibility Check

Write a program that takes the user's **age** and **income** as input.

* If the user's age is **greater than 18**:

  * Check whether their income is **more than 5 million tomans**.

    * If yes, display:

      > **"You are eligible for a loan."**
    * Otherwise, display:

      > **"You are not eligible for a loan."**

* If the user's age is **less than 18**, display:

  > **"Your age is not suitable for a loan."**

# Exercise 3 — Triangle Type Checker

Write a program that takes the **three sides of a triangle** as input from the user and determines whether these sides can form a triangle or not.

If they can form a triangle, determine what type of triangle it is:

* **Equilateral**
* **Isosceles**
* **Scalene**
* **Right-angled**

# Exercise 4 — Character Type Checker

Write a program that takes a **character** from the user and uses its **ASCII code** to determine which category it belongs to:

* **Number**
* **Symbol**
* **English letter**

If the character is an **English letter**, also determine which range of the English alphabet it belongs to.

### Hint

Use the **ASCII code** to identify the type of character.

For example, you can check which ASCII range the entered character belongs to.

# Exercise 5 — Happy Number

Write an algorithm to determine whether a number `n` is a **happy number**.

A **happy number** is a number defined by the following process:

* Starting with any positive integer, replace the number with the **sum of the squares of its digits**.
* Repeat this process until the number becomes `1`, where it will stay, or enters a **cycle that does not include `1`**.
* A number is considered **happy** if the process eventually ends at `1`.

Return `true` if `n` is a happy number, and `false` otherwise.

## Example 1

```text
Input: n = 19
Output: true
```

### Explanation

```text
1² + 9² = 82
8² + 2² = 68
6² + 8² = 100
1² + 0² + 0² = 1
```

Since the process ends at `1`, **19 is a happy number**.

## Example 2

```text
Input: n = 2
Output: false
```

Since the process enters a cycle that does not include `1`, **2 is not a happy number**.

# Exercise 6 — Longest Common Prefix

Write a function to find the **longest common prefix** string among an array of strings.

If there is no common prefix, return an empty string `""`.

## Example 1

```text
Input: strs = ["flower", "flow", "flight"]
Output: "fl"
```

### Explanation

The longest prefix shared by all three strings is `"fl"`.

## Example 2

```text
Input: strs = ["dog", "racecar", "car"]
Output: ""
```

### Explanation

There is no common prefix among the input strings, so the result is an empty string `""`.

# Exercise 7 — String Compression

Write a function that takes a string as input and places the **number of consecutive occurrences of each character** next to it.

Only characters that appear **consecutively** should be grouped together. If the same character appears again later in the string, it should be counted separately.

## Example 1

```text
Input: "aaabbccccd"
Output: "a3b2c4d1"
```

## Example 2

```text
Input: "xxxyzz"
Output: "x3y1z2"
```

## Example 3

```text
Input: "aabcca"
Output: "a2b1c2a1"
```

In the third example, the two `a` characters at the beginning and end are not combined because they do not appear consecutively.

