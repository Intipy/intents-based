import discord
from discord.ext import commands
import json
import random
import pickle
import numpy as np
import time
from konlpy.tag import Okt
okt = Okt()

from tensorflow.keras.models import load_model



#############################


ignore_letters = ['이', '!', '.', ',']

intents = json.loads(open('intents.json', encoding='UTF-8').read())

words = pickle.load(open("pk-words.pkl", "rb"))
classes = pickle.load(open("pk-classes.pkl", "rb"))

model = load_model('bot_model.h5')



def tokenize(sentence):     # 문장을 토큰화 한 후에 조사, 감탄사, 불용어 제거, 어근 추출
    clean_words = []
    for word in okt.pos(sentence, norm=True, stem=True): 
        if word[1] not in ['Josa', 'Exclamation']:
            if word[0] not in ignore_letters:
                clean_words.append(word[0])
    return clean_words



def clean_sentence(sentence):
    sentence_words = tokenize(sentence)
    print(sentence_words)
    return sentence_words



def bag_of_words(sentence):
    sentence_words = clean_sentence(sentence)
    bag = [0]*len(words)  
    for w in sentence_words:
        for i,word in enumerate(words):
            if word == w: 
                bag[i] = 1
    return np.array(bag)     # 넘파이 2차원 행렬 형태 0001000



def predict_class(sentence):

    bow = bag_of_words(sentence)               # 넘파이 2차원 행렬 형태 0001000
    res = model.predict(np.array([bow]))[0]    # intent 별로 확률을 예측함                                 

    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    intent_prob_list = []
    for r in results:
        intent_prob_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    
    if float(intent_prob_list[0]['probability']) < 0.98:
        print(intent_prob_list)
        f = open('ErrorList.txt', 'a', encoding="UTF-8")
        f.write(sentence)
        f.write("\n")
        f.write(intent_prob_list[0]['intent'])
        f.write("\n")
        f.write(intent_prob_list[0]['probability'])
        f.write("\n")
        f.write("------")
        f.write("\n")
    else:
        print(intent_prob_list)
    
    return intent_prob_list    #intent_list -->  [{'intent': '인사', 'probability': '0.9999933'}]



def getResponse(intents_list, intents_json):
    
    if float(intents_list[0]['probability']) < 0.98:
        error_result = "probability_low"
        return error_result
    
    else:
        tag = intents_list[0]['intent']   #intent_list -->  [{'intent': '인사', 'probability': '0.9999933'}]
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if i['tag'] == tag:
                result = random.choice(i['responses'])
                break
        return result



########################



client = commands.Bot(command_prefix=")")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=")도움말"))
    print("Bot Ready")


@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content.startswith(")"):
        if message.content == ")도움말":
            embed=discord.Embed(title="឵ ឵ ឵឵ ឵ ឵឵ ឵ ឵឵ ឵ ឵", color=0x00ff56)
            embed.set_author(name="[ 파이드 도움말 ]", icon_url="https://cdn.discordapp.com/attachments/851075781413437474/851339042448605224/1.png")
            embed.add_field(name="឵파이드는 AI 챗봇입니다", value="- ឵ ឵឵ ឵ `prefix: )`", inline=False) 
            embed.add_field(name="឵) 뒤에 하고싶은 말을 해보세요", value="- ឵ ឵឵ ឵ ឵`)안녕`", inline=False) 
            embed.add_field(name="파이드는 현재 영어를 지원하지 않습니다", value="- ឵ ឵឵ ឵ ឵`한글만 사용해주세요`", inline=False) 
            embed.add_field(name="឵파이드는 계속 학습 중입니다", value="`개발 초기 단계이며 아직 학습량이 적어 여러 오류나 부적절한 행동이 있을 수 있습니다(학습 상태를 참조해주세요)`", inline=False) 
            embed.add_field(name="개발자", value="- ឵ ឵឵ ឵ `Intipy#2784`", inline=False) 
            embed.add_field(name="개발 일자", value="- ឵ ឵឵ ឵ `2021.06.05.`", inline=False) 
            embed.add_field(name="파이드 개발자를 모집합니다", value="- ឵ ឵឵ ឵ `개발자 계정으로 문의 바람`", inline=False) 
            embed.add_field(name="파이드 공식 지원 서버", value="- ឵ ឵឵ ឵ https://discord.gg/yUQDS2sWZH", inline=False) 
            embed.add_field(name="학습 상태", value="- ឵ ឵឵ ឵ `0.00000032 (매우 약함)`", inline=False) 
            await message.channel.send(embed=embed)
        else:
            uMsg = message.content[1:]
            ints = predict_class(uMsg)
            res = getResponse(ints, intents)

            if res == "json_time_set":
                now = time.localtime()
                res = "지금은 %02d시 %02d분이야 ㅎㅎ" % (now.tm_hour, now.tm_min)
                await message.channel.send(res)
            elif res == "json_date_set":
                now = time.localtime()
                res = "오늘은 %04d년 %02d월 %02d일이야 ㅎㅎ" % (now.tm_year, now.tm_mon, now.tm_mday)
                await message.channel.send(res)
            elif res == "probability_low":
                res = random.choice(["그랭", "그래", "그래 ㅎ", "응", "웅", "응 ㅎㅎ", "그래 ㅎㅎ", "웅 ㅎㅎ"])
                await message.channel.send(res)
            else:
                await message.channel.send(res)

            


client.run("NzkwODQ2MTM1MzIxMjMxMzgx.X-Gi2w.oD8w5xtQqnymqJJCcc2oWjIwKpA")




