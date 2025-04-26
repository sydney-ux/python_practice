num= int(input("Enter a number: "))
fact = 1
count = 1
#count loops from 1 to the number chosen as long it is less than or equal to it
while count <= num:
    fact = fact * count
    #loop increments
    count= count+ 1

print(fact)
