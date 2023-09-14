/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function (nums) {
  let ans = [];
  let arr = [];
  function recursion(nums, i, arr) {
    if (i === nums.length) {
      ans.push(arr);
      return;
    }
    recursion(nums, i + 1, arr);
    recursion(nums, i + 1, [...arr, nums[i]]);
  }
  recursion(nums, 0, arr);
  return ans;
};
