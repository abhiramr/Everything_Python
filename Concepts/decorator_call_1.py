##Illustrating the decorator call concept
# Example 1
from decorator import decorator_func
from datetime import datetime

def dec_call():
    print("This is implemented using the bald representation for decorators.")

def non_decorator_call():
    print("This is called without using a decorator.")

@decorator_func
def dec_call_2():
    print("This is implemented using syntactic sugar representation for decorators.")

print("Time now  = "+str(datetime.now().hour))
dec_call = decorator_func(dec_call)


dec_call()
non_decorator_call()
dec_call_2()