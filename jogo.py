nick = input('digite o seu nick: ')
classe = input('escolha a sua classe (Arqueiro, Guerreiro e Mago)').lower()
hp_monstro = 100
energia = 20
dano = 0
print(f'\n{"="*30}')
print(f'Olá, {nick}, o monstro possui {hp_monstro}! ')
print(f'\n{"="*30}')
while hp_monstro > 0:
    print(f'\n--- STATUS: HP DO MONSTRO: {hp_monstro} | ENERGIA: {energia} ---')
    
    atk_desejado = input('Escolha o seu ataque (básico ou especial): ').lower()

    if classe == 'guerreiro':
        if atk_desejado == 'básico':
            dano = 15
        elif atk_desejado == 'especial':
            if energia >= 10:
                dano = 30
                energia -= 10
            else:
                print('Energia insuficiente!')
                dano = 0

    elif classe == 'mago':
        if atk_desejado == 'básico':
            dano = 10
        elif atk_desejado == 'especial':
            if energia >= 20:
                dano = 50
                energia -= 20
            else:
                print('Energia insuficiente!')
                dano = 0

    elif classe == 'arqueiro':
        if atk_desejado == 'básico':
            dano = 5
        elif atk_desejado == 'especial':
            if energia >= 5:
                dano = 20
                energia -= 10
            else:
                print('Energia insuficiente!')
                dano = 0
    else:
        print('Classe inválida!')
        break
    hp_monstro = hp_monstro - dano
    print(f'\n>>> {nick} usou {atk_desejado} e causou {dano} de dano!')
    print(f'>>> Energia restante: {energia}')
    print(f'>>> Hp do monstro: {hp_monstro}')

    if hp_monstro <= 0:
        print('\n🏆 PARABÉNS!!!!! O monstro foi derrotado!')
    else:
        print('\n💀 O monstro sobreviveu ao seu ataque!')