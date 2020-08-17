my_tuple1 = (("Наименование:  "), input("Введите название товара: "),
             ("Цена товара в рублях:  "), input(
    "Введите цену товара: "), ("  рублей"),
             ("количество  "), input("Введите кол-во: "),
             input("Введите единицу измерения: "))

my_tuple2 = (("Наименование:  "), input("Введите название товара: "),
             ("Цена товара в рублях:  "), input(
    "Введите цену товара: "), ("  рублей"),
             ("количество  "), input("Введите кол-во: "),
             input("Введите единицу измерения: "))

my_tuple3 = (("Наименование:  "), input("Введите название товара: "),
             ("Цена товара в рублях:  "), input(
    "Введите цену товара: "), ("  рублей"),
             ("количество  "), input("Введите кол-во: "),
             input("Введите единицу измерения: "))
a = 0

big_list = [my_tuple1, my_tuple2, my_tuple3]
for i in big_list:
    a = a + 1
    print(a, i)

answ_list = ["Да", "да", "Нет", "нет"]

my_dict1 = {my_tuple1[0]: (my_tuple1[1], my_tuple2[1], my_tuple3[1])}
my_dict2 = {my_tuple1[2]: (my_tuple1[3], my_tuple2[3], my_tuple3[3])}
my_dict3 = {my_tuple1[5]: (my_tuple1[6], my_tuple2[6], my_tuple3[6])}
my_dict4 = {"Единица измерения": my_tuple1[7]}

ever_list = [my_dict1, my_dict2, my_dict3, my_dict4]

c = (input("Желаете посмотреть аналитику по товарам? Введите Да или Нет:  "))

if c == answ_list[0]:
    for i in ever_list:
     print(i)
elif c == answ_list[1]:
    for i in ever_list:
     print(i)
elif c == answ_list[2]:
     print("Как пожелаете!")

elif c == answ_list[3]:
    print("Как пожелаете!")

else: print("Тут должна быть крутая функция, чтобы опять вызвать вопрос в случае невнятного ответа, но я пока не знаю как это хорошо сделать)")
