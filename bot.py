import discord
import random
from discord.ext import commands


client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('minh is a nigger lol'))
    print('Bot is ready.')


@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked.')
@kick.error
async def kick_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send('You do not have the permission to kick people.')



@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify a number of messages to delete.')



@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned.')
@ban.error
async def ban_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send('You do not have the permission to ban people.')


@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member : discord.Member=None):
    await ctx.send(f'{member.mention} has been muted.')
    if not member:
        await ctx.send('Please specify a member!')
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
@mute.error
async def mute_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send('You do not have the permission to mute people.')

@client.command()
async def unmute(ctx, member : discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.remove_roles(role)
            await ctx.send("{} has been unmuted." .format(member.mention,ctx.author.mention))
            return

@client.command()
async def avatar(ctx, member: discord.Member):
    show_avatar = discord.Embed(

        color = discord.Color.dark_blue()
    )
    show_avatar.set_image(url='{}'.format(member.avatar_url))
    await ctx.send(embed=show_avatar)

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes - definitely.',
                'You may rely on it.',
                'As I see it, yes.',
                'Most likely.',
                'Outlook good.',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Dont count on it.',
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful.']
    
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


client.run(process.env.BOT_TOKEN);
