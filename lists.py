# ip_address = '192.168.0.3'
# ip_address_parts = ip_address.split('.')
# valid = 'ДА'
# for part in ip_address_parts:
#     if int(part) not in range(1, 256):
#         valid = 'НЕТ'
#         break
# print(valid)

# a = [1, 5, 6, 7, 9]
# n = len(a)
#
#
# for i in range(n - 1):
#     flag = False
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:                  # если порядок элементов пары неправильный
#             a[j], a[j + 1] = a[j + 1], a[j]  # меняем элементы пары местами
#             flag = True
#     if flag is False:
#         break

# print('Отсортированный список:', a)

a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
n = len(a)

for i in range(n - 1):
    minimum = a[i]
    min_ind = i
    for j in range(i + 1, n):
        if a[j] < minimum:
            minimum = a[j]
            min_ind = j
    a[i], a[min_ind] = minimum, a[i]

print('Отсортированный список:', a)