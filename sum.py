def get_sum(a,b,c):
    sum = a+b+c
    return sum

print (get_sum(1,2,3))

#NON-KEYWORD ARGUMENT
def sum_all(*args):
    return sum(args)
result = sum_all(1,2,3,4,5)
print(result)


#KEYWORD ARGUMENT
def get_details(**kwargs):
    print(kwargs)

get_details(name="Sydney", age=45)



def get_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

get_details(name="Sydney", age=45)