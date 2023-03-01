print("----------------------------------------------------------------")
print("                          CALCULADORA                           ")
print("----------------------------------------------------------------")
a = float(input('Digite o primeiro valor para o calculo: '))
b = float(input('digite o segundo valor para o calculo: '))
operador  = input('Digite uma das opções a seguir (+, -, /, *, **): ')
operacao = float
if operador == '+':
    operacao = a + b
elif operador == '-':
    operacao = a - b
elif operador == '/':
    operacao = a / b
elif operador == '*':
    operacao = a * b
elif operador == '**':
    operacao = a ** b
else:
    print("Digite apenas um dos operadores lógicos das opções mostradas")

print(operacao)
