import math
import sys

def load_data(file_name):
    with open(file_name) as f:
        data = f.readlines()
    
    res = [[], []]
    for line in data:
        x, y = line.strip().split()
        res[0].append(int(x))
        res[1].append(y)
    
    return res

def generate_primes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n+1):
        if is_prime[i] and i*i<=n:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    
    res = []
    for num, is_p in enumerate(is_prime):
        if is_p:
            res.append(num)
    
    return res
    
def part1(file_name):
    nums, words = load_data(file_name)
    primes = generate_primes(101)

    ans = []
    for num in nums:
        if num % 2:
            continue
        
        
        for p1 in primes:
            end = False
            for p2 in reversed(primes):
                if p1 + p2 == num:
                    ans.append((num, p1, p2))
                    end = True
                    break
            if end:
                break
    
    return ans

def part2(file_name):
    nums, words = load_data(file_name)
    
    ans = []
    for word in words:
        cnt = 1
        mx = 1
        mx_str = word[0]
        for i in range(1, len(word)):
            if word[i-1] != word[i]:
                cnt = 1
            else:
                cnt += 1
            
            if mx < cnt:
                mx = cnt
                mx_str = word[i] * cnt

        ans.append((mx_str, mx))
    
    return ans

def part3(file_name):
    nums, words = load_data(file_name)
    
    ok = []
    for num, word in zip(nums, words):
        if num == len(word):
            ok.append((num, word))
            
    return sorted(ok)[0]

file_name = sys.argv[1]

print(f"Podpunkt 1:")
for a, b, c in part1(file_name):
    print(f"{a}, {b}, {c}")
    
print(f"Podpunkt 2:")
for a, b in part2(file_name):
    print(f"{a}, {b}")
    
print(f"Podpunkt 3: {part3(file_name)}")
                
    