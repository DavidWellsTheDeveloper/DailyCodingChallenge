# Good morning! Here's your coding interview problem for today.
# This problem was asked by Google.
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
# For example, given the following Node class
#
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# The following test should pass:
#
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

# lets navigate the tree by depth first. Serialize I believe works.
def serialize(node):

    if node is None:
        return
    if node.val == 'root':
        f = open("serialize.txt", "w")
    else:
        f = open("serialize.txt", "a")
    print(node.val)
    f.write(node.val + ",")
    f.close()
    serialize(node.left)
    serialize(node.right)
    # There should just be 1 line
    f = open("serialize.txt", "r")
    return f.readline()

# deserialize isn't working yet. There's probably a recursive way to do it...
def deserialize(serializedNode):
    node_str = serializedNode.split(',')
    node_str = node_str[:(len(node_str)-1)]
    node = Node('root')
    for n in node_str:
        working_node = node
        address = n.split('.')
        for location in address:
            if location == "left":
                working_node = node.right
            if location == "right":
                working_node = node.right
        working_node = Node(n)
    return Node()

# Initial thoughts... this is a problem that seems like recursion would make for an idea solution.
# Let's do pre-ordering...
if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
