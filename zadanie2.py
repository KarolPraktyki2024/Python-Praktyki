lista = []

while(True):
    number = input("wprowadź numner do list:")

    if(number == "STOP"):
        break
    else:
        lista.append(number)

def minMax(myList):
    return min(myList), max(myList)

minMaxValues = minMax(lista)

print('Najniższa wartość: ',minMaxValues[0])
print('Najwyższa wartość: ',minMaxValues[1])
