#WAP using recursion to calculate super digit of a given integer.

def super_digit(n):
    if n == 0:
        return 0
    else:
        n= (n % 10 + super_digit(int(n / 10)))

    if n > 9:
        n=super_digit(n)
    return n

num = int(input('Enter number: '))
result = super_digit(num)
print(result)
