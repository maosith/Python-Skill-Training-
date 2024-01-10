print("Olá, bem-vindo a calculadora Python.")

operação = input('''
Escolha uma operação para continuar:

+ para somar
- para subtrair
/ para dividir
* para multiplicar
''')

num_1 = int(input("Primeiro número: "))
num_2 = int(input("Segundo número: "))

if operação == '+':
    print('{} + {} = '.format(num_1,num_2))
    print(num_1 + num_2)

elif operação == '-':
    print('{} - {} = '.format(num_1,num_2))
    print(num_1 - num_2)

elif operação == '/':
    print('{} / {} = '.format(num_1,num_2))
    print(num_1 / num_2)

elif operação == '*':
    print('{} * {} = '.format(num_1,num_2))
    print(num_1 * num_2)

else:
    print("Poxa, nenhuma operação foi escolhida. Tente novamente")

