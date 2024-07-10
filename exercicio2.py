
# numeros = [1,2,3,4,5,6,7,8,9,10]
# nomes = ['hitallo,emanuel,soares,souza']
# ano =[1997,2024]

# soma_impares = 0

# for num in range(1,11):
#     if num % 2 != 0:
#         soma_impares += num
   
# print(soma_impares)


# for num in range(100,90,-1):
#     print(num)

# numero_digitado = int(input("Digite um numero"))

# for i in range(1,11):
#     result = numero_digitado * i
#     print(f'Numero {numero_digitado} x {i} resultado {result}')



# numero = int(input('Digite um numero: '))

# for i in range(1,11):
#     result = numero * i
#     print(f'Numero {numero} x {i} = {result}')

#  Crie uma lista de números e utilize um loop for para 
# calcular a soma de todos os elementos. Utilize um bloco
# try-except para lidar com possíveis exceções.


numeros = [1,2,3,4,5]

try:
    soma = 0
    for numero in numeros:
        soma += numero
        print(f'a soma dos numero é igual: {soma}')
except:
         print('ocorreu algum erro')


