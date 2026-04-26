n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda  nota: '))
n3 = float(input('digite a terceira nota: '))
freq = float(input('digite a frequencia do aluno (0 a 100) '))
media_arti = (n1 + n2 + n3) /3
if freq < 75:
    print('Você foi reprovado por excesso de faltas! ')
elif  media_arti >= 7.0:
    print('Você foi aprovado! ')
elif media_arti >= 4.0 and media_arti <= 6.9:
    print('Você está de recuperação! ')
else:
    print('Você esta reprovado por nota')