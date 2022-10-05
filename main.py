import random
import requests
from bs4 import BeautifulSoup
import resource

if __name__ == '__main__':
    for i in range(0, 10):
        headers = {
            'User-Agent': random.choice(resource.user_Agent),
            'Cookie': 'll="118254"; bid=65N9pHVm0Do; __gads=ID=0be353168f7fe61b-226b6780e8d0004a:T=1646830290:RT=1646830290:S=ALNI_Mbn978gn1xpvgEPoJzhYN96eKR5sQ; __gpi=UID=000005addd52e8c4:T=1653310722:RT=1655789591:S=ALNI_MYVa8ZboNItjBGm8Fmg2kCQUrYeuQ; dbcl2="263207696:qs13W7Ez1KU"; ck=PUUL; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1664434945%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.3ac3=*; __utma=30149280.335913384.1648121337.1655789573.1664434945.4; __utmc=30149280; __utmz=30149280.1664434945.4.4.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt_douban=1; __utma=81379588.1304925188.1664434945.1664434945.1664434945.1; __utmc=81379588; __utmz=81379588.1664434945.1.1.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; push_noty_num=0; push_doumail_num=0; __utmb=30149280.2.10.1664434945; __utmb=81379588.2.10.1664434945; _pk_id.100001.3ac3=c02c16a28a561d03.1664434945.1.1664435087.1664434945.'
        }
        res = requests.get(resource.url[i], headers=headers)
        soup = BeautifulSoup(res.text, 'lxml')
        tags = soup.find_all('td', attrs={'width': None, 'valign': 'top'})
        for tag in tags:
            # 提取书名和链接
            link = tag.find('a').get('href')
            name = tag.find('a').get('title')
            # 提取作者
            author = tag.find('p').get_text()
            end = author.find('/')
            author = author[0:end - 1]
            # 提取评分
            rating = tag.find('span', attrs={'class': 'rating_nums'}).get_text()
            # 提取引言
            try:
                quote = tag.find('span', attrs={'class': 'inq'}).get_text()
            except AttributeError:
                quote = None
            print(name, author, rating, quote, link)
