class Add:
    def calculate(self, a, b):
        return a + b


class Sub:
    def calculate(self, a, b):
        return a - b


class Multiply:
    def calculate(self, a, b):
        return a * b


class Divide:
    def calculate(self, a, b):
        if b == 0:
            raise ValueError("Division by zero")
        return a / b


class CalculationFactory:

    @staticmethod
    def get_operation(operation_type):

        operations = {
            "Add": Add(),
            "Sub": Sub(),
            "Multiply": Multiply(),
            "Divide": Divide()
        }

        return operations[operation_type]