import discord
import openpyxl

import datetime
import requests
import asyncio



from captcha. image import ImageCaptcha
import random
import os
import time


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    client.loop.create_task(status_task())
async def status_task():
    gm = True
    while gm is True:
        game = discord.Game("'엘봇아 도움' 하면 도와 줄게!")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game("피드백, 문의 @이엘#9142 내 사장님임")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game(str(len(client.guilds)) + "개의 서버안에서" + "관리하는 중..")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game("엘봇은 되게 깜찍한다는 학계의 전설")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game("version 0.3")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith('엘봇아 도움'):
         embed=discord.Embed(title="DM을 확인해주세요.", color=0xff0000)
         embed.add_field(name="DM으로메세지가 전송됩니다.", value="만약 전송이 안되신다면 개인정보 및 보안을 낮음으로 설정해주세요.", inline=True)
         await message.channel.send(embed=embed)
         author = message.guild.get_member(int(message.author.id))
         embed=discord.Embed(title="엘봇명령어 목록", description=None, color=0x00a9f7)
         embed.add_field(name="깜찍한엘봇 명령어", value="`,경고목록` `,신고목록", inline=False)
         embed.add_field(name="관리자", value="미공개", inline=False)
         embed.add_field(name="대화", value="`안녕 엘봇`, '잘가 엘봇', '엘봇 바보'" , inline=False)
         embed.add_field(name="정보", value="`,정보` `,서버정보` `,현재시간`", inline=False)
         embed.add_field(name="놀이", value="`가위바위보 `,  `,숫자게임`", inline=False)
         embed.add_field(name="봇", value="`-봇제작자`", inline=False)
         await author.send(embed=embed)

    if message.content.startswith('엘봇아 안녕'):
        await message.channel.send("반가워")

    if message.content.startswith('엘봇아 잘가'):
        await message.channel.send("또 보자!!")

    if message.content.startswith('엘봇이 바보'):
        await message.channel.send("흥칫뿡 너랑 안 놀아!")

    if message.content.startswith('엘봇아 업로드해줘'):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith('엘봇아 메세지보내줘'):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)

    if message.content.lower().startswith("엘봇아 내정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        emb = discord.Embed(title='정보[info]', color=0x00ff00)
        emb.add_field(name="이름", value=message.author.name, inline=True)
        emb.add_field(name="서버정보", value=message.author.display_name, inline=True)
        emb.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        emb.add_field(name="아이디", value=message.author.id, inline=True)
        emb.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(content=None, embed=emb)

    if message.content.lower().startswith('엘봇아 갓챠'):
        if message.channel.id == 603392454036684802:
            Image_captca = ImageCaptcha()
            a = ""
            for i in range(6):
                a += str(random.randint(0, 9))
            name = str(message.author.id) + ".png"
            Image_captca.write(a, name)

            await message.channel.send(file=discord.File(name))
            def check(msg):
                return msg.author == message.author and msg.channel == message.channel

            try:
                msg = await client.wait_for("message", timeout=10, check=check)
            except:
                emb = discord.Embed(title='시간이 초과되었습니다. 다시 `인증`을 입력해주세요.', color=0x1d6bda)
                await message.channel.send(content=None, embed=emb)
                return

            if msg.content == a:
                emb = discord.Embed(title='인증이 완료되었습니다.', color=0x1d6bda)
                await message.channel.send(content=None, embed=emb)
            else:
                emb = discord.Embed(title='오답입니다. 다시 `인증`을 입력해주세요.', color=0x1d6bda)
                await message.channel.send(content=None, embed=emb)
        else:
            emb = discord.Embed(title='이 채널에서는 사용할수없는 명령어입니다.', color=0x1d6bda)
            await message.channel.send(content=None, embed=emb)

    if message.content.lower().startswith("엘봇아 현재시간"):
        a = datetime.datetime.today().year
        b = datetime.datetime.today().month
        c = datetime.datetime.today().day
        d = datetime.datetime.today().hour
        e = datetime.datetime.today().minute
        f = datetime.datetime.today().second
        emb = discord.Embed(title='현재시간[Time]', color=0xffbf00)
        emb.add_field(name=str(a) + "년 " +  str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초 입니다.", value='[Korea]', inline=False)
        await message.channel.send(content=None, embed=emb)

    if message.content.lower().startswith(",서버정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.guild.id) >> 22) + 1420070400000) / 1000)
        emb = discord.Embed(title='서버정보[Severinfo]', color=0x00ff00)
        emb.add_field(name="이름", value=message.guild.name, inline=True)
        emb.add_field(name="생성일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        emb.add_field(name="아이디", value=message.guild.id, inline=True)
        emb.add_field(name="자기정보", value=message.author.display_name, inline=True)
        emb.set_thumbnail(url=message.guild.icon_url)
        await message.channel.send(content=None, embed=emb)


    if message.content.startswith("엘봇아 가위바위보 가위"):
        rsp = "123"
        rsp1 = random.choice(rsp)
        if rsp1 == "1":
            emb = discord.Embed(title='가위바위보', color=0xfff000)
            emb.add_field(name='결과', value='봇 :v: 당신 :v: 무승부!')
            await message.channel.send(content=None, embed=emb)
        if rsp1 == "2":
            emb = discord.Embed(title='가위바위보', color=0xff0000)
            emb.add_field(name='결과', value='봇 :fist: 당신 :v: 봇 승리!')
            await message.channel.send(content=None, embed=emb)
        if rsp1 == "3":
            emb = discord.Embed(title='가위바위보', color=0x0dff00)
            emb.add_field(name='결과', value='봇 :raised_hand: 당신 :v: 당신 승리!')
            await message.channel.send(content=None, embed=emb)
    if message.content.startswith("엘봇아 가위바위보 바위"):
        rsp = "123"
        rsp1 = random.choice(rsp)
        if rsp1 == "1":
            emb = discord.Embed(title='가위바위보', color=0x0dff00)
            emb.add_field(name='결과', value='봇 :v: 당신 :fist: 당신 승리!')
            await message.channel.send(content=None, embed=emb)
        if rsp1 == "2":
            emb = discord.Embed(title='가위바위보', color=0xfff000)
            emb.add_field(name='결과', value='봇 :fist: 당신 :fist: 무승부!')
            await message.channel.send(content=None, embed=emb)
        if rsp1 == "3":
            emb = discord.Embed(title='가위바위보', color=0xff0000)
            emb.add_field(name='결과', value='봇 :raised_hand: 당신 :fist: 봇 승리!')
            await message.channel.send(content=None, embed=emb)

    if message.content.startswith("엘봇아 가위바위보 보"):
        rsp = "123"
        rsp1 = random.choice(rsp)
        if rsp1 == "1":
            emb = discord.Embed(title='가위바위보', color=0xff0000)
            emb.add_field(name='결과', value='봇 :v: 당신 :raised_hand: 봇 승리!')
            await message.channel.send(content=None, embed=emb)
        if rsp1 == "2":
            emb = discord.Embed(title='가위바위보', color=0x0dff00)
            emb.add_field(name='결과', value='봇 :fist: 당신 :raised_hand: 당신 승리!')
            await message.channel.send(content=None, embed=emb)
        if rsp1 == "3":
            emb = discord.Embed(title='가위바위보', color=0xfff000)
            emb.add_field(name='결과', value='봇 :raised_hand: 당신 :v: 무승부!')
            await message.channel.send(content=None, embed=emb)

    if message.content.startswith(',숫자게임'):
        number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        botnumber = random.sample(number, 3)
        mynumber = random.sample(number, 3)
        emb = discord.Embed(title='숫자게임', color=0x0016ff)
        emb.add_field(name='결과', value='봇의 숫자' + str(botnumber) + '당신의 숫자' + str(mynumber), inline=False)
        await message.channel.send(content=None, embed=emb)
        if botnumber == mynumber:
            emb = discord.Embed(title='숫자게임', color=0xfff000)
            emb.add_field(name='승자',value='봇의 숫자' + str(botnumber, 3) + '당신의 숫자' + str(mynumber, 3) + '이므로 무승부!',inline=False)
            await message.channel.send(content=None, embed=emb)
        if botnumber > mynumber:
            emb = discord.Embed(title='숫자게임', color=0xff0000)
            emb.add_field(name='승자',value='봇의 숫자' + str(botnumber) + '당신의 숫자' + str(mynumber) + '이므로 봇의 승리!',inline=False)
            await message.channel.send(content=None, embed=emb)
        else:
            emb = discord.Embed(title='숫자게임', color=0x0dff00)
            emb.add_field(name='승자', value='봇의 숫자' + str(botnumber) + '당신의 숫자' + str(mynumber) + '이므로 당신의 승리!', inline=False)
            await message.channel.send(content=None, embed=emb)









            










client.run("NjE5MDg3MDY5MjcyMzQyNTM5.XXLs2A.v7oFmYP_UJYUnvkvzqyiDcJaV-M")
