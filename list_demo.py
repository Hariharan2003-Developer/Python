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
