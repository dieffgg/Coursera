n = 1 
while n < 100: 
    print(n)
    if n % 3 == 0 and n % 5 == 0:
        print("fizzBuzz")
    else:
        if n % 5 == 0 and not (n % 3 == 0):
            print("buzz")
        else:
            if (n % 3 == 0) and not (n % 5 == 0):
                print("fizz")
            else:
                print("n")
    n += 1 