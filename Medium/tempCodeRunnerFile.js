   function swap(a, b) {
      let swapArr = nums;
      let temp = nums[a];
      swapArr[a] = swapArr[b];
      swapArr[b] = temp;
      return swapArr;
    }