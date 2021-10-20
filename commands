#Ping @client.command(name='ping',help='Returns current ping') async def ping(ctx): await ctx.send(f'🏓Pong! {round(client.latency * 1000)}ms')

#Responses @client.command(aliases=['8ball', 'test'],help= 'Ask question which has positive/negative answer,test to counter it') async def eightball(ctx, *, question): responses = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes - Definitely.', 'As I see it, yes.', 'Most likely.', 'Yes.', 'Ask again later.', 'You dont wanna hear it.', 'Cant tell you right now', 'Cannot predict now', 'Obviously', 'Im Sorry', 'My research says no', 'Unfortunately! No!!!', 'Very Doubtful',] await ctx.send( random.choice(responses))

@client.command(name='clear',help='Clears x message') async def clear(ctx, amount=5): await ctx.channel.purge(limit=amount)

#Kick/Ban @client.command(name='kick',help='Kicks member from server') @commands.has_permissions(kick_members=True) async def kick(ctx, member : discord.Member, *, reason=None): await member.kick(reason=reason)

@client.command(name='ban',help='Bans member from server') @commands.has_permissions(ban_members=True) async def ban(ctx, member : discord.Member, *, reason=None): await member.ban(reason=reason)

#Disconnect @client.event async def on_disconnect(): general_channel = client.get_channel('channel ID') await general_channel.send('Nikl Pehli Fursat Mein!')

@client.event async def on_message_delete(message): general_channel = client.get_channel('channel ID') await general_channel.send('This Message Was Deleted')

@client.event async def on_typing(channel,user,when): general_channel = client.get_channel('channel ID') await asyncio.sleep(30) await general_channel.send('Send bhi krde bsdk')

@client.event async def on_message_edit(before, after): general_channel = client.get_channel('channel ID') embed= discord.Embed(title=f"{before.author} edited a message!", description=f"Before: \n{before.content}", color=0x3333c7) embed.add_field(name=f"After:", value=f"{after.content}", inline=False) await general_channel.send(embed=embed)

@client.command(pass_context=True,help='Hugs a user') async def hug(ctx): user = choice(ctx.message.channel.guild.members) await ctx.send(f'{ctx.message.author.mention} hugged {user.mention}')

@client.event async def on_member_join(member): print(f'{member} has joined this server.')
