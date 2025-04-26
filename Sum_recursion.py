def sum_recursion(n):
    if n == 1:
        print("NUMBER:1")
        return 1
    else:
        s_number = sum_recursion(n-1)
        total = n + s_number
        #Gives of the number and the sum
        #it then continues till it reaches the last number/conditioin
        print("the Sum of",n ,"and",s_number,"is",total)
        return total
    
#TOTALS THE FIRST 10 NUMBERS 

print("Sum of first 10 numbers:", sum_recursion(8))
