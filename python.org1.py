#Topic : Recursion 
# solve a problem by solving smaller instances of the same problem
#project : Factorial of a numbers
#Hint : Factorial of (5)= 5*4*3*2*1 == 120
#       n = n*(n-1)
def number(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        return n * number(n - 1)

print(number(5))         


