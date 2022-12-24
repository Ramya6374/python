# Car = {
#  "brand":"Tata",
#  "model":"altroz",
#  "year":2022
# }
# # print(Car)

# Car = {
#     "brand":"Tata",
#     "model":"altroz",
#     "year":2022
# }
# # print(Car["model"])

# Dictionary length

# Car = {
#     "brand":"Tata",
#     "model":"altroz",
#     "year":"2022"
# }
# print(len(Car))

# Dictionary item_ data types


# Car = {
#     "brand":"Tata",
#     "model":"altroz",
#     "year":2022,
#     "colors":["blue", "block","white"]
# }
# print(Car)

# dictionary type


# Car = {
#     "brand":"Tata",
#     "model":"altroz",
#     "year":2022
# }
# print(type(Car))


# Car = {
#     "brand":"Ford",
#     "model":"mustang",
#     "year":2022
# }
# x = Car["brand"]
# print(x)

# get method

# Car ={
#   "brand":"Tata",
#   "model":"altroz",
#   "year":2022
# }
# x = Car.get("brand")
# # print(x)

# key method

# Car = {
#     "brand":"Tata",
#     "model":"altroz",
#     "year":2022
# }
# x = Car.keys()
# # print(x)

# Car = {
#     "brand":"Tata",
#     "model":"altroz",
#     "year":2022
# }
# x = Car.keys()
# print(x)
# Car["color"]="block"
# print(x)

# values method

# Car = {
#     "brand":"Tata",
#     "model":"altroz",
#     "year":2022
# }
# x = Car.values()
# # print(x)


# Car = {
#     "brand":"Tata",
#     "model":"altroz",
#     "year":2022
# }
# x = Car.values()
# print(x)
# Car["year"] = 2018
# # print(x)


# Car = {
#     "brand":"Tata",
#     "model":"altorz",
#     "year":2022
# }
# x = Car.values()
# print(x)
# Car["color"] = "blue"
# # # print(x)

# # dictinory items

# Car = {
#     "brand":"Tata",
#     "model":"altroz",
#     "year":2022
# }
# x = Car.items()
# print(x)
# Car["year"] = 2020
# # print(x)

# Car = {
#     "brand":"Tata",
#     "model":"altroz",
#     "year":2022
# }
# x = Car.items()
# print(x)
# Car["color"] = "white"
# # print(x)

# if method

# Car = {
#     "brand":"Tata",
#     "model":"altroz",
#     "year":2022
# }
# if "model" in Car:
#     print("yes,'model is one of the keys is Car dictionary")

# change method

# Car = {
#     "brond":"Tata",
#     "model":"altroz",
#     "year":2022
#  }
# Car["year"] = 2016
# # print(Car)

# update method

Car = {
    "brand":"Tata",
    "model":"altroz",
    "year":2022
 }    
Car.update({"year":2018})
print(Car)

# Car = {
#     "brand":"Tata",
#     "model":"altroz",
#     "year":2022
# }
# Car.update({"color":"yellow"})
# print(Car)

# # pop method

# Car = {
#     "brand":"Tata",
#     "model":"altroz",
#     "year":2022
# }
# Car.pop("model")
# print(Car)


# # pop items

# Car = {
#     "brand":"Tata",
#     "model":"altroz",
#     "year":2022
# }
# Car.popitem()
# print(Car)


# delete method

# Car = {
#     "brand":"Tata",
#     "model":"altroz",
#     "year":2022
# }
# del Car["model"]
# # print(Car)


# Car = {
#     "brand":"Tata",
#     "model":"altroz",
#     "year":2022
# }
# Car.clear()
# print(Car)

# # loop method

# Car = {
#     "brand":"Tata",
#     "model":"altroz",
#     "year":2022
# }
# for x in Car:
# #     print(x)

# Car = {
#     "brand":"Tata",
#     "model":"altroz",
#     "year":2022
# }
# for x in Car:
#     print(Car[x])

# Car = {
#     "brand":"Tata",
#     "model":"altroz",
#     "year":2022
# }
# for x in Car.values():
#     print(x)

# Car = {
#     "brand":"Tata",
#     "model":"altroz",
#     "yeaar":2022
#   }
# for x in Car.keys():
# #     print(x)


# Car = {
#     "brand":"Tata",
#     "model":"altroz",
#     "year":2022
# }
# for x,y in Car.items():
# #     print(x,y)


# copy methods

# Car = {
#     "brand":"Tata",
#     "model":"altrz",
#     "year":2022
# }
# mydict = Car.copy()
# # print(mydict)

# nested dictionary

# myfamily = {
#     "child1":{
#         "name":"charu",
#         "age":20
#     },
#     "child2":{
#         "name":"sabari",
#         "age":15
#     },
#     "child3":{
#         "name":"sharvika",
#         "age":5
#     }
# }
# # print(myfamily)


# myfamily = {
#     "child1":{
#         "name":"charu",
#         "age":20
#     },
#     "child2":{
#         "name":"sabari",
#         "age":15
#     },
#     "child3":{
#         "name":"sharvika",
#         "age":5
#     }

# }
# myfamily = {
#     "child1":" child1",
#     "child2": "child2",
#     "child3": "child3"
# }
# print(myfamily)
