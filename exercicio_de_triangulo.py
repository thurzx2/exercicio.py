ld1 = int(input('digite o primeiro lado do triangulo: '))
ld2 = int(input('digite o segundo lado do triangulo: '))
ld3 = int(input('digite o terceiro lado do triangulo: '))
if (ld1 + ld2 > ld3) and (ld1 + ld3 > ld2) and (ld2 + ld3 > ld1):
    print('OS valores formam um triangulo! ')
    if ld1 == ld2 == ld3:
        print('Voce tem um triangulo equilatero! ')
    elif ld1 == ld2 or ld1 == ld3 or ld3 == ld2:
     print('Voce tem um triangulo isocelis! ')
    else:
        print('voce tem um tringulo escaleno! ')
else:
   print('Os valores informados nao formam um triangulo')