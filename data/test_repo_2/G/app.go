package main

import "fmt"

func main() {
	fmt.Println(doSum(1, 2))
	fmt.Println(doMultiply(3, 4))
	fmt.Println(doMinus(5, 6))
}

func doSum(a int, b int) int {
	return a + b
}

func doMultiply(a int, b int) int {
	return a * b
}

func doMinus(a int, b int) int {
	return a - b
}
