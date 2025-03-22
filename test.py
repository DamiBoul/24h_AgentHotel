from lang.ChatInstance import ChatInstance

chat = ChatInstance(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)


result = chat.ask(
    {
        "input_language": "English",
        "output_language": "German",
        "input": "I love programming.",
    }
)

print(result.content)
