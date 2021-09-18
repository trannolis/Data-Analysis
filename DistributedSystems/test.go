package main

import ("fmt"
        "os"
        "bufio"
        "errors")

type Person struct {
    Name string
    Age int
    Friends []*Person
}

func (self *Person) IsTooOld() bool {
    return self.Age > 60
}

func addOne(x int) int {
    return x+1
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

func main() {
    var z string
    z = "whatever"
    y := "something"
    // y := "new variable" -- error
    //me := Person{Name:"Bob Smith", Age:99}

    somelist := []int{1,2,3,4}
    somelist = append(somelist, 5)

    mydict := map[string]int{}
    mydict["five"] = 5
    result, ok := mydict["four"]
    if ok {
        fmt.Println("Found ", result)
    } else {
        fmt.Println("Not found")
    }


    fmt.Println(z)
    fmt.Println(addOne(99))
    fmt.Println(y)

    fmt.Println(somelist)

    anotherlist := []string{"A","B","C"}

    for idx, item := range anotherlist {
        fmt.Println(idx, item)
    }

    x := 0
    for x < 5 {
        fmt.Println(x)
        x++
    }

/*    for {
        fmt.Println("Hi")
    }
*/
}