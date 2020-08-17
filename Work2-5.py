my_list = [7, 5, 3, 3, 2]
i = int(input("Введите новый элемент рейтинга:  "))


if i == my_list[0]: my_list.insert(1, i)
if i <= my_list[-1]: my_list.append(i)
if i == my_list[3]: my_list.insert(4, i)
if i > my_list[0]: my_list.insert(0, i)
if i == 6: my_list.insert(1, i)
if i ==4: my_list.insert(2, i)

print(my_list)

