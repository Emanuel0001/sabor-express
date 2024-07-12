pessoa = { 'nome': 'hitalo', 'idade': 26, 'cidade':'santo antonio do retiro'}


# pessoa['idade'] = 50
pessoa.update({'idade': 50, 'sexo': 'masculino'})
valor_removido = pessoa.pop('cidade')
print(valor_removido)
print(pessoa)