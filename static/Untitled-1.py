
import discord
from discord.ext import commands
import google.generativeai as genai

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True  
intents.message_content = True  

bot = commands.Bot(command_prefix='/', intents=intents)

genai.configure(api_key="AIzaSyC1yUEgZuCDQRX2CFrv_v4bSUIJ9Jv1zjY")

# Set up the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                             generation_config=generation_config,
                             safety_settings=safety_settings)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command()
async def generate(ctx, *, prompt: commands.clean_content):
    try:
        response = model.generate_content([prompt])
        if response.parts: 
            await ctx.send(response.text)
        else:
            await ctx.send("Sorry, I couldn't generate a response for that prompt.")
    except Exception as e:
        print(e)
        await ctx.send("An error occurred while generating the response.")


bot.run('MTIxMDk4MTE0MjczNjY3MDc5MA.G1IHky.FqEfJF_a5qDAdhd7FEyzBcqMmYkjYQoTzAniVM')
