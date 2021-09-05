import os
import re
import requests
import json
import html2text as ht

user_agent = r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'
session = requests.Session()
leetcode_gql_url = 'https://leetcode-cn.com/graphql'
headers = {
    'User-Agent': user_agent, 
    'Connection': 'keep-alive',
    'Content-Type': 'application/json'
}

folder_name = '剑指'

pic_pattern = re.compile('(https?://.+\.(?:png|jpg))')

def get_problem_by_slug(slug):
    params = {'operationName': 'getQuestionDetail',
        'variables': {'titleSlug': slug},
        'query': '''query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionTitle
                questionFrontendId
                translatedTitle
                translatedContent
                difficulty
            }
        }'''
    }

    json_data = json.dumps(params).encode('utf8')
    headers['Referer'] = f'https://leetcode-cn.com/problems/{slug}'
    resp = session.post(leetcode_gql_url, data = json_data, headers = headers, timeout = 10)
    content = resp.json()

    # 题目详细信息
    question = content['data']['question']
    return question

if not re.search(folder_name, os.getcwd()):
    if os.path.isdir(folder_name):
        os.chdir(folder_name)
    else:
        os.mkdir(folder_name)

# item_no = input('请输入题目编号. 名称: ')
# item_name = item_no.split('. ')[-1]
# item_no = item_no.split('. ')[0]
item_url = input('请输入题目url: ')
item_slug = item_url.split('problems/')[1].replace('/', '')
data = get_problem_by_slug(item_slug)
item_no = data['questionFrontendId'].split(' ')[-1]
item_name = data['translatedTitle']

dir_path = item_no + item_name
if os.path.exists(dir_path):
    input('题目已存在, 退出\n')
os.mkdir(dir_path)

# get pic
pic_list = pic_pattern.findall(data['translatedContent'])
for i in pic_list:
    tmp = session.get(i, headers=headers)
    pic_name = i.split('/')[-1]
    pic_path = dir_path + '/' + pic_name
    with open(pic_path, 'wb') as f:
        f.write(tmp.content)
    print(f'下载图片 {pic_name} 到 {pic_path}')
    data['translatedContent'] = data['translatedContent'].replace(i, './' + pic_name)


content = '# 题目\n\n## {0}\n\n### 来源:\n\n[力扣-{0}]({1})\n\n### 题目内容\n\n'.format(
    item_name, item_url)

content += ht.html2text(data['translatedContent'])


with open(dir_path + '/README.md', 'w', encoding='utf-8') as f:
    f.write(content)

with open(dir_path + '/' + item_url.split('/')[-2].replace('-', '') + '.py',
          'w', encoding='utf-8') as f:
    f.write('# ')
