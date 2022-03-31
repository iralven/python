#задача1
list=[1, 4, 5.0, 'hello']
print(list)
for n in list:
    print(type(n))

#задача2 - я решение не могу предложить. ввести список - да.
entered_list = input("Введите список чисел, разделенных пробелом: ").split()
print("Введенный список:", entered_list)

num_list = list(map(int, entered_list))
print("Список чисел: ", num_list)

#задача3
seasons = {

'Зима': ['12', '1', '2'],

'Лето': ['6', '7', '8'],

'Осень': ['9', '10', '11'],

'Весна': ['3', '4', '5']

}

month_user = input()
for month_user in seasons:
    if month_user == seasons[month]:
        print (month)

# решение через список. если честно, вообще неясно, как тут список применить. на мой взгляд - логичнее решать чере з условие если-то.
mounts=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n=int(input("введите номер месяца"))
for n in range (0,2)
    print('', n,'-зима')
for n in range (3,5)
    print('', n, '-весна')
for n in range(6, 8)
    print('', n, '-лето')
for n in range (9,11)
    print('', n,'-осень')

#задача4
entered_list = input("Введите несколько слов через пробел: ").split()
for n in entered_list:
    print(n)

#задача5
my_list = [2, 6, 8, 1, 10]
n = int(input('введите натуральное число'))
my_list.append(n)
my_list.sort(reverse=True)
print(my_list)