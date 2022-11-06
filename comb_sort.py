import random

def comb_sort(array: list) -> list:
  gap = len(array)
  swap = True
  while gap > 1 or swap:
    gap = int(gap // 1.247)
    if gap < 1: gap = 1
    swap = False
    for i in range(len(array)-gap):
      if array[i] > array[i+gap]:
        array[i], array[i+gap] = array[i+gap], array[i]
        swap = True
  return array



for i in range(10):
  _array = [random.randint(-1000,1000) for _ in range(1000)]
  assert comb_sort(_array) == sorted(_array), f"Comb sort: {comb_sort(_array)} != Sorted {sorted(_array)}"