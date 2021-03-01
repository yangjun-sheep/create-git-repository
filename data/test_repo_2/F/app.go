package main

import "fmt"

func main() {
	fmt.Println(doSum(1, 2))
	fmt.Println(doMultiply(3, 4))
}

func doSum(a int, b int) int {
	return a + b
}

func doMultiply(a int, b int) int {
	return a * b
}
