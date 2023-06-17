class TreeNode:
  def __init__(self, val):
    self.val = val
    if val != None:
      self.left = TreeNode(None)
      self.right = TreeNode(None)

  def set_left_and_right(self, left=None, right=None):
    self.left = TreeNode(left)
    self.right = TreeNode(right)
    return self

def init_tree():
  root = TreeNode('A')
  b = root.set_left_and_right('B', 'C').left
  d = b.set_left_and_right('D', 'E').left
  g = d.set_left_and_right('F', 'G').right
  g.set_left_and_right('H', 'I')
  return root

def dfs(node, search_val):
  open_list = []
  closed_list = []
  open_list.insert(0, node)

  count = 1
  while open_list: # 2
    print(f"loop: {count}")
    print(f"n: {open_list[0].val}, Left: {open_list[0].left.val}, Right: {open_list[0].right.val}")
    print(f"open_list: {list(map(lambda x: x.val, open_list))}")
    print(f"closed_list: {list(map(lambda x: x.val, closed_list))}")
    print("---------------------")
    subject_node = open_list.pop(0)
    if subject_node.val == search_val:
      return subject_node.val
    closed_list.insert(0, subject_node)
    # 深さ優先探索固有のロジック
    if subject_node.right.val:
      open_list.insert(0, subject_node.right)
    if subject_node.left.val:
      open_list.insert(0, subject_node.left)
    # ここまで
    count += 1
  return None

def bfs(node, search_val):
  open_list = []
  closed_list = []
  open_list.insert(0, node)

  count = 1
  while open_list: # 2
    print(f"loop: {count}")
    print(f"n: {open_list[0].val}, Left: {open_list[0].left.val}, Right: {open_list[0].right.val}")
    print(f"open_list: {list(map(lambda x: x.val, open_list))}")
    print(f"closed_list: {list(map(lambda x: x.val, closed_list))}")
    print("---------------------")
    subject_node = open_list.pop(0)
    if subject_node.val == search_val:
      return subject_node.val
    closed_list.insert(0, subject_node)
    # 深さ優先探索固有のロジック
    if subject_node.left.val:
      open_list.append(subject_node.left)
    if subject_node.right.val:
      open_list.append(subject_node.right)
    # ここまで
    count += 1
  return None

def main():
  root = init_tree()
  print('================')
  print('dfs start')
  print('================')
  result = dfs(root, 'C')
  print(result)

  print('================')
  print('bfs start')
  print('================')
  result = bfs(root, 'I')
  print(result)

main()
