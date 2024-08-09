def func_12_month():
    for i in range(1, 14):
        for j in range(1, 13):
            for k in range(1, 12):
                if 28 * i + 30 * j + 31 * k == 365:
                    print(i, j, k)


def func_count_animals():
    for b in range(1, 10):
        for k in range(1, 20):
            for t in range(1, 200):
                if (b*10 + k*5 + t*0.5 == 100) and (b + k + t == 100):
                    print(b, k, t)


def func_eyler():
    for a in range(1, 150):
        for b in range(a, 150):
            for c in range(b, 150):
                for d in range(c, 150):
                    e = (a**5 + b**5 + c**5 + d**5) ** 0.2
                    if int(e) == round(e, 10):
                        print(a+b+c+d+e)


def ramanujan_number():
    z_min = 1729

    count = 0
    z_c = z_min
    x_c = 0
    y_c = 0

    while count < 4:
        z_min += 1
        for x in range(1, int((z_min - 1) ** (1 / 3)) + 1):
            for y in range(x, int((z_min - 1) ** (1 / 3)) + 1):
                if x ** 3 + y ** 3 == z_min:
                    if z_min == z_c and x_c + y_c != x + y:
                        count += 1
                        print("Point XXX", x, y, z_min)
                    else:
                        z_c, x_c, y_c = z_min, x, y


