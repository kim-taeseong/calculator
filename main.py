from .calculator import Calculator

x = float(input("첫 번째 값을 입력하세요: "))
y = float(input("두 번째 값을 입력하세요: "))

cal = Calculator()
result = cal.add_cal(x,y)

print("두 값의 합은?:" , result)