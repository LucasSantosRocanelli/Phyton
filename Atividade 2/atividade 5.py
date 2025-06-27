def right_justify(palavra, tamanhopalavra):

     espaco = ' '
     resultado = espaco * (70 - tamanhopalavra)

     print(resultado + palavra)

palavra = str(input("digite uma palavra"))
tamanhopalavra = len(palavra)

right_justify(palavra, tamanhopalavra)

