function maxSubArray(nums: number[]): number {
  let min;
  let dp = [0];
  let result;
  for (let i = 0; i < nums.length; i++) {
    let temp = 0;
    if (i === 0) {
      temp = nums[0];
      result = nums[0];
      min = 0;
    } else temp = dp[i] + nums[i];
    dp.push(temp);
    if (temp - min > result) result = temp - min;
    if (temp < min) {
      min = temp;
    }
  }
  return result;
}
