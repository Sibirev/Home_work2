my_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: 'June', 7: "July", 8: "August",
           9: "September", 10: "October", 11: "November", 12: "December"}
i = int(input("Enter the number of a month: "))

print("Month according to your number is:  ", my_dict.get(i))

my_list = ["Пустышка", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
           "Ноябрь", "Декабрь"]
c = int(input("Введите номер месяца:  "))

print("Ваш номер соответствует месяцу: ", my_list[c])
