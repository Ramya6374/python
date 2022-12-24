# # A = "flower is beautiful"
# # B = "tree is green"
# # print(A.capitalize())
# # print(B.upper())
# # print(A.index("beautiful"))
# # B = A.replace("is","are")
# # print(B)



# # A = int(input("Enter the value of A:"))
# # B = int(input("Enter the value of B:"))
# # sum = A+B
# # sub = A-B
# # divide = A/B
# # multiple = A*B
# # print("sum",sum)
# # print("sub",sub)
# # print("divide",divide)
# # print("multiple",multiple)



# # A = ["apple","grape","orange","mango"]
# # B = input("Enter a word")

# # A.append(B)
# # print(A)
# # C = len(A)
# print(C)


# lis = []
# for i in range(200,250,10):
#     lis.append(i)
# print(lis)
# B = sum(lis)
# print(B)


# # A = "flowers"
# # for i in A:
# #     print(i)
# #     if(i=="l"):
# #         print("it is lotus")
# #     elif(i=="r"):
# #         print("it is rose")
# #     else:
# #         print("others")   

# dictionary

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
# #   "year": 1964
# # }




A = [{"Name":"rajalakshmi",
"Age":"21",
"dept":"cse",
"sub": {"maths":87,"science":75,"tamil":65,"english": 76}
},
{"Name":"roja",
"Age":"21",
"dept":"cse",
"sub": {"maths":88,"science":79,"tamil":25,"english": 96}
}]
B = []
for i in A:
    name = i.get("Name")
    subjects = i.get("sub")
for keys,values in subjects.items():
    if values <50:
        print(keys,values,"fail")
    else:
        print(keys,values,"pass")


print(B)




# keys = {'abi9,maha,raji,prathab'}
# values = {'java','python','js'}
# data = dict(zip(keys,values))
# print(data)


# temp = int(input("what is the temperature outside?: "))
# if temp >= 0 and temp <= 30:
#     print("the temprature is good today!")
#     print("go outside!")
# elif temp < 0 or temp> 30:
#     print("the temprature is bad today!
#     print("stay inside!")

a = {"Name":"roja",
"Age":"21",
"dept":"cse",
"sub": {"maths":88,"science":79,"tamil":25,"english": 96}
}
a["Name"]= "ramya"
print(a)
B =  []


subjects = a.get("sub")

for keys,values in subjects.items():
    print(values)
    B.append(values)
print(B)
print(sum(B))

    




    