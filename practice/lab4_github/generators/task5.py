def down_def(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for i in down_def(n):
    print(i)