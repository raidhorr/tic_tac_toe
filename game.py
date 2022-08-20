def game():
    desc = init_desc()
    player = 'X'
    while True:
        show_desc(desc)
        if player == 'X':
            move = move_x(desc)
        else:
            move = move_0(desc)
        if control_move(move, desc):
            step(move, desc)
            player = '0' if player == 'X' else 'X'
        else:
            print(f'{player} ходит не верно')
        if res := end_game(desc):
            show_desc(desc)
            print(res)
            break


def init_desc():
    res = []
    for i in range(3):
        res.append([None]*3)
    return res


def show_desc(desc):
    print('  0 1 2')
    for i in range(3):
        print(i, ' '.join([j if j else '_' for j in desc[i]]))


def move_x(desc):
    xy = input('Ходит X. Введите две цифры координат (пример: 00):')
    return 'X', xy


def move_0(desc):
    xy = input('Ходит 0. Введите две цифры координат (пример: 00):')
    return '0', xy


def control_move(move, desc):
    if len(move[1]) == 2 and 0 <= int(move[1][0]) < 3 and 0 <= int(move[1][1]) < 3:
        return desc[int(move[1][0])][int(move[1][1])] is None
    else:
        False


def step(move, desc):
    desc[int(move[1][0])][int(move[1][1])] = move[0]


def end_game(desc):
    res = False
    res = res or desc[0][0] == desc[1][1] == desc[2][2] and desc[0][0]
    res = res or desc[0][2] == desc[1][1] == desc[2][0] and desc[0][2]
    res = res or desc[0][0] == desc[0][1] == desc[0][2] and desc[0][0]
    res = res or desc[1][0] == desc[1][1] == desc[1][2] and desc[1][0]
    res = res or desc[2][0] == desc[2][1] == desc[2][2] and desc[2][0]
    res = res or desc[0][0] == desc[1][0] == desc[2][0] and desc[0][0]
    res = res or desc[0][1] == desc[1][1] == desc[2][1] and desc[0][1]
    res = res or desc[0][2] == desc[1][2] == desc[2][2] and desc[0][2]
    if res:
        return f'{res} выиграл'
    elif all(map(all, desc)):
        return 'Ничья'
    else:
        return False

game()
