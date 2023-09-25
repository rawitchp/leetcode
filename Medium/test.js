var characterReplacement = function (s, k) {
  let hashMap = { else: 0 };
  let start = 0;
  let max = 1;
  for (let end = 0; end < s.length; end++) {
    if (hashMap[s[end]] >= 0 && s[end] === s[start]) {
      hashMap[s[end]] = hashMap[s[end]] + 1;
    } else if (s[end] !== s[start]) {
      if (hashMap[`else`] === k || end === s.length - 1) {
        max > end - start + 1 ? null : (max = end - start + 1);
        console.log(max);
        hashMap[`else`] === 0;
      }
      hashMap[`else`]++;
    } else {
      hashMap[s[end]] = 1;
    }
  }
  return max;
};
characterReplacement('ABAB', 2);
