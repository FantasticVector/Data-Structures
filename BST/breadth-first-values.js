// Initializing Binary Tree
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

// Stack Implementation
const breadthFirstValues = (root) => {
  if (root === null) return [];
  const queue = [root];
  const result = [];
  while (queue.length > 0) {
    current = queue.shift();
    result.push(current.val);
    if (current.left) queue.push(current.left);
    if (current.right) queue.push(current.right);
  }
  return result;
};

result = breadthFirstValues(a);
console.log(result);

// Cannot Implement using queue
