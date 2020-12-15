class Stack_with_min_element:
    def __init__(self):
        self.stack = []
        self.minim = []
        self.SIZE = 0
    def Empty(self):
        return (self.SIZE == 0)
    def Insert_element(self, x):
        self.stack.append(x)
        self.minim.append(x)
        if (self.SIZE > 0):
            self.minim[-1] = min(self.minim[-1], self.minim[-2])
        self.SIZE += 1
    def Erase_element(self):
        self.stack.pop()
        self.minim.pop()
        self.SIZE -= 1
    def Get_minimum(self):
        return self.minim[-1]

class Queue_with_min_element:
    def __init__(self):
        self.stack1 = Stack_with_min_element()
        self.stack2 = Stack_with_min_element()
    def Empty(self):
        return self.stack1.Empty() and self.stack2.Empty()
    def Insert_element(self, x):
        self.stack1.Insert_element(x)
    def Erase_element(self):
        if (not(self.stack2.Empty())):
            self.stack2.Erase_element()
        else:
            if (self.stack1.Empty()):
                return
            while (not(self.stack1.Empty())):
                elem = self.stack1.stack[-1]
                self.stack2.Insert_element(elem)
                self.stack1.Erase_element()
            self.stack2.Erase_element()
    def Get_minimum(self):
        if (self.stack1.Empty()):
            return self.stack2.Get_minimum()
        if (self.stack2.Empty()):
            return self.stack1.Get_minimum()
        return min(self.stack1.Get_minimum(), self.stack2.Get_minimum())
    
def solution():
    n = int(input())
    STRUCTURE = Queue_with_min_element()
    for i in range(n):
        query = [str(j) for j in input().split()]
        if (query[0] == "Insert"):
            STRUCTURE.Insert_element(int(query[1]))
        if (query[0] == "Erase"):
            if (not(STRUCTURE.Empty())):
                STRUCTURE.Erase_element()
        if (query[0] == "Get"):
            if (not(STRUCTURE.Empty())):
                print(STRUCTURE.Get_minimum())
            else:
                print("Error")
                
if __name__ == "__main__":
    solution()
    
