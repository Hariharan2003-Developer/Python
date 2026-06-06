no = 28

divisor = 1
sum = 0

while divisor < no:
    if no % divisor == 0:
        sum = sum + divisor
    divisor = divisor + 1

if sum == no:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
