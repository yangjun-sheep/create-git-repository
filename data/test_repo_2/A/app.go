package main

import "fmt"

func main() {
	fmt.Println(sum(1, 2))
}

func sum(a uint, b uint) int {
	var v int = 0
	var i uint = 0
	for i = 0; i < a; i++ {
		v += 1
	}
	for i = 0; i < b; i++ {
		v += 1
	}
	return v
}
