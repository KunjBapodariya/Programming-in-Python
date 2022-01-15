#20CS006 Kunj Bapodariya
#creating a tuple
kunj = (7, 1, 0, 55, 33, 17)
print(kunj)
#using merge of tuples with the + operator you can add an element and it will create a new tuple, because tuples are immutable
kunj =kunj + (94,)
print(kunj)
#adding items in a specific index
kunj= kunj[:5] + (25, 2, 56) + kunj[:5]
print(kunj)
#converting the tuple to list
listx = list(kunj)
#use different ways to add items in list
listx.append(30)
kunj = tuple(listx)
print(kunj)