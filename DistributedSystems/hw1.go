// Nick Tran
// Distributed Systems - Fall 2021
// Homework 1

package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
)

type Movie struct {
	Name   string
	Actors []*Person
}

type Person struct {
	// this struct will store the name, movie that the Person was in
	Name   string
	Movies []*Movie
}

func readFirstLine(filename string) (string, error) {
	f, err := os.Open(filename)
	if err != nil {
		return "", err
	}
	defer f.Close()
	scanner := bufio.NewScanner(f)
	if scanner.Scan() {
		return scanner.Text(), nil
	} else {
		return "", errors.New("File probably empty")
	}
}

//some graph traversal algorithm
func main() {

	// we need to make the adjacency list for the data
	// we also need to keep track of the movies using a map
	// then, we need to be able to pass an actor string arguement from the scanner
	// into the map to get the actor's struct which carries it's own adjacency list to see the movies that it is within
	// we parse through that adjacency list and check for

	somelist := []int{1, 2, 3, 4}
	somelist = append(somelist, 5)

	mydict := map[string]int{}
	mydict["five"] = 5
	result, ok := mydict["four"]
	if ok {
		fmt.Println("Found ", result)
	} else {
		fmt.Println("Not found")
	}
}
