"""
NOTE: do not modify this code do your tasks on your folders 
"""

from teammate_one.add import addition
from teammate_two.subtract import subtraction

"""
NOTE: do not modify this code do your tasks on your folders 
"""

from teammate_one.add import addition
from teammate_two.subtract import subtraction


# explanation on the testing and the criteron here 
def test_collaboration(a, b):

    teamate_one_add = addition(a, b)
    
    teamate_two_subtract = subtraction(a, b)
    
    
    if teamate_one_add > teamate_two_subtract:
        print("Passed: Addition is greater than Subtraction")
    else:
        print("Failed: Addition is not greater than Subtraction")


if __name__ == "__main__":
    a = 10
    b = 5 
    test_collaboration(a, b)

