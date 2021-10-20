#Audio Commands @client.command(pass_context = True,help='Makes Xynox pause the music') async def pause(ctx): voice = discord.utils.get(client.voice_clients,guild=ctx.guild) if voice.is_playing(): voice.pause() else: await ctx.send("At the moment,no music is being played in the voice channel")

@client.command(pass_context = True,help='Makes Xynox resume the music') async def resume(ctx): voice = discord.utils.get(client.voice_clients,guild=ctx.guild) if voice.is_paused(): voice.resume() else: await ctx.send("At the moment,no song is paused!")

@client.command(pass_context = True,help='Makes Xynox stop the music') async def stop(ctx): voice = discord.utils.get(client.voice_clients,guild=ctx.guild) voice.stop()

@client.command(pass_context = True, aliases=['n', 'nex'],help='Makes Xynox skip the music') async def next(ctx): voice = discord.utils.get(client.voice_clients,guild=ctx.guild)

if voice and voice.is_playing():
    print("Playing next song")
    voice.stop()
    await ctx.send("Next song")
else:
    print("No Music playing Failed to play next song")
    await ctx.send("No Music playing Failed")
#YT files @client.command(pass_context=True, aliases=['pl','pla']) async def plays(ctx, url:str): song_there= os.path.isfile("song.mp3") try: if song_there: os.remove("song.mp3") print("removed old song file") except PermissionError: print("Trying to delete song file, but it's being played") await ctx.send("ERROR: Music playing") return await ctx.send("Getting everything ready now")

voice = get(client.voice_clients, guild=ctx.guild)

ydl_opta = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
    }],
}
try:
    with youtube_dl.YoutubeDL(ydl_opta) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])
except:
    print("FALLBACK: youtube_dl does not support this url,using spotify(This is normal if Spotify URL")
    c_path = os.path.dirname(os.path.realpath(__file__))
    system("spotdl -f " + '"' + c_path + '"' + " -s " + url)

for file in os.listdir("./"):
    if file.endswith(".mp3"):
        name=file
        print(f"Renamed File: {file}\n")
        os.rename(file, "song.mp3")

voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print(f"{name} has finished playing"))
voice.source = discord.PCMVolumeTransformer(voice.source)
voice.source.volume = 0.07

nname = name.rsplit("-", 2)
await ctx.send(f"Playing: {nname[0]}")
#Queue files @client.command(pass_content=True,help='Queues songs') async def queue(ctx, arg): voice = ctx.guild.voice_client song = arg + '.wav' source = FFmpegPCMAudio(song)

guild_id = ctx.message.guild.id

if guild_id in queues:
    queues[guild_id].append(source)

else:
    queues[guild_id] = [source]

await ctx.send("Added to queue")
