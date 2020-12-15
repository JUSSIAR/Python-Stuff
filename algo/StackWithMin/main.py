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

def solution():
    n = int(input())
    STRUCTURE = Stack_with_min_element()
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
    
