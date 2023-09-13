/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let i = 0;
  let j = height.length - 1;
  let max = 0;
  function findArea(height_i, height_j, dis) {
    return height_i > height_j ? height_j * dis : height_i * dis;
  }
  for (let k = 0; k < height.length; k++) {
    let area = findArea(height[i], height[j], j - i);
    max = area > max ? area : max;
    height[i] > height[j] ? j-- : i++;
  }
  return max;
};
