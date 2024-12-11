def load_data(file_name):
  with open(file_name) as f:
    data = f.readlines()
  
  km = []
  speed = []
  for row in data:
    x, y = row.split()
    km.append(row)
    speed.append(int(y))
  
  return km, speed

def sol1(file_name):
  km, speed = load_data(file_name)
  speed.reverse()
  
  cnt_jams, max_jam, max_diff = 1, 1, 0
  
  min_speed = speed[0]
  last_jam = 0
  for i in range(1, len(speed)):
    if speed[i] <= min_speed:
      min_speed = speed[i]
      cnt_jams += 1
      max_jam = max(max_jam, i - last_jam)
      last_jam = i
      
    max_diff = max(max_diff, speed[i] - min_speed)
  
  return cnt_jams, max_jam, max_diff
  
st, si = sol1("zad1/test.in"), sol1("zad1/input.in")
print(f"Test:\n Number of columns: {st[0]}\n Longest column: {st[1]} \n Maximum speed differance: {st[2]}")
print(f"Solution:\n Number of columns: {si[0]}\n Longest column: {si[1]} \n Maximum speed differance: {si[2]}")