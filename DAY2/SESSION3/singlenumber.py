def single_number(num):
    xor=0
    for n in num:
        xor=xor^n
    a=0
    b=0
    for n in num:
        if(n&xor)==0:
            a=a^n
        else:
            b=b^n
    return [a, b]

num = [1, 2, 1, 3, 2, 5]
print(single_number(num))
