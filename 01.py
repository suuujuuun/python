#put 5, answer 120{1*2*3*4*5}

def recursion(fac_number):
    
    if fac_number < 0:
        return "음수는 계산할 수 없습니다."

    if fac_number == 1:
        return 1

    return recursion(fac_number-1) * fac_number


a = 5
print(recursion(a))

