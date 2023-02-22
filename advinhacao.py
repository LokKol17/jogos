import random

print('********************************')
print('Bem vindo ao jogo de Advinhação!')
print('********************************')

numero_secreto = random.randint(1, 100)
tentativas_restantes = 7

while tentativas_restantes > 0:
    print(tentativas_restantes, "tentativas restantes")
    chute = int(input("Digite seu numero: "))

    if chute < 0 or chute > 100:
        print("numero invalido")
        chute = int(input("Digite seu numero: "))

    acertou = chute == numero_secreto

    if acertou:
        print('Parabéns você acertou!')
        tentativas_restantes = 0
        break
    else:
        if chute < numero_secreto:
            print('O numero secreto é maior')
        else:
            print('O numero secreto é menor')
    tentativas_restantes = tentativas_restantes - 1
print('Fim de Jogo! O numero secreto era:', numero_secreto)
