import asyncio
from dotenv import load_dotenv
import discord
import os
from pyrandmeme import *
from pyjokes import get_joke



from app.chatgpt_ai.openai import chatgpt_response, dalle_response

load_dotenv()

idea_lock = asyncio.Lock()
discord_token = os.getenv('DISCORD_TOKEN')

async def get_idea():
    suggest_image = [{'role': 'system', 'content': 'come up with an idea for a painting'}]
    suggest_image = chatgpt_response(messages=suggest_image)
    idea = suggest_image[-1]['content']

    async with idea_lock:
        dalle_res = dalle_response(idea)
        return (idea, dalle_res)

class MyClient(discord.Client):
    conversation = [{'role': 'system', 'content': 'answer the question as short and concise as possible.'}]
    async def on_ready(self):
        print ("Succcessfull logged in as: ", self.user)
    

    async def on_message (self, message):
        print (message.content)
        print (message.author)
        author = ''
        author += str(message.author)
        if message.author == self.user:
            return
        # elif author == 'Xiaokun_Li#7031':
        #     await message.channel.send('Please shut the fuck up!!')

        command, user_message = None, None
        for text in ['!ai', '!bot', '!gpt', '!session', '!image', '!meme', '!joke', '!usage', '!lucky']:
            if message.content.startswith(text):
                arr = message.content.split(' ');
                command=arr[0]
                user_message=' '.join(arr[1:])
                print(user_message)

        if command == '!ai' or command == '!bot' or command == '!gpt':
            MyClient.conversation.append({'role':'user', 'content':user_message})
            MyClient.conversation = chatgpt_response(messages=MyClient.conversation)
            await message.channel.send(f"{MyClient.conversation[-1]['content']}")
        elif command == '!lucky':
            idea, dalle_res = await get_idea()
            await message.channel.send(f'{dalle_res}')
            await message.channel.send(f'{idea}')

        elif command == '!usage':
            await message.channel.send(f"The bot will respond to messages starting with `!ai`, `!bot`, or `!gpt` with chatbot responses generated by OpenAI's GPT-3.5 model.You can start a new conversation with the bot by sending the message `!session`.The bot can also generate images using OpenAI's DALL-E model. Simply send a message starting with `!image` followed by a description of the image you want to generate. `!meme` to get a random meme. `!joke` to a random joke about programming. ") 
        elif command == '!session':
            MyClient.conversation = [{'role': 'system', 'content': 'answer the question as short and concise as possible.'}]
            MyClient.conversation.append({'role':'user', 'content':user_message})
            MyClient.conversation = chatgpt_response(messages=MyClient.conversation)
            await message.channel.send(f"{MyClient.conversation[-1]['content']}")
        elif command == '!image':
            dalle_res = dalle_response(user_message)
            await message.channel.send(f"{dalle_res}")
        elif command == '!meme':
            await message.channel.send(embed=await pyrandmeme())
        elif command == '!joke':
            await message.channel.send(get_joke())


intents = discord.Intents.default()
intents.message_content=True

client = MyClient(intents=intents)


        