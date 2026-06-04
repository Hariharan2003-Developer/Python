no = 13
i = 1
count = 0

while i <= no:
    if no % i == 0:
        count += 1
    i += 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")
