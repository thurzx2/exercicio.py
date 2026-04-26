salario = float(input('digite o seu salario: '))
if salario <= 1500.00:
    aumento = salario * 0.20
    print('Você teve um aumento de 20%! ')
elif salario <= 1500.01 and salario <= 3000.00:
    aumento = salario  * 0.15
    print('Você teve um aumento de 15%! ')
elif salario <= 3000.01 and salario <= 5000.00:
    aumento = salario * 0.10
    print('Você teve um aumento de 10%! ')
else:
    aumento = salario * 0.05
    print('Você teve um aumento de 5%!')
novo_salario = salario + aumento
print(f'valor do aumento R$: {aumento:.2f}')
print(f'Novo salario R$: {novo_salario:.2f} ')