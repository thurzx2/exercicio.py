from datetime import date

an = int(input('digite o seu ano de nascimento: '))
mes = int(input('digite seu mes de nascimento ' ))
dia = int(input('digite o dia do seu nascimento '))
data_atual = date.today()
if mes<data_atual.month:
    idade = data_atual.year - an
elif mes>data_atual.month:
    idade = data_atual.year - an -1
else:
    if dia  <= data_atual.day:
        idade = data_atual.year - an
    else:
        idade = data_atual.year - an - 1
print(f'nesse ano voce tem {idade} ')