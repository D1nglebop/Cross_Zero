
def output (N, M, matrix):
    for i in range(N):
        for j in range(M):
            print(matrix[i][j], end=" ")
        print()


def inp_row():

    row = None

    while row not in [0, 1, 2]:
        row = int(empty_chek(input('Введите номер строки от 1 до 3 '))) - 1
        if row not in [0, 1, 2]:
            print('Вы ввели значение, не входящее в требуемый интервал')

    return row


def inp_col():

    col = None

    while col not in [0, 1, 2]:
        col = int(empty_chek(input('Введите номер столбца от 1 до 3 '))) - 1
        if col not in [0, 1, 2]:
            print('Вы ввели значение, не входящее в требуемый интервал')

    return col


def empty_chek(i):
    if i.isnumeric():
        return i
    else:
        return -1


def stringer(matrix):
    string = []
    for i in range(3):
        for j in range(3):
            string.append(matrix[i][j])
    return string


area = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


print('Поиграем?')
print('Поле 3х3. Каждая строка и столбец имеют номер от 1 до 3')
print('Чтобы поставить символ, вводите номера строк и столбцов, соответствующие желаемому полю')
print('Начинаем с крестика')

step = 1
while True:
    if area[0][0] == area[0][1] == area[0][2] and area[0][0] != '-':
        if area[0][0] == 'X':
            print('Игра завершена. Победили крестики')
            break
        else:
            print('Игра завершена. Победили нолики')
            break

    elif area[1][0] == area[1][1] == area[1][2] and area[1][0] != '-':
        if area[1][0] == 'X':
            print('Игра завершена. Победили крестики')
            break
        else:
            print('Игра завершена. Победили нолики')
            break

    elif area[2][0] == area[2][1] == area[2][2] and area[2][0] != '-':
        if area[2][0] == 'X':
            print('Игра завершена. Победили крестики')
            break
        else:
            print('Игра завершена. Победили нолики')
            break

    elif area[0][0] == area[1][0] == area[2][0] and area[0][0] != '-':
        if area[0][0] == 'X':
            print('Игра завершена. Победили крестики')
            break
        else:
            print('Игра завершена. Победили нолики')
            break

    elif area[0][1] == area[1][1] == area[2][1] and area[0][1] != '-':
        if area[0][1] == 'X':
            print('Игра завершена. Победили крестики')
            break
        else:
            print('Игра завершена. Победили нолики')
            break

    elif area[0][2] == area[1][2] == area[2][2] and area[0][2] != '-':
        if area[0][2] == 'X':
            print('Игра завершена. Победили крестики')
            break
        else:
            print('Игра завершена. Победили нолики')
            break

    elif area[0][0] == area[1][1] == area[2][2] and area[1][1] != '-':
        if area[1][1] == 'X':
            print('Игра завершена. Победили крестики')
            break
        else:
            print('Игра завершена. Победили нолики')
            break

    elif area[0][2] == area[1][1] == area[2][0] and area[1][1] != '-':
        if area[1][1] == 'X':
            print('Игра завершена. Победили крестики')
            break
        else:
            print('Игра завершена. Победили нолики')
            break

    elif '-' not in stringer(area):
        print('Победил панк-рок. А у вас ничья')
        break


    else:
        if step % 2 == 1:
            print('Ставим крестик')
            while True:
                r = int(inp_row())
                c = int(inp_col())
                if area[r][c] == '-':
                    area[r][c] = 'X'
                    break
                print('Поле занято. Повторите ввод')
                print('Ставим крестик')
            output(3, 3, area)
            step +=1

        elif step % 2 == 0:
            print('Ставим нолик')
            while True:
                r = int(inp_row())
                c = int(inp_col())
                if area[r][c] == '-':
                    area[r][c] = 'О'
                    break
                print('Поле занято. Повторите ввод')
                print('Ставим нолик')
            output(3, 3, area)
            step += 1
