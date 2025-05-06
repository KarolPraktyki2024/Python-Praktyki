s = 'Ala ma kota'
print('1 - Zlicz Wyrazy')
print('2 - Zlicz Litery')
print('3 - Zbadaj Częstotliwość')

instructions = input('Wprowadź instrukcje: ')

for i in instructions:
    if(i == '1'):
        words = 0
        for j in s:
            if(j == ' '):
                words+=1
        words+=1
        print('Ilość wyrazów:',words)
    elif(i == '2'):
        letters = 0
        for j in s:
            if(j.isalpha()):
                letters += 1
        print('Ilość liter:',letters)
        break
    elif(i == '3'):
        listLetters = []
        listOccurs = []

        for j in s:
            if(j.isalpha()):
                found = False
                for k in range(len(listLetters)):
                    if(listLetters[k] == j.lower()):
                        found = True
                        listOccurs[k] += 1
                        break
                if(found == False):
                    listOccurs.append(1)
                    listLetters.append(j.lower())
        print(listLetters)
        print(listOccurs)
    else:
        print("Nieznana instrukcja")
