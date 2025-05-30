
def concatena_texto(texto1, texto2):
    texto_inteiro = texto1 + texto2
    imprime_2_vezes (texto_inteiro)


    def imprime_2_vezes(texto_inteiro):
        print(texto_inteiro)
        print(texto_inteiro)

texto1 = 'Já que me ensinou a beber, já que me ensinou a sofrer'
texto2 = 'Me ensina por favor como é que faz pra te esquecer'

concatena_texto(texto1 + texto2)