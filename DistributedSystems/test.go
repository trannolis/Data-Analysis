// Go Tutorial
// September 13, 2021
// Distributed Systems

func readFirstLine(filename string) (string, error) {
	F, err := os.Open(filename)
	If err != nill {
		return "", err
	}
	defer f.Close() // this will close the file as soon as the function closes. 
					// It gets called as part of the return. 
					// Multiple Defers: opposite order of what they were called
	scanner := bufio.NewScanner(f)
	if scanner.Scan() {
		return scanner.Text(), nil
	} else {
		Return "", errors.New("File probably empty")
	}
}


