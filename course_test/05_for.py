# coding=utf-8

for num in range(10, 20):       # to iterate between 10 to 19 exclude 20
    for i in range(2, num):     # to iterate on the factors of the number
        if num % i == 0:        # to determine the first factor
            j = num / i         # to calculate the second factor
            print('%d equals %d * %d' % (num, i, j))
            break               # 跳出本层循环
    else:  # else part of the loop
        print(num, 'is a prime number')

n = 0
length = len(range(10))
for i in range(10):
    print(i)
    n += 1
    if n == length:
        print('last item:', i)
        print('n:', n)
