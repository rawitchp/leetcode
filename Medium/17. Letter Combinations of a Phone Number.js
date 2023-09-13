/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function (digits) {
  let hashMap = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
  };
  if (digits.length == 0) {
    return [];
  }
  function combine(ans, str) {
    let arr = [];
    ans.map((item) => {
      for (let j = 0; j < hashMap[str].length; j++) {
        arr.push(item + hashMap[str][j]);
      }
    });
    return arr;
  }
  let ans = [];
  for (let j = 0; j < hashMap[`${digits[0]}`].length; j++) {
    ans.push(hashMap[`${digits[0]}`][j]);
  }
  for (let i = 1; i < digits.length; i++) {
    ans = combine(ans, digits[i]);
  }
  return ans;
};
