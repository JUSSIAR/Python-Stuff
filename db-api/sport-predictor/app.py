import sqlite3

conn = sqlite3.connect('SkiSport.db3')
cursor = conn.cursor()

types = frozenset(['ADD', 'GET', 'EXIT'])


class validator:
    queries = int(0)

    def __init__(self):
        pass

    @staticmethod
    def ADD(query):
        validator.queries += 1
        if len(query) != 4:
            print("Invalid")
            return False
        try:
            float(query[3]) + 1
        except:
            print("Invalid")
            return False
        finally:
            pass
        return True

    @staticmethod
    def GET(query):
        validator.queries += 1
        if len(query) != 2:
            print("Invalid")
            return False
        try:
            float(query[1]) + 1
        except:
            print("Invalid")
            return False
        finally:
            pass
        return True

    @staticmethod
    def EXIT(query):
        validator.queries += 1
        if len(query) != 1:
            print("Invalid")
            return False
        return True

    def __str__(self):
        return "Validator has got %d queries" %validator.queries


def ADD_(query):
    # print(query)
    cursor.executescript("""
        INSERT INTO race1 (name, time, dist) 
        VALUES ("SMTH", "err", 2);
    """)
    conn.commit()


def print_string(arr=['Pos', 'Name', 'Time']):
    _arr = [str(x) for x in arr.copy()]
    for z in range(len(arr)):
        _arr[z] = ' ' * 3 + _arr[z]
        while len(_arr[z]) < 20:
            _arr[z] += ' '
    print('|'.join(_arr))


def separator():
    kol = 20
    print('-' * kol, end='')
    print('+', end='')
    print('-' * kol, end='')
    print('+', end='')
    print('-' * kol, end='\n')


def GET_(query):
    # cursor.execute("SELECT name, time FROM race1")
    cursor.execute("SELECT name, time FROM race1 WHERE dist <= %f" % float(query[-1]))
    res = cursor.fetchall()
    print_string()
    for i, elem in enumerate(res):
        separator()
        print_string([i] + list(elem))


while True:
    command = input().split()
    if command[0] not in types:
        print("Invalid")
        continue
    if command[0] == 'EXIT':
        if validator.EXIT(command):
            print("finished")
            break
    elif command[0] == 'GET':
        if validator.GET(command):
            GET_(command[-1])
    else:
        if validator.ADD(command):
            ADD_(command[1::])


conn.close()