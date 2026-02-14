class StringHandler:
    def __init__(self):
        self.s = ""

    def getString(self):
        # Use input() to accept a string from the console
        self.s = input()

    def printString(self):
        # Print the stored string converted to uppercase using the upper() method
        print(self.s.upper())

# Example usage:
# Create an instance of the StringHandler class
handler = StringHandler()

# Call the method to get the string from the user input
handler.getString()

# Call the method to print the string in uppercase
handler.printString()
