import openai

openai.api_key = ""

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-4.0-turbo",
        messages = [{"role": "user", "content": prompt}]
    )