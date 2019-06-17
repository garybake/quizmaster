package main

import (
	"net/http"
	"log"
	"io/ioutil"
	"os"
)

func main() {
	MakeRequest()
}

func MakeRequest() {
	url := os.Args[1]

	resp, err := http.Get(url)
	if err != nil {
		log.Fatalln(err)
	}

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
	}

	log.Println(string(body))
}