from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user",
         "content": "Write how is Shuaib, He is big fan of fortnite"}
    ]
)

print(response.choices[0].message.content)
