if __name__ == "__main__":
	print("модуль derevo_otrezkov запущен")
	
'''
построение дерева максимумов
групповой запрос максимума на отрезке
запрос на изменение ячейки
'''
import random
INF = int(10**9)

class node:
    def __init__(self, left_child = None, right_child = None):
        self.left = int(0)
        self.right = int(0)
        self.max = int(0)
        self.left_child = left_child
        self.right_child = right_child

def build (left, right, val):
    root = node()
    root.left = left
    root.right = right
    if left == right:
        root.left_child = None
        root.right_child = None
        root.max = val[left]
    else:
        middle = (left + right) // 2
        root.left_child = build(left, middle, val)
        root.right_child = build(middle + 1, right, val)
        answer1 = root.left_child.max
        answer2 = root.right_child.max
        root.max = max(answer1, answer2)
    return root

def query (root, left, right):
    global INF
    if (root.left > right) or (root.right < left):
        return (-1) * INF
    if (root.left >= left) and (root.right <= right):
        return root.max
    answer1 = query(root.left_child, left, right)
    answer2 = query(root.right_child, left, right)
    return max(answer1, answer2)

def update (root, index, val):
    if (root.left > index) or (root.right < index):
        return
    if (root.right == index) and (root.left == index):
        root.max = val
        return
    update(root.left_child, index, val)
    update(root.right_child, index, val)
    answer1 = root.left_child.max
    answer2 = root.right_child.max
    root.max = max(answer1, answer2)
    
