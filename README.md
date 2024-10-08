# Project A Calculator using Jupyter Notebooks

Project A Calculator

Introduction

This project implements a simple, user-friendly calculator with basic arithmetic operations, memory functionality, and nth root calculation capabilities.

Features

Basic Arithmetic: Performs addition, subtraction, multiplication, and division.
Memory: Stores the current result in memory for further calculations.
Memory Operations: Supports adding to, subtracting from, multiplying by, and dividing the memory value.
Nth Root: Calculates the nth root of the value in memory.
Error Handling: division by zero and invalid input for the nth root function (negative base with even root).

Installation

This Python project doesn't require any specific installation steps. 

Usage

Run the script: Execute python main.py in your terminal.
Welcome message: The calculator will greet you and display a menu.
Choose an action: Select the desired operation from the menu (1: Add, 2: Subtract, etc.).
Enter numbers: When prompted, enter the numbers you want to operate on.
Results: The calculator will display the result of the operation.
Memory reset: Use option 6 to clear the memory value.
Exit: Enter 7 to terminate the program.


Example Usage

Welcome to Calculator!

Choose an action!
 1. Add  2. Subtract  3. Multiply  4. Divide 
 5. Take (n) root  6. Memory reset  7. Exit
Enter your choice: 1

Enter a number for your action: 5.2
Memory: 0
Result: 5.2

Choose an action!
 1. Add  2. Subtract  3. Multiply  4. Divide 
 5. Take (n) root  6. Memory reset  7. Exit
Enter your choice: 3

Enter a number for your action: 3.1
Memory: 5.2
Result: 16.32

Choose an action!
 1. Add  2. Subtract  3. Multiply  4. Divide 
 5. Take (n) root  6. Memory reset  7. Exit
Enter your choice: 5

Enter a number for your action: 2
Memory: 16.32
Result: 4.03125

Choose an action!
 1. Add  2. Subtract  3. Multiply  4. Divide 
 5. Take (n) root  6. Memory reset  7. Exit
Enter your choice: 6

Memory reset successful :)
Memory value: 0

Choose an action!
 1. Add  2. Subtract  3. Multiply  4. Divide 
 5. Take (n) root  6. Memory reset  7. Exit
Enter your choice: 7

Goodbye! Have a nice day!

How it Works

The Calculator class is the core of the code, encapsulating the calculation logic. It provides methods for various operations, including add, substract, multiply, divide, and take_n_root. These methods handle basic calculations, memory manipulation, and error handling for division by zero and invalid nth root operations.

The main function drives the user interaction. It displays the menu, prompts for user input, and calls the appropriate methods based on the chosen operation. The get_number function ensures that only valid numbers are accepted from the user.


Additional Notes

The calculator performs calculations in floating-point precision.

