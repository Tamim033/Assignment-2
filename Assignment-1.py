list_1 = input('Plz input numbers using space in list-1 :').split()
list_2 = input('Plz input numbers using space in list-2 :').split()
list_3 = []
for a in range (len(list_1)):
    list_3.append(int(list_1[a]) + int(list_2[a]))
print("Addition of the Lists :", list_3)
print("Reverse List:", list_3[::-1])
i1= input("Plz input after which item need to add 9 :")
i2= list_3.index(int(i1))
list_3.insert(i2+1,9)
print("Added List", list_3 )
list_4 = [5, 20, 15, 20, 25, 50, 20]
item = 20
print("Repeated item list : ", list_4 , "item to be removed: ", item )
list_4 = [i for i in list_4 if i != int(item)]
print("Removed List :", list_4)