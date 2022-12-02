list_1 = input('Plz input numbers using space in list-1 :').split()
list_2 = input('Plz input numbers using space in list-2 :').split()
list_3 = []
for a in range (len(list_1)):
    list_3.append(int(list_1[a]) + int(list_2[a]))
print("Addition of the Lists :", list_3)
print("Reverse List:", list_3[::-1])
list_3.insert(0,9)
print("Added in Beginning-", list_3 )
list_5 = [5, 20, 15, 20, 25, 50, 20]
print("Repeated item list :", list_5)
item = input('Plz input item to remove from new list: ')
list_5 = [i for i in list_5 if i != int(item)]
print("Removed List :", list_5)