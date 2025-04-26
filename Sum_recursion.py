def sum_recursion(n):
    if n == 1:
        print("NUMBER:1")
        return 1
    else:
        return n + sum_recursion(n-1)
    

print("Sum of first 10 numbers:", sum_recursion(10))
