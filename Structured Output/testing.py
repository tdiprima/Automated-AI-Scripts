from ollama import chat

response = chat(
    model='llama3.2',
    messages=[
        {'role': 'user', 'content': 'Hello! Who are you?'}
    ]
)

print(response['message']['content'])
