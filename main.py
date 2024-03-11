from .calculator import Calculator

number1 = float(input('첫 번째 값을 입력하세요: '))
number2 = float(input('두 번째 값을 입력하세요: '))
operator = input('연산자를 입력하세요(+, -, *, /): ')

cal = Calculator(number1, number2)

cal_plus = cal.add_cal()
cal_minus = cal.subtraction()
cal_multiply = cal.multiply()
cal_divide = cal.divide()

print("두 값의 합은?:" , cal_plus)
print("두 값의 차는?:" , cal_minus)
print("두 값의 곱은?:" , cal_multiply)
print("두 값의 나눗셈은?:" , cal_divide)