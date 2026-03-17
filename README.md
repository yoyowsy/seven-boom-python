## Seven Boom! 🚀 -- Slouthbyte Weekly Challenge
https://slothbytes.beehiiv.com/p/how-does-google-maps-find-the-fastest-route

This repository contains my solution for the Seven Boom! logic challenge from the Slouthbyte newsletter.

## 📝 The Challenge
Create a function that takes an array of numbers and for every 7 found, add one "Boom!" to your result. If no 7 is found anywhere, return "there is no 7 in the array".

Examples

[1, 2, 3, 4, 5, 6, 7] ➞ "Boom!"

[8, 6, 33, 100] ➞ "there is no 7 in the array"

[2, 55, 60, 97, 86] ➞ "Boom!" (97 contains a 7)

[7, 77, 100] ➞ "Boom! Boom! Boom!" (7 has one, 77 has two)

## 🛠️ My Solution
I used Python to solve this. The core logic involves:

Converting the input list into a single string to catch "7"s inside larger numbers (like 97 or 77).

Using the .count() method for efficiency.

Using ast.literal_eval to allow the user to input data in the exact [1, 2, 3] format.

## How to Run

Ensure you have Python installed.

Run the script: python seven_boom.py

Enter your list when prompted, for example: [7, 17, 77]

## 🚀 Skills Demonstrated
- String Manipulation
- List Processing
- Error Handling (try/except)
- User Input Parsing
