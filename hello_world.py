#!/bin/python3
class Main:
    def __init__(self):
        self.message = "Hello World"

    def show_message(self):
        print(f"The Message: {self.message}")

if __name__ == "__main__":
    obj = Main()
    obj.show_message()
