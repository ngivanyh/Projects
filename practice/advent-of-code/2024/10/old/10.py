# advent of code day 10 — 2024 (https://adventofcode.com/2024/day/10)
from pathlib import Path
from typing import Tuple, List
from re import sub

class Map:
    def __init__(self, path: Path):
        self.raw = sub(r"[ \t]", "", open(path).read())
        self.map = []
        
        for str_row in self.raw.split():
            row = []
            for val in str_row:
                row.append(int(val) if val != '.' else -1)
                
            self.map.append(tuple(row))
        self.map = tuple(self.map)
        
        self.rows = len(self.raw.split())
        self.cols = len(self.map[0])
    
    def __repr__(self):
        return f"Map(raw={self.raw}, map={self.map})"
    
    def distanced(self, a: Tuple[int, int], b: Tuple[int, int]):
        # no diagonal a: (y, x), b: (y, x)
        x_diff = abs(a[1] - b[1])
        y_diff = abs(a[0] - b[0])
        return {"x": x_diff, "y": y_diff, "sum": x_diff + y_diff}
    
    def locate(self, val: int):
        # general locate, scans every row
        hits = []
        
        for y, row in enumerate(self.map):
            for x, point in enumerate(row):
                if point == val: hits.append((y, x))
        return tuple(hits)
    
    def locate_surroundings(self, point: Tuple[int, int], val: int):
        # searches for val near (up, down, left, right of) point
        # if point[0] >= self.rows or point[1] >= self.cols:
        #     return None

        try: u = (point[0] + 1, point[1]) if self.map[point[0] + 1][point[1]] == val else None
        except IndexError: u = None
        
        try: d = (point[0] - 1, point[1]) if self.map[point[0] - 1][point[1]] == val else None
        except IndexError: d = None
        
        try: l = (point[0], point[1] - 1) if self.map[point[0]][point[1] - 1] == val else None
        except IndexError: l = None
        
        try: r = (point[0], point[1] + 1) if self.map[point[0]][point[1] + 1] == val else None
        except IndexError: r = None
    
        return {
            "up": u,
            "down": d,
            "left": l,
            "right": r
        }

class Trail:
    def __init__(self):
        self.trail = {
            0: None,
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None,
            9: None
        }
    
    def __repr__(self):
        return str(self.trail)
    
    def add_coord(self, map: Map, coords):
        # (y, x) Tuple[int, int]
        self.trail[map.map[coords[0]][coords[1]]] = coords
    
    def isEmpty(self):
        for i in range(10):
            if self.trail[i] == None:
                return True
        return False
    
def isViable(map: Map, start: Tuple[int, int], end: Tuple[int, int]):
        # start end are coords (y, x)
        length_threshold = map.map[end[0]][end[1]] - map.map[start[0]][start[1]]
        
        return False if map.distanced(start, end)["sum"] > length_threshold else True
    
def opposite_num(n: int):
    return 9 - n

def trailsAreCompleted(trails: List[Trail]):
    for trail in trails:
        if trail.isEmpty():
            return False
    return True

def main(mapPath: Path):
    map = Map(mapPath)
    trails = []
    
    start = map.locate(0)
    end = map.locate(opposite_num(0))
    
    for trailhead in start:
        for destination in end:
            temp = Trail()
            temp.add_coord(map, trailhead)
            temp.add_coord(map, destination)
            
            if isViable(map, trailhead, destination):
                trails.append(temp)

    pot_trails = len(trails)
    
    cur_node = 0 # and vice versa: 9
    while pot_trails != 0 or (not trailsAreCompleted(trails)):
        old_trail = trails
        rm = []
        print(f"cur: {old_trail}")
        
        for pot_trail in old_trail:
            start = map.locate_surroundings(pot_trail.trail[cur_node], cur_node + 1)
            end = map.locate_surroundings(pot_trail.trail[opposite_num(cur_node)], opposite_num(cur_node + 1))

            for start_node in start.values():
                if start_node == None:
                    continue
                
                for end_node in end.values():
                    if end_node == None:
                        continue
                    
                    if isViable(map, start_node, end_node):
                        temp = pot_trail
                        temp.add_coord(map, start_node)
                        temp.add_coord(map, end_node)
                        
                        trails.append(temp)
                        print(trails)
                    else:
                        rm.append(pot_trail)
        for rm_item in rm:
            trails.remove(rm_item)
                        
        cur_node += 1
                        
    print(trails)
    print(map)

if __name__ == "__main__":
    main(Path("./map"))
