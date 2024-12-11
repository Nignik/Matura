from matplotlib import pyplot as plt
from collections import defaultdict
import pandas as pd

with open("owoce.txt", 'r', encoding='UTF-8') as file:
    lines = file.read().split('\n')

m, t, p = "maliny", "truskawki", "porzeczki"

months = defaultdict(lambda: defaultdict(int))
month_map = {5: "maj", 6: "czerwiec", 7: "lipiec", 8: "sierpień", 9: "wrzesień"}

current = {m: 0, t: 0, p: 0}
konfitury = {"malinowo-truskawkowe": 0, "malinowo-porzeczkowe": 0, "truskawkowo-porzeczkowe": 0}
kg = {"malinowo-truskawkowe": 0, "malinowo-porzeczkowe": 0, "truskawkowo-porzeczkowe": 0}

for idx, line in enumerate(lines):
    if idx < 1:
        continue
    
    if len(line.split("\t")) < 4:
        continue
    data, maliny, truskawki, porzeczki = line.split("\t")
    maliny, truskawki, porzeczki = int(maliny), int(truskawki), int(porzeczki)
    month = month_map[int(data.split(".")[1])]
    months[month][m] += maliny
    months[month][t] += truskawki
    months[month][p] += porzeczki
    
    current[m] += maliny
    current[t] += truskawki
    current[p] += porzeczki
    
    wm, wt, wp = current[m], current[t], current[p]
    
    if wm > wp and wt > wp:
        konfitury["malinowo-truskawkowe"] += 1
        sub = min(wm, wt)
        current[m] -= sub
        current[t] -= sub
        kg["malinowo-truskawkowe"] += sub
        
    elif wm > wt and wt < wp:
        konfitury["malinowo-porzeczkowe"] += 1
        sub = min(wm, wp)
        current[m] -= sub
        current[p] -= sub
        kg["malinowo-porzeczkowe"] += sub
        
    elif wm < wp and wt > wm:
        konfitury["truskawkowo-porzeczkowe"] += 1
        sub = min(wt, wp)
        current[p] -= sub
        current[t] -= sub
        kg["truskawkowo-porzeczkowe"] += sub
    

print("Zadanie 6.1: ") 
df = pd.DataFrame.from_dict(months, orient='index')
print(df)

print("\nZadanie 6.3")
print(konfitury)

print("\nZadanie 6.4")
print(kg)

# Plotting the DataFrame
ax = df.plot(kind='bar', figsize=(10, 6))
ax.set_title('Zestawienie owoców')
ax.set_xlabel('Miesiac')
ax.set_ylabel('Liczba kilogramów')
ax.legend(title='Zadanie 6.2')

# Show the plot
plt.tight_layout()
plt.show()

