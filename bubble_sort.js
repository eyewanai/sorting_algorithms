const array = [1,2,-10,423,0,0,-143];

function sort(array) {
  for (i=0; i<array.length; i++) {
    for (j=i+1; j<array.length; j++) {
      if (array[i] > array[j]) {
        [array[i], array[j]] = [array[j], array[i]];
      }
    }
  }
  return array;
}

console.log(...sort(array));