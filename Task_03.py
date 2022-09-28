# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных 
# координат точек в этой четверти (x и y).

def DefinRange (numQuarter):
    if (numQuarter < 1 or numQuarter > 4):
        print ("Введите корректные данные.")
    elif (numQuarter == 1 ):
        print ("1 ->  x > 0 and y > 0")
    elif (numQuarter == 2 ):
        print ("2 ->  x < 0 and y > 0")
    elif (numQuarter == 3 ):
        print ("3 ->  x < 0 and y < 0")
    elif (numQuarter == 4 ):
        print ("4 ->  x > 0 and y < 0")

numberofQuarter = int (input("Введите номер четверти координатной плоскости (от 1 до 4) и нажмите Enter: "))
DefinRange (numberofQuarter)