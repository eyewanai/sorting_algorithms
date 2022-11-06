package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main(){
	array := createRandArray(10)
	fmt.Println("Unsorted", array)
	sorted_array := bubbleSort(array)
	fmt.Println("Sorted", sorted_array)
}


func bubbleSort(array []int) []int {
	for i := 0; i < len(array); i++ {
		for j := i+1; j < len(array); j++ {
			if array[i] > array[j] {
				array[i], array[j] = array[j], array[i]
			}
		}
	}
	return array
}

func createRandArray(size int) []int {
	var array []int
	rand.Seed(time.Now().UnixNano())
	for i := 0; i<size+1; i++ {
		randint := -100 + rand.Intn(200) 
		array = append(array, randint)
	}
	return array
}