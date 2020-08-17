my_str = input("Введите несколько слов через пробел: ").split(" ")
numb = 0

for i in my_str:
    numb = numb + 1
    print(numb, i[0:10])
