import sys
import math

def load_numbers_data():
    with open("dane/liczby_przyklad.txt" if sys.argv[1] == "przyklad" else "dane/liczby.txt") as f:
        data = f.readlines()
        
    return [int(line.strip()) for line in data]

def load_primes_data():
    with open("dane/pierwsze_przyklad.txt" if sys.argv[1] == "przyklad" else "dane/pierwsze.txt") as f:
        data = f.readlines()
        
    return [int(line.strip()) for line in data]


def is_prime(n): 
    m = math.ceil(math.sqrt(n))
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, m+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
                
    return is_prime
    
def task1():
    data = load_numbers_data()
    prime = is_prime(5000)
    return [n for n in data if 100 <= n <= 5000 and prime[n]]

def task2():
    data = load_primes_data()
    prime = is_prime(10000000)
    return [num for num in data if prime[int(str(num)[::-1])]]

def w(n):
    if len(str(n)) == 1:
        if n == 1:
            return 1
        else:
            return 0
        
    return w(sum(int(x) for x in str(n)))

def task3():
    data = load_primes_data()
    return sum(w(n) for n in data)
    

print(f"Podpunkt 1: \n{task1()}")
print(f"Podpunkt 2: \n{task2()}")
print(f"Podpunkt 3: \n{task3()}")
