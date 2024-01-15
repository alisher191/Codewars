def get_sum(a,b):
    if a == b:
        return a
    elif a > b:
        return sum(range(b, a+1))
    return sum(range(a, b+1))
