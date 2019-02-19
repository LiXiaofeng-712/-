# t1 = (1,2,3,4)
# t2 = (1,2,4,3)
# print(t1 < t2)

# names1 = ['Amir', 'Barry', 'Chales', 'Dao']
# names2 = [name.lower() for name in names1]
#
# print(names2)

confusion = {}
confusion[1] = 1
confusion['1'] = 2
confusion[1.0] = 4

print(confusion)