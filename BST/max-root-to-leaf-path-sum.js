// Initializing Binary Tree
class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const a = new Node(30);
const b = new Node(12);
const c = new Node(10);
const d = new Node(5);
const e = new Node(2);
const f = new Node(50);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

// Recursive Solution...
const rootToLeafPathSum = (root) => {
  if (root === null) return -Infinity;
  if (root.left === null && root.right === null) return root.val;
  const maxChild = Math.max(
    rootToLeafPathSum(root.left),
    rootToLeafPathSum(root.right)
  );
  return root.val + maxChild;
};

result = rootToLeafPathSum(a);
console.log(result);
