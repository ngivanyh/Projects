class node:
    def __init__(self, value, node_type="unknown", parent=None):
        if not value:
            self.children = None
            self.childrens = 0
            self.node_type = "dead-end"
        else:
            match node_type:
                case "odd":
                    self.children = {
                        1: None,
                        2: None,
                        3: None
                    }
                    self.node_type = node_type
                    self.childrens = len(self.children)
                case "even":
                    self.children = {
                        1: None,
                        2: None
                    }
                    self.node_type = node_type
                    self.childrens = len(self.children)
                case _:
                    self.children = None
                    self.childrens = 0
                    self.node_type = "unknown"
        self.value = value
        self.parent = parent
    
    def __repr__(self):
        if self.children is not None:
            if isinstance(self.parent, node):
                parent_out = self.parent.value
            else:
                parent_out = "None"
            
            return f"node(value={self.value})\nchildren: {tuple(self.children.values())}\nparent: {parent_out}\n"
        
        return f"Dead end -> 0\nparent: {self.parent}\n"

    def add_child(self, pos, value, child_odd_even):
        if not (1 >= pos <= self.childrens):
            return
        
        self.children[pos] = node(child_odd_even, value, self)
    
    def available(self):
        if self.children is None:
            return None
        
        for i in range(self.childrens, self.childrens + 1):
            if self.children[i] is None: return i
        
        return None
        
        
tree = node(-1)

def main():
    global tree
    nodes = [int(n) for n in input().split(" ")]
    print(nodes)

    tree = node(nodes[0], "odd" if nodes[0] & 1 else "even")
    # print(tree)

    build(nodes, nodes[0], 0, "down")

def build(nodes_list, current_node, current_node_index, direction):
    global tree
    if current_node_index == (len(nodes_list) - 1):
        return
    print(tree)
    
    
    
    pass
# left -> (mid) -> right

if __name__ == "__main__":
    main()