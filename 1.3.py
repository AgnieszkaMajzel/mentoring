def gcd (a, b):
    while a!=b:
        if a > b:
            a = a - b
        elif b > a:
            b = b - a
    return a

print(gcd(60,100))
