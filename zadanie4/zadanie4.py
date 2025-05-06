myList = []

while(True):
    number = input("wprowadź numner do list (aby zakończyć wprowadzanie wpisz 'STOP'): ")

    if(number == "STOP"):
        break
    else:
        myList.append(number)


for i in range(len(myList)):
    for j in range(len(myList)-1):
        temp = myList[j]
        if(temp > myList[j+1]):
            myList[j] = myList[j+1]
            myList[j+1] = temp

print(myList)
