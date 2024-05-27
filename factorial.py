def IsInt (num):
    return type(num) ==int


def factorial(num):
    fact = 1
    if IsInt(num) == False:
        return None
    if num <0 :
        return None
    if num == 0:
        return 1
    while num>0:
        fact = fact * num
        num = num -1
    return fact 



print(factorial(4))

#using recursion

def factorialRec(num):
    if IsInt(num) == False:
        return None
    if num <0 :
        return None
    if num == 0:
        return 1
    return num * factorialRec(num-1)

print(factorialRec(4))