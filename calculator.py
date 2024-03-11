class Calculator:
    pass
    # 덧셈
    # 뺄셈
    # 곱셈
    # 나눗셈
    def division(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print('나누는 숫자가 0인지 확인해주세요')