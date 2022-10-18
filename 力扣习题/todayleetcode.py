import requests
import json
import datetime
import  html2text as ht

user_agent = r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34'
session = requests.Session()
leetcode_gql_url = 'https://leetcode-cn.com/graphql'
headers = {
    'User-Agent': user_agent, 
    'Connection': 'keep-alive',
    'Content-Type': 'application/json'
}

def get_today_problem():
    params = {
        'operationName': 'questionOfToday',
        'variables': {},
        'query': '''query questionOfToday {
            todayRecord {
                question {
                    questionFrontendId
                    questionTitleSlug
                }
            }
        }'''
    }
    json_data = json.dumps(params).encode('utf8')
    headers['Referer'] = 'https://leetcode-cn.com/problemset/all/'
    resp = session.post(leetcode_gql_url, data = json_data, headers = headers, timeout = 10)
    content = resp.json()
    return content['data']['todayRecord'][0]['question']['questionTitleSlug']


def get_problem_by_slug(slug):
    params = {'operationName': 'getQuestionDetail',
        'variables': {'titleSlug': slug},
        'query': '''query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionTitle
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

today_problem = get_today_problem()
res = get_problem_by_slug(today_problem)
print(f'今日每日一题: {res["translatedTitle"]}, 难度: {res["difficulty"]}')

# date = datetime.datetime.now()
# file_name = f'{date.strftime("%Y%m%d")}_{today_problem}.md'
# with open(file_name, 'w', encoding='utf-8') as f:
#     f.write(f'# {res["translatedTitle"]}\n### 难度 {res["difficulty"]}\n{res["translatedContent"]}')

# print(f'题目描述已经保存到 {file_name}')
md = ht.html2text(res['translatedContent'])
print(md)

input('press any key to continue')
