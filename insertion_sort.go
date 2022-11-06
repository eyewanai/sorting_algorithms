package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	array := createRandArray(10)
	fmt.Println("Unsorted", array)
	fmt.Println("Sorted", insertSort(array))
}

func insertSort(array []int) []int {
	for i := 1; i < len(array); i++ {
		value := array[i]
		j := i - 1
		for j >= 0 && array[j] > value {
			array[j+1] = array[j]
			j = j - 1
		}
		array[j+1] = value
	}
	return array
}

func createRandArray(size int) []int {
	var array []int
	rand.Seed(time.Now().UnixNano())
	for i := 0; i < size+1; i++ {
		randint := -100 + rand.Intn(200)
		array = append(array, randint)
	}
	return array
}
