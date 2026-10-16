# student1 = {
#     "Name" : "Harsha",
#     "Name" : "A.Harshavardhan sai",
#     "AGE" : 17,
#     "City" : "Sullurpeta",
#     "Marks" : [531, 444, 957, 7.98],
#     "Active" : True
# }

# student4 = student1

# print(student1)
# print(student4)

# student1["AGE"] = 25
# print(student1)
# print(student4)

# student2 = student4
# student1["AGE"] = 31
# print(student1)
# print(student4)
# print(student4)

# print("\n\n\nUsing copy")

# student5 = student4.copy()
# student5["AGE"] = 26
# print(student1)
# print(student4)
# print(student5)
# student4["AGE"] = 18
# print(student1)
# print(student4)
# print(student5)

# print("\n\n\nUsing Deep copy")
# import copy
# std1 = copy.deepcopy(student1)
# print(student1)
# print(std1)
# student1["AGE"] = 25
# print(student1)
# print(std1)
# std1["AGE"] = 17
# print(student1)
# print(std1)
# # a = 10
# b = a
# print(a)
# print(b)
# a = 15
# print(a)
# print(b)

# print(len(student1))
# print(student4 == student1)

# student4.update(
#     {
#         "Marks" : {
#             "Maths" : 100,
#             "Physics" : 99,
#             "Chemistry" : 99
#         }
#     }
# )

# print(student4, "\n\n")
# for key, val in student4.items():
#     if key == "Marks":
#         for k , v in val.items():
#             print(f"{k} = {v}")
#     else:
#         print(f"{key} =  {val}")

# print(student4["Marks"]["Maths"])

# squares = {
#     x : x * x for x in range(1, 6, 1)
# }
# print(squares)


# student1["Memory"] = "Low"
# print(student1, "\n\n")
# student1.popitem()
# print(student1, "\n\n")
# a = student1.pop("Active")
# print(a, "\n\n")
# a1 = student1.keys()
# print(a1)

# student1.update({
#     "City" : "Thirupathi"
# })

# print(student1, "\n\n")
# b1 = student1

# print(b1)

# for key in student1:
#     print(key)

# for val in student1.values():
#     print(val)

# print("Keys          values")
# for key, val in student1.items():
#     print(f"{key:<7}-->   {val}")

# for key, val in student1.items():
#     print(val, key)

# print("A.Harshavardhan sai" in student1.values())

# student2 = dict(
#     name = "Harshavardhan sai",
#     surname = "Angalagunta",
#     age = 17,
# )

# student3 = dict([
#     ("name", "Harsha"),
#     ("age", 20),
#     ("name", "A.Harshavardhan sai")
# ])

# print(student1,"\n\n")
# student1["Name"] = 'Angalagunta Harshavardhan sai'
# print(student1,"\n\n")


# print(student2, "\n\n")
# student2["name"] = "Angalagunta Harshavardhan sai"
# print(student2, "\n\n")


# print(student3, "\n\n")
# student3["name"] = "Angalagunta harshavardhan sai"
# print(student3, "\n\n")

# print(student1["Name"], "\n\n")
# print(student1.get("Name"))
# del student1["Active"]
# print(student1.get("Active"))


# def CS(li):
#     dic = {}
#     print(li)
#     for n in li:
#         dic[n] = dic.get(n, 0) + 1
#     for k, v in dic.items():
#         print(f"{k} = {v}")
# li = [1,2,1,3,1,3,1,2,4,3,4,5,4,6,3,4,5,6,7,8]
# CS(li)

# std = {
#     "Name" : "Harshavardhan sai",
#     "Class" : "B-tech",
#     "Age" : 17,
#     "Department" : "Artificial Intelligence & Data Science"
# }

# ND = {}
# for k, v in std.items():
#     ND[v] = k
# print(ND)


# a = input("Enter the a number: ")
# b = input("Enter the b number: ")

# c = max(a, b)
# print("Largest number is ", c)

# a = int(input("Enter the a number: "))

# for i in range(1, 11):
#     print(a, " * ", i,"=", a * i)

# num = int(input("Enter the input: "))
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
# print(fact)

# name = input("Enter Your name: ")
# print("Your name is", name)
# name = name[::-1]
# print("Reversed name is ", name)

# str = input("Enter the String: ")
# vowels = "aeiouAEIOU"
# cnt = 0
# for i in str:
#     if i in vowels:
#         cnt += 1
# print("Number os vowels is ", cnt)

# str = input("Enter the String: ")

# words = str.split()
# words.reverse()
# print(" ".join(words))

# dic = {}
# for ch in str:
#     if ch != " ":
#         dic[ch] = dic.get(ch, 0) + 1
# for k, v in dic.items():
#     print(k, ": ", v)

# str = input("Enter the String: ")
# dic = {}
# for ch in str:
#     if ch in dic.keys():
#         dic[ch] += 1
#     else:
#         dic[ch] = 1
# for k, v in dic.items():
#     print(k, " ", v)


# str = input("Enter the String: ")
# words = str.split()
# for i in range(len(words) - 1, -1, -1):
#     print(words[i], end = " ")

# val = input("Enter the number: ").strip()
# print(val)
# cnt = 0

# for i in range(len(val)):
#     if val[i] == '1':
#         j = i + 1
#         while j < len(val) and val[j] == '0':
#             j += 1
#         if j > i + 1 and j < len(val) and val[j] == '1': 
#             cnt += 1
# print(cnt)

# str1 = input("Enter the String-1: ")
# str2 = input("Enter the String-2: ")
# result = str1.replace(str2, "")
# print(result)

# str = input("Enter the string: ")
# l = len(str)
# fact = 1
# for i in range(1, l + 1):
#     fact *= i
# print(fact)

# line = input("Enter the Line of string: ")
# line = line.lower()
# words = line.split()

# dict = {}
# for w in words:
#     w = w.strip(".,!?")
#     dict[w]=dict.get(w, 0) + 1
# for k, v in dict.items():
#     print(k, "=",v)

# l1 = [1,2,3]
# l2 = l1
# print(l1)
# print(l2)
# l2.append(4)
# print(l1)
# print(l2)
# print("\n\n\nUsing copy")
# l3 = l2.copy()
# l3.append(5)
# print(l1)
# print(l2)
# print(l3)

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for row in matrix:
#     for val in row:
#         print(val, end = " ")
#     print()

# matrix = [
#     [0 for i in range(3)]
#     for j in range(3)
# ]
# print(matrix)

# matrix = [1,2,3]
# print(matrix)
