#!/bin/python3
class Main:
    def __init__(self):
        self.message = "Hello World"
        self.info = "Sample Read and Write Message"

    def show_message(self):
        print(f"The Message: {self.message}")

    def write_message(self, new_content):
        self.message += new_content

if __name__ == "__main__":
    obj = Main()
    obj.show_message()
    obj.write_message(new_content = ", Have a nice day")
