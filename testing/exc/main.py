from datetime import datetime
import sys as system
from time import time as clocks
import random as rnd

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
    @property
    def name(self):
        return self._name
    #getName
    @name.getter
    def name(self):
        return self._name
    #setName
    @name.setter
    def name(self, newName):
        if (self._name != newName):
            self._name = newName
            return True
        return False

    #age
    @property
    def age(self):
        return self._age
    #getAge
    @age.getter
    def age(self):
        return self._age 
    #setAge
    @age.setter
    def age(self, newAge):
        if (self._age < newAge):
            self._age = newAge
            return True
        return False

    #time - only get
    @property
    def time(self):
        return self._time
    #getTime
    @time.getter
    def time(self):
        return str(self._time)

    #skills
    @property
    def skills(self):
        return self._skills
    #getSkills
    @skills.getter
    def skills(self):
        return self.skills.join(' ')
    #setSkills
    @skills.setter
    def skills(self, newSkills):
        self.skills = newSkills
        return True

    #salary
    @property
    def salary(self):
        return self._salary
    #getSalary
    @salary.getter
    def salary(self):
        return self._salary
    #setSalary
    @salary.setter
    def salary(self, newSalary = int(0)):
        if (newSalary < 0):
            return False
        self._salary = newSalary
        return True
    
    def work(self, function):
        try:
            result = function()
            raise Exception(result)
        except Exception as ex:
            print(ex, end = '\n\n')
        finally:
            pass
        
    def who(self):
        return "TrueCoder"
    
    @staticmethod
    def CountDevelopers():
        return Developer.__total_count_developers

    def __str__(self):
        return self._name + ' ' + (' ').join(self._skills)

    def __del__(self):
        print("Goodbye", "Developer", self._name, sep = '\t', end = '\n\n')
    

class Frontend(Developer):
    def __init__(self, name, age, skills, salary):
        super().__init__(name, age, skills, salary, "Frontend ")
        
    @classmethod
    def workFront():
        return "Frontend"
        
    def work(self, workTime = 6):
        while (workTime > 0):
            #working
            workTime -= 1
        super().work(Frontend.workFront)
        
    def who(self):
        return Frontend.workFront()

class Backend(Developer):
    def __init__(self, name, age, skills, salary):
        super().__init__(name, age, skills, salary, "Backend ")
        
    @classmethod
    def workBack():
        return "Backend"
    
    def work(self, workTime = 10):
        while (workTime > 0):
            #working
            workTime -= 1
        super().work(Backend.workBack)
    
    def who(self):
        return Backend.workBack()

class FullStack(Developer):
    def __init__(self, name, age, skills, salary):
        super().__init__(name, age, skills, salary, "FullStack ")
        
    @classmethod
    def workFull():
        return "FullStack"
    
    def work(self, workTime = 16):
        while (workTime > 0):
            #working
            workTime -= 1
        super().work(FullStack.workFull)
        
    def who(self):
        return FullStack.workFull()

class Corporation:
    __corp_count = 0
    
    def __init__(self, name = "noname", front = 0, back = 0, full = 0):
        self.workerNames = set()
        self.workers = set()
        self.__name = name
        self.front_salary = front
        self.back_salary = back
        self.full_salary = full
        Corporation.__corp_count += 1
        print("Corporation " + name, end = '\n\n')

    def addNewWorker(self, person, prof = "True"):
        if person.name in self.workerNames:
            return False
        newWorker = person
        if prof == "Frontend":
            print("Frontend", "employee")
        elif prof == "Backend":
            print("Frontend", "employee")
        elif prof == "FullStack":
            print("Frontend", "employee")
        else:
            goodMoney = rnd.randint(0, sum([self.front_salary, self.back_salary, self.full_salary]))
            newWorker.salary = goodMoney
        self.workerNames.add(person.name)
        self.workers.add(newWorker)
        print(newWorker)
        return True
                

    def printMedSalary(self):
        summ = 0
        for person in self.workers:
            summ += person.salary
        try:
            summ /= len(self.workers)
        except ZeroDivisionError as DBZ:
            print("No workers to analyze")
            print(DBZ, '\n')
        except Exception as ex:
            extraFinalDec(extraFinal)
        else:
            print("Result: " + str(summ))
        finally:
            print('OK\n')        
            
    def getWorkers(self):
        return self.workers
    
    def getSalary(self):
        return [self.front_salary, self.back_salary, self.full_salary]
    
    @staticmethod
    def CountCorps():
        return Corporation.__corp_count
    
    def __str__(self):
        return self.__name + " Corporation"

    def __del__(self):
        print("Goodbye", "Corporation", self.__name, sep = '\t', end = '\n\n')

def MergeCorporations(first, second):
    global lastOperation
    if (first == None) and (second == None):
        return None
    lastOperation = datetime.now()
    if (first == None):
        return second
    if (second == None):
        return first
    allWorkers = first.getWorkers().Union(second.getWorkers())
    firstSal = first.getSalary()
    secondSal = second.getSalary()
    front_back_full = list()
    for id, element in enumerate(firstSal):
        temporary = set(element).Insersection(set(secondSal[id]))
        front_back_full.append(list(sorted(temporary))[-1])
    front, back, full = tuple([element in front_back_full])
    resultCorp = Corporation(first.getName(), front, back, full)
    for person in allWorkers:
        resultCorp.addNewWorker(person)
    return resultCorp
    

def testingRun():
    global lastOperation
    print(lastOperation)
    print('--------------------------\n')
    dev = Developer("Aa", 1, ['x1', 'y1'], 1, "True ")
    front = Frontend("Bb", 2, ['x2', 'y2'], 2)
    back = Backend("Cc", 3, ['x3', 'y3'], 3)
    full = FullStack("Dd", 4, ['x4', 'y4'], 4)
    
    corp = Corporation("CorpEe", 15, 16)
    corp.printMedSalary()
    
    for person in [front, back, full]:
        #print(person)
        prof = person.who
        corp.addNewWorker(person, prof)
    
    print(len(corp.getWorkers()))
    for person in frozenset(corp.getWorkers()):
        person.work()
    
    print(Corporation.CountCorps(), '\n')
    corp.printMedSalary()

if __name__ == "__main__":
    #running this module
    testingRun()
    extraFinalDec(extraFinal)
