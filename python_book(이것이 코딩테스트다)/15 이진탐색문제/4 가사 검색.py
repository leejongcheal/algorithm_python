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
        if q[0] == '?':
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