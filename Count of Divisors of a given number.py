no = 12
i = 1
count = 0

while i <= no:
    if no % i == 0:
        print(i)
        count += 1
    i += 1

print("Count =", count)
