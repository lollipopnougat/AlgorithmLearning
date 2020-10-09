import os

item_no = input('请输入题目编号. 名称: ')
item_name = item_no.split('. ')[-1]
item_no = item_no.split('. ')[0]
item_url = input('请输入题目url: ')
dir_path = item_no + item_name
os.mkdir(dir_path)

content = '# 题目\n\n## {0}\n\n### 来源:\n\n[力扣-{0}]({1})\n\n### 题目内容'.format(
    item_name, item_url)

with open(dir_path + '/README.md', 'w', encoding='utf-8') as f:
    f.write(content)

with open(dir_path + '/' + item_url.split('/')[-2].replace('-', '') + '.py',
          'w', encoding='utf-8') as f:
    f.write('# ')
