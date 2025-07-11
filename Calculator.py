# Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.
# Perform the calculation and display the result.
class Calculator:
    def __init__(self):
        # Operator to method mapping
        self.operator_map = {
            '+': self._add,
            '-': self._subtract,
            '*': self._multiply,
            'x': self._multiply,
            '/': self._divide
        }

    def _add(self, num1, num2):
        return num1 + num2

    def _subtract(self, num1, num2):
        return num1 - num2

    def _multiply(self, num1, num2):
        return num1 * num2

    def _divide(self, num1, num2):
        return "Error: Division by zero is not possible." if num2 == 0 else num1 / num2

    def evaluate(self, input_expr):
        """
        Process the user input and compute the result.
        Validates input format and performs operation.
        """
        tokens = input_expr.strip().split()

        if len(tokens) != 3:
            return "Error: Please enter in format 'number operator number'."

        try:
            operand1 = float(tokens[0])
            operator = tokens[1].lower()
            operand2 = float(tokens[2])
        except ValueError:
            return "Error: Invalid numbers entered."

        if operator not in self.operator_map:
            valid_ops = ', '.join(self.operator_map.keys())
            return f"Error: Unsupported operator '{operator}'. Use {valid_ops}."

        # Perform and return result
        return self.operator_map[operator](operand1, operand2)

    def launch(self):
        """
        Starts the calculator for user interaction.
        """
        print("\n🔢 SIMPLE PYTHON CALCULATOR 🔢")
        print("Type expressions like '4 + 5', '6 / 2', '3 x 7'")
        print("Type 'exit' anytime to quit the program.\n")

        while True:
            user_input = input(">> ").strip()

            if user_input.lower() == 'exit':
                print("👋 Thanks for using the calculator. Goodbye!")
                break

            outcome = self.evaluate(user_input)

            if isinstance(outcome, str) and outcome.startswith("Error"):
                print(outcome)
            else:
                items = user_input.split()
                if len(items) == 3:
                    print(f"{items[0]} {items[1]} {items[2]} = {outcome}")
                else:
                    print(f"Result: {outcome}")
            print("-" * 40)


if __name__ == '__main__':
    app = Calculator()
    app.launch()

