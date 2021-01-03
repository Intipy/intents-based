# -*- coding: utf-8 -*- 

import discord
import asyncio
import os
from discord.ext import commands
from discord.ext.commands import bot
import random
from discord.utils import get

w = 'NzkwODQ2MTM1MzIxMjMxMzgx.X-Gi2w.wd8kpfrRxsrJVKvGISXl8ICgzq'+'U'

bot = commands.Bot(command_prefix = '파이드 ') 

@bot.command()  
async def 도움말(ctx):
    embed = discord.Embed(colour = 808000)
    embed.add_field(name='파이드와 대화하기', value='파이드 [하고 싶은 말] <--(ex: 파이드 사랑해)', inline=False)
    embed.add_field(name='파이드의 기능들', value='파이드 명령어라고 해보세요!', inline=False)
    embed.add_field(name='파이드에게 대답 가르치기', value='파이드 배워라고 해보세요!', inline=False)
    embed.add_field(name='파이드가 대답을 안한다면?', value='오류보단 대답을 몰라서 못하는 경우가 많아요. 대답을 못한다면 대답을 가르쳐보세요!', inline=False)
    embed.add_field(name='파이드 업데이트', value='파이드는 매일 11시~12시 사이에 업데이트를 해요. 여러분이 가르친 말, 버그 수정 등이 적용돼요.', inline=False)
    await ctx.send(embed=embed)

@bot.command() 
async def sta(ctx):
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("'파이드 도움말'이라고 하면 파이드 이용 방법을 알려드려요"))

@bot.command()
async def 배워(ctx):
    embed = discord.Embed(colour = 808000)
    embed.add_field(name='무엇을 배울까요?', value='[가르칠 말] [대답] <--(ex:엄준식 화이팅)', inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 명령어(ctx):
    embed = discord.Embed(colour = 808000)
    embed.add_field(name='파이드 주사위', value='1~6까지의 숫자가 나와요!', inline=False)
    embed.add_field(name='파이드 동전', value='앞면, 또는 뒷면이 나와요!', inline=False)
    embed.add_field(name='파이드 세로로엄준식', value='엄준식을 세로로 완성해드려요!', inline=False)
    embed.add_field(name='파이드 명언', value='파이드가 명언을 읊어줘요!', inline=False)
    await ctx.send(embed=embed)

rannum = ['1이 나왔어요!', '2가 나왔어요!', '3이 나왔어요!', '4가 나왔어요!', '5가 나왔어요!', '6이 나왔어요!']

@bot.command()
async def 주사위(ctx):
   await ctx.send(rannum[random.randint(0,5)])

@bot.command()
async def 동전(ctx):
    if random.randint(1,2) == 1:
        await ctx.send('앞면이 나왔네요!')

    else:
        await ctx.send('뒷면이 나왔네요!')

@bot.command()
async def 세로로엄준식(ctx):
    embed = discord.Embed(colour = 808000)
    embed.add_field(name='엄', value='ㅤ', inline=False)
    embed.add_field(name='준', value='ㅤ', inline=False)
    embed.add_field(name='식', value='ㅤ', inline=False)
    await ctx.send(embed=embed)

mu = ['길을 아는 것과 그 길을 걷는 것은 다르다.','남의 불행 위에 내 행복을 쌓으면 남의 불행이 사라지는 순간 행복이 무너질 것이다.','성공은 친구를 만들고 역경은 친구를 시험한다.','모든 길의 끝은 발길을 돌리는 그 지점이다.','당신이 죽어도 생명은 죽지 않는다.','삶이 있는 한 희망은 있다.','산다는것 그것은 치열한 전투이다. ','돈이란 바닷물과도 같다. 그것은 마시면 마실수록 목이 말라진다.','하루에 3시간을 걸으면 7년 후에 지구를 한바퀴 돌 수 있다.','언제나 현재에 집중할수 있다면 행복할것이다.','진정으로 웃으려면 고통을 참아야하며 , 나아가 고통을 즐길 줄 알아야 해.','신은 용기있는자를 결코 버리지 않는다.','피할수 없으면 즐겨라.','단순하게 살아라. 현대인은 쓸데없는 절차와 일 때문에 얼마나 복잡한 삶을 살아가는가?','먼저 자신을 비웃어라. 다른 사람이 당신을 비웃기 전에.','행복한 삶을 살기위해 필요한 것은 거의 없다.','어리석은 자는 멀리서 행복을 찾고, 현명한 자는 자신의 발치에서 행복을 키워간다.','어리석은 자는 멀리서 행복을 찾고, 현명한 자는 자신의 발치에서 행복을 키워간다.','한번의 실패와 영원한 실패를 혼동하지 마라.','내일은 내일의 태양이 뜬다.','행복은 습관이다. 그것을 몸에 지니라.','평생 살 것처럼 꿈을 꾸어라.그리고 내일 죽을 것처럼 오늘을 살아라.','1퍼센트의 가능성, 그것이 나의 길이다. -나폴레옹-','통이 남기고 간 뒤를 보라! 고난이 지나면 반드시 기쁨이 스며든다.','나이가 60이다 70이다 하는 것으로 그 사람이 늙었다 젊었다 할 수 없다. 늙고 젊은 것은 그 사람의 신념이 늙었느냐 젊었느냐 하는데 있다.','만약 우리가 할 수 있는 일을 모두 한다면 우리들은 우리자신에 깜짝 놀랄 것이다.','눈물과 더불어 빵을 먹어 보지 않은 자는 인생의 참다운 맛을 모른다. ','해야 할 것을 하라. 모든 것은 타인의 행복을 위해서, 동시에 특히 나의 행복을 위해서이다.','사람이 여행을 하는 것은 도착하기 위해서가 아니라 여행하기 위해서이다. ','재산을 잃은 사람은 많이 잃은 것이고, 친구를 잃은 사람은 더 많이 잃은 것이며, 용기를 잃은 사람은 모든것을 잃은 것이다.','이룰수 없는 꿈을 꾸고 이길수 없는 적과 싸우며, 이룰수 없는 사랑을 하고 견딜 수 없는 고통을 견디고, 잡을수 없는 저 하늘의 별도 잡자.','작은 기회로 부터 종종 위대한 업적이 시작된다.','인생이란 학교에는 불행 이란 훌륭한 스승이 있다. 그 스승 때문에 우리는 더욱 단련되는 것이다.','세상은 고통으로 가득하지만 그것을 극복하는 사람들로도 가득하다.','인간의 삶 전체는 단지 한 순간에 불과하다 . 인생을 즐기자.','절대 어제를 후회하지 마라 . 인생은 오늘의 나 안에 있고 내일은 스스로 만드는 것이다','삶이 그대를 속일지라도 슬퍼하거나 노하지 말아라 슬픈 날에 참고 견디라 . 즐거운 날은 오고야 말리니 마음은 미래를 바라느니 현재는 한없이 우울한것 모든건 하염없이 사라지나가 버리고 그리움이 되리니','문제점을 찾지 말고 해결책을 찾으라.','길을 잃는 다는 것은 곧 길을 알게 된다는 것이다.','삶을 사는 데는 단 두가지 방법이 있다. 하나는 기적이 전혀 없다고 여기는 것이고 또 다른 하나는 모든 것이 기적이라고 여기는방식이다.','당신 가슴 속 작은 사람은 언제 죽었는가?','먼지 한톨이 잘 정비된 우주선을 폭파시킨다.','성공으로 가는 엘리베이터는 고장입니다. 당신은 계단을 이용해야만 합니다. 한계단 한계단씩','가난은 가난하다고 느끼는 곳에 존재한다.','인생에 뜻을 세우는데 있어 늦은 때라곤 없다.','인생을 다시 산다면 다음번에는 더 많은 실수를 저지르리라.','우리는 두려움의 홍수에 버티기 위해서 끊임없이 용기의 둑을 쌓아야 한다. ','겨울이 오면 봄이 멀지 않으리.','엄준식은 하룻밤에 생기지 않았다.','모든것들에는 나름의 경이로움과 심지어 어둠과 침묵이 있고 , 내가 어떤 상태에 있더라도 나는 그속에서 만족하는 법을 배운다.','계단을 밟아야 계단 위에 올라설수 있다.','고개 숙이지 마십시오. 세상을 똑바로 정면으로 바라보십시오.','길이 끊겼는가? 뛰어라. 길이 막혔는가? 넘어라. 길이 없는가? 만들어라.','대부분 사람 안의 마음은 연약하디 연약해 쉬이 부서지지만 이는 자신의 마음이 단단하지 않다는 증거이다.','죽은 시체 위에서 밥을 배불리 먹을수 있으랴.','꿈은 산보다 높고 하늘보다 높으며 우주보다 높다. 한가지 다행인점은 떨어져도 다시 오를 수 있다는 것이다.','지상과 지하의 다른점은 빛이 있느냐 없느냐가 아닌 빛이 올 것이라 믿느냐이다.','발등 위 무릎보단 저멀리 손가락이 발등에 닿는 법이다.','당신이 모든걸 잃는다면, 당신은 죽은것이 아니라 그저 다시 태어났을 뿐이다.','내 안에서 불타는 투지는 무엇보다 뜨거워 어떤 공포로 얼어붙은 마음이든 녹일 수 있다.','기름보단 물이 깨끗하지만, 그렇다고 비싼건 아니다.','청렴이라는 허상은 청렴을 요구하는 사람들의 비디오게임에서나 가능하다.','의외로 불꽃 안이 덜 뜨거운 법이다.','태풍의 눈이 고요하다고 그곳에 쉽게 갈 수 있는가? 완벽히 아니다. ','깨끗한 물이 흐르면 소리가 잘 들리지만 더러운 구정물이 흐르면 냄새만 날 뿐이다.','떨어질 때가 가장 많은 생각이 들 것이다.','내 인생은 완벽한 각본대로 움직이는 완벽한 쇼였고 나는 만족한다고 생각하는 것이 내가 하는 연기이다.','죽었지만 살아있는 땅을 기는 인생, 얼마나 비참한가. 나는 그것을 사람의 살을 뜯어먹는 좀비라 부른다. 의외로 좀비가 실존한다는걸 아는가?','되찾을 수 없는게 세월이니 시시한 일에 시간을 낭비하지 말고 순간순간을 후회 없이 잘 살아야 한다.','너에게 아무도 시간을 팔지 않는다. 마찬가지로 니가 팔 수도 없다. 그저 이용할 뿐이다.','니 영화는 최악이야. 재미가 없지. 아무도 거들떠 보지 않아. 대부분의 사람의 인생은 이런 영화와 같다.','신념에 있어 옳고 그름은 신만이 판단할 수 있다','그대 자신의 영혼을 탐구하라.','꿈을 계속 간직하고 있으면 반드시 실현할 때가 온다.','화려한 일을 추구하지 말라. 중요한 것은 스스로의 재능이며, 자신의 행동에 쏟아 붓는 사랑의 정도이다.','흔히 사람들은 기회를 기다리고 있지만 기회는 기다리는 사람에게 잡히지 않는 법이다. ','너 자신을 알라.','무언가를 모른다면 자신에게 거짓말을 하지말라. 그저 배울 뿐이다.','당신의 인생은 성공했는가? 그렇다면 얼마에 팔 수 있는가? 당신의 목숨값보다 귀하다면 그것은 성공한 것이다.','세상을 향해 질문을 하면 당연히 대답해 줄 거라고 생각지 마라. 그것은 어린아이와 같은 유치한 생각이다.','사람들은 진실을 말해주지 않는다. 그들이 말하는 것은 자신에게 유리한 것일 뿐,진위는 모르는 것이다. 스스로 찾아라.','사회는 장난이 아니다. 진검승부다. 죽음과 연결된다. 그것을 바로 인식하지 못하면 무엇도 해낼 수 없다. 언제나 낙오자이며 사회 부적합자일 뿐이다.','현재를 즐겨라.','돈은 목숨보다 중하다.','네 눈물은 그저 물이다. 그 뿐이다.','니 어리광을 받아주는건 살아있지 못한 것 뿐일것이다.','당신의 죽음의 가치는 그저 사람 하나, 그 정도다. 그 가치를 올린다면 당신은 죽어도 죽지 않을 것이다.','독을 탄 진수성찬보다 선의로 보이는 사탕 하나를 조심하라','목숨은 두번째다. 첫번째는 인생이다.','전투가 아니라 전쟁에서 승리하라.','천사가 내려와 금과 지혜 중 고르라하면 무엇을 가져야하는가? 천사를 쓰러트려서라도 모두 가져가라. 빼앗고 얻는 것이 인생이다.','죽음보단 죽은 삶이 무서운 법이다.','바닥을 닦아도 바닥은 바닥이다.','돋보기로 뭔가를 보면 크게 잘보인다. 하지만 시야를 잃는다. 이 시야가 무엇보다 중할 때가 소리 없이 온다. 이득이 아니라 인생을 보라.','나무가 아니라 숲을 보라지만 나무 하나를 진득히 바라봐야 할 때가 있는 법이다.','뒤를 보면 잡힌다.','기회라는 놀이동산은 쉽게 찾아온다. 당신은 대부분 그곳에 들어가고도 어딘지도 모르며 나갈것이다. 놓친 기회는놀이동산의 출구이다. 다시 돌아와도 열리지 않는 문이다.','지구 위에 기회는 얼마든지 있다. 하지만 단언컨대 그걸 믿지 못하는 사람에게 기회는 쉽게 토라져 등돌린다.','목소리는 섞이면 그저 소음이다. 하지만 합창단은 사람의 마음을 움직이는 법이다.','인생이 망했다고 생각하는가? 그렇다면 당신의 인생은 망했고, 망할 것이며, 망해야 할 것이다.']

@bot.command()
async def 명언(ctx):
    await ctx.send(mu[random.randint(0,99)])

@bot.command(aliases=['안영','않영','않녕','앉영','앉녕'])
async def 안녕(ctx):
    await ctx.send('반가워요!')

@bot.command(aliases=['빙신', '븅신', '피융신'])
async def 병신(ctx):
    await ctx.send('어 좆까~')

@bot.command(aliases=['너검'])
async def 느금(ctx):
    await ctx.send('응 니미~')

@bot.command(aliases=['너검마'])
async def 느금마(ctx):
    await ctx.send('어 니애미~')

@bot.command(aliases=['좃까', '좆가', '족까','좃가','족가'])
async def 좆까(ctx):
    await ctx.send('니 좆이나 까 소추새끼야~')

@bot.command(aliases=['은아니매','응아니메','응아니매'])
async def 은아니메(ctx):
    await ctx.send('은 마즈메')

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
    await ctx.send('크아악! 너무 강해요!')

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

@bot.command(aliases=['페미니스트'])
async def 페미(ctx):
    await ctx.send('여성인권을 위해 싸우시는 대단한 분들이에요!')

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
    await ctx.send('자살은 안돼요!')

@bot.command()
async def 박정희(ctx):
    await ctx.send('탕탕')

@bot.command()
async def 탕탕(ctx):
    await ctx.send('좀 더 대국적으로 하십시오')

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
    await ctx.send('쥬석ㅋㅋㅋㅋㅋ 쥬기장ㅋㅋㅋㅋㅋ 쥬메이카ㅋㅋㅋㅋ 쥬스민ㅋㅋㅋㅋㅋ')

@bot.command(aliases=['광주는?'])
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
    await ctx.send('네 다음 디첩')

@bot.command()
async def 월수(ctx):
    await ctx.send('양산형 김근육 좆같이 찍어내는 공장')

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

@bot.command(aliases=['라면먹고갈래?'])
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
    await ctx.send('롤모델!')

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
    await ctx.send('으 으흣 으힉 우흥~')

@bot.command()
async def 애교(ctx):
    await ctx.send('어 꺼져')

@bot.command()
async def 예뻐(ctx):
    await ctx.send('아... 네...')

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

@bot.command(aliases=['음란물'])
async def 음란(ctx):
    await ctx.send('안돼요!')

@bot.command(aliases=['(갸우뚱)'])
async def 갸우뚱(ctx):
    await ctx.send('크시세요?')

@bot.command()
async def 크시따라해봐(ctx):
    await ctx.send('(갸우뚱)')

@bot.command()
async def 히토미(ctx):
    await ctx.send('hitomi 사랑해요')

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
async def 따랑해(ctx):
    await ctx.send('싫어요!')

@bot.command(aliases = ['5월23일'])
async def 오월이십삼일(ctx):
    await ctx.send('노무현 전 대통령 서거일이에요!')

@bot.command(aliases=['523'])
async def 오이삼(ctx):
    await ctx.send('중력!')

@bot.command(aliases=['5시23분'])
async def 다섯시이십삼분(ctx):
    await ctx.send('중력시네요!')

@bot.command(aliases=['Skydra'])
async def skydra(ctx):
    await ctx.send('야갤 네임드!')

@bot.command()
async def 성의없어(ctx):
    await ctx.send('앞으론 잘 할게요...')

@bot.command()
async def 좌파(ctx):
    await ctx.send('정치 성향에 대한 편견은 없어요!')

@bot.command()
async def 우파(ctx):
    await ctx.send('우파루파!')

@bot.command()
async def 어머니(ctx):
    await ctx.send('어쩌라고')

@bot.command()
async def 복(ctx):
    await ctx.send('많이 받으세요!')

@bot.command()
async def 김유식(ctx):
    await ctx.send('나쁜놈!')

@bot.command(aliases=['디시인사이드', 'dcinside', 'dc인사이드'])
async def 디시(ctx):
    await ctx.send('싫어요!')

@bot.command()
async def 네이트판(ctx):
    await ctx.send('능지 딸리는 병신 사이트라고 들었어요!')

@bot.command(aliases=['트짹'])
async def 트위터(ctx):
    await ctx.send('트위터는 그저 하나의 음란물 클라우드이다 -존 로렌스')

@bot.command()
async def 서버(ctx):
    await ctx.send('???: 서버 샀죠')

@bot.command()
async def 니엄마(ctx):
    await ctx.send('우리 엄마 없엉ㅅ!')

@bot.command()
async def 노갤(ctx):
    await ctx.send('화무현 갤러리 노이팅!')

@bot.command()
async def 애미(ctx):
    await ctx.send('애미 말고 어머니라고 하는건 어떨까요?')

@bot.command()
async def 고아(ctx):
    await ctx.send('고아는 아니라구요!')

@bot.command()
async def 애미고아년(ctx):
    await ctx.send('헉')

@bot.command()
async def 샌즈(ctx):
    await ctx.send('WA!')

@bot.command()
async def 시발련아(ctx):
    await ctx.send('욕하지 마요!')

@bot.command()
async def 알았어(ctx):
    await ctx.send('고마워요')

@bot.command()
async def 싫은데(ctx):
    await ctx.send('너무해요')

@bot.command(aliases=['봉하'])
async def 봉하반점(ctx):
    await ctx.send('안돼요!')

@bot.command()
async def 봉하마을(ctx):
    await ctx.send('고향!')

@bot.command()
async def 엉덩이(ctx):
    await ctx.send('뒷치기')

@bot.command(aliases=['싫은데?'])
async def 싫은은데(ctx):
    await ctx.send('왜요...')

@bot.command()
async def 오레가사바크(ctx):
    await ctx.send('오크님을 응원합니다')

@bot.command()
async def 니얼굴(ctx):
    await ctx.send('잘생김')

@bot.command()
async def 당벅(ctx):
    await ctx.send('동생이나 형이나 병신')

@bot.command()
async def 워마드(ctx):
    await ctx.send('려성인권단체워마드힘내세요연대합시다')

@bot.command()
async def 싸우자(ctx):
    await ctx.send('반월동으로 와라 ㅋㅋ')

@bot.command()
async def 브베(ctx):
    await ctx.send('브베입니당')

@bot.command()
async def 고무통(ctx):
    await ctx.send('대령 전현무 노고통')

@bot.command()
async def 느개비(ctx):
    await ctx.send('응 느개비 따개비 바람개비~')

@bot.command()
async def 유치해(ctx):
    await ctx.send('응 아니거등~ 너가 너 유치하거등~')

@bot.command()
async def 멍청해(ctx):
    await ctx.send('똑똑해요!')

@bot.command()
async def 엄마도(ctx):
    await ctx.send('흒먼이야')

@bot.command()
async def 엄신(ctx):
    await ctx.send('엄마 신나')

@bot.command()
async def 게이(ctx):
    await ctx.send('길우진')

@bot.command()
async def 노무현자서전(ctx):
    await ctx.send('남자는 여자가 서너명은 있어야돼. 한명은 가정용 또 한명은 함께 춤출 수 있는 뻉뺑이용 그리고 인생과 예술을 논할 수 있는 오솔길용. 그 정도는 있어야 되는거 아니야? -노무현 자서전 중-')

@bot.command()
async def 김대중자서전(ctx):
    await ctx.send('나는 내가 호남사람이라는 것을 자랑스럽게 생각한다. -김대중 자서전 중-')

@bot.command()
async def 엄마가준비한식사(ctx):
    await ctx.send('여성혐오단어입니다사용을지양해보는건어떨까요지금대한민국은여혐이만연한한한남민국이라고해도과언이아닙니다')

@bot.command()
async def 반월동(ctx):
    await ctx.send('전라도')

@bot.command()
async def 레즈(ctx):
    await ctx.send('ㄲㅈ')

@bot.command()
async def 천안문(ctx):
    await ctx.send('나는 베이징의 천안문을 사랑해')

@bot.command()
async def 톈안먼(ctx):
    await ctx.send('워 아이 베이찡 톈안먼')

@bot.command()
async def 카카오톡(ctx):
    await ctx.send('툭하면 정지때리고 상담도 좆같이하는 독점기업 망해라!')

@bot.command()
async def 한강(ctx):
    await ctx.send('풍덩~')

@bot.command()
async def 노굼마(ctx):
    await ctx.send('누금마')

@bot.command()
async def 전화번호(ctx):
    await ctx.send('010 7079 2313')

@bot.command(aliases=['경찰서'])
async def 경찰(ctx):
    await ctx.send('국번없이 112')

@bot.command()
async def 소방서(ctx):
    await ctx.send('국번없이 119')

@bot.command()
async def 학교폭력(ctx):
    await ctx.send('학교폭력 신고는 117이에요!')

@bot.command()
async def 후장(ctx):
    await ctx.send('퍽퍽퍽')

@bot.command()
async def 이세돌(ctx):
    await ctx.send('화세돌 이이팅!')

@bot.command()
async def tv(ctx):
    await ctx.send('바보상자!')

@bot.command()
async def 개그콘서트(ctx):
    await ctx.send('망했어요!')

@bot.command(alaises=['싸이버펑크'])
async def 사이버펑크(ctx):
    await ctx.send('병신 죽어 ㅗㅗㅗㅗ')

@bot.command(aliases=['사펑'])
async def 싸펑(ctx):
    await ctx.send('응아니야 ㅗㅗㅗㅗ')

@bot.command()
async def ㄹ(ctx):
    await ctx.send('ㄹ첩 죽어 ')


bot.run(w)
