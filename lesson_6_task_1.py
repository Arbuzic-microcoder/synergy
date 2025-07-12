#Сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте, сколько из них равны нулю, и выведите это количество.
n = int(input())
cnt = 0
for i in range (n):
    number = int(input())
    if number == 0:
        cnt += 1
print(cnt)