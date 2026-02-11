def collatz(n):
    if n % 2 == 0:
        even = n // 2
        print("Even number:", even)
        return n // 2
    else:
        odd = 3 * n + 1
        print("Odd number:", odd)
        return 3 * n + 1
    
number = int(input("Enter a positive number: "))

# Program will continue to run until the number becomes 1
while number != 1:
    print(number)
    number = collatz(number)