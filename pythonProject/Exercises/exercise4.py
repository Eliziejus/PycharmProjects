number = int(input("Put number: "))

x = list(range(1,number+1))
# for element in x:
#      print(element)
list = []

for new_number in x:
    if number % new_number == 0:
        list.append(new_number)

print(list)
