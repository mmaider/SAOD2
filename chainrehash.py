import random
import time


class ChainHashMap:
    def __init__(self, arr, size_map):
        self.map = {}
        self.size = size_map
        for i in arr:
            self.insert_map(i)

    def hash_thing(self, thing):
        return thing % self.size

    def insert_map(self, thing):
        counter = 0
        linkplace = None
        flag = True
        while flag:
            tmp = self.hash_thing(thing + counter)
            if tmp not in self.map.keys() or self.map[tmp][0] is None:
                self.map[tmp] = [thing, None]
                flag = False
                if linkplace is not None:
                    self.map[linkplace][1] = tmp
            elif self.map[tmp][1] is None and linkplace is None:
                linkplace = tmp
            counter += 1

    def search_map(self, thing):
        counter = thing
        for i in range(self.size):
            tmp = self.hash_thing(counter)
            if tmp not in self.map.keys() or self.map[tmp][0] is None:
                print("Элемент не найден")
                return False
            elif self.map[tmp][0] == thing:
                print("Элемент найден. Хэш:", tmp)
                return tmp
            elif self.map[tmp][1] is not None:
                counter = self.map[tmp][1]
            else:
                counter += 1
        print("Элемент не найден")
        return False

    def del_map(self, thing):
        tmp = self.search_map(thing)
        if tmp:
            self.map[tmp][0] = None
            print("Элемент удалён")
        else:
            print("Элемент не найден")


def gen_mas(size, borders):
    arr = []
    for i in range(size):
        arr.append(random.randint(borders[0], borders[1]))
    return arr


length = int(input("Введите размер массива"))
borders = [int(i) for i in input("Введите границы рандома через пробел").split()]
arr = gen_mas(length, borders)
start_time = time.time()
newmap = ChainHashMap(arr, length)
end_time = time.time() - start_time
print("Время работы: ", end_time)
print(arr)
print(newmap.map)
while True:
    task = input("Введите действие (добавить - 1/найти - 2/удалить - 3/выход)")
    if task == "1":
        num = int(input("Введите число"))
        arr = [i[0] for i in list(newmap.map.values())]
        arr.append(num)
        newmap = ChainHashMap(arr, len(arr))
    elif task == "2":
        num = int(input("Введите число"))
        start_time = time.time()
        newmap.search_map(num)
        end_time = time.time() - start_time
        print("Время работы: ", end_time)
    elif task == "3":
        num = int(input("Введите число"))
        newmap.del_map(num)
        arr = [i[0] for i in list(newmap.map.values())]
    else:
        break
    print(newmap.map)
