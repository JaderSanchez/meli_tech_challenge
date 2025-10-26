# Problem

Create a Go command-line application that summarizes the contents of a text file using a free, public GenAI API (such as HuggingFace Inference API or any other public endpoint).

## Requirements

- The CLI must be written in Go.

- The CLI must accept:
  - `--input` or a `positional argument`: path to the text file to summarize.

  - `--type` or `-t` : summary type, one of short, medium , or bullet.

- The CLI must call a free, public GenAI API for summarization (e.g., HuggingFace Inference API).

- The prompt sent to the API should be engineered to match the summary type:
  - **short**: a concise summary (1-2 sentences)
  - **medium** : a paragraph summary
  - **bullet** : a list of bullet points

- The CLI should output the summary to `stdout`.

- The CLI should handle API errors gracefully and print user-friendly messages.

- Document the Go version used in your code comments.

## Functionality Example

`go run solution_summarizer.go --input article.txt --type bullet`

or

`go run solution_summarizer.go -t short article.txt`

## Sample Output

```
- Point 1: ...
- Point 2: ...
- Point 3: ...
```

or 

`This article discusses ...`

## Evaluation Criteria

- Correctness of CLI argument parsing.

- Proper use of Go HTTP client for API calls.

- Prompt engineering: how the summary type is reflected in the prompt.

- Error handling and code clarity.

- Documentation/comments in the code.

## API Suggestions

You may use the HuggingFace Inference API (free tier, no key required for some models) or any other public GenAI summarization endpoint.

Provide a link to the API documentation in your code comments.

## How I'll solve it

1. Get and validate args from CLI.

2. Verify file exists.

3. Read file content.

4. According to the selected summarize type, generate instructions for the prompt.

5. Make a request to the AI API sending file content and summarize instructions.

6. Print summarize result in `stdout` (console).
