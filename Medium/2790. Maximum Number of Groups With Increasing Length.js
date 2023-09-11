/**
 * @param {number[]} groupSizes
 * @return {number[][]}
 */
var groupThePeople = function (groupSizes) {
  let ans = [];
  let hashMap = {};
  groupSizes.map((num, i) => {
    console.log(hashMap[num]);
    hashMap.hasOwnProperty(num) ? hashMap[num].push(i) : (hashMap[num] = [i]);
    if (hashMap[num].length == num) {
      ans.push(hashMap[num]);
      hashMap[num] = [];
    }
  });
  return ans;
};
