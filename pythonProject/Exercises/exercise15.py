def myName():
    enter=input("Enter long strings:  ")
    splitResults = enter.split()
    res=[]
    x = len(splitResults)-1
    while x >=0:
        res.append(splitResults[x])
        x=x-1
    result =" ".join(res)
    return result
print(myName())

