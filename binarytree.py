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


arr = [5, 12, 6, 14, 3]
root = make_a_tree(arr)
num = int(input("Введите число"))
result = root.findval(num)
if result:
    task = input("Хотите удалить этот элемент? y/n")
    if task == "y":
        arr.remove(num)
        root = make_a_tree(arr)
else:
    task = input("Хотите добавить этот элемент? y/n")
    root.insert(num)
root.PrintTree()
