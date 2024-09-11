import datetime

print("Bem-vindo ao nosso evento! ")

data_def = int(input("Qual a data desse mês? "))

if data_def <10:
    print("Data do evento invalida ")
else:
    print("Data validada")

data_2 = datetime.date(2024/9/11)
print(data)

print(data.ctime())

ano = data.year
mes = data.mouth
dia = data.day
#hora = data.hora # erro!
print(ano, mes, dia)

nova_data = data.replace(day=2)
print(nova_data)
print(data)

