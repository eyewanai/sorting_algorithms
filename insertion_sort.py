import random

def insert_sort(array: list) -> list:
  for i in range(1, len(array)):
    value = array[i]
    j = i - 1
    while j >= 0 and array[j] > value:
      array[j+1] = array[j]
      j-=1
    array[j+1] = value
  return array


for i in range(1):
  _array = [random.randint(-1000,1000) for _ in range(10)]
  print(_array)
  assert insert_sort(_array) == sorted(_array), f"Comb sort: {insert_sort(_array)} != Sorted {sorted(_array)}"
  print(_array)