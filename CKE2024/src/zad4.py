from collections import defaultdict
from itertools import combinations

def load_data(file_name):
  with open(file_name) as f:
    data = f.readlines()
    
  res = []
  for line in data:
    res.append(list(map(int, line.strip().split())))
    
  return res

def sol1(file_name):
  squares = load_data(file_name)
  
  return max(w * h for w, h in squares), min(w * h for w, h in squares)

def sol2(file_name):
  sq = load_data(file_name)
  
  max_cnt = 0
  max_hw = 0
  cnt = 1
  for i in range(1, len(sq)):
    if sq[i][0] > sq[i-1][0] or sq[i][1] > sq[i-1][1]:
      cnt = 1
    else:
      cnt += 1
      if max_cnt < cnt:
        max_cnt = cnt
        max_hw = [sq[i][0], sq[i][1]]
      
  return max_cnt, max_hw 
  

def sol3(file_name):
  sqs = load_data(file_name)
  
  types = defaultdict(list)
  for x in sqs:
    types[x[0]].append(x[1])
   
  ans = [0, 0, 0]
  for sq in types.values():
    for i in range(len(sq)):
      for j in range(i+1, len(sq)):
        ans[0] = max(ans[0], sq[i] + sq[j])
        for k in range(j+1, len(sq)):
          ans[1] = max(ans[1], sq[i] + sq[j] + sq[k]) 
          for a in range(k+1, len(sq)):
            for b in range(a+1, len(sq)):
              ans[2] = max(ans[2], sq[i] + sq[j] + sq[k] + sq[a] + sq[b])

  for sq in types.values():
    for comb in combinations(sq, 2):
      ans[0] = max(ans[0], sum(comb))
    for comb in combinations(sq, 3):
      ans[1] = max(ans[1], sum(comb))
    for comb in combinations(sq, 5):
      ans[2] = max(ans[2], sum(comb))
      
  return ans

def sol3_normalnie(file_name):
  sqs = load_data(file_name)
  
  types = defaultdict(list)
  for x in sqs:
    types[x[0]].append(x[1])
    
  for key in types:
    types[key].sort(reverse=True)
  
  ans = [0, 0, 0] 
  for sq in types.values():
    ans[0] = max(ans[0], sum(sq[:2]))
    ans[1] = max(ans[1], sum(sq[:3]))
    ans[2] = max(ans[2], sum(sq[:5]))

  return ans
  
print(f"Podpunkt 1:\nTest: {sol1('data/prostokaty_przyklad.txt')}\nRozwiazanie: {sol1('data/prostokaty.txt')}\n\n")
print(f"Podpunkt 2:\nTest: {sol2('data/prostokaty_przyklad.txt')}\nRozwiazanie: {sol2('data/prostokaty.txt')}\n\n")
print(f"Podpunkt 3:\nTest: {sol3_normalnie('data/prostokaty_przyklad.txt')}\nRozwiazanie: {sol3_normalnie('data/prostokaty.txt')}\n\n")