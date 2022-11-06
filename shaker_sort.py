import random


def shaker_sort(array: list) -> list:
  swapped = True
  while swapped:
    swapped = False
    for i in range(len(array)-2):
      if array[i] > array[i+1]:
        array[i], array[i+1] = array[i+1], array[i]
        swapped = True

    if swapped == False:
      break

    swapped = False
    for i in range(len(array)-2, 0, -1):
      if array[i] > array[i+1]:
        array[i], array[i+1] = array[i+1], array[i]
        swapped = True
  return array

for i in range(10):
  _array = [random.randint(-1000,1000) for _ in range(100)]
  assert shaker_sort(_array) == sorted(_array), f"Shaker sort: {shaker_sort(_array)} != Sorted {sorted(_array)}"