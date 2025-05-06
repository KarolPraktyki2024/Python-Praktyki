lista = [1,4,-4,7]

def minMax(myList):
    return min(myList), max(myList)

minMaxValues = minMax(lista)

print('Najniższa wartość: ',minMaxValues[0])
print('Najwyższa wartość: ',minMaxValues[1])
