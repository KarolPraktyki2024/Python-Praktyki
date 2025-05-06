myList = []

while(True):
    number = input("wprowadź numner do list (aby zakończyć wprowadzanie wpisz 'STOP'): ")

    if(number == "STOP"):
        break
    else:
        myList.append(int(number))

numberL = int(input("Wprowadź liczbę L:"))


found = False
for i in range(len(myList)):
    firstNum = myList[i]
    for j in range(len(myList)):
        secondNum = myList[j]
        if(firstNum + secondNum == numberL and not i == j):
            print('Zakończono poszukiwania par liczb mających sumę',numberL,": ",firstNum,secondNum)
            found = True
            break
    if(found):
        break

if(found == False):
    print("nie ma takich dwóch liczb")
