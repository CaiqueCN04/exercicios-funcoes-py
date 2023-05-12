def numeros_natural(a,b,c,d):
    if type(a) != float  or type(b) != float or type(c) != float or a<0 or b<0 or c<0:
        raise TypeError('os valores devem ser float ou positivos')
    if a*b*c==d or a*b*d==c or a*c*d==b or c*b*d==a:
        return True
    else:
        return False



while True:
    try:
        a= float(input('coloque o primeiro numero: '))
        b= float(input('coloque o segundo numero: '))
        c= float(input('coloque o terceiro numero: '))
        d= float(input('coloque o resultado: '))
        print(numeros_natural(a,b,c,d))

    except ValueError:
            print('Erro: Os valores informados não são numeros')
    except TypeError as erro:
            print(f'Erro: {erro}')
    else:
        print('progama finalizado')
        break        
            
    