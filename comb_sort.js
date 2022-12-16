const array = [1,2,-10,423,0,0,-143];

function comb_sort(array) {
  gap = array.length;
  swap = true;
  while (gap > 1 || swap) {
    gap = Number(gap / 1.247);
    if (gap < 1) gap = 1;
    swap = false;
    for (i=0;i<array.length-gap; i++) {
      if (array[i] > array[i+gap]) {
        [array[i], array[i+gap]] = [array[i+gap], array[i]];
        swap = true;
      }
    }
  }
  return array;
}

console.log(...comb_sort(array));