def ja(n):
    if n <= 1:
        return 1
    else:
        return n * ja(n-1)
print(ja(int(input())))