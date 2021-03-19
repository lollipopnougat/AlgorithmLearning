import re


class Node:
    def __init__(self, char: str) -> None:
        self.num = 1
        self.char = char
        self.next = {}


def trie_tree(root: Node, words: str):
    head = root
    for i in words:
        if i == ' ':
            root = head
            continue
        if i in root.next:
            root = root.next[i]
            root.num += 1
        else:
            root.next[i] = Node(i)
            root = root.next[i]


def get_word_frequency(root: Node, word: str) -> int:
    for i in word:
        if i in root.next:
            root = root.next[i]
        else:
            return 0
    return root.num


def del_punctuation(st: str) -> str:
    return re.sub(r'[^\w\s]', '', st).replace('\n', ' ')


def main():
    root = Node('')
    head = root
    with open('article.txt', 'r',encoding='utf-8') as f:
        strs = f.read()
        res = del_punctuation(strs).lower()
        trie_tree(root, res)
        print(get_word_frequency(root, 'today'))
        print(get_word_frequency(root, 'life'))

main()



