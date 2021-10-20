#meme commands

@client.command(name='pak') async def version(context): print("Done") myEmbed = discord.Embed(title='HAPPY INDEPENDENCE DAY 🎉🎆',Color=0x00cc00) myEmbed.set_image(url="https://cdn.dribbble.com/users/1592949/screenshots/3696709/flag-of-pakistan.gif") myEmbed.add_field(name='Quotes',value='"There is no power on Earth that can undo Pakistan"-Quaid e Azam',inline=False) myEmbed.add_field(name='•',value='"Faith,Unity & Discipline"-Quaid e Azam',inline=False) myEmbed.add_field(name='•',value='"I do not believe in taking the right decision, I take a decision and make it right"-Quaid e Azam',inline=False) myEmbed.add_field(name='•',value='"The ultimate aim of the ego is not to see something, but to be something"-Allama Iqbal',inline=False)

await context.message.channel.send(embed=myEmbed)
@client.command(name='meme') async def meme(ctx): async with aiohttp.ClientSession() as cs: async with cs.get("https://www.reddit.com/r/memes.json") as r: memes = await r.json() myEmbed = discord.Embed( color= discord.Colour.purple() ) myEmbed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"]) myEmbed.set_footer(text="Powered By Qari Enterprises! ") await ctx.send(embed=myEmbed)

@client.command(pass_context=True) async def best(ctx, member: discord.Member=None): user = random.choice(ctx.guild.members) await ctx.send(f'{user.mention} is the best player')

@client.command(name='hello', help='Returns random welcome message') async def hello(ctx): responses = ['Idiot Why did you interrupted in my technical analysis?', 'Wassup!!!', 'What labour do you want me to execute?', 'NIGGA!,WHY TF YOU WOKE ME UP?', "Yes My beautiful human being","" ] await ctx.send(choice(responses))

#Bot entry in vc @client.command(pass_content = True, help='Makes Xynox join vc') async def vc(ctx): if (ctx.author.voice): channel = ctx.message.author.voice.channel await channel.connect() else: await ctx.send("Join a Voice Channel Dumb!")

@client.command(pass_context = True,help='Makes Xynox join vc') async def dc(ctx): if (ctx.voice_client): await ctx.guild.voice_client.disconnect() await ctx.send("I left the Voice Channel") else: await ctx.send("I am not in a voice channel")
