#Change Custom Status

@client.event async def on_ready(): # Setting 'Playing' Status await client.change_presence(activity=discord.Game(name="on {len(client.guilds)} servers | $help"))

    # Setting 'Streaming' Status
    await client.change_presence(activity=discord.Streaming(name="My Stream", url="my_youtube_url"))

    # Setting 'Listening' Status
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name="Havanna"))

    # Setting 'Watching' Status 
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name="over the mods"))

    print=("Ready")
async def change_presence(): await client.wait_until_ready()

statuses = ["Cyberpunk 2077", f"on {len(client.guilds)} servers | %help", "discord.py"]

while not client.is_closed():

    status = random.choice(statuses)

    await client.change_presence(activity=discord.Game(name=status))

    await asyncio.sleep(10)
client.loop.create_task(change_presence())
