numero = int(input('digite um numero: '))
if numero % 2 == 0:
    print(f'numero {numero} é par')
else:
    print(f'numero {numero} é impar')

idade = int(input('Digite sua idade'))
if idade <= 12:
   print('voce é criança')
elif idade >= 13 and idade <=18:
   print('voce é adolecente')
else: 
   print('voce é adulto')

usuario = 'hitallo'
senha = '10203040'

usuario_test = input('usuario: ')
senha_test = input('senha: ')

if usuario == usuario and senha == senha_test:
   print('login success')
else:
   print('usuario e senha invalidos')