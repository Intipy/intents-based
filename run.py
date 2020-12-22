import discord
import os




client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('파이드 안녕'):
        await message.channel.send('반갑다 씹년아')

    if message.content.startswith('파이드 사랑해'):
        await message.channel.send('나는 너 사랑 안하는데? 역겨워 ㄲㅈ')

    if message.content.startswith('파이드 병신'):
        await message.channel.send('좆까 개씹수 쓰레기놈아')

    if message.content.startswith('파이드 니애미'):
        await message.channel.send('너희 엄마는 확실히 쩔드라')

    if message.content.startswith('파이드 노무현'):
        await message.channel.send('노무현이 아니라 누무현입니다. 일베충 나가디지샌')

    if message.content.startswith('파이드 전두환'):
        await message.channel.send('땅크 나가신다~')

    if message.content.startswith('파이드 광주는?'):
        await message.channel.send('광주는 총기를 들고 일어난 하나의 그... 민주화운동이야~')

    if message.content.startswith('파이드 전라도'):
        await message.channel.send('훠이미 어찌 우덜을 겁도없시 욕을 한당께요~ 노예생활좀 해보랑께~')

    if message.content.startswith('파이드 섹스'):
        await message.channel.send('퍽퍽퍽 헤으응 퓨븃')

    if message.content.startswith('파이드 자지'):
        await message.channel.send('좆까 니 자지좀 씻고다녀라 냄시나노')

    if message.content.startswith('파이드 보지'):
        await message.channel.send('하앍 핥핥핥')

    if message.content.startswith('파이드 느금'):
        await message.channel.send('좆까~')

    if message.content.startswith('파이드 이름성'):
        await message.channel.send('저의 주인님 입니다만...?')

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
