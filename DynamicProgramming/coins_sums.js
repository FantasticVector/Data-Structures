// This problem is taken from project euler 31
const coinSums = (targetSum, coins, memo={}) => {
  if (targetSum in memo) return memo[targetSum]
  if (targetSum === 0) return 1
  if (targetSum < 0) return 0
  var result = 0
  for (let coin of coins) {
    const remainder = targetSum - coin
    const ways = coinSums(remainder, coins, memo)
    result+=ways
  }
  memo[targetSum] = result
  return result
}

console.log(coinSums(200, [1, 2, 5, 10, 20, 50, 100, 200]))