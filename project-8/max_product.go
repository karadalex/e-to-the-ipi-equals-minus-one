package main

import (
	"fmt"
)

func findMaxProduct(num string, r int) int {
	maxProduct := 0
	for i := 0; i < len(num); i++ {
		product := 1
		for j := 0; j < r; j++ {
			product = product * num[j]
		}
		if product > maxProduct {
			maxProduct = product
		}
	}
	return maxProduct
}

func main() {
	fmt.Println(findMaxProduct("123456789", 4))
}