numero = int(input("Digite um número inteiro: "))

if numero % 5 == 0 and numero % 3 == 0:
    print(f"O número {numero} é divisível por 5 e por 3.")
elif numero % 5 == 0:
    print(f"O número {numero} é divisível apenas por 5.")
elif numero % 3 == 0:
    print(f"O número {numero} é divisível apenas por 3.")
else:
    print(f"O número {numero} não é divisível por 5 nem por 3.")