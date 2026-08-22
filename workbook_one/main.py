"""
NOTE: do not modify this code do your tasks on your folders 
"""

from teammate_one.add import addition
from teammate_two.subtract import subtraction

MIN = 5



if __name__ == "__main__":
    total = addition(2, 2) + subtraction(2,4)
    
    check = max (MIN,total)

    if check == 5:
        print("Failed")
    else:
        print("passed")

