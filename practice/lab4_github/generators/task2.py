def even_numbers_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input())

even_nums = even_numbers_generator(n)

for num in even_nums:
    print(num, end=" ")

print()
