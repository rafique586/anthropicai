from anthropic import Anthropic

client = Anthropic()

message = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    messages=[
        {"role": "user",
         "content": "Write how is Shuaib, He is big fan of fortnite"}
    ]
)

print(message.content[0].text)
