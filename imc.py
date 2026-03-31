altura = float(input('digite sua altura '))
peso = float(input('digite seu peso '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('voce esta abaixo do peso ')
elif imc >= 18.5 and imc < 25:
    print ('voce esta normal ')
elif imc >= 25 and imc  < 30:
    print('voce esta com sobrepeso' )
else:
    print('voce esta obeso')

print(f'o seu imc sera {imc:.2f} ')

