"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It's guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

Find the unique number (this kata)
Find the unique string
Find The Unique
"""

def find_uniq(arr):
    n = 0
    n_count = 1
    dct = {}
    for i in arr:
        if i not in dct:
            dct[i] = 0
        dct[i] += 1
    for k in dct:
        if dct[k] <= n_count:
            n_count = dct[k]
            n = k
    return n   # n: unique number in the array

print(find_uniq([ 3, 10, 3, 3, 3 ]))