# age = int(input("ასაკი: "))

# parent = input("მშობელთან ერთად ხართ?: ")

# if  age >= 18 or (12 <= age <= 17 and parent == "კი"):

#     answer = ("შესვლა დაშვებულია")

# else:
#     answer = ("შესვლა დაუშვებელია")

# print(answer)


# სავარჯიშო #2

a = int(input("პირველი რიცხვი: "))
b = int(input("მეორე რიცხვი: "))
c = int(input("მესამე რიცხვი: "))

if  a >= b and a >= c:
    biggest = a

elif b >= a and b >= c:
    biggest = b

else:
    biggest = c

print("უდიდესი რიცხვია: ", biggest)