// Brute Force
// const howSum = (targetSum, numbers) => {
//   if (targetSum === 0) return []
//   if (targetSum < 0) return null;
//   for (let num of numbers) {
//     const remainder = targetSum - num
//     const remainderResult = howSum(remainder, numbers);
//     if (remainderResult !== null) {
//       return [...remainderResult, num];
//     }
//   }
//   return null;
// }
// console.log(howSum(6, [2, 3]))

// Memoization
const howSum = (targetSum, numbers, memo={}) => {
  if (targetSum in memo) return memo[targetSum];
  if (targetSum === 0) return []
  if (targetSum < 0) return null;
  for (let num of numbers) {
    const remainder = targetSum - num
    const remainderResult = howSum(remainder, numbers, memo);
    if (remainderResult !== null) {
      memo[targetSum] = [...remainderResult, num];
      return memo[targetSum];
    }
  }
  memo[targetSum] = null;
  return null;
}
console.log(howSum(300, [2, 5]))

