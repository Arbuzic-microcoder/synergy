# Объявляем переменные
word = input()
vowels = ['a','e','i','o','u']
vowels_in_word = []
quantity_consonants  = 0
quantity_vowels = 0
quantity_a = 0
quantity_e = 0
quantity_i = 0
quantity_o = 0
quantity_u = 0

for i in word:
    print (i) # Проверяем каждую гласную в слове
    if i in vowels: # Если i из гласных, определяем её в список гласных
        vowels_in_word+= i
    else:            #если буква не гласная, то она согласная
        quantity_consonants += 1 

quantity_vowels = len(vowels_in_word) # кол-во гласных всего
# вывод
print('Всего:', quantity_consonants, 'согласных')
print('Всего:', quantity_vowels, 'гласных.')

if vowels_in_word.count('a') != 0: 
    print ('В этом слове ровно', vowels_in_word.count('a'), 'буквa a!')
else:
    print ('a = False')


if vowels_in_word.count('e') != 0:
    print ('В этом слове ровно', vowels_in_word.count('e'), 'буквa e!')
else:
    print ('e = False')

if vowels_in_word.count('i') != 0:
    print ('В этом слове ровно', vowels_in_word.count('i'), 'буквa i!')
else:
    print ('i = False')

if vowels_in_word.count('o') != 0:
    print ('В этом слове ровно', vowels_in_word.count('o'), 'буквa o!')
else:
    print ('o = False')

if vowels_in_word.count('u') != 0:
    print ('В этом слове ровно', vowels_in_word.count('u'), 'буквa u!')
else:
    print ('u = False')

