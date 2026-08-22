# The teammate files are separate contributions that are combined here.
"""
NOTE: do not modify this code do your tasks on your folders 
"""

from teammate_one.add import addition
from teammate_two.subtract import subtraction

# Calculate the result from each teammate's function.
# Check: With a positive b, a + b must be greater than a - b.
# Note: for this check to work b must be  a positive whole number and b must not be zero
# This is the simple collaboration check for this exercise.
# These sample values let the shared check run after both files are merged.


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

