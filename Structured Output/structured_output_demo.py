from ollama import chat

# Gives a string of JSON
messages = [
    {"role": "user", "content": "Extract the title, author, and publication year from this text: 'The Great Gatsby by F. Scott Fitzgerald, published in 1925. Return in JSON format.'"}
]

# Gives tick marks and formats the JSON
# messages = [
#     {"role": "user", "content": "Please provide the result in JSON format with the fields: title, author, and publication_year. Text: 'The Great Gatsby by F. Scott Fitzgerald, published in 1925.'"}
# ]

# Call the chat function
response = chat(
    model="llama3.2",  # Replace with the specific model name you're using
    messages=messages
)

# Print the structured response
print(response["message"]["content"])
