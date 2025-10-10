def VerificarFeriado(mes, dia):
    match mes:
        case 10:
            print(f"dia (dis) dia da independencia")
            print(f"dia (dis) dia das crianças")

    match dia:
        case 12:
            print(f"esse dia nao existe")

            def main():
                dia =int(input("Digite o dia: "))
                mes =int(input("Digite o mes: "))

                VerificarFeriado(mes, dia)

                if_name_='_main_'
                main()