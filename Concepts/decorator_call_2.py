##Illustrating the decorator call with arguments concept
# Example 1
from decorator import decorator_func

@decorator_func
def dec_call3(name):
    print(f"Hi this is the diff file call by {name}")

dec_call3("Abhiram")
