# Discord Chatbot with OpenAI

The chatbot can respond to messages starting with '!ai', '!bot', or '!gpt' with chatbot responses generated by OpenAI's GPT-3.5 model. The bot also has the ability to generate images using OpenAI's DALL-E model in response to messages starting with '!image'. The conversation history is saved and can be continued across multiple messages.


## Getting Started

1. Clone this repository and navigate to the project directory.
2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a .env file in the root directory and add your Discord bot token:
    ```
    DISCORD_TOKEN=your_token_here
    CHATGPT_API_KEY=your_token_here
    ```

4. Start the bot by running 'python run.py' in the terminal.

# Usage

Once the bot is running, you can start messaging it on Discord. The bot will respond to messages starting with '!ai', '!bot', or '!gpt' with chatbot responses generated by OpenAI's GPT-3 model. The conversation history is saved and can be continued across multiple messages. You can start a new conversation with the bot by sending the message '!session'.

The bot can also generate images using OpenAI's DALL-E model in response to messages starting with ```!image```. Simply send a message starting with '!image' followed by a description of the image you want to generate.
