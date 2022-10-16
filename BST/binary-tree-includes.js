// Given tree and target value find if value is
// in binary tree
class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");
const e = new Node("e");
const f = new Node("f");

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

// stack implementation
const binaryTreeIncludes = (root, target) => {
  if (root === null) return [];
  const queue = [root];
  while (queue.length > 0) {
    const current = queue.shift();
    if (current.val === target) return true;
    if (current.left) queue.push(current.left);
    if (current.right) queue.push(current.right);
  }
  return false;
};

result = binaryTreeIncludes(a, "k");
console.log(result);

// Recursive Implementation
const binaryTreeIncludesRec = (root, target) => {
  if (root === null) return false;
  if (root.val === target) return true;
  return (
    binaryTreeIncludes(root.left, target) ||
    binaryTreeIncludes(root.right, target)
  );
};

result = binaryTreeIncludesRec(a, "j");
console.log(result);
