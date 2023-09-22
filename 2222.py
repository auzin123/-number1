age = int(input("Скольько тебе лет? "))

if age % 10 == 0:
      print(age, "лет")
elif age % 10 == 1 and age != 11:
    print(age, "год")
elif age % 10 > 4:
    print(age, "лет")
elif age > 10 < 4:
    print(age, "лет") 
else:
    print("года")
