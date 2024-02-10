#!/usr/bin/python3

"""
This is a simple Python script that adheres to PEP 8 guidelines.
"""


class ExampleClass:
    """
    This is an example class.
    """

    def __init__(self, name):
        """
        Initialize the ExampleClass with a name.
        """
        self.name = name

    def greet(self):
        """
        Print a greeting message with the name of the instance.
        """
        print("Hello, {}!".format(self.name))


def main():
    """
    Main function to demonstrate the usage of the ExampleClass.
    """
    example = ExampleClass("Alice")
    example.greet()


if __name__ == "__main__":
    main()
