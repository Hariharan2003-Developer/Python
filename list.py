name = 'Hariharan'
list_name = list(name)
print(list_name)
j = 0
while j < len(name):
    letter = name[j]
    count = 1
    i = j+1
    if list_name[j] != '*':
        while i < len(name):
            if letter == list_name[i]:
                list_name[i] = '*'
                count+=1
            i+=1
        print(letter, count)
    j+=1
