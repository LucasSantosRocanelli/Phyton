
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Não é possível dividir por zero"

print("Resultados das operações:")
print(f"{num1} + {num2} = {soma}")
print(f"{num1} - {num2} = {subtracao}")
print(f"{num1} * {num2} = {multiplicacao}")
print(f"{num1} / {num2} = {divisao}")