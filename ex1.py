def soma_numeros(a,b,c):
    if type(a) != float  or type(b) != float or type(c) != float or a<0 or b<0 or c<0:
        raise TypeError('os valores devem ser float ou positivos')
    if a + b==c or b+c==a or a+c==b:
        return True
    else:
        return False

while True:
    try:
        a= float(input("Primeiro numero:"))
        b= float(input('Segundo numero:'))
        c= float(input('Terceiro numero:'))
        print(soma_numeros(a,b,c))
    except ValueError:
        print('Erro: Os valores informados não são numeros')
    except TypeError as erro:
        print(f'Erro: {erro}')
    else:
        print('progama finalizado')
        break
    
