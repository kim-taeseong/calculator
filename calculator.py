class Calculator:
    # 초기화
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    # 덧셈
    # 이재준 더하기 함구 구현
    def add_cal(self):
        return self.number1 + self.number2

    # 뺄셈
    def subtraction(self):
        return self.number1 - self.number2

    # 곱셈
    def multiply(self):
        return self.number1 * self.number2

    # 나눗셈
    def divide(self):
        try:    
            return self.number1 / self.number2
        except ZeroDivisionError:
            print('나누는 숫자가 0인지 확인해주세요')
