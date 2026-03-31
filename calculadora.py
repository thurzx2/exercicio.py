
n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo  numero: '))
operacoes = input('digite a operaçao (+, -, *, /) : ')
match operacoes :
    case '+':
        print(n1 + n2 )

    case '-' :
        print (n1 - n2 )
    case '*' :
        print (n1 * n2 )
    case '/' :
        print (n1 / n2 )
    case _ :
        print('operacao invalida ')






