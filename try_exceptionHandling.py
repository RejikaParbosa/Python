print("Practicing for try block")
try:
    numerator=50
    denom=int(input("Enter the denominator: "))
    quotient=(numerator/denom)
    print("Division performed successfully")
except ZeroDivisionError:
    print("Denominator as Zero....not allowed")
print("OUTSIDE try...except block")
