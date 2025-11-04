class node:
    def __init__(self, value: int, parent: node | None=None):
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
    
    def __repr__(self):
        return f"node(value={self.value}, childrens={self.children})"
    
    def hasSpace(self):
        if (self.children == None) or (None not in self.children.values()):
            return False
        return True
    
    def addChild(self, child: node):
        if not self.hasSpace():
            return None
        
        for i, val in enumerate(self.children.values()):
            if val == None: 
                self.children[i + 1] = child
                return (self.value, child.value)

node_list = [int(n) for n in input().split(" ")]

tree = node(node_list[0], None)
cur = tree; connected_pairs = []; node_value_diff = 0 # without (n, 0) pairs

for n_val in node_list[1:]:
    if not cur.hasSpace():
        while (cur := cur.parent) and (not cur.hasSpace()):
            pass
        if cur is None:
            break
        
    new = node(n_val, cur)
    connected_pairs.append(cur.addChild(new))
    cur = new

for pair in connected_pairs:
    if 0 not in pair:
        node_value_diff += abs(pair[0] - pair[1])

print(node_value_diff)