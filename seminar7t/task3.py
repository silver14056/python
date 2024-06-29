

def same_by(characteristic, object1):
    flag = True
    list_1 = [characteristic(x) for x in object1]
    for i in range(len(list_1)-1):
        if list_1[i] != list_1[i+1]:
            flag = False
    return flag


values = [1, 3, 13, 3]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
