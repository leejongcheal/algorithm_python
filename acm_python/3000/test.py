for i in range(1, n):
    a = i;
    m = 1;
    q = []
    while 1:
        q += [a]
        if a < n and l[a] > 0:
            m = l[a]
            break
        a = a // 2 if a % 2 == 0 else a * 3 + 1

    for i in reversed(q):
        m = max(i, m)
        if i < n:
            l[i] = m
