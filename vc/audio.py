#Audio Files Join @client.command(pass_content = True,help='Makes Xynox join vc and play the beat') async def join(ctx): if (ctx.author.voice): channel = ctx.message.author.voice.channel voice = await channel.connect() source = FFmpegPCMAudio('ex.wav') player = voice.play(source)

else:
    await ctx.send("Join a Voice Channel Dumb!")
