import random

def insert_sort(array: list) -> list:
  for i in range(1, len(array)):
    j = i - 1
    while j >= 0 and array[j] > array[i]:
      array[j+1] = array[j]
      j-=1
    array[j+1] = array[i]
  return array


for i in range(10):
  _array = [random.randint(-1000,1000) for _ in range(10)]
  assert insert_sort(_array) == sorted(_array), f"Comb sort: {insert_sort(_array)} != Sorted {sorted(_array)}"