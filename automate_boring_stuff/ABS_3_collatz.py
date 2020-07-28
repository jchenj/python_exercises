def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return(number // 2)
    elif number % 2 == 1:
        result = (3 * number + 1)
        print(result)
        return(result)

try:
    print("Enter an integer.")
    value = int(input())
    while value != 1:
        value = collatz(int(value))

except ValueError:
        print("Error - enter whole numbers only.")



