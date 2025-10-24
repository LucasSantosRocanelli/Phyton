import os

for i in range(1, 21):
    print(i, end=' ')
print()

input("Pressione qualquer tecla para continuar...")

os.system('cls' if os.name == 'nt' else 'clear')

for i in range(20, 0, -1):
    print(i, end=' ')
print()