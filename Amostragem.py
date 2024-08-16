print("Bem-vindo ao Gerador de Amostragem!")
pontos = int(input("Deseja gerar amostragem de quantos pontos? "))

porcentagem = 0

if pontos <= 99 and pontos >= 60:
    porcentagem1 = int(input("Quantos % de amostragem deseja? 5% 10% 50% 100% "))
    porcentagem += porcentagem1
    aviso1 = input(f'Deseja confirmar amostragem de {porcentagem}%? "Sim" ou "Não": ')
    if aviso1 == "Sim":
        quantidade_de_pontos = round(int(pontos * (porcentagem / 100) + 1))
        print(f"A amostragem de {porcentagem}% escolhida, exibirá {quantidade_de_pontos} pontos")
    else:
        print("Amostragem não confirmada.")
elif pontos <= 59 and pontos >= 30:
    porcentagem2 = int(input("Quantos % de amostragem deseja? 10% 50% 100% "))
    porcentagem += porcentagem2
    aviso2 = input(f'Deseja confirmar amostragem de {porcentagem}%? "Sim" ou "Não": ')
    if aviso2 == "Sim":
        quantidade_de_pontos = round(int(pontos * (porcentagem / 100) + 1))
        print(f"A amostragem de {porcentagem}% escolhida, exibirá {quantidade_de_pontos} pontos")
    else:
        print("Amostragem não confirmada.")
elif pontos <= 29 and pontos >= 6:
    porcentagem3 = int(input("Quantos % de amostragem deseja? 50% 100% "))
    porcentagem += porcentagem3
    aviso3 = input(f'Deseja confirmar amostragem de {porcentagem}%? "Sim" ou "Não": ')
    if aviso3 == "Sim":
        quantidade_de_pontos = round(int(pontos * (porcentagem / 100) + 1))
        print(f"A amostragem de {porcentagem}% escolhida, exibirá {quantidade_de_pontos} pontos")
    else:
        print("Amostragem não confirmada.")
elif pontos <= 5 and pontos >= 1:
    restante = input(f'Deseja gerar amostragem dos {pontos} pontos restante? "Sim" ou "Não": ')
    if restante == "Sim":
        print(f"A amostragem do total de {pontos} pontos restantes foi gerada com sucesso!")
    else:
        print("Tudo bem, amostragem não gerada!")
else:
    porcentagem4 = int(input("Quantos % de amostragem deseja? 3% 5% 10% 50% 100% "))
    porcentagem += porcentagem4
    aviso4 = input(f'Deseja confirmar amostragem de {porcentagem}%? "Sim" ou "Não": ')
    if aviso4 == "Sim":
        quantidade_de_pontos = round(int(pontos * (porcentagem / 100) + 1))
        print(f"A amostragem de {porcentagem}% escolhida, exibirá {quantidade_de_pontos} pontos")
    else:
        print("Amostragem não confirmada.")

