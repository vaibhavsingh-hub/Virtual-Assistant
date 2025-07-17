# pip insatll openAI
from openai import OpenAI

client = OpenAI(
    api_key  = "Your API key"
)

completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a smart virtual assistant named Jarvis, skilled in general tasks like Alexa and Google"},
        {"role": "user", "content" : "what is programming?"}
    ]
)

print(completion.choices[0].message.content)