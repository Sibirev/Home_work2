user_list = input("Enter any values in a row  :")
my_list = list(user_list)
print("Your List looks like:  ", my_list)

for i in range(1, len(my_list), 2):
    my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
    print(my_list)
