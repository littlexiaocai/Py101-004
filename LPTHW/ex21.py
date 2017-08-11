def add(a,b):
    print"adding %d + %d" %(a,b)
    return a+b

def subtract(a,b):
    print"subtracting %d-%d" %(a,b)
    return a-b

def multiply(a,b):
    print"multiplying %d*%d" %(a,b)
    return a*b

age = add(34,23)
height = subtract(34,4)
weight = multiply(89,2)

print"age:%d,height:%d,weight:%d"%(age,height,weight)
what = add(age,subtract(height,multiply(weight,23)))
print what

