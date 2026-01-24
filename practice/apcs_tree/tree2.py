class Node:
    def __init__(self, value: int, parent: Node | None=None):
        self.value = value
        self.parent = parent
        
        if value == 0:
            self.children = None
        elif value & 1:
            self.children = {
                1: None,
                2: None,
                3: None
            }
        else:
            self.children = {
                1: None,
                2: None
            }
            
    def hasSpace(self):
        return False if (self.children is None) or (None not in self.children.values()) else True
    
    def addChild(self, child: Node):
        if not self.hasSpace(): return None
        
        for i, val in enumerate(self.children.values()):
            if val == None: 
                self.children[i + 1] = child
                return (self.value, child.value)

node_list = [int(n) for n in input().split(" ")]

cur = tree = Node(node_list[0], None)
connected_pairs = [] # without (n, 0) pairs

for n_val in node_list[1:]:
    if not cur.hasSpace():
        while (cur := cur.parent) and (not cur.hasSpace()): pass
        if cur is None: break
        
    new = Node(n_val, cur)
    connected_pairs.append(cur.addChild(new))
    cur = new

print(sum([abs(p - c) for p, c in connected_pairs if 0 not in (p, c)]))