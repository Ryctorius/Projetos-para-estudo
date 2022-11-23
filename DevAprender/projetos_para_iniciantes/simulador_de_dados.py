def testador_de_resposta(resposta_recebida):
    while resposta_recebida != ('n' or 'N' or 's' or 'S'):
        resposta_recebida = input(str('Opção Inválida. Tente Novamente'))
    return resposta_recebida  


from random import randint
while True:
    sorteio_dado = randint(1,6)
    print('O número sorteado foi:',sorteio_dado)
    continuar_while = input(str('\nDeseja sortear um novo número?(s/n)'))
    resposta_correta = testador_de_resposta(continuar_while)
    if continuar_while == 'n' or continuar_while == 'N':
        print('\n Obrigado por jogar com a gente!!!')
        break
