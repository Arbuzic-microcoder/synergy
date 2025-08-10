def create():
    last = len(pets)
    pets[last] = {input('Введите имя питомца: \n'):{
                    'Вид питомца': input('Какой породы ваш питомец? \n'),
                    'Возраст питомца': int(input('Теперь мне нужен возраст, сколько ему лет? \n')),
                    'Имя владельца': input('Как вас зовут? \n')
        }
    }
def read(name):
    for i in pets:
        inner_dict = pets[i]
        if name in inner_dict:
            age = str(pets[i][name]['Возраст питомца'])
            if age[-1] == '1' and age [-2:] != '11':
               age += ' год'
            elif age[-1] in ['2', '3', '4'] and age [-2:] not in ['12', '13', '14']:
                age += ' года'
            else:
                age += ' лет'

            print(f'Это {pets[i].key()} по кличке "{next(iter(pets[1]))}". Возраст питомца: {age}. Имя владельца: {pets[i][name]['Имя владельца']}')
            break

def update(name):
     for i in pets:
        inner_dict = pets[i]
        if name in inner_dict:
            pets[i] = {
                input('Введите имя питомца: \n'):
                        {
                        'Вид питомца': input('Какой породы ваш питомец? \n'),
                        'Возраст питомца': int(input('Теперь мне нужен возраст, сколько ему лет? \n')),
                        'Имя владельца': input('Как вас зовут? \n')
                        }
                    }
            break
def delete():
    name = input('Какого питомца нужно удалить из базы данных? \n')
    for i in pets:
        inner_dict = pets[i]
        if name in inner_dict:
            del pets[i][name]
            break
pets = {}
command = input('create, read, update, delete \n')
while command != 'stop':
    if command == 'create':
        create()
    if command == 'read':
        read(input('Введите имя интересуешего питомца\n'))
    if command == 'update':
        update(input('Введите имя интересуешего питомца\n'))
    if command == 'delete':
        delete()
    command = input('create, read, update, delete\n')
