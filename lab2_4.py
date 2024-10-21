from array import array


def secure_inp(parametr):
    inp_num = ""
    while not (inp_num.isdigit()):
        try:
            inp_num = input(f"Введите натуральное число {parametr} для вычисления количества сочетаний: ")
        except ValueError:
            continue
    return int(inp_num)


n = secure_inp("n")
k = secure_inp("k")

fact = array('i', [1])

for i in range(1, n + 1):
    fact.append(fact[-1] * i)

print(f"Число сочетаний из n по k равно {fact[n] / fact[k] / fact[n - k]}.")
