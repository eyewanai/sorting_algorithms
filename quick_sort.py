import random

def quick_sort(array: list) -> list:
  less, greater, pivots = [], [], []
  if len(array) <= 1:
    return array
  pivot = array[0]
  for el in array:
    if el < pivot: less.append(el)
    elif el > pivot: greater.append(el)
    else: pivots.append(pivot)
  less = quick_sort(less)
  greater = quick_sort(greater)
  return less + pivots + greater



for i in range(1):
  _array = [random.randint(-1000,1000) for _ in range(10)]
  assert quick_sort(_array) == sorted(_array), f"Comb sort: {quick_sort(_array)} != Sorted {sorted(_array)}"