import sys

def load_data(idx):
    with (open(f"data/przyklad{idx}.txt") if sys.argv[1] == "przyklad" else open(f"data/dane{idx}.txt")) as f:
        data = f.readlines()
    return [line.strip().split() for line in data]

def task1():
    a, b = load_data(1), load_data(2)
    return sum(x[-1] == y[-1] for x, y in zip(a, b)) 
    
def task2():
    a, b = load_data(1), load_data(2)
    solve = lambda tab: sum(int(x) % 2 for x in tab) == 5
    return sum(solve(x) and solve(y) for x, y in zip(a, b))
    
def task3():
   a, b = load_data(1), load_data(2)
   ans = [idx+1 for idx, (x, y) in enumerate(zip(a, b)) if set(x) == set(y)]
   return len(ans), ans
   
def task4():
    a, b = load_data(1), load_data(2)
    return [sorted([int(num) for num in x] + [int(num) for num in y]) for x, y in zip(a, b)]

print(f"podpunkt 1: {task1()}")
print(f"podpunkt 2: {task2()}")
print(f"podpunkt 3: {task3()}")
print(f"podpunkt 4: ")
t4 = task4()
for x in t4:
    for y in x:
        print(y, end=" ")
    print()