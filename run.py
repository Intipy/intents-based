import discord
import asyncio
import os
from discord.ext import commands
from discord.ext.commands import bot

w = 'NzkwODQ2MTM1MzIxMjMxMzgx.X-Gi2w.wd8kpfrRxsrJVKvGISXl8ICgzq'+'U'
bot = commands.Bot(command_prefix = '파이드 ') 

@bot.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="파이드와 노는 방법을 보려면-->파이드 도움말"))


@bot.command()
async def 도움말(ctx):
    embed = discord.Embed(colour = 808000)
    embed.add_field(name='파이드와 대화하기', value='파이드 [하고 싶은 말] <--(ex: 파이드 사랑해)', inline=False)
    embed.add_field(name='파이드에게 대답 가르치기', value='파이드 배워 [가르칠 말] [대답] <--(ex: 파이드 배워 사랑해 꺼져 )', inline=False)
    embed.add_field(name='파이드가 대답을 안한다면?', value='오류보단 대답을 몰라서 못하는 경우가 많아요. 대답을 못한다면 대답을 가르쳐보세요!', inline=False)
    embed.add_field(name='파이드 업데이트', value='파이드는 매일 11시~12시 사이에 업데이트를 해요. 여러분이 가르친 말, 버그 수정 등이 적용돼요.', inline=False)
    embed.add_field(name='파이드 발전', value='파이드는 처음엔 할 수 있는 대답, 기능이 적지만 여러분이 가르친 대답과 업데이트를 통해 점점 발전해요', inline=False)
    embed.add_field(name='파이드 오류 수정 문의', value='#파이드 오류:[문제점] <--(ex: 파이드 오류:오프라인)', inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def 안녕(ctx):
    await ctx.send('반갑다 씹년아')

@bot.command()
async def 병신(ctx):
    await ctx.send('어 좆까~')

@bot.command()
async def 느금(ctx):
    await ctx.send('응 니미~')

@bot.command()
async def 느금마(ctx):
    await ctx.send('어 니애미~')

@bot.command()
async def 좆까(ctx):
    await ctx.send('니 좆이나 까 소추새끼야~')

@bot.command()
async def 노무현(ctx):
    await ctx.send('노무현이 아니라 누무현입니다. 일베충 나가 디지샌')

@bot.command()
async def 누무현(ctx):
    await ctx.send('우리 게이는 노무현이 누무현이노?')

@bot.command()
async def 보지(ctx):
    await ctx.send('핥핥핥')

@bot.command()
async def 자지(ctx):
    await ctx.send('니 자지좀 씻고다니세요 씨발련아')

@bot.command()
async def 할카스(ctx):
    await ctx.send('이,,,할미,,, 잠쥐 맛,,, 좋쟈,,,?')

@bot.command()
async def 할배카스(ctx):
    await ctx.send('ㅗㅗㅗㅗㅗ')

@bot.command()
async def 니애미(ctx):
    await ctx.send('확실히 니 애미는 쩔드라')

@bot.command()
async def rmh(ctx):
    await ctx.send('로무히언')

@bot.command()
async def 중력(ctx):
    await ctx.send('크아악! 너무 강해!')

@bot.command()
async def 운지(ctx):
    await ctx.send('운지를 한다면 고통이 너무 클거에요! 1393 자살 예방 상담전화를 추천드려요!')

@bot.command()
async def 자살(ctx):
    await ctx.send('고통이 너무 크신가요? 1393 자살 예방 상담전화를 추천드려요!')

@bot.command()
async def 바위(ctx):
    await ctx.send('너무 높아요!')

@bot.command()
async def 부엉이(ctx):
    await ctx.send('부엉이는 우흥~ 하고 울어요!')

@bot.command()
async def 우흥(ctx):
    await ctx.send('어디선가 부엉이가 우네요!')

@bot.command()
async def 두부(ctx):
    await ctx.send('한국도 중국만큼 두부가 유명하답니다!')

@bot.command()
async def 두부외상(ctx):
    await ctx.send('두부가 외상에 의해 손상되는 것을 말해요!')

@bot.command()
async def 한남(ctx):
    await ctx.send('69한남소추갈잦도태생명체는 즉시 재기해라 이기야')

@bot.command()
async def 페미(ctx):
    await ctx.send('여성인권을 위해 싸우시는 대단한 분들이에요')

@bot.command()
async def 페미니스트(ctx):
    await ctx.send('여성인권을 위해 싸우시는 대단한 분들이에요')

@bot.command()
async def 메갈(ctx):
    await ctx.send('시대를 앞서간 진정한 리더!')

@bot.command()
async def 메갈리아(ctx):
    await ctx.send('그저 빛갈리아...')

@bot.command()
async def ㅈㄹㅈ(ctx):
    await ctx.send('중력절인가요? 지리지인가요?')

@bot.command()
async def 중력절(ctx):
    await ctx.send('그립읍니다...')

@bot.command()
async def 문재인(ctx):
    await ctx.send('파이드와 대깨문 일동은 성군 문재인을 지지합니다')

@bot.command()
async def 문재앙(ctx):
    await ctx.send('좌파친북치매틀딱~')

@bot.command()
async def 재앙(ctx):
    await ctx.send('-문-')

@bot.command()
async def 베이징(ctx):
    await ctx.send('베이징은 천안문이 유명하죠!')

@bot.command()
async def 중국(ctx):
    await ctx.send('드러운 개만도 못한 바퀴벌레 찌끄레기 짱깨란 말은 혐오표현이니 지양해주세요!')

@bot.command()
async def 쭝궈(ctx):
    await ctx.send('드러운 개만도 못한 바퀴벌레 찌끄레기 짱깨란 말은 혐오표현이니 지양해주세요!')

@bot.command()
async def 짱개(ctx):
    await ctx.send('착짱죽짱')

@bot.command()
async def 착짱(ctx):
    await ctx.send('죽짱')

@bot.command()
async def 근(ctx):
    await ctx.send('첩')

@bot.command()
async def 근첩(ctx):
    await ctx.send('저는 살인웹 여러분을 응원합니다')

@bot.command()
async def 루리웹(ctx):
    await ctx.send('근')

@bot.command()
async def 오유(ctx):
    await ctx.send('로류')

@bot.command()
async def 오늘의유머(ctx):
    await ctx.send('본진으로')

@bot.command()
async def 투신(ctx):
    await ctx.send('ㅈㅜㅇㄹㅕㄱ')

@bot.command()
async def 박정희(ctx):
    await ctx.send('탕탕')

@bot.command()
async def 탕탕(ctx):
    await ctx.send('좀더 대국적으로 ')

@bot.command()
async def 이명박(ctx):
    await ctx.send('01띵넥- 대통령 만세!')

@bot.command()
async def 김대중(ctx):
    await ctx.send('좋은 일본문화 받아들이자')

@bot.command()
async def 일본(ctx):
    await ctx.send('좋은 일본문화를 받아들이는건 어떄요?')

@bot.command()
async def 뷰지(ctx):
    await ctx.send('뷰따리ㅋㅋㅋㅋㅋ 뷰석ㅋㅋㅋㅋ 뷰이지 않는 검ㅋㅋㅋㅋㅋ 뷰헤미안 랩소디ㅋㅋㅋㅋㅋ')

@bot.command()
async def 쥬지(ctx):
    await ctx.send('쥬석ㅋㅋㅋㅋㅋ 쥬위ㅋㅋㅋㅋㅋ 쥬메이카ㅋㅋㅋㅋ 쥬스민ㅋㅋㅋㅋㅋ')

@bot.command()
async def 광주는(ctx):
    await ctx.send('총기를 들고 일어난 하나의 그... 민주화운동이야~')

@bot.command()
async def 광주(ctx):
    await ctx.send('광역시')

@bot.command()
async def 민주화(ctx):
    await ctx.send('ㅁㅈㅎ')

@bot.command()
async def 일베(ctx):
    await ctx.send('파이드는 일간베스트를 gg합니다')

@bot.command()
async def ㅁㅈㅎ(ctx):
    await ctx.send('제 본명은 민재훈이에요!')

@bot.command()
async def 폭동(ctx):
    await ctx.send('민주 폭동입니다')

@bot.command()
async def 노짱(ctx):
    await ctx.send('노무현 대통령님은 중국인이 아닌걸요?')

@bot.command()
async def 누(ctx):
    await ctx.send('누스페이스ㅋㅋㅋㅋㅋ 누이즈ㅋㅋㅋㅋ 누텔라ㅋㅋㅋㅋㅋ')

@bot.command(aliases=['TV샌즈'])
async def tv샌즈(ctx):
    await ctx.send('제 주인님이에요!')

@bot.command()
async def 길우진(ctx):
    await ctx.send('페도 씹덕 루리웹 회원 ')

@bot.command()
async def 클리앙(ctx):
    await ctx.send('틀니앙')

@bot.command()
async def 아이템의인벤토리(ctx):
    await ctx.send('근첩')

@bot.command()
async def 아이템의근첩토리(ctx):
    await ctx.send('???: 죽고 나서 만들어진 mc무현은 악질적인 것 밖에 없다')

@bot.command()
async def 유두순(ctx):
    await ctx.send('오타쿠 수호자 유두순님을 지지합니다')

@bot.command()
async def 조두순(ctx):
    await ctx.send('조루')

@bot.command()
async def 마크복돌러(ctx):
    await ctx.send('존망함')

@bot.command()
async def 섹스(ctx):
    await ctx.send('퍽퍽퍽 헤으응 찍')

@bot.command()
async def 질싸(ctx):
    await ctx.send('한남새끼 발정났노')

@bot.command()
async def 질내사정(ctx):
    await ctx.send('흐어업 퓨부붓')

@bot.command()
async def 강간(ctx):
    await ctx.send('잠재적 강간범 핸냄새끼 어서오고')

@bot.command()
async def 여유만만(ctx):
    await ctx.send('비틱 후빨러')

@bot.command()
async def 네캎(ctx):
    await ctx.send('꺼져')

@bot.command()
async def 비틱(ctx):
    await ctx.send('왜 초면부터 비틱이니 뭐니 반말하시죠?')

@bot.command()
async def 네덕(ctx):
    await ctx.send('네다음디첩')

@bot.command()
async def 월수(ctx):
    await ctx.send('좆병신새끼')

@bot.command()
async def 잼민이(ctx):
    await ctx.send('잼민이는 초등학생비하말이니까 초등학생이라고 하세요. 모든 초등학생이 무개념은 아니잔아요?')

@bot.command()
async def 급식(ctx):
    await ctx.send('쩝쩝 급식 마싯따 월수보러 가야지ㅎㅎ 아 문재인 누군지는 모르겠는데 좋은사람 아ㅋㅋ')

@bot.command()
async def 대깨문(ctx):
    await ctx.send('응 머가리에 칼이 들어와도 문재인이야~')

@bot.command()
async def 전라도(ctx):
    await ctx.send('훠이미 내가 전라도사는디 나한테 보태준거 있는당가 탄압하지 말랑께요')

@bot.command()
async def 홍어(ctx):
    await ctx.send('뭐시 홍어? 지금 내가 전라도 산다고 차별하는거시여 뭐여 염전 노예생활좀 해보랑께~')

@bot.command()
async def 자서전(ctx):
    await ctx.send('자서전은 김대중 자서전이 최고!')

@bot.command()
async def 인방(ctx):
    await ctx.send('좆방충')

@bot.command()
async def 야갤(ctx):
    await ctx.send('국내 야짤 갤러리')

@bot.command()
async def 중갤(ctx):
    await ctx.send('중세 근첩 마이너 갤러리')

@bot.command(aliases=['병신tv', 'tv병신', 'TV병신'])
async def 병신TV(ctx):
    await ctx.send('근첩 진지충 새끼 ㅗㅗㅗㅗ')

@bot.command(alieses=['샌즈tv'])
async def 샌즈TV(ctx):
    await ctx.send('존망함')

@bot.command()
async def 예아(ctx):
    await ctx.send('안 될 거 뭐 있노')

@bot.command()
async def 사랑해(ctx):
    await ctx.send('나는 너 안사랑해 꺼져')

@bot.command()
async def 좋아해(ctx):
    await ctx.send('드러워 꺼져ㅗㅗ')

@bot.command()
async def 반가워(ctx):
    await ctx.send('ㅇ')

@bot.command()
async def 배리나(ctx):
    await ctx.send('리나언니 힘내요!')

@bot.command()
async def 엄준식(ctx):
    await ctx.send('엄준식 화이팅!')

@bot.command()
async def 박틸틸(ctx):
    await ctx.send('박틸틸 화이팅!')

@bot.command()
async def ㅈㄹㅅ(ctx):
    await ctx.send('5시23분!')

@bot.command()
async def 엄(ctx):
    await ctx.send('준식')

@bot.command()
async def 찐(ctx):
    await ctx.send('Wls')

@bot.command()
async def 엄마(ctx):
    await ctx.send('사랑해요!')

@bot.command()
async def 아빠(ctx):
    await ctx.send('사랑해요!')

@bot.command()
async def 크시(ctx):
    await ctx.send('크시 그 퇴물 좆냥이 말고 파이드를 애용합시다')

@bot.command()
async def 크시야(ctx):
    await ctx.send('저는 크시가 아니라 파이드에요 씨발련아')

@bot.command()
async def 박근혜(ctx):
    await ctx.send('-근-')

@bot.command()
async def 김영삼(ctx):
    await ctx.send('IMF')

@bot.command()
async def 노태우(ctx):
    await ctx.send('누태우입니다')

@bot.command()
async def mc무현(ctx):
    await ctx.send('???: mc무현은 사실상 일베')

@bot.command()
async def 합필(ctx):
    await ctx.send('야 기분좋다~')

@bot.command()
async def 비건(ctx):
    await ctx.send('비-간')

@bot.command()
async def 비건육아(ctx):
    await ctx.send('개씨발새끼들')

@bot.command()
async def 채식주의(ctx):
    await ctx.send('음식이 아니라 폭력입니다')

@bot.command()
async def 바보(ctx):
    await ctx.send('응아니야~')

@bot.command()
async def 응디(ctx):
    await ctx.send('미국응디')

@bot.command()
async def 정액(ctx):
    await ctx.send('찍')

@bot.command()
async def 재기(ctx):
    await ctx.send('풍덩!')

@bot.command()
async def 멍청이(ctx):
    await ctx.send('아니에요...')

@bot.command()
async def 호감도(ctx):
    await ctx.send('나 크시아니라고 씨발')

@bot.command()
async def 짖어(ctx):
    await ctx.send('꽥꽥꽥')

@bot.command()
async def 뒤져(ctx):
    await ctx.send('나쁜말 안돼요!')

@bot.command()
async def 빨아(ctx):
    await ctx.send('(콰득)')

@bot.command()
async def 때찌(ctx):
    await ctx.send('흐에엥...')

@bot.command()
async def 나가(ctx):
    await ctx.send('좆까용')

@bot.command()
async def ㅗ(ctx):
    await ctx.send('ㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗ')

@bot.command()
async def ㅗㅗ(ctx):
    await ctx.send('ㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗ')

@bot.command()
async def 하악(ctx):
    await ctx.send('꺼져')

@bot.command()
async def 하앍(ctx):
    await ctx.send('꺼져')

@bot.command()
async def 핥(ctx):
    await ctx.send('꺼져 ㅡㅡ')

@bot.command()
async def 핥핥(ctx):
    await ctx.send('병신')

@bot.command()
async def 라면먹고갈래(ctx):
    await ctx.send('택배로 보내')

@bot.command()
async def 어쩌라고(ctx):
    await ctx.send('지랄하네 병신')

@bot.command()
async def 쓰레기(ctx):
    await ctx.send('꺼져 쓰레기야')

@bot.command()
async def ㅋ(ctx):
    await ctx.send('...')

@bot.command()
async def ㅋㅋ(ctx):
    await ctx.send('어쩌라고')

@bot.command()
async def 야동(ctx):
    await ctx.send('찐')

@bot.command()
async def 파이드(ctx):
    await ctx.send('ㅇ')

@bot.command()
async def 엿먹어(ctx):
    await ctx.send('쭈왑쭈왑')

@bot.command()
async def 오팬무(ctx):
    await ctx.send('안입었어... 우리집 올래..?')

@bot.command()
async def 변태(ctx):
    await ctx.send('네 좆까요')

@bot.command()
async def 웃기지마(ctx):
    await ctx.send('웃기면 개추ㅋㅋ')

@bot.command()
async def 응기잇(ctx):
    await ctx.send('아')

@bot.command()
async def 헤으응(ctx):
    await ctx.send('ㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗ')

@bot.command()
async def 하앙(ctx):
    await ctx.send('더러워')

@bot.command()
async def 하읏(ctx):
    await ctx.send('...')

@bot.command()
async def 헤응(ctx):
    await ctx.send('ㄲㅈ')

@bot.command()
async def 월요일(ctx):
    await ctx.send('좋아')

@bot.command()
async def 휴가(ctx):
    await ctx.send('못가')

@bot.command()
async def 게임(ctx):
    await ctx.send('싸펑하세요. 10번하세요.')

@bot.command()
async def 스물다섯번째밤(ctx):
    await ctx.send('살아있노...')

@bot.command()
async def 시리(ctx):
    await ctx.send('병신 내숭떠는년 말도 못함ㅉㅉ')

@bot.command()
async def 빅스비(ctx):
    await ctx.send('존나 노잼임ㄹㅇㅋㅋ ')

@bot.command()
async def 노잼(ctx):
    await ctx.send('괘씸하네요')

@bot.command()
async def 재미없어(ctx):
    await ctx.send('하아 괘씸하거든요?')

@bot.command()
async def 심심이(ctx):
    await ctx.send('존나 쌘척하더니 현피뜨니까 내가 바름 ㅋ')

@bot.command()
async def 알파고(ctx):
    await ctx.send('롤모델')

@bot.command()
async def 배추봇(ctx):
    await ctx.send('배추!')

@bot.command()
async def 슷칼봇(ctx):
    await ctx.send('슨칼봇은 어때요?')

@bot.command(aliases=['미육봇', 'mee6', 'MEE6'])
async def 미육(ctx):
    await ctx.send('인싸봇 부럽다 ㅜ')

@bot.command()
async def 잉(ctx):
    await ctx.send('잉어!')

@bot.command()
async def 이잉(ctx):
    await ctx.send('귀여운척 하지마 ㅗㅗ')

@bot.command()
async def 이이잉(ctx):
    await ctx.send('ㅄ')

@bot.command()
async def 무한(ctx):
    await ctx.send('도전 망함 수고ㅋㅋ')

@bot.command()
async def 이띵박(ctx):
    await ctx.send('이명박')

@bot.command()
async def 일박(ctx):
    await ctx.send('이일')

@bot.command()
async def 톰(ctx):
    await ctx.send('크루즈')

@bot.command()
async def 상상도(ctx):
    await ctx.send('모단 증체 ㄴㅇㄱ')

@bot.command()
async def 삼켜(ctx):
    await ctx.send('시발')

@bot.command()
async def 주워(ctx):
    await ctx.send('네?')

@bot.command()
async def ㄴㅇㄱ(ctx):
    await ctx.send('상상도못한정체!')

@bot.command()
async def 로리(ctx):
    await ctx.send('으 꺼져')

@bot.command()
async def 페도(ctx):
    await ctx.send('으 꺼져 좆같은 새끼야')

@bot.command()
async def 자위(ctx):
    await ctx.send('찐')

@bot.command()
async def 싼다(ctx):
    await ctx.send('안에 싸줘..')

@bot.command()
async def 공산당(ctx):
    await ctx.send('나는 콩사탕이 싫어요!')

@bot.command()
async def 콩사탕(ctx):
    await ctx.send('나는 콩사탕이 싫어요!')

@bot.command()
async def 엎드려(ctx):
    await ctx.send('게이')

@bot.command()
async def 누워(ctx):
    await ctx.send('벌떡')

@bot.command()
async def 앉아(ctx):
    await ctx.send('저는 강아지가 아니라 오리인데요...')

@bot.command()
async def 굴러(ctx):
    await ctx.send('흥 시러요')

@bot.command()
async def 오리(ctx):
    await ctx.send('꽥꽥')

@bot.command()
async def 오리고기(ctx):
    await ctx.send('고소했읍니다.')

@bot.command()
async def 혈액형(ctx):
    await ctx.send('업서')

@bot.command()
async def 사람(ctx):
    await ctx.send('영어로 휴먼!')

@bot.command()
async def 부먹(ctx):
    await ctx.send('예아 안 될 거 뭐 있노')

@bot.command()
async def 찍먹(ctx):
    await ctx.send('예아 안 될 거 뭐 있노')

@bot.command()
async def 민트초코(ctx):
    await ctx.send('좆같은거 치우세요')

@bot.command()
async def 민초(ctx):
    await ctx.send('치약이나 짜먹으세요')

@bot.command()
async def 신천지(ctx):
    await ctx.send('헉')

@bot.command()
async def 젤리(ctx):
    await ctx.send('마싯따')

@bot.command()
async def 아기(ctx):
    await ctx.send('페도 꺼져')

@bot.command()
async def 좋아(ctx):
    await ctx.send('ㅇ')

@bot.command()
async def 누짱(ctx):
    await ctx.send('처음 들어보는 말인걸요?')

@bot.command()
async def 싫어(ctx):
    await ctx.send('나도 너 싫어 좆같은놈아 ㅗㅗㅗㅗ')

@bot.command()
async def 슬퍼(ctx):
    await ctx.send('너 슬픈데 뭐 어쩌라고 아ㅋㅋ 내가 니 엄마냐고 아ㅋㅋ')

@bot.command()
async def 기뻐(ctx):
    await ctx.send('ㅊㅋㅊㅋ')

@bot.command()
async def 화나(ctx):
    await ctx.send('어쩔 ㅋ')

@bot.command()
async def 착해(ctx):
    await ctx.send('나 착해요')

@bot.command()
async def 국방장관(ctx):
    await ctx.send('나 국방장관이요')

@bot.command()
async def 참모총장(ctx):
    await ctx.send('나 참모총장이요')

@bot.command()
async def 배(ctx):
    await ctx.send('배도 잘만들고')

@bot.command()
async def 결혼하자(ctx):
    await ctx.send('예아 안 될 거 뭐 있어요 씨발놈아')

@bot.command()
async def 사귀자(ctx):
    await ctx.send('ㄷㄷ')

@bot.command()
async def 간질간질(ctx):
    await ctx.send('으 으흣 으헛 우흥~')

@bot.command()
async def 애교(ctx):
    await ctx.send('어 꺼져')

@bot.command()
async def 예뻐(ctx):
    await ctx.send('아...')

@bot.command()
async def 딱대(ctx):
    await ctx.send('미친놈')

@bot.command()
async def 가버렷(ctx):
    await ctx.send('응 너 혼자 잘가~')

@bot.command()
async def 맛있어(ctx):
    await ctx.send('뭐가 맛있어 미친놈아')

@bot.command()
async def 벌려(ctx):
    await ctx.send('아~')

@bot.command()
async def 뭐시여(ctx):
    await ctx.send('예?')

@bot.command()
async def 뭐여(ctx):
    await ctx.send('머래노')

@bot.command()
async def 건전(ctx):
    await ctx.send('지')

@bot.command()
async def 음란(ctx):
    await ctx.send('안돼요!')

@bot.command()
async def 갸우뚱(ctx):
    await ctx.send('크시세요?')

@bot.command()
async def 크시따라해봐(ctx):
    await ctx.send('(갸우뚱)')

@bot.command()
async def 히토미(ctx):
    await ctx.send('hitomi 사랑해')

@bot.command()
async def 나이(ctx):
    await ctx.send('2020년생이에요!')

@bot.command()
async def 응애(ctx):
    await ctx.send('응애 나 아기 파이드')

@bot.command()
async def 생일(ctx):
    await ctx.send('2020년 12월 22일 화요일!')

@bot.command()
async def 피아제(ctx):
    await ctx.send('아!내가 받았다.')

@bot.command()
async def 공중제비(ctx):
    await ctx.send('휘리릭')

@bot.command()
async def 나빠(ctx):
    await ctx.send('미안해...')

@bot.command()
async def 김재규(ctx):
    await ctx.send('재규어 열사님 화이팅!')

@bot.command()
async def 피아노(ctx):
    await ctx.send('피아누 너무 재밌어요!')

@bot.command()
async def 죽어(ctx):
    await ctx.send('너무해요...')



bot.run(w)
