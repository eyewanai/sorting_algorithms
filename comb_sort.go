package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	array := createRandArray(10)
	fmt.Println("Unsorted", array)
	fmt.Println("Sorted", combSort(array))
}

func combSort(array []int) []int {
	gap := len(array)
	swap := true
	for gap > 1 || swap == true {
		// gap = gap * 1247 / 1000
		gap = gap * 4 / 5
		if gap < 1 {
			gap = 1
		}
		swap = false
		for i := 0; i < len(array)-gap; i++ {
			if array[i] > array[i+gap] {
				array[i], array[i+gap] = array[i+gap], array[i]
				swap = true
			}
		}
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
