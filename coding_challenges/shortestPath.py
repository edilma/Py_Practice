def shortest_steps_to_num(num):
    if num==1:
        return 0
    if num%2==0:
        return 1+shortest_steps_to_num(num/2)
    else:
        return 1+shortest_steps_to_num(num-1)


def shortest_steps_v2(num):
        steps = 0
        while num != 1:
            if num % 2:
                num -= 1
            else:
                num //= 2
            
            steps += 1
        return steps

def shortest_steps_to_num(num):
    return num.bit_length() + bin(num).count('1') - 2

#def contandoBits(n):
def count_bits(n):
    numberBite = str(bin(n))
    countofOne= numberBite.count('1')
    return countofOne


def countBits(n):
   return str(bin(n)).count('1')


#print (shortest_steps_to_num(12))
#print (shortest_steps_v2(12))
print (contandoBits(1234))


if __name__ == "__main()__":
    #shortest_steps_to_num(12)
    #shortest_steps_v2(12)
    contandoBits(n=1234)



