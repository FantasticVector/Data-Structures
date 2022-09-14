// Iterative
const depthFirstPrint = (graph, source) => {
  const stack = [ source ]
  while (stack.length > 0) {
    const current = stack.pop()
    console.log(current)
    
    for (let neighbor of graph[current]) {
      stack.push(neighbor)
    }
  }
}

// Recursive
const depthFirstRecursive = (graph, source) => {
  console.log(source);
  for (let neighbor of graph[source]) {
    depthFirstRecursive(graph, neighbor)
  }
}
const graph = {
  a : ['b', 'c'],
  b: ['d'],
  c: ['e'],
  d: ['f'],
  e: [],
  f: [],
}
depthFirstPrint(graph, 'a')
console.log()
depthFirstRecursive(graph, 'a')