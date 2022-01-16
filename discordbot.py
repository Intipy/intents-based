import discord
from discord.ext import commands
from discord.utils import get
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
    return np.array(bag)     # 원 핫 인코딩


def predict_class(sentence):
    bow = bag_of_words(sentence)               # 원 핫 인코딩
    res = model.predict(np.array([bow]))[0]    # intent 별로 확률을 예측함                                 
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    intent_prob_list = []
    for r in results:
        intent_prob_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    print(intent_prob_list)
    return intent_prob_list    #intent_list -->  [{'intent': '인사', 'probability': '0.9999933'}]


def getResponse(intents_list, intents_json):
    if float(intents_list[0]['probability']) < 0.6:
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


uMsg = "your sentence"
ints = predict_class(uMsg)
res = getResponse(ints, intents)

print(res)
