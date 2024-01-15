"""
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
Go challenge Build Tower Advanced once you have finished this :)
"""
def tower_builder(n_floors):
    lst = []
    for i in range(1, n_floors + 1):
        spaces = ' ' * (n_floors - i)
        stars = '*' * ((i * 2) - 1)
        floor = spaces + stars + spaces
        lst.append(floor)
    return lst