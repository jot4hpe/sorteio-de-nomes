import random
print('sorteio de nomes')
print('----------------')
n1= str(input('digite um nome: '))
print        ('----------------')
n2= str(input('digite um nome: '))
print        ('----------------')
n3= str(input('digite um nome: '))
print        ('----------------')
n4= str(input('digite um nome: '))
print        ('----------------')
lista = [n1, n2, n3, n4]
escolhido = random.choice (lista)
print(f'o nome escolhido foi {escolhido}')
