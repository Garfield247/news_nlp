import re
import jieba
from jieba import analyse
from newspaper import Article



def crawl_and_cut(url):
    news = Article(url, language='zh')
    news.download()
    news.parse()
    title = news.title
    text = news.text #re.sub(r'\n+','\n',news.text)
    keys = list(jieba.cut(text))
    context = ''.join([' `%s` |'%s if s != '\n' else '\n' for s in keys])
    textrank = {x:str(w) for x, w in analyse.extract_tags(text, withWeight=True ,topK=10)}
    result = '## 新闻标题\n\
**{titles}**\n\
## 关键词\n\
|关键词|&nbsp;词频|&nbsp;&nbsp;权重|\n\
| ---- | ---- | ---- |\n\
{textranks}\n\n\
## 分词结果\n  \
{contexts}'.format(titles=title,textranks = '\n'.join(['|%s |&nbsp; %d |&nbsp; %s|'%(str(k),keys.count(k),str(textrank[k])[0:5]) for k in textrank]),contexts=context)
    return result

def text_cut(text):
    keys = list(jieba.cut(text))
    context = ''.join([' `%s` |'%s if s != '\n' else '\n' for s in keys])
    textrank = {x:str(w) for x, w in analyse.extract_tags(text, withWeight=True ,topK=10)}
    result = '## 关键词\n\
|关键词|&nbsp;词频|&nbsp;&nbsp;权重|\n\
| ---- | ---- | ---- |\n\
{textranks}\n\n\
## 分词结果\n  \
{contexts}'.format(textranks = '\n'.join(['|%s |&nbsp; %d |&nbsp; %s|'%(str(k),keys.count(k),str(textrank[k])[0:5]) for k in textrank]),contexts=context)
    return result


# crawl_and_cut('https://news.163.com/18/1210/10/E2LILNA50001875P.html')
