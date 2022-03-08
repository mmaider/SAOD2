import random
import time


class HashMap:
    def __init__(self, arr, size_map):
        self.map = {}
        self.size = size_map
        for i in arr:
            self.insert_map(i)

    def hash_thing(self, thing):
        return thing % self.size

    def insert_map(self, thing):
        counter = 0
        flag = True
        while flag:
            tmp = self.hash_thing(thing + counter)
            if tmp not in self.map.keys() or self.map[tmp] is None:
                self.map[tmp] = thing
                flag = False
            counter += 1

    def search_map(self, thing):
        counter = 0
        for i in range(self.size):
            tmp = self.hash_thing(thing + counter)
            if tmp not in self.map.keys() or self.map[tmp] is None:
                print("Элемент не найден")
                return False
            elif self.map[tmp] == thing:
                print("Элемент найден. Хэш:", tmp)
                return tmp
            counter += 1
        print("Элемент не найден")
        return False

    def del_map(self, thing):
        tmp = self.search_map(thing)
        if tmp:
            self.map[tmp] = None
            print("Элемент удалён")


def gen_mas(size, borders):
    arr = []
    for i in range(size):
        arr.append(random.randint(borders[0], borders[1]))
    return arr


length = int(input("Введите размер массива"))
borders = [int(i) for i in input("Введите границы рандома через пробел").split()]
arr = gen_mas(length, borders)
start_time = time.time()
newmap = HashMap(arr, length)
end_time = time.time() - start_time
print("Время работы: ", end_time)
print(arr)
print(newmap.map)
while True:
    task = input("Введите действие (добавить - 1/найти - 2/удалить - 3/выход)")
    if task == "1":
        num = int(input("Введите число"))
        arr = list(newmap.map.values())
        for i in arr:
            if i is None:
                arr.remove(i)
        arr.append(num)
        newmap = HashMap(arr, len(arr))
    elif task == "2":
        num = int(input("Введите число"))
        start_time = time.time()
        newmap.search_map(num)
        end_time = time.time() - start_time
        print("Время работы: ", end_time)
    elif task == "3":
        num = int(input("Введите число"))
        newmap.del_map(num)
        arr = list(newmap.map.values())
        for i in arr:
            if i is None:
                arr.remove(i)
    else:
        break
    print(newmap.map)
