const changeMaking = (target, coins, memo={}) =>  {
  if (target in memo) return memo[target]
  if (target === 0) return [[]]
  if (target < 0) return null
  const result = []
  for (let coin of coins) {
    const remainder = target - coin
    const combinationWays = changeMaking(remainder, coins, memo)
    if (combinationWays !== null) {
      const targetWays = combinationWays.map(way => [...way, coin]) 
      result.push(...targetWays)
    }
  }
  memo[target] = result
  return result
}


console.log(changeMaking(200, [1, 2, 5, 10]))