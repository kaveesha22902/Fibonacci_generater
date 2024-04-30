Fibonacci Sequence Generator
Overview
This Python script generates a Fibonacci sequence up to a specified length. The user is prompted to enter the desired length of the sequence, and the script outputs the Fibonacci numbers accordingly.

How to Use
Clone the Repository:
bash
Copy code
git clone https://github.com/kaveesha22902/Fibonacci_generater.git
cd fibonacci-generator
Run the Script:
Copy code
python fibonacci_generator.py
Enter the Length of Fibonacci Sequence:
When prompted, enter the desired length of the Fibonacci sequence.
The length must be a positive integer.
View the Generated Sequence:
The script generates the Fibonacci sequence based on the user input.
It then displays the generated sequence in the console.


Features
Flexible Length: Users can specify the length of the Fibonacci sequence they want to generate.
Error Handling: The script checks for invalid inputs, such as non-integer values or negative integers, and provides appropriate error messages.
Efficient Generation: The script uses a generator function to lazily generate Fibonacci numbers, ensuring efficient memory usage, especially for large sequences.

Example :

Copy code
Enter the length of Fibonacci sequence: 10
Fibonacci sequence of length 10 is: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
