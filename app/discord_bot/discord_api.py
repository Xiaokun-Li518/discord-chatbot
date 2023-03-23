from dotenv import load_dotenv
import discord
import os
from pyrandmeme import *
from pyjokes import get_joke

from memeMaker import makeMeme


from app.chatgpt_ai.openai import chatgpt_response, dalle_response

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    conversation = [{'role': 'system', 'content': 'answer the question as short and concise as possible.'}]
    async def on_ready(self):
        print ("Succcessfull logged in as: ", self.user)

    async def on_message (self, message):
        print (message.content)
        if message.author == self.user:
            return
        command, user_message = None, None
        for text in ['!ai', '!bot', '!gpt', '!session', '!image', '!meme', '!joke']:
            if message.content.startswith(text):
                arr = message.content.split(' ');
                command=arr[0]
                user_message=' '.join(arr[1:])
                print(user_message)

        if command == '!ai' or command == '!bot' or command == '!gpt':
            MyClient.conversation.append({'role':'user', 'content':user_message})
            MyClient.conversation = chatgpt_response(messages=MyClient.conversation)
            await message.channel.send(f"{MyClient.conversation[-1]['content']}")
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


        