l = "hello"
print(l, end= '  ')
my_list = [l, "Tamim" , 34]
my_list.reverse()
print(my_list, end= '  ')
print(my_list.reverse(), end= '  ')
print(my_list[0:3])
my_input = input("please enter a number:  ")
print(int (my_input) , end= ' ')
a = float(my_input)
print(a, end= '  ' )
print(type(a))
if a > 55 :
    print("Greater than 55")
elif a==33:
    print('a is equal 33')     
else :
    print("less than 55")
my_input = input('Plz Enter :').split()
print(my_input)
for b in range(2, 10, 2) :
    print(b, end= '  ')

my_list2 = [20, 30, 49, 44]
newv = 0
for c in my_list2:
    newv=newv + c

print(newv)
