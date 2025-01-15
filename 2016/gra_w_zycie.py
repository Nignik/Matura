import copy

def load_data(file_name):
    with open(file_name) as f:
        data = f.readlines()
        
    cells = []
    for i, row in enumerate(data):
        row = row.strip()
        cells.append([])
        for x in row:
            cells[i].append(1 if x == 'X' else 0)
    
    return cells

def count_neighbors(cells, i, j):
    neighbors_alive = 0
    n = len(cells)
    m = len(cells[0])
    
    for d in ((0, -1), (1, 0), (0, 1), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)):
        if cells[(i + d[0] + n) % n][(j + d[1] + m) % m]:
            neighbors_alive += 1
            
    return neighbors_alive

def count_cells(cells):
    cnt = 0
    for row in cells:
        for cell in row:
            cnt += cell
    return cnt

def compute_generations(cells, num_of_gens):
    n = len(cells)
    m = len(cells[0])
        
    for g in range(num_of_gens):
        cp = copy.deepcopy(cells)
        for i in range(n):
            for j in range(m):
                neighbors_alive = count_neighbors(cp, i, j)
                
                if cp[i][j]:
                    if neighbors_alive < 2 or neighbors_alive > 3:
                        cells[i][j] = 0
                elif neighbors_alive == 3:
                    cells[i][j] = 1
    
    return cells

        
def solve1(file_name):
    cells = load_data(file_name)
    compute_generations(cells, 36)
    
    print(count_neighbors(cells, 1, 18))
    
def solve2(file_name):
    cells = load_data(file_name)
    compute_generations(cells, 1)
    
    print(count_cells(cells))
    
def solve3(file_name):
    cells = load_data(file_name)
    prev = copy.deepcopy(cells)
    for i in range(100):
        compute_generations(cells, 1)
        if prev == cells:
            print(i+2)
            print(count_cells(cells))
            break
        
        prev = copy.deepcopy(cells)
        
    
solve1("data/gra_w_zycie.txt")
solve2("data/gra_w_zycie.txt")
solve3("data/gra_w_zycie.txt")