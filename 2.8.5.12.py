# определяем выигрыш проигрыш или ничья

print("Введите кол-во очков за игру:")

x = int(input())

if x < 0 or x > 3 or x ==2:
    print("Такое кол-во очков нельзя получить за игру.")
else:
    if x == 3:
        print("Выигрыш.")
    elif x == 1:
        print("Ничья.")
    elif x == 0:
        print("Проигрыш.")
        