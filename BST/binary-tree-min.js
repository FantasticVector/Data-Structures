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

// Iteratively

const binaryTreeMin = (root) => {
  if (root === null) return 0;
  const stack = [root];
  let minValue = root.val;
  while (stack.length > 0) {
    const current = stack.pop();
    minValue = Math.min(minValue, current.val);
    if (current.right) stack.push(current.right);
    if (current.left) stack.push(current.left);
  }
  return minValue;
};

// result = binaryTreeMin(a);
// console.log(result);

// Recursively

const binaryTreeSumRec = (root) => {
  if (root === null) return Infinity;
  return Math.min(
    root.val,
    binaryTreeSumRec(root.left),
    binaryTreeSumRec(root.right)
  );
};

result = binaryTreeSumRec(a);
console.log(result);
