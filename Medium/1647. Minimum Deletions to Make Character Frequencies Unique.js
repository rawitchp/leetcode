/**
 * @param {string} s
 * @return {number}
 */
var minDeletions = function (s) {
  if (s.length < 2) {
    return 0;
  }
  let hashMap = {};
  let charArr = [];
  for (let i = 0; i < s.length; i++) {
    hashMap[s[i]] ? (hashMap[s[i]] = hashMap[s[i]] + 1) : (hashMap[s[i]] = 1);
    if (!charArr.includes(s[i])) {
      charArr.push(s[i]);
    }
  }
  let countChar = [];
  let countAction = 0;
  charArr.map((char) => {
    while (check(char)) {
      if (hashMap[char] === 0) {
        continue;
      }
      countAction = countAction + 1;
      hashMap[char] = hashMap[char] - 1;
    }
    if (hashMap[char] !== 0) {
      countChar.push(hashMap[char]);
    }
  });
  function check(char) {
    if (countChar.includes(hashMap[char])) {
      console.log(char);
      return true;
    }
    return false;
  }
  return countAction;
};
