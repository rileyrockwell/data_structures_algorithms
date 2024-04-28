# collaborators: ashok

# depth first search

# assume Node class is given

# testing

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_max_depth(root: Node) -> int:
	# if node does not exist
	if not root:
		return 0

	# base case
	if root.left == None and root.right == None:
		return 0

	def dfs(root)
		# if there exists a left node
		if root.left:
			# recursive call
			return tree_max_depth(root.left) + 1

		if root.right:
			# recursive call
			return tree_max_depth(root.right) + 1


	return max(dfs(root.left), dfs(root.right))



# algomonster
def tree_max_depth(root: Node) -> int:
    def dfs(root):
        # null node adds no depth
        if not root:
            return 0
        # num nodes in longest path of current subtree = max num nodes of its two subtrees + 1 current node
        return max(dfs(root.left), dfs(root.right)) + 1

    return dfs(root) - 1 if root else 0


# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    # root = build_tree(iter(input().split()), int)

    tree = "6 x 9 x 11 x 7 x x"
    root = build_tree(iter(str(tree).split()), int)
    res = tree_max_depth(root)
    print(res)
