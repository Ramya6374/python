# Color = ["rad","blue","white","block"]
# print(Color)

# # list length
# Color = ["red","white","block","blue"]
# print(len(Color))

# list item

# list1 = ["red","white","block"]
# list2 = [1,6,8,9]
# list3 = ["apple"",orange","grapes"]
# print(list1)
# print(list2)

# list1 = ["abc", "true" , 40, "female"]
# print(list1)

# type of the list
# mylist = ["apple","grapes","orange"]
# # print(type(mylist))

# list = ["cat","dog","fish"]
# print(list[2])

# negattive indexng

# animals = ["lion","tiger","cow",]

# print(animals[-1])

# range of list

# colors = ["blue","pink","yellow","green"]
# print(colors[2:3])


# fruits = ["apple","banana","orange","grapes","mango"]
# print(fruits[:4])

# fruits = ["apple","banana","orange","mango"]
# print(fruits[3:])

# colors = ["red","blue","white","yellow","green","block"]
# print(colors[-3:-1])

# if item method


# colors = ["red","blue","block","white","green"]
# if "blue" in colors:
#     print("yes, 'blue' is in the colors list" )


# change the list value

# colors = ["block","blue","green"]
# colors[2] = "yellow"
# print(colors)

# # change the range of item values
# fruits = ["apple","cherry","mango","grapes"]
# fruits[1:2]=["banana","orange"]
# print(fruits)


# insert items


# fruits = ["orange","cherry","grapes","apple"]
# fruits.insert(2,"watermelon")
# print(fruits)

# append method

# colors = ["red","yellow","white"]
# colors.append("blue")
# print(colors)


# insert items

# fruits = ["apple","cherry","watermelon","orange"]
# fruits.insert(1,"grapes")
# # print(fruits)

# list = ["apple","banana","orange"]
# fruits = ["mango","grapes","pineapple"]
# list.extend(fruits)
# print(list)

# remove list

# colors = ["blue","yellow","white","green"]
# colors.remove("yellow")
# print(colors)

# pop method


# colors = ["green","orange","yellow","blue"]
# colors.pop(2)
# print(colors)

# colors = ["yello","green","orange","red"]
# colors.pop()
# # print(colors)

# delete method
# fruits = ["oange","apple","cherry"]
# del fruits[2]
# print(fruits)

# clear the list

# fruits = ["apple","mango","orange"]
# fruits.clear()
# print(fruits)

# loop method


# colors = ["red","green","blue"]
# for x in colors:
#     print(x)


# fruits = ["banana","cherry","mango"]
# for i in  range(len(fruits)):
#     print(fruits[i])


# colors = ["orange","green","yeellow"]
# [print(x) for x in colors]
# from symbol import comparison


# # list comparison

fruits = ["orange","apple","banana"] 
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

# fruits = ["cherry","watermelon","apple"]
# newlist = [ x for x in fruits if "a"in x]
# # print(newlist)

# colors = ["green","white","block","pink"]
# newlist = [x for x in colors if x !="white"]
# # print(newlist)


# fruits =["apple","banana","cherry"]
# newlist = [x for x in fruits]
# # print(newlist)

# newlist = [ x for x in range(10)]
# print(newlist)

# newlist = [ x for x in range(10)if x<5]
# print(newlist)


# fruits = ["cherry","orange","watermelon","banana"]
# newlist = [x.upper()for x in fruits]
# print(newlist)


# fruits = ["grapes","kiwi","orange","cherry"]
# newlist = ['hello'for x in fruits]
# # print(newlist)

# colors = ["red","yellow","pink","white"]
# newlist = [x if x !="yellow"else "pink"for x in colors]
# print(colors)

# sort list

# fruits = ["apple","orange","grapes","cherry"]
# fruits.sort()
# print(fruits)

# sort the list numerically

# list = [25,30,56,86,28,65]
# list.sort()
# print(list)

# fruits = ["mango","cherry","watermelon","grapes"]
# fruits.sort(reverse = True)
# print(fruits)

# customized sort function

# def myfunc(n):
#     return abs(n-60)
# list = [100,67,54,96,82]
# list.sort(key = myfunc)
# print(list)

# list = ["ramya","charu","ashok","sabari","sathiya"]
# list.sort(key = str.lower)
# # print(list)

# reverse orsder

# list = ["ramya","charu","sabari","sathiya","ashok"]
# list.reverse()
# print(list)

# # copy list

# list = ["priya","kani","raji","sabitha"]
# mylist = list.copy()
# print(mylist)

# fruits = ["apple","orange","cherry","grapes"]
# mylist = list(fruits)
# print(mylist)

# # join list

# list1 = ["c","o","r","k","s"]
# list2 = [1,8,6,4]
# list3 = list1+list2
# print(list3)


# list1 = ["f","h","i","k","p"]
# list2 = [6,8,5,9,3,7]
# for x in list2:
#     list1.append(x)
# print(list1)

# list1 = ["j","y","d","l"]
# list2 =[5,8,3,9]
# list1.extend(list2)
# print(list1)