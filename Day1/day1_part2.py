import sys

lista1 = []
lista2 = []
sum = 0

for linha in sys.stdin:
    numbers = linha.split()
    lista1.append(int(numbers[0]))
    lista2.append(int(numbers[1]))

for key in range(len(lista1)):
    number_keys = 0
    for number in range(len(lista2)):
        if(lista2[number] == lista1[key]):
            number_keys += 1

    sum += (lista1[key] * number_keys)        

print(sum)