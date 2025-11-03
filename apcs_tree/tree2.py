class node:
    def __init__(self, value, parent=None):
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
    
    def addChild(self, child):
        if not self.hasSpace():
            return None
        
        for i, val in enumerate(self.children.values()):
            if val == None: self.children[i + 1] = child; break
            
node_list = [int(n) for n in input().split(" ")]

tree = node(node_list[0], None)
cur = tree

for n_val in node_list[1:]:
    if cur.hasSpace():
        new = node(n_val, cur)
        cur.addChild(new)
        cur = new
    print(tree)