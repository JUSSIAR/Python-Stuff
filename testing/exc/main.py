from datetime import datetime
import sys as system
from time import time as clocks

lastOperation = datetime.now()
start = clocks()

def extraFinalDec(F):
    global start
    def beforeF():
        print("Unfortunately, program finished!")
        print("LastOperation: ", lastOperation)
        print("\nTime: ", clocks() - start)
        F()
    beforeF()

#@extraFinalDec
def extraFinal():
    system.exit(0)

class Developer:
    __total_count_developers = 0
    def __init__(self, name, age, skills, salary, message = str()):
        self._name = name
        self._age = age
        self._skills = skills
        self._salary = salary
        self._time = datetime.now()
        Developer.__total_count_developers += 1
        mySep = message
        if (len(message) > 0):
            mySep = ' '
        print(message, "Developer", sep = mySep, end = '\n\n')

    #name
    #@capacity.getter
    def getName(self):
        return self._name
    #@capacity.setter
    def setName(self, newName):
        if (self._name != newName):
            self._name = newName
            return True
        return False

    #age
    #@capacity.getter
    def getAge(self):
        return self._age    
    #@capacity.setter
    def setAge(self, newAge):
        if (self._age < newAge):
            self._age = newAge
            return True
        return False

    #time - only get
    #@capacity.getter
    def getTime(self):
        return str(self._time)

    #skills
    #@capacity.getter
    def getSkills(self):
        return self.skills.join(' ')
    #@capacity.setter
    def setSkills(self, newSkills):
        self.skills = newSkills
        return True

    #salary
    @property
    def salary(self):
        return self._salary
    #@capacity.getter
    def salary(self):
        return self._salary
    #@capacity.setter
    def salary(self, newSalary):
        if (newSalary < 0):
            return False
        self._salary = newSalary
        return True

    def __str__(self):
        return self._name + ' ' + self._skills.join(' ')

    def __del__(self):
        print("Goodbye", "Developer", self._name, sep = '\t', end = '\n\n')
    

class Frontend(Developer):
    def __init__(self, name, age, skills, salary):
        super().__init__(name, age, skills, salary, "Frontend ")

class Backend(Developer):
    def __init__(self, name, age, skills, salary):
        super().__init__(name, age, skills, salary, "Backend ")

class FullStack(Developer):
    def __init__(self, name, age, skills, salary):
        super().__init__(name, age, skills, salary, "FullStack ")

class Corporation:
    __corp_count = 0
    def __init__(self, name = "noname", front = 0, back = 0, full = 0):
        self.workers = set()
        self.__name = name
        self.front_salary = front
        self.back_salary = back
        self.full_salary = full
        Corporation.__corp_count += 1
        print("Corporation " + name, end = '\n\n')

    def newWorker(name, age, skills, prof):
        pass

    def printMedSalary(self):
        summ = sum([0])
        try:
            summ /= len(self.workers)
        except ZeroDivisionError as DBZ:
            print("No workers to analyze")
            print(DBZ, '\n')
        except Exception as DBZ:
            extraFinalDec(extraFinal)
        else:
            print("Result: " + str(summ))
        finally:
            print('OK\n')        
            

    @staticmethod
    def CountCorps():
        return Corporation.__corp_count

    def __del__(self):
        print("Goodbye", "Corporation", self.__name, sep = '\t', end = '\n\n')

def MergeCorporations(first, second):
    if (first == None):
        return second
    if (second == None):
        return first    

def testingRun():
    global lastOperation
    print(lastOperation)
    print('--------------------------\n')
    dev = Developer("Aa", 1, ['x1', 'y1'], 1, "True ")
    front = Frontend("Bb", 2, ['x2', 'y2'], 2)
    back = Backend("Cc", 3, ['x3', 'y3'], 3)
    full = FullStack("Dd", 4, ['x4', 'y4'], 4)
    corp = Corporation("CorpEe", 15, 16)

    print(Corporation.CountCorps(), '\n')
    corp.printMedSalary()

if __name__ == "__main__":
    #running this module
    testingRun()
    extraFinalDec(extraFinal)
