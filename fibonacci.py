# Print Fibonacci series
n = int(input("Fibonacci series upto: "))
a, b = 0, 1
counter = 0
while counter < n:
    print(a)
    a, b = b, a+b
    counter += 1
