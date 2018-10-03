##Illustrating the decorator call with arguments concept
# Example 1
from decorator import decorator_func
import pytest

@decorator_func
def dec_call3(name):
    print(f"Hi this is the diff file call by {name}")

@decorator_func
def dec_call4(name):
    print(f"Hi this is the diff file second call by {name}. Returning YAY")
    return "YAY"


dec_call3("Abhiram")
ret_val = dec_call4("Kratos")
print("Ret val = "+str(ret_val))

try:
    assert ret_val == None
except:
    assert ret_val == "YAY"