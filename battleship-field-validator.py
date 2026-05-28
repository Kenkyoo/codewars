from collections import deque, Counter

def validate_battlefield(field):
    # write your magic here
    rows, cols = len(field), len(field[0])
    visits = [[False]*cols for _ in range(rows)]
    neigh = [(-1,0),(1,0),(0,-1),(0,1)]
    ships = []

    def bfs(r, c):
        queue = deque([(r, c)])
        visits[r][c] = True
        ship = []

        while queue:
            r, c = queue.popleft()
            ship.append((r, c))

            for dr, dc in neigh:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if not visits[nr][nc] and field[nr][nc] == 1:
                        visits[nr][nc] = True
                        queue.append((nr, nc))
        return ship
    for r in range(rows):
        for c in range(cols):
            if field[r][c] == 1 and not visits[r][c]:
                ships.append(bfs(r, c))
                
field = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                       [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                       [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


    for ship in ships:
        ship_rows = set(r for r, c in ship)
        ship_cols = set(c for r, c in ship)
        if len(ship_rows) > 1 and len(ship_cols) > 1:
            return False

    all_cells = set(cell for ship in ships for cell in ship)
    for ship in ships:
        ship_set = set(ship)
        for (r, c) in ship:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    if (r+dr, c+dc) in all_cells and (r+dr, c+dc) not in ship_set:
                        return False
    counter_ships = []

    for i, f in enumerate(ships):
        counter_ships.append(len(f))
    
    fields = Counter(counter_ships)

    rules = {
    1: 4,
    2: 3,
    3: 2,
    4: 1
    }

    return fields == rules