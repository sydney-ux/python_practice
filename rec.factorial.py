def factorial(n):
    #BASE CASE
    if n ==0 or n==1:
        return 1
    else:
       #RECURSIVE CASE
        return  n * factorial(n-1)
    #INPUT THE NUMBER
number = int(input("Enter a number:"))
result = factorial(number)
print(result)
