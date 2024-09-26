import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def ask_gpt(question):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question},
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"
