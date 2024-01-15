def remove_consecutive_duplicates(s):
    lis = []
    for i in s.split():
        if len(lis) != 0:
            if i == lis[-1]:
                continue
            else:
                lis.append(i)
        else:
            lis.append(i)
    return " ".join(lis)

