"""
Implement a function that accepts 3 integer values a, b, c. 
The function should return true if a triangle can be built 
with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).
"""

def is_triangle(a, b, c):
    s_list = sorted([a, b, c])
    if s_list[0] + s_list[1] <= s_list[2]:
        return False
    return True
