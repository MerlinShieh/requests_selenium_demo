
from requests_html import HTMLSession
from pprint import pprint
import pandas as pd
url = 'https://search.51job.com/list/040000,000000,0000,00,9,99,%25E8%25BD%25AF%25E4%25BB%25B6%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?'
session = HTMLSession()
r = session.get(url=url)
# print(r)

class html_51job:
	def __init__(self, url, web_html_file='../file/web_html.html'):
		self.url = url
		self.web_html_file = web_html_file

# html = r.html.xpath("//div[@id='resultList']/div")
html = r.html.xpath("//div[@class='dw_table']/div[@class='el']")
# pprint(type(html))
dict_ = {}


job_name = []
com_name = []
com_local = []
money = []

for ele in range(len(html)):
	text = html[ele].text
	links = html[ele].links

	text_list = text.split()
	list_links = links

	dict_[text] = links
	job_name.append(text_list[0])
	com_name.append(text_list[1])
	com_local.append(text_list[2])
	money.append(text_list[3])
df = pd.DataFrame()
df['职位名称'] = job_name
df['公司名称'] = com_name
df['公司位置'] = com_local
df['工资'] = money
print(df)
df.to_csv('data.csv')