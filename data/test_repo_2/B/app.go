package main

import "fmt"

func main() {
	fmt.Println(sum(1, 2))
}

func sum(a uint, b uint) int {
	return int(a + b)
}
