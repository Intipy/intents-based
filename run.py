import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content('파이드 안녕'):
        await message.channel.send('반갑다 씹년아')

    if message.content('파이드 안녕k'):
        await message.channel.send('반갑다 dd')

    if message.content.startswith('파이드 사랑해'):
        await message.channel.send('나는 너 사랑 안하는데? 역겨워 꺼져')

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

    if message.content.startswith('파이드 문재인'):
        await message.channel.send('조선인에게서 아이가 생기지 않도록 할 수 있을까?')

    if message.content.startswith('파이드 박정희'):
        await message.channel.send('탕탕')

    if message.content.startswith('파이드 누무현'):
        await message.channel.send('우리 게이는 노무현이 누무현이노?')

    if message.content.startswith('파이드 섹스하자'):
        await message.channel.send('너무 좆아요 주인님!')

    if message.content.startswith('파이드 섹스할래?'):
        await message.channel.send('너무 좆아요 주인님!')

    if message.content.startswith('파이드 아기'):
        await message.channel.send('만들자')

    if message.content.startswith('파이드 씨발'):
        await message.channel.send('여성혐오 단어 쓰지 마세요. ppap 따서 여성가족부에 보냈다 ㅅㄱ')

    if message.content.startswith('파이드 강간'):
        await message.channel.send('잠재적 강간범 69 한남 어서오고~')

    if message.content.startswith('파이드 한남'):
        await message.channel.send('핸냄 게이야...')

    if message.content.startswith('파이드 한녀'):
        await message.channel.send('대단하다!')

    if message.content.startswith('파이드 페미'):
        await message.channel.send('능지 딸리는 한남새끼 뿔났노?')

    if message.content.startswith('파이드 메갈'):
        await message.channel.send('그저 빛갈리아...')

    if message.content.startswith('파이드 워마드'):
        await message.channel.send('이 시대의 진정한 리더!')

    if message.content.startswith('파이드 김대중'):
        await message.channel.send('좋은 일본 문화 받아들이자.')

    if message.content.startswith('파이드 파이드'):
        await message.channel.send('파이드 존나 호감이면 개추ㅋㅋ 일단 나부터ㅋㅋ')

    if message.content.startswith('파이드 크시'):
        await message.channel.send('크시 그 존나 멍청해서 말도 못알아 듣는 퇴물 좆냥이 버리고 파이드와 함께해요~')

    if message.content.startswith('파이드 피아제'):
        await message.channel.send('아내가 받았다.')

    if message.content.startswith('파이드 부엉'):
        await message.channel.send('부엉이는 우흥~ 하고 울어요')

    if message.content.startswith('파이드 우흥'):
        await message.channel.send('부엉이가 울어요!')

    if message.content.startswith('파이드 부엉이바위'):
        await message.channel.send('로 가자~')

    if message.content.startswith('파이드 운지'):
        await message.channel.send('고통이 너무 크다')

    if message.content.startswith('파이드 인싸'):
        await message.channel.send('괘씸하거든요?')

    if message.content.startswith('파이드 문크예거'):
        await message.channel.send('훠어어어어ㅓㅓㅓ!!!!!!')

    if message.content.startswith('파이드 크시야'):
        await message.channel.send('나는 크시가 아니라 파이드에요 이 씨발련아')

    if message.content.startswith('파이드 박원순'):
        await message.channel.send('원순열을 공부해보자')

    if message.content.startswith('파이드 뇌물'):
        await message.channel.send('하지맙시다')

    if message.content.startswith('파이드 배리나'):
        await message.channel.send('리나언니 힘내요!')

    if message.content.startswith('파이드 응디'):
        await message.channel.send('미국 응디 뒤에 숨어가지고')

    if message.content.startswith('파이드 죽어'):
        await message.channel.send('조까요')

    if message.content.startswith('파이드 마크복돌러'):
        await message.channel.send('이 새끼 페도 루리웹 회원이래요~ 얼레리 꼴레리~')

    if message.content.startswith('파이드 오나홀'):
        await message.channel.send('찐따 게이야...')

    if message.content.startswith('파이드 샌즈'):
        await message.channel.send('아시는구나!')

    if message.content.startswith('파이드 언더테일'):
        await message.channel.send('토비폭스 사망 기원 1일차')

    if message.content.startswith('노짱'):
        await message.channel.send('예아')

    if message.content.startswith('파이드 길우진'):
        await message.channel.send('십덕 아이템 월수 여유만만 인방충 문재인 구독자')

    if message.content.startswith('파이드 좋아해'):
        await message.channel.send('꺼지세요')

    if message.content.startswith('파이드 이름성 나이'):
        await message.channel.send('만 9세 판곡초등학교 2학년 4반 16번')

    if message.content.startswith('파이드 폭동'):
        await message.channel.send('폭동(x) 민주 폭동(o)')

    if message.content.startswith('파이드 민주화'):
        await message.channel.send('안될꺼머있노')

    if message.content.startswith('파이드 중력'):
        await message.channel.send('크아악!! 중력이 너무 쌔요!')

    if message.content.startswith('파이드 523'):
        await message.channel.send('ㅈㄹㅈ')

    if message.content.startswith('파이드 중력시'):
        await message.channel.send('523523523523523523523523523523523523523')

    if message.content.startswith('파이드 파피루스'):
        await message.channel.send('할줄아는거 좆도 없는 하등 벌레새끼')

    if message.content.startswith('헋'):
        await message.channel.send('헋')

    if message.content.startswith('에휴'):
        await message.channel.send('에휴')

    if message.content.startswith('에후'):
        await message.channel.send('에후')

    if message.content.startswith('애휴'):
        await message.channel.send('애휴')

    if message.content.startswith('애후'):
        await message.channel.send('애후')

    if message.content.startswith('병신'):
        await message.channel.send('병신')

    if message.content.startswith('병슨'):
        await message.channel.send('병슨')

    if message.content.startswith('븅슨'):
        await message.channel.send('븅슨')

    if message.content.startswith('변슨'):
        await message.channel.send('변슨')

    if message.content.startswith('뷴신'):
        await message.channel.send('뷴신')

    if message.content.startswith('변신'):
        await message.channel.send('변신')

    if message.content.startswith('ㅂㅅ'):
        await message.channel.send('ㅂㅅ')

    if message.content.startswith('ㅄ'):
        await message.channel.send('ㅄ')

    if message.content.startswith('븅신'):
        await message.channel.send('븅신')

    if message.content.startswith('뷴슨'):
        await message.channel.send('뷴슨')

    if message.content.startswith('파이드 허언이'):
        await message.channel.send('허언이 엉덩이 조물조물')

    if message.content.startswith('파이드 악잠'):
        await message.channel.send('악잠 쭈인님!')

    if message.content.startswith('파이드 히토미'):
        await message.channel.send('힡옴이 쵝오!')

    if message.content.startswith('파이드 폰허브'):
        await message.channel.send('라이브')

    if message.content.startswith('69'):
        await message.channel.send('74...인줄 알았지~? 한남이지롱~')

    if message.content.startswith('파이드 루리웹'):
        await message.channel.send('-근-')

    if message.content.startswith('파이드 skydra'):
        await message.channel.send('야갤 네임드')

    if message.content.startswith('파이드 박틸틸'):
        await message.channel.send('고닉 박틸틸을 응원합니다')

    if message.content.startswith('파이드 근'):
        await message.channel.send('첩')

    if message.content.startswith('파이드 페도'):
        await message.channel.send('취향입니다만?')

    if message.content.startswith('파이드 엄준식'):
        await message.channel.send('엄준식 화이팅!')

    if message.content.startswith('엄준식'):
        await message.channel.send('와! 엄준식! 아시는구나!')

    if message.content.startswith('파이드 아이템의 인벤토리'):
        await message.channel.send('???: 죽고 나서 올라온 mc무현 작품은 악질적인 것 밖에 없다.')

    if message.content.startswith('파이드 근첩토리'):
        await message.channel.send('오늘 알아볼 것은...')

    if message.content.startswith('파이드 뷰지'):
        await message.channel.send('뷰빨 한번 괜찮겠습니까?')

    if message.content.startswith('파이드 송모찌'):
        await message.channel.send('사랑해')

    if message.content.startswith('파이드 광주'):
        await message.channel.send('광역시')

    if message.content.startswith('파이드 문재앙'):
        await message.channel.send('좌파 친북 치매 틀딱~')

    if message.content.startswith('파이드 비틱'):
        await message.channel.send('-----비적비 시전중...-----')

    if message.content.startswith('파이드 네덕'):
        await message.channel.send('저는 네덕분들을 지지합니다')

    if message.content.startswith('파이드 네캎'):
        await message.channel.send('디첩새끼 괘씸하거든요? 하아.. 엄보지카이..')

    if message.content.startswith('파이드 예아'):
        await message.channel.send('안될거머있누')

    if message.content.startswith('파이드 여친'):
        await message.channel.send('제 여친은 크시에요!')

    if message.content.startswith('파이드 주식'):
        await message.channel.send('오늘 알아볼 회사는 노무현 엔터테인트먼트(주) 입니다')

    if message.content.startswith('파이드 샌즈tv'):
        await message.channel.send('화력 재기했노 이기야')

    if message.content.startswith('파이드 rmh'):
        await message.channel.send('로무연')

    if message.content.startswith('파이드 탕탕'):
        await message.channel.send('좀더 대국적으로 ')

    if message.content.startswith('파이드 중력절'):
        await message.channel.send('그립읍니다...')

    if message.content.startswith('파이드 고통'):
        await message.channel.send('이 너무 크다..')

    if message.content.startswith('파이드 자살'):
        await message.channel.send('고통이 너무 크신가요? 자살 예방 상담을 추천드려요!')

m = "NzkwODQ2MTM1MzIxMjMxMzgx"+".X-Gi2w.wd8kpfrRxsrJVKvGISXl8ICgzqU"
client.run(m)
