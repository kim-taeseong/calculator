class Calculator:
    # 덧셈
    # 이재준 더하기 함구 구현
    def add_cal(x,y):
        return x + y

    # 뺄셈
    def subtraction():
        숫자1 = float(input("첫 번째 숫자를 입력하세요: "))
        연산자 = input("연산자를 입력하세요 (-): ")
        숫자2 = float(input("두 번째 숫자를 입력하세요: "))

        if 연산자 == '-':
            결과 = 숫자1 - 숫자2
        else:
            print("올바른 연산자를 입력해주세요.")
            return
        print("결과:", 결과)

    # 곱셈
    def multiply(a, b):
        return a*b

    # 나눗셈
    def divide(a, b):
        try:    
            return a / b
        except ZeroDivisionError:
            print('나누는 숫자가 0인지 확인해주세요')
