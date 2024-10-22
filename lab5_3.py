from random import randint


def model_steps(n, whoes_step_now):
    if n <= 1: return whoes_step_now % 2 == 0
    h = [model_steps(n - 1, not whoes_step_now), model_steps(n - 2, not whoes_step_now),
         model_steps(n - 3, not whoes_step_now)]
    return any(h) if (not whoes_step_now) % 2 == 0 else all(h)


def artifical_intelligence(n):
    if not (model_steps(n - 1, 1)): return 1
    if not (model_steps(n - 2, 1)): return 2
    return 3


def game(n):
    user_take = ""
    while not (user_take.isdigit()):
        try:
            user_take = input(f'В куче {n} камней. Сколько камней возьмёте из кучи?\n')
            user_take = int(user_take)
            if user_take < 1 or user_take > min(3, n):
                print(f'Столько камней взять нельзя! Попробуйте снова=)')
                user_take = ""
                continue
            break
        except ValueError:
            print(f'Вы ввели не число! Попробуйте снова=)')
            continue
    n -= user_take
    print(f'В куче {n} камней.')
    if n == 1:
        print(f'Поздравляю с победой! Быть может в следующий раз мне повезёт больше=)')
        return;
    if n == 0:
        print(f'Вы проиграли.. Но не расстраивайтесь, может в следующий раз повезёт вам=)')
        return;
    ai_take = artifical_intelligence(n)
    n -= ai_take
    print(f'Я решил взять {ai_take} камней из кучи.')
    game(n)


n = randint(4, 30)

print(
    f'Добро пожаловоть в игру "Камешки". В данной игре {n} - начальное количество камней в куче. Можно за ход взять 1, 2 либо 3 камня.')
print(f'Выигрывает тот, кто не сможет взять последний камень. Удачи!\n')

game(n)
