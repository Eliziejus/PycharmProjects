a = [5, 10, 15, 20, 25]

nList = []


def newList():
    for x in a:
        if x == a[0]:
            nList.append(a[0])

            if x == a[-1]:
                nList.append(a[-1])

    return nList

print(nList)


