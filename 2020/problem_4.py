"""
    Reference : https://www.snoopybox.co.kr/2054
""" 

REVERSED = 1
STRAIGHT = 0
MAX = 100001

def solution(words, queries):
    trie = make_trie(words)
    return request_queries(queries, trie)
        
def make_trie(words):
    trie = [[{}, {}] for _ in range(MAX)] 

    for word in words:
        cur = trie[len(word)][STRAIGHT]
        r_cur = trie[len(word)][REVERSED]

        for i in range(len(word)):
            cur['count'] = cur.get('count', 0) + 1
            r_cur['count'] = r_cur.get('count', 0) + 1

            cur.setdefault(word[i], {})
            r_cur.setdefault(word[len(word) - i - 1], {})

            cur = cur[word[i]]
            r_cur = r_cur[word[len(word) - i - 1]]

    return trie

def request_queries(queries, trie):
    return [search(query, trie) for query in queries]

def search(query, trie):
    cur = trie[len(query)][REVERSED] if query[0] == '?' else trie[len(query)][STRAIGHT]
    for character in query[::-1] if query[0] == '?' else query:
        if character == '?': return cur.get('count', 0)
        elif character not in cur: return 0
        else: cur = cur[character]
