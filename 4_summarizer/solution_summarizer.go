// GO version: 1.25.3

package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"slices"
	"strings"

	"github.com/go-resty/resty/v2"
)

func getSummarize(filePath string, summarizeType string) string {

	fileContent := getFileContent(filePath)
	summarizeInstructions := getSummarizeInstructions(summarizeType)

	return generateSummarize(summarizeInstructions + fileContent)

}

func getFileContent(filePath string) string {

	content, err := os.ReadFile(filePath)

	if err != nil {
		log.Fatalf("Error reading file %s: %v", filePath, err)
	}

	return string(content)

}

func getSummarizeInstructions(summarizeType string) string {
	switch summarizeType {
	case "short":
		return "Provide a concise super short summary of the following text (in the same language of the text) in 1-2 sentences only. Be brief and capture only the main idea:\n\n"
	case "medium":
		return "Summarize (in the same language of the text) the following text in exactly a single, clear, and complete paragraph. Include key points and important details:\n\n"
	case "bullet":
		return "Summarize (in the same language of the text) the following text as a list of bullet points. Each bullet point should highlight a key fact or important detail. Format each point starting with a dash (-):\n\n"
	default:
		return "Summarize (in the same language of the text) the following text:\n\n"
	}
}

func generateSummarize(prompt string) string {

	// IMPORTANT: I know API KEYS should be in a .env file and should not be uploaded to the repository
	// But this API KEY wil,l be only available 5 days while the challenge is reviewed
	// Aditionally I couldn't found a public API that doesn't require an API KEY
	token := "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"

	client := resty.New()

	// Construct request body
	body := map[string]any{
		"messages": []map[string]string{
			{"role": "user", "content": prompt},
		},
		"model": "swiss-ai/Apertus-8B-Instruct-2509:publicai",
	}

	var result map[string]interface{}

	_, err := client.R().
		SetHeader("Authorization", "Bearer "+token).
		SetHeader("Content-Type", "application/json").
		SetBody(body).
		SetResult(&result).
		Post("https://router.huggingface.co/v1/chat/completions")

	if err != nil {
		log.Fatalf("Error sending request to IA: %v", err)
	}

	choices, ok := result["choices"].([]any)
	if !ok || len(choices) == 0 {
		log.Fatal("No message found in response")
	}

	firstChoice := choices[0].(map[string]any)
	message := firstChoice["message"].(map[string]any)
	content := message["content"].(string)

	return content

}

func main() {

	// ======================= Validate args =======================

	// Define arguments (flags)
	input := flag.String("input", "", "Path to .txt file to be summarized")
	typ := flag.String("type", "", "Type of summarize (short, medium, bullet)")

	// Define short alias for type argument
	flag.StringVar(typ, "t", "", "Alias for --type")

	// Parse arguments from CLI
	flag.Parse()

	// If input flag was not sent, and there are positional arguments
	// Then use first positional argument as input
	// flag will have preference, so if flag and positional were sent, positional will be ignored
	if strings.TrimSpace(*input) == "" && flag.NArg() > 0 {
		input = &flag.Args()[0]
	}

	// Verify arguments were sent
	if strings.TrimSpace(*input) == "" {
		fmt.Println("input argument is missing, you can set it with --input or as positional argument ")
		return
	}

	if strings.TrimSpace(*typ) == "" {
		fmt.Println("type argument is missing, you can set it with --type or -t")
		return
	}

	// Verify type is valid
	allowedTypes := []string{"short", "medium", "bullet"}

	if !slices.Contains(allowedTypes, *typ) {
		fmt.Println("invalid type value. Allowed types: short, medium, bullet")
		return
	}

	// Validate input is a .txt
	if !strings.HasSuffix(*input, ".txt") {
		fmt.Println("invalid input file. Input should be a path for a .txt file")
		return
	}

	// Validate input file exists in file system
	_, err := os.Stat(*input)

	if os.IsNotExist(err) {
		fmt.Printf("File %s doesn't exists", *input)
		return
	} else if err != nil {
		fmt.Println("Error validating file exists")
		return
	}

	// ======================= Get summarize =======================

	summmarize := getSummarize(*input, *typ)

	print(summmarize)

}
