import pyowm
import pyttsx3
import time

var1=0
var2=20
var3=-20

bot = commands.Bot(command_prefix='')
@bot.event
async def on_ready():
print ("Bot is ready to work")

await bot.change_presence (status= discord.Status.online, activity = discord.Game('Google Chrome'))

TOKEN = 'NzA2MzkxMjQ0MDAzMjEzMzIy.XtzZEQ.JUhffFVwFPXkjdU-XFkGr1NzAU0'
owm=pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc')
engine = pyttsx3.init()

@bot.command(pass_context=True)
async def Hello (ctx):
await ctx.send("Hello my friend!")
engine.say ("Hello my friend!")
engine.runAndWait()
@bot.command(pass_context=True)
async def Погода (ctx, city):
observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature = w.get_temperature('celsius')['temp']
await ctx.send("In the "+city+ " temperature "+str(temperature)+" on Celsius")
engine.say("In the"+ "temperature"+str(temperature)+"on Celsius")
if str(temperature)>=str(var1) and str(temperature)<str(var2):
await ctx.send("It's warm today")
engine.say("It's warm today")
if str(temperature)<str(var1) and str (temperature)>str(var3):
await ctx.send("It's cold today")
engine.say("It's cold today")
if str(temperature)<=str(var3):
await ctx.send("It's freezing outside, put on some warm clothes")
engine.say("It's freezing outside, put on some warm clothes")
if str(temperature)>=str(var2):
await ctx.send("it's hot outside, go to the beach")
engine.say("it's hot outside, go to the beach")

engine.runAndWait()

bot.run(TOKEN)
