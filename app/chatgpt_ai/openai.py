from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')





def chatgpt_response(prompt):
    conversation = []
    conversation.append({'role': 'system', 'content': 'You are an advanced assistant. Your job is to answer the user question as short and concise as possible. Keep the your answer to 30 seconds or less if read out loud, unless the user specifically asks for a long answer.'})
    conversation.append ({'role':'user', 'content': prompt})
    messages = conversation
    response = openai.ChatCompletion.create (
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=100
    )

    response_dict = response.get("choices")
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0]["message"].content

    return prompt_response