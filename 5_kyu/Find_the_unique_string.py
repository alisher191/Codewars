"""
There is an array of strings. All strings contains similar letters except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

It's guaranteed that array contains more than 2 strings.
"""
def find_uniq(arr):
    dct = {}
    unique = None
    for string in arr:
        key = frozenset(set(string.lower()).difference(' '))
        if key in dct:
            unique = key
        if unique is not None:
            if key != unique:
                return string
            if len(dct) > 1:
                del dct[unique]
                return next(iter(dct.values()))
        dct[key] = string

print(find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]))