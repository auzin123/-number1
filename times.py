lesson_num = int(input("Введите номер урока: "))
total_minutes = 45 + ((lesson_num - 1) * 55)

correction = 8.5 * 60
total_minutes = total_minutes + correction
hours = int(total_minutes // 60)
minutes = int(total_minutes % 60)
hours %= 24
if minutes >= 10:
    print(hours, ":", minutes, sep="")
else:
    print(hours, ":", "0", minutes, sep="")
