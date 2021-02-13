import discord
import time
from snscrape.modules.twitter import TwitterSearchScraper
from datetime import date, timedelta
import envVariable as env

TOKEN = env.TOKEN

client = discord.Client()

@client.event
async def on_ready():
    exist_tweet_id = []
    print('We have logged in as {0.user}'.format(client))
    
    for guild in client.guilds:
        await guild.text_channels[0].send("Hi I'm Elon Musk Dogecoin bot back to ready state now!")
    
    while(True):
        print("Checking Elon Musk Tweet!")
        today = date.today()
        yesterday = today - timedelta(days=1)
        query = 'from:elonmusk since:'+str(yesterday)
        tweets = TwitterSearchScraper(query).get_items()
        for i, tweet in enumerate(tweets):
            if i > 10:
                break
            content = tweet.content
            tweet_id = tweet.id
            if ('doge' in content.lower() and tweet_id not in exist_tweet_id):
                print(content)
                print(tweet_id)
                print('=============================================================')
                exist_tweet_id.append(tweet_id)
                await client.guilds[0].text_channels[0].send("Seem like this tweet involve with Dogecoin check it out! @everyone\n"+str(tweet))
        
        print("Checking Elon Musk Tweet Done sleeping for 60 second")
        time.sleep(60)
            
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

if __name__ == '__main__':
    client.run(TOKEN)
