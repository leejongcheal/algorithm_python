from bisect import bisect_left, bisect_right

def solution(words, queries):
    answer = []
    word_by_len = [[] for _ in range(11000)]
    reverse_by_len = [[] for _ in range(11000)]
    for w in words:
        word_by_len[len(w)].append(w)
        reverse_by_len[len(w)].append(w[::-1])
    for w in range(len(word_by_len)):
        word_by_len[w].sort()
        reverse_by_len[w].sort()
    for q in queries:
        len_q = len(q)
        # 거꾸로
        cnt = 0
        if q[0] == '?':from bisect import bisect_left, bisect_right
def solution(words, queries):
    cnt_words = [[] for _ in range(10001)]
    cnt_reverse_words = [[] for _ in range(10001)]
    words.sort()
    res = []
    for w in words:
        cnt_words[len(w)].append(w)
        cnt_reverse_words[len(w)].append(w[::-1])
    for i in range(10001):
        cnt_reverse_words[i].sort()
    for querie in queries:
        left = ""
        right = ""
        # change 내장함수로 시간초과인경우 줄이기
        for q in querie:
            if q == "?":
                left += "a"
                right += "z"
            else:
                left += q
                right += q
        if querie[0] != "?":
            cnt = bisect_right(cnt_words[len(querie)], right) - bisect_left(cnt_words[len(querie)], left)
        else:
            left, right = left[::-1], right[::-1]
            cnt = bisect_right(cnt_reverse_words[len(querie)], right) - bisect_left(cnt_reverse_words[len(querie)], left)
        res.append(cnt)
    return res
words = list(input().split())
queries = list(input().split())
print(solution(words,queries))


"""
예시 
frodo front frost frozen frame kakao
fro?? ????o fr??? fro??? pro?

        for q in querie:
            if q == "?":
                left += "a"
                right += "z"
            else:
                left += q
                right += q
        이부분을 간편하게 left = q.replace("?", "a") 처럼 사용해도 되는데 시간초과 뜨니 상관없음
"""
            rq = q[::-1]
            ra = rq.replace('?', "a")
            rz = rq.replace('?', "z")
            cnt = bisect_right(reverse_by_len[len_q],rz) - bisect_left(reverse_by_len[len_q], ra)
        elif q[0] != '?':
            qa= q.replace('?', "a")
            qz= q.replace('?', 'z')
            cnt = bisect_right(word_by_len[len_q], qz) - bisect_left(word_by_len[len_q], qa)
        answer.append(cnt)
    return answer


words = list(input().split())
queries = list(input().split())
print(solution(words,queries))