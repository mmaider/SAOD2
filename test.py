import copy
import random
import time

# бинарный поиск
def BinarySearch(list, item):
    list.sort()
    low = 0
    high = len(list) - 1
    i = 0
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        i = i + 1
    return -1


# Фибоначчиев поиск
def FibonacciSearch(lys, val):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(lys)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(lys) - 1))
        if (lys[i] < val):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (lys[i] > val):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else:
            return i
    if (fibM_minus_1 and index < (len(lys) - 1) and lys[index + 1] == val):
        return index + 1
    return -1


# Интерполяционный
def InterpolationSearch(lys, val):
    low = 0
    high = (len(lys) - 1)
    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low + int(((float(high - low) / (lys[high] - lys[low])) * (val - lys[low])))
        if lys[index] == val:
            return index
        if lys[index] < val:
            low = index + 1
        else:
            high = index - 1
    return -1


# Бинарное дерево

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                print(lkpval, "не найден.")
                return False
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                print(lkpval, "не найден.")
                return False
            return self.right.findval(lkpval)
        else:
            print(self.data, ' найден.')
            return True

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


def make_a_tree(arr):
    root = Node(arr[0])
    for i in arr[1::]:
        root.insert(i)
    return root


def insert_mas(mas):
    print("Добавить новый элемент? ")
    ans = input()
    if ans.lower() == "да":
        el = int(input("Введите число: "))
        tmplys = copy.deepcopy(mas)
        tmplys.append(el)
        print(tmplys)


def del_mas(mas):
    print("Удалить элемент? ")
    ans = input()
    if ans.lower() == "да":
        ind = BinarySearch(mas, int(input("Введите элемент: ")))
        tmplys = []
        for i in range(len(mas)):
            if i != ind:
                tmplys.append(mas[i])
        print(tmplys)


def gen_mas(size, borders):
    arr = []
    for i in range(size):
        arr.append(random.randint(borders[0], borders[1]))
    return arr


length = int(input("Введите размер массива"))
borders = [int(i) for i in input("Введите границы рандома через пробел").split()]
mas = gen_mas(length, borders)

print("Исходный массив: ")
print(mas)

mas.sort()
print("Сортировка массива: ")
print(mas)

# бинарный поиск
print("Бинарный поиск")
print("Введите элемент, который хотите найти: ")
element = int(input())
start_time_bin = time.time()
b = BinarySearch(mas, element)
end_time_bin = time.time() - start_time_bin
print("Время работы: ", end_time_bin)
if b == -1:
    print("Элемент не найден")
else:
    print("Элемент найден. Индекс: ", b)
insert_mas(mas)
del_mas(mas)

# интерполяционный поиск
print("Интерполяционный поиск")
print("Введите элемент, который хотите найти: ")
element = int(input())
start_time_inter = time.time()
b = InterpolationSearch(mas, element)
end_time_inter = time.time() - start_time_inter
if b == -1:
    print("Элемент не найден")
else:
    print("Элемент найден. Индекс: ", b)
print("Время работы: ", end_time_inter)
insert_mas(mas)
del_mas(mas)

# Фибоначчиев поиск
print("Фибоначчиев поиск")
print("Введите элемент, который хотите найти: ")
element = int(input())
start_time_fib = time.time()
b = FibonacciSearch(mas, element)
end_time_fib = time.time() - start_time_fib
if b == -1:
    print("Элемент не найден")
else:
    print("Элемент найден. Индекс: ", b)
print("Время работы: ", end_time_fib)
insert_mas(mas)
del_mas(mas)

# Бинарное деререво
print("Бинарное деререво")
root = make_a_tree(mas)
num = int(input("Введите число для поиска"))
start_time_tree = time.time()
result = root.findval(num)
end_time_tree = time.time() - start_time_tree
print("Время работы: ", end_time_tree)
task = input("Добавить элемент? ")
if task == "да" or task == "Да":
    num = int(input("Введите элемент, который хотите внести: "))
    root.insert(num)
    root.PrintTree()
task = input("Удалить элемент? ")
if task == "да" or task == "Да":
    num = int(input("Введите элемент, который хотите удалить: "))
    mas.remove(num)
    root = make_a_tree(mas)
    root.PrintTree()
