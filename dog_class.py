class Dog:
    """A simple attempt to model a dog"""
    def __init__(self, name, age):
        """initialize name and age attributes."""
        self.name = name
        self.age = age
    def sit(self):
        """simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """simulate a dog rolling over in the response to a command."""
        print(f"{self.name} rolled over!")