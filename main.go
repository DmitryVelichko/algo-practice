package main

import (
	"fmt"
	"reflect"
	"strconv"
)

func main() {
	a := "5000"
	b := strconv.atoi(a)
	fmt.Println(b)
}
