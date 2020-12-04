def dels(list1,list2):
    if len(list1)>len(list2):
        for i in range(len(list2)):
            del list1[0]
        return list1
    elif len(list1)<len(list2):
        newList = [list2[0]]
        list2.remove(list2[0])
        for i in range(len(list1)):
            newList.append(list1[i])
        for i in range(len(list2)):
            newList.append(list2[i])
        return newList
    else:
        emptyList = list()
        return emptyList



list1 = [2,5]
list2 = [3,4,7,8,9]

print(dels(list1,list2))
