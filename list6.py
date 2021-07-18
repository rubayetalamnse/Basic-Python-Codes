mylist = ["banana","cherry","apple"]
print(mylist)

item = mylist[0]
print(item)
print(mylist[1])
print(mylist[0:3])
print(mylist[0:2])
print(mylist[-1])
print(mylist[-2])

list2 = [1,2,3,4,5,6,7,8,"yeasa",3.40]
print(list2)

for i in list2:
    print(i)

if 3.40 in list2:
    print("yes")
else:
    print("no")

print(len(list2))
mylist.append("mango")
print(mylist)
mylist.insert(1,"pear")
mylist.pop()
print(mylist)
mylist.remove("banana")
print(mylist) 
mylist.clear()
print(mylist)
list2.reverse()
print(list2)
newlist = [67,23,56,10,98,13244]
newlist.sort()
print(newlist)
list3 = [1]*5
print(list3)
list4 = [0]*5
sum_list = list3+list4
print(sum_list) 
a = sum_list[::-1]
print(a)
b= newlist[::2]
print(b)
print(newlist[::1])
print(newlist[::2])
print(newlist[::-1])
fruits = ['banana', 'grapes', 'mango','berry','jackfruit','lichi','apple']
print(fruits)
new_fruit = fruits.copy()
print(new_fruit)
old_fruit = fruits[:]
print(old_fruit)

num_list =[1,2,3,4,5,6]
c =[i*i for i in num_list]
print(num_list)
print(c)