import sys

lista1 = []
lista2 = []
sum = 0

for linha in sys.stdin:
    numbers = linha.split()
    lista1.append(int(numbers[0]))
    lista2.append(int(numbers[1]))

lista1.sort()
lista2.sort()

for number in range(len(lista1)):
    sum += abs(lista1[number] - lista2[number])

print(sum)