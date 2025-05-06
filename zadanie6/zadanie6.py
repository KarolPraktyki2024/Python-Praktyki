myList = []

for i in range(100):
    myList.append(i)



searchNumber = int(input("Wprowadź szukaną liczbę"))

while(len(myList) > 1):
    leng = len(myList)
    print(leng//2)
    if(searchNumber<=myList[leng//2]):
        print("LEWA")
        temp = []
        for i in range((leng//2)):
            temp.append(myList[i])
        myList = list(temp)
    elif (searchNumber>myList[leng//2]):
        print("PRAWA")
        temp = []
        for i in range(leng,leng//2):
            temp.append(myList[i])
        myList = list(temp)
    
    else:
        print(myList)
    print(myList)
