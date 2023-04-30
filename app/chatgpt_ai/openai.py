from dotenv import load_dotenv
import openai
import os
import random


load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')

def chatgpt_response(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Make sure to use an existing model like "text-davinci-002"
            messages=messages,
            temperature=1,
            # max_tokens=100
        )
        response_dict = response.get("choices")

        if response_dict and len(response_dict) > 0:
            messages.append({'role': response_dict[0]["message"].role, 'content':response_dict[0]["message"].content})

    except openai.OpenAIError as e:
        print(f"Error during API call: {e}")
        # Handle the exception, or return an appropriate error message

    return messages


def dalle_response(prompt):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        ) 
        response_dict = response.get("data")
        return response_dict[0].url
    except:
        im = ['https://media.tenor.com/3p5KHNlNpVYAAAAC/flip-off.gif', 
              'https://media.tenor.com/tP0M0uP3apQAAAAd/no-fuck-off-fuck-off.gif',
              'https://media.tenor.com/Jns9XX2xpKsAAAAM/fuck-fuck-off.gif',
              'https://media.tenor.com/FzEjMu4P5fIAAAAM/middle-finger-fuck-off.gif', 
              'https://media.tenor.com/8gpOOFO31fgAAAAM/fuck-off-go-away.gif',
              'https://media.makeameme.org/created/nope-try-again-845dad4218.jpg',
              'https://media.tenor.com/Ovl6WVOhOSMAAAAM/try-again.gif',
              'https://media.tenor.com/1OK2Woyhz-AAAAAM/try-again-never-again.gif',
              'https://media.tenor.com/-wsLV6WhY-QAAAAC/try-again-keegan-michael-key.gif'
              ]
        random_int = random.randint(0, 8)
        return im[random_int]

        