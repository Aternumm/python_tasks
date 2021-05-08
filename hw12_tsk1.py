def return_day(userNumber):
    if userNumber == 1:
        return "Понедельник"
    elif userNumber == 2:
        return "Вторник"
    elif userNumber == 3:
        return "Среда"
    elif userNumber == 4:
        return "Четверг"
    elif userNumber == 5:
        return "Пятница"
    elif userNumber == 6:
        return "Субота"
    elif userNumber == 7:
        return "Воскресенье"
userNumber = int (input ("Пожалуйста, введите число от 1 до 7"))
print(return_day(userNumber))
