# #John is planning a hiking trip across a beautiful national park. To plan his journey better, he wants to convert the distances of various trails from meters to kilometers.
# n = int(input("Enter the Meters: "))
# print(f"{(n / 1000):.2f}")
# print("{:.2f}".format(n / 1000))


# n = int(input())

# b = bin(n)[2:]
# b = str(b)

# o = 0

# for i in b:
#     if (i == "1") :
#         o = o + 1
# print(o)


n = int(input())
p = int(input())

b = str(bin(n)[2:])
print(b)

if p > 0 :
    if b[-p] == "1":
        print("SET")
    else:
        print("NOT SET")