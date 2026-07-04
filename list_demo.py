#grocery_list = ['soap', 12, True, 'rice', 'veggies',4.5]
#
#print(grocery_list)
#
#for grocery_item in grocery_list:
#    if type(grocery_item) == str:
#        print(grocery_item)



l1 = ['Sai', 'Abhishek', 'Sanju', 'Shreyas']
l2 = [65, 85, 105, 56]

player_score_list = [l1, l2]

#print(player_score_list)
#
#for inner_list in player_score_list:
#    print(inner_list)

for inner_list in player_score_list:
    for list_item in inner_list:
        print(list_item, end=' ')
    print()


q = [90,87,65,67,89]
h = [96,97,95,69,99]
a = [99,98,100,76,49]

marks = [q,h,a]

for exam_list in marks:
    total = 0
    for mark in exam_list:
        total = total + mark
    print(total)


q = [90,87,65,67,89]
h = [96,97,95,69,99]
a = [99,98,100,76,49]

marks = [q,h,a]

#q --> marks[0]
#h --> marks[1]
#a --> marks[2]

print((marks[0][0] + marks[1][0] + marks[2][0])//3)


for exam_list in marks:
    total = 0
    for mark in exam_list:
        total = total + mark
    print(total, total // len(exam_list))


q = [90,87,65,67,89]
h = [96,97,95,69,99]
a = [99,98,100,76,49]

marks = [q,h,a]

#q --> marks[0]
#h --> marks[1]
#a --> marks[2]

print((marks[0][0] + marks[1][0] + marks[2][0])//3)

highest_total = 0
for exam_list in marks:
    total = 0
    for mark in exam_list:
        total = total + mark
    print(total, total // len(exam_list))
    if total > highest_total:
        highest_total = total

print('Highest Total is', highest_total)


l = [10,20,10,10,20,30]
count = 0
key = 10
for number in l:
    if key == number:
        count+=1
print(count)
