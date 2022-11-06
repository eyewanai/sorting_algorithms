import random


def bubble_sort(array: list) -> list:
  for i in range(len(array)):
    for j in range(i+1, len(array)):
      if array[i] > array[j]:
        array[i], array[j] = array[j], array[i]
  return array

for i in range(100):
  array = [random.randint(-1000,1000) for _ in range(100)]
  assert bubble_sort(array) == sorted(array)

