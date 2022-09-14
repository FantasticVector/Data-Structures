// const countConstruct = (target, wordBank) => {
//   if (target === '') return 1

//   let totalCount = 0
//   for (let word of wordBank) {
//     if (target.indexOf(word) === 0) {
//       const suffix = target.slice(word.length)
//       const numWays = countConstruct(suffix, wordBank)
//       totalCount += numWays
//     }
//   }
//   return totalCount
// }
// Memoization
const countConstruct = (target, wordBank, memo={}) => {
  if (target in memo) return memo[target]
  if (target === '') return 1

  let totalCount = 0
  for (let word of wordBank) {
    if (target.indexOf(word) === 0) {
      const suffix = target.slice(word.length)
      const numWays = countConstruct(suffix, wordBank, memo)
      totalCount += numWays
    }
  }
  memo[target] = totalCount
  return totalCount
}

console.log(countConstruct('abcdef', ['abc','def','ab', 'de', 'cd', 'ef']))