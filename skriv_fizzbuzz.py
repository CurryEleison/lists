#3: Skriv "FizzBuzz"
for i in range(101):
    if i % 3 == 0:
        print("fizz")
        continue
    elif i % 5 == 0:
        print("buzz")
        continue
    elif i % 3 == 0:
        if i % 5 == 0:
            print("fizzbuzz")
            continue
    print(i)

