"""
Sprint2 Project A Calculator
Turing College DS program, learner Greta Prekeriene
2024-06-20
"""

# for root calculation
import math


class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations and stores results in memory.
    """

    def __init__(self):
        """
        Initializes the calculator's memory with a value of 0.
        """
        self.memory = 0

    def add(self, number):
        """
        Adds the given number to the memory and returns the result.

        Args:
            number: The number to add.

        Returns:
            The sum of the number and the value stored in memory.
        """
        print(f"Memory value: {self.memory}")
        self.memory += number
        return self.memory

    def substract(self, number):
        """
        Subtracts the given number from the memory and returns the result.

        Args:
            number: The number to subtract.

        Returns:
            The difference between the value stored in memory and the number.
        """
        print(f"Memory value: {self.memory}")
        self.memory -= number
        return self.memory

    def multiply(self, number):
        """
        Multiplies the given number with the memory and returns the result.

        Args:
            number: The number to multiply.

        Returns:
            The product of the number and the value stored in memory.
        """

        print(f"Memory value: {self.memory}")
        self.memory *= number
        return self.memory

    def divide(self, number):
        """
        Divides the memory by the given number and returns the result,
        handling potential division by zero errors gracefully.

        Args:
            number: The number by which to divide.

        Returns:
            The result of the division or an error message if division by zero.
        """
        print(f"Memory value: {self.memory}")
        try:
            self.memory /= number
            return self.memory
        except ZeroDivisionError:
            return("Error. Division by zero is not allowed.")

    def take_n_root(self, number):
        """
        Calculates the nth root of the value in memory and returns the result.

        Args:
            number: The power of the root (e.g., 2 for square root, 3 for cube root).

        Returns:
            The nth root of the value stored in memory.
        """
        print(f"Memory value: {self.memory}")
        # Condition to handle even roots with negative base
        if number <= 0 and self.memory % 2 == 0:
            raise ValueError("Cannot take even root of a negative number.")
        self.memory = math.pow(self.memory, 1 / number)
        return self.memory

    def memory_reset(self):
        """
        Resets the memory to 0.
        """
        self.memory = 0
        print("Memory reset successful :)")
        print(f"Memory value: {self.memory}")


def main():
    calc = Calculator()
    print("Welcome to Calculator!")
    while True:
        print(
            "Choose an action!\n 1.Add 2.Substract 3.Multiply 4.Divide 5.Take (n) root 6.Memory reset 7.Exit"
        )

        choice = input("Enter your choice: ")

        if choice == "1":
            number = get_number()
            result = calc.add(number)
            print("Result: ", result)
        elif choice == "2":
            number = get_number()
            result = calc.substract(number)
            print("Result: ", result)
        elif choice == "3":
            number = get_number()
            result = calc.multiply(number)
            print("Result: ", result)
        elif choice == "4":
            number = get_number()
            result = calc.divide(number)
            print("Result: ", result)
        elif choice == "5":
            number = get_number()
            result = calc.take_n_root(number)
            print("Result: ", result)
        elif choice == "6":
            result = calc.memory_reset()
        elif choice == "7":
            print("Goodbye! Have a nice day!")
            break

        else:
            print("Invalid choice.")


def get_number(prompt="Enter a number for your action: "):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
