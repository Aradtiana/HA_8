a = int(input("Введите число: "))
sum = 0
for i in range(1, a + 1):
    if i % 2 == 0:
        sum = sum + i
print("Сумма чётных чисел от 1 до", a, "равна", sum)