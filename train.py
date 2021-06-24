import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD
import random
from konlpy.tag import Okt
okt = Okt()
import json
import pickle



######################################



ignore_letters = ['이', '!', '.', ',']
intents = json.loads(open('intents.json', encoding='UTF-8').read())     # intents.json 불러오기

words=[]           #모든 토큰
classes = []      # 모든 태그
documents = []    # 모든 토큰과 태그   [(토큰, 토큰, 토큰):(태그)]



def tokenize(sentence):     # 문장을 토큰화 한 후에 조사, 감탄사 제거, 어근 추출
    clean_words = []
    for word in okt.pos(sentence, norm=True, stem=True): 
        if word[1] not in ['Josa', 'Exclamation']: 
            clean_words.append(word[0])
    return clean_words



for intent in intents['intents']:        # intents.json의 intents
    for pattern in intent['patterns']:   # intents.json의 intents의 patterns 

        word = tokenize(pattern) # 질문(patterns) 문장을 토큰화 한 후에 조사, 감탄사 제거, 어근 추출
        words.extend(word)       # words[]에 모든 토큰을 저장 word[] > words[] 상속
        documents.append((word, intent['tag']))  # [(토큰, 토큰, 토큰):(태그)]  형태로 모든 토큰과 태그를 documents[]에 저장

        if intent['tag'] not in classes:   # 모든 태그를 classes[]에 저장
            classes.append(intent['tag'])



words = sorted(list(set(words)))         
classes = sorted(list(set(classes)))     # words[] 그리고 classes[] 를 정렬, 중복 제거 

pickle.dump(words,open('pk-words.pkl','wb'))
pickle.dump(classes,open('pk-classes.pkl','wb'))    # words[] 그리고 classes[] 를 pickle 형태로 저장



training = []
output_empty = [0] * len(classes)

for doc in documents:    
    bag = []      
    pattern_words = doc[0]

    for word in words:
        bag.append(1) if word in pattern_words else bag.append(0)
        
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)


train_x = list(training[:,0])
train_y = list(training[:,1])
print("학습 데이터 생성됨")



model = Sequential()
model.add(Dense(200, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(100, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y), epochs=1500, batch_size=5, verbose=1)
model.save('bot_model.h5', hist)

print("모델 생성됨")