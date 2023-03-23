from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')





def chatgpt_response(messages):
    response = openai.ChatCompletion.create (
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=100
    )

    response_dict = response.get("choices")
    if response_dict and len(response_dict) > 0:
        messages.append({'role': response_dict[0]["message"].role, 'content':response_dict[0]["message"].content})

    return messages