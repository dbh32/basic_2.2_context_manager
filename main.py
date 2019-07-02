import time

def create_dish():
    '''Создание списков под каждое блюдо'''
    dish = []
    count = int(f.readline().strip())
    cycle = 0
    while cycle != count:
        cycle += 1
        dish.append(create_ingredients())
    f.readline().strip()
    return dish


def create_ingredients():
    '''Наполняем списки блюд ингридиентами'''
    l1 = f.readline().strip()
    l2 = l1.split(' | ', 3)
    # вспомогательные переменные
    ingredients = {'ingredient_name': l2[0],
                   'quantity': l2[1],
                   'measure': l2[2]}
    return ingredients


with open('recipes.txt', 'r', encoding='utf-8-sig') as f:
    print(time.strftime('%X', time.localtime()))
    start = time.time()
    cook_book = {}
    for line in f:
        line = line.strip()
        cook_book[line] = create_dish()
    print(cook_book)
    finish = time.time()
    exec_time = finish - start
    print(time.strftime('%X', time.localtime()))
    print("Общее время выполнения: " + str(exec_time) + " seconds.")
