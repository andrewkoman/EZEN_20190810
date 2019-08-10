from calculator.model import CalculatorModel

class CaculatorController:
    def __init__(self):
        num1 = int( input("첫번째 값 : \n"))
        num2 = int(input("두번째 값 : \n"))
       # op = input("연산자 입력 : \n")
        self.calc = CalculatorModel(num1, num2)

    def exe(self):
        op = input('연산자 입력 : ')
        if op == '+' :
            result = self.calc.add()
        elif op == '-' :
            result = self.calc.sub()
        elif op == '*' :
            result = self.calc.mul()
        elif op == '/' :
            result = self.calc.div()

        return result