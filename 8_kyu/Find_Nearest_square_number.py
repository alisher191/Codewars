def nearest_sq(n):
    square = [i*i for i in range(1, 10000)]
    if n in square:
        return n
    else:
        for i in range(len(square)):
            if square[i] < n and square[i+1] > n:
                before = n - square[i]
                after = square[i+1] - n
                return square[i] if before < after else square[i+1]

print(nearest_sq(9999)) 
