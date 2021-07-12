
class Tree(object):
    def __init__(self, data, depth, parent):
        self.data = data
        self.depth = depth
        self.parent = parent
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

def search_and_remove(lines, tree: Tree, depth):
    new_lines = []
    for line in lines:
        elements = line.split(')')
        if elements[0] == tree.data:
            tree.children.append(Tree(elements[1], depth, tree))
        else:
            new_lines.append(line)
    return new_lines

def sum_depth(tree: Tree) :
    depth = 0
    for child in tree.children:
        depth += child.depth
        depth += sum_depth(child)
    return depth

def build_subtree(lines, tree: Tree, depth):
    # populate children
    lines = search_and_remove(lines, tree, depth)
    for child in tree.children:
        lines = build_subtree(lines, child, depth + 1)
    return lines

def find(tree: Tree, name):
    for child in tree.children:
        if child.data == name:
            return child
        else:
            you = find(child, name)
            if (you):
                return you
    return None



f = open("input.txt", 'r')
lines = f.readlines()

lines_stripped = []
for line in lines:
    lines_stripped.append(line.rstrip())
lines = lines_stripped
f.close()

COM = Tree('COM', 0, None)
curr = COM
depth = 0
lines = build_subtree(lines, curr, depth + 1)

# take a sum total of all the depths
depth = sum_depth(COM)
print("total orbits in map:", depth)
print()

# locate YOU
print("finding you...")
you = find(COM, 'YOU')
print("Found YOU!!!")
print()

curr = you.parent
san = None
jumps = 0
print("locating santa...")
while san == None:
    san = find(curr, 'SAN')
    if san == None:
        curr = curr.parent
        jumps += 1

print("Found Santa!!!")
print()
additional_jumps = (san.depth - 1) - curr.depth # jumping to same planet as santa. Santa is not a planet
total_jumps = jumps + additional_jumps
print("Total Jumps required to reach santa:", total_jumps)







