# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def dayofWeek (num):
    if (num >= 1 and num <= 5): 
        print (num, "-> нет")
    elif (num >= 6 and num <= 7):
        print (num, "-> да")
    else:
        print ("Введите корректное число.")     

number = int (input("Введите номер дня недели и нажмите Enter: "))
dayofWeek (number)

