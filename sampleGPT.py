import logging
import os
import openai


if __name__ == '__main__':
    openai.api_key = os.getenv('chat-gpt-sandbox')

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}
        ]
    )

    print(completion.choices[0].message.content)


