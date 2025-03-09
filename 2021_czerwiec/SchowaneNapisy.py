import sys
from collections import Counter

def load_data():
    with open(sys.argv[1]) as f:
        data = f.readlines()
    return [line.strip() for line in data]
    
    
def task1():
    data = load_data()
    cnt = 0
    for s in data:
        for c in s:
            if c.isdigit():
                cnt += 1
                
    print(cnt)
    
def task2():
    data = load_data()
    for i in range(20, len(data)+1, 20):
        print(data[i-1][i//20-1], end="")
        
def task3():
    data = load_data()
    for row in data:
        opt1 = row + row[0]
        opt2 = row[-1] + row
        if opt1 == opt1[::-1]:
            print(opt1[len(opt1)//2], end="")
        elif opt2 == opt2[::-1]:
            print(opt2[len(opt1)//2], end="")
            
def task4():
    data = load_data()
    cnt_x = 0
    for row in data:
        digits = [x for x in row if x.isdigit()]
        for i in range(0, len(digits), 2):
            num = int("".join(digits[i:i+2]))
            if num < 65 or num > 90:
                continue
                
            asc = chr(num)
            print(asc, end='')
            
            if asc == 'X':
                cnt_x += 1
            else:
                cnt_x = 0
            if (cnt_x >= 3):
                return
                

task1()
print("-----------------------------------")
task2()
print()
print("-----------------------------------")
task3()
print()
print("-----------------------------------")
task4()
print()