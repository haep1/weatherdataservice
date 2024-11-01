from openai import OpenAI
client = OpenAI()

def start_chat(chat):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": chat
            }
        ]
    )
    print(completion.choices[0].message)
    return completion.choices[0].message