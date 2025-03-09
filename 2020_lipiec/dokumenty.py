import sys
import re

def load_data():
    with open(sys.argv[1]) as f:
        data = f.readlines()
    
    lines = [re.split(r'(\d+)', line.strip()) for line in data]
    return [[part for part in parts if part] for parts in lines]

def task1():
    data = load_data()
    hashed = {x: sum(int(c) for c in y) for x, y in data}
    mx = max(hashed, key=lambda key: hashed[key])
    mx = hashed[mx]
    return ["".join(tab) for tab in data if hashed[tab[0]] == mx]

def task2():
    data = load_data()
    return ["".join([x, y]) for x, y in data if x == x[::-1] or y == y[::-1]] 


def task3():
    data = ["".join(row) for row in load_data()]
    w = [7, 3, 1, 0, 7, 3, 1, 7, 3]
    return [row for row in data if sum(((ord(c)-55) if not c.isdigit() else int(c)) * w[i] for i, c in enumerate(row)) % 10 != int(row[3])]    
    
    
    
print(f"Podpunkt 1: {task1()}")
print(f"Podpunkt 2: {task2()}")
print(f"Podpunkt 3: {task3()}")
