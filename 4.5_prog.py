class AddNumbers:
    def __init__(self):
        self.num1 = float(input("Enter the first number: "))
        self.num2 = float(input("Enter the second number: "))

    def perform_addition(self):
        result = self.num1 + self.num2
        print(f"The sum of {self.num1} and {self.num2} is: {result}")

# Subclass inheriting from AddNumbers
class AddNumbersWithMessage(AddNumbers):
    def display_message(self):
        print("Performing addition with user input.")

# Example usage:
def main():
    # Create an object of the subclass
    addition_object = AddNumbersWithMessage()

    # Call the method from the parent class
    addition_object.perform_addition()

    # Call the method from the subclass
    addition_object.display_message()

if __name__ == "__main__":
    main()
