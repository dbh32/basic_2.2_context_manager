import time


class CM:
    # Context Manager
    s_time = str(0)
    f_time = str(0)

    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.f = open(self.file_path)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()


def main():
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

    def show_time():
        print(time.strftime('%X', time.localtime()))

    with CM('recipes.txt') as f:

        show_time()
        start = time.time()
        time.sleep(2)
        # Чтобы было более наглядно

        cook_book = {}
        for line in f:
            line = line.strip()
            cook_book[line] = create_dish()
        print(cook_book)

        show_time()
        finish = time.time()
        exec_time = finish - start

        print("Общее время выполнения: " + str(exec_time) + " seconds.")


if __name__ == '__main__':
    main()

# print(globals())
