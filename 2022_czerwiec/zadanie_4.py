import sys
import math

def load_data():
    with open(sys.argv[1]) as f:
        data = [line.strip() for line in f]
    return data 

def get_primes(n):
    is_prime = [True] * (n+1)
    m = math.ceil(math.sqrt(n))
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, m+1):
        if is_prime[i]:
            for j in range(i*2, n+1, i):
                is_prime[j] = False 
    
    return is_prime 

def task1():
    data = load_data()
    for num in data:
        if int(num[::-1]) % 17 == 0:
            print(num[::-1])

def task2():
    data = load_data()
    best = ["", 0]
    for num in data:
        rev = num[::-1]
        x = abs(int(num) - int(rev))
        if best[1] < x:
            best = [num, x]
    
    print(best)

def task3():
    data = load_data()
    is_prime = get_primes(10000)
    for num in data:
        if is_prime[int(num)] and is_prime[int(num[::-1])]:
            print(num)

def task4():
    data = load_data()
    cnt = {}
    for num in data:
        if num not in cnt:
            cnt[num] = 1
        else:
            cnt[num] += 1 
    print(f"{len(cnt)}, {sum([1 if val == 2 else 0 for val in cnt.values()])}, {sum([1 if val == 3 else 0 for val in cnt.values()])}")
    

task1()
print("-------------------")
task2()
print("-------------------")
task3()
print("-------------------")
task4()
