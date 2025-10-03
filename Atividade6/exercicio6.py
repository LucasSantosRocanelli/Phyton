
nota_formativa1 = float(input("Digite a nota da primeira formativa: "))
nota_formativa2 = float(input("Digite a nota da segunda formativa: "))
nota_prova_bimestral = float(input("Digite a nota da prova bimestral: "))

media_formativas = (nota_formativa1 + nota_formativa2) / 2

media_bimestral = (media_formativas * 0.3) + (nota_prova_bimestral * 0.7)

print(f"Média das formativas: {media_formativas:.1f}")
print(f"Nota da prova bimestral: {nota_prova_bimestral:.1f}")
print(f"Média bimestral final: {media_bimestral:.1f}")

if media_bimestral >= 6.0:
    print("Situação: Aprovado!")
else:
    print("Situação: Reprovado!")