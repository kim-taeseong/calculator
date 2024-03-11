class Calculator:
    pass
    # 덧셈
    # 이재준 더하기 함구 구현
def add_cal(x,y):
    return x + y

x = float(input("첫 번째 값을 입력하세요: "))
y = float(input("두 번째 값을 입력하세요: "))

result = add_cal(x,y)
print("두 값의 합은?:" , result)
    # 뺄셈
    # 곱셈
    # 나눗셈
    def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print('나누는 숫자가 0인지 확인해주세요')