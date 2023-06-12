import openai

def main():
    # Set up OpenAI API credentials
    openai.api_key = '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'

    # Define your prompt
    prompt = "Write your prompt here"

    # Generate a completion using OpenAI's ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )

    # Extract the generated text from the response
    completion_text = response.choices[0].text.strip()

    # Process and use the generated completion as desired
    print(completion_text)

if __name__ == '__main__':
    main()

