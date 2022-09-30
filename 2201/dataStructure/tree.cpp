#include <cstddef>
#include <iostream>

typedef struct node
{
  int          data;
  struct node* left;
  struct node* right;
  node();
  node(int data);
} t_node;

node::node() : data(0), left(NULL), right(NULL) {}
node::node(int data) : data(data), left(NULL), right(NULL) {}

class binaryTree
{
private:
  node n;
  bool isFirst;

  void insertRecursive(node* nd, int data);
  void _traversePreOrder(node* nd);
  void _traverseInOrder(node* nd);
  void _traversePostOrder(node* nd);

public:
  binaryTree();
  void insertNode(int data);
  void traversePreOrder();
  void traverseInOrder();
  void traversePostOrder();
};

// private

// nodeを挿入する適切な位置を検索し、新しいnodeを用意して返却する
void binaryTree::insertRecursive(node* nd, int data) {
  if (data < nd->data) {
    if (nd->left == NULL) {
      nd->left = new node(data);
      return;
    } else {
      insertRecursive(nd->left, data);
      return;
    }
  } else { // data >= nd->data
    if (nd->right == NULL) {
      nd->right = new node(data);
      return;
    } else {
      insertRecursive(nd->right, data);
      return;
    }
  }
}

void binaryTree::_traversePreOrder(node* nd) {
  if (nd != NULL) {
    std::cout << nd->data << std::endl;
    _traversePreOrder(nd->left);
    _traversePreOrder(nd->right);
  }
}

void binaryTree::_traverseInOrder(node* nd) {
  if (nd != NULL) {
    _traverseInOrder(nd->left);
    std::cout << nd->data << std::endl;
    _traverseInOrder(nd->right);
  }
}
void binaryTree::_traversePostOrder(node* nd) {
  if (nd != NULL) {
    _traversePostOrder(nd->left);
    _traversePostOrder(nd->right);
    std::cout << nd->data << std::endl;
  }
}

// public
binaryTree::binaryTree() : n(), isFirst(true) {}

void binaryTree::insertNode(int data) {
  if (isFirst) {
    n.data  = data;
    isFirst = false;
    return;
  }
  insertRecursive(&n, data);
}

void binaryTree::traversePreOrder() { _traversePreOrder(&n); }
void binaryTree::traverseInOrder() { _traverseInOrder(&n); }
void binaryTree::traversePostOrder() { _traversePostOrder(&n); }

int main() {
  binaryTree tree;
  int        numbers[] = { 31, 12, 44, 2, 91, 5 };
  for (int i = 0; i < 6; ++i) {
    tree.insertNode(numbers[i]);
  }
  tree.traversePreOrder();
  std::cout << "--------------------" << std::endl;
  tree.traverseInOrder();
  std::cout << "--------------------" << std::endl;
  tree.traversePostOrder();
}
