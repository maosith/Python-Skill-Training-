#Exemplos com nome e perguntas:

name = input("Digite seu nome:")

print("Olá"",",name)

#Exemplos com números:

num = int(input("Me dê um número:"))

print("Seu número é:",num)

num2 =int(input("Agora me dê mais um número para completarmos a soma de ambos:"))

print("Você me deu o número",num2,"como sequencia do outros que pedi")

print("Agora vou te dar a soma dos dois, ela é:")

print(num + num2)

#Exemplos com float(input)

print(name,"me diga mais um número com virgula")

flo = float(input("Qual é o seu número (float)?"))

print("Seu número é:",flo)

flo2 = float(input("Agora mais um número pra nós por exemplos, ver a divisão: "))

print("Aqui está o resultado de: ",flo / flo2)

#Exemplo de if, else

print(name,"agora vamos ver a diferença de grandeza dos números")

a = int(input("Me dê qualquer número: "))
b = int(input("Agora mais um número: "))

if a > b:
    print(a,"é maior que",b)

else:
    print(a,"não é maior que",b)

