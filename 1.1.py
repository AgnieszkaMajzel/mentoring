for i in range (1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} - FizzBuzz")
    if i % 3 == 0:
        print(f"{i} - Fizz")
    elif i % 5 == 0:
        print(f"{i} - Buzz")
    else:
        print(i)