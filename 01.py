def recursion(fac_number):
    
    if fac_number < 0:
        return "음수는 계산할 수 없습니다."

    if fac_number == 1:
        return 1

    return recursion(fac_number-1) * fac_number

def calculator(K):

    a = str(input("연산자를 선택하세요 : "))

    if a == '+':
        b = int(input(f"{K}{a}?"))
        a = K + b
    elif a == '-':
        b = int(input(f"{K}{a}?"))
        a = K - b
    elif a == '*':
        b = int(input(f"{K}{a}?"))
        a = K * b
    elif a == '/':
        b = int(input(f"{K}{a}?"))
        a = K / b
    else:
        print("연산자가 옳지 않습니다. 재실행 해주세요")

    return a

print(calculator(4))

ㅇdsdf

