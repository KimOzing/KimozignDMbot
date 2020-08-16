
# 김오징입니다.


import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("봇실행이 시작되었습니다(24시간 온라인).")
    game = discord.Game('~하는 중 ex)봇만들기 하는 중')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id == 디스코드ID를 적기!!:
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="최상단 제목")
                        embed.add_field(name="제목", value=msg, inline=True)
                        embed.set_footer(text=f"서버초대코드")
                        await i.send(embed=embed)
                except:
                    pass


client.run('봇의 토큰을 넣어주세용')
