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

# test
# subtraction
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

