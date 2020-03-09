A = input()
B = input()
ha,ma,sa = map(int,A.split(":"))
hb,mb,sb = map(int,B.split(":"))
if A == B:   # 24시간 기달려야함
    print('24:00:00')
elif A < B: # B - A
    s = sb - sa
    if s<0:
        s+= 60
        mb -= 1
    m = mb - ma
    if m<0:
        m += 60
        hb -= 1
    h = hb - ha
    print("%02d:%02d:%02d"%(h,m,s))
else:  # A>B (B+ 24-A)
    s = 0 - sa
    if s<0:
        s += 60
        ma += 1
    m = 0 - ma
    if m < 0:
        m += 60
        ha += 1
    h = 24 - ha
    s = s + sb
    if s >= 60:
        s -= 60
        m += 1
    m = m +mb
    if m >=60:
        m -= 60
        h += 1
    h = h+ hb
    if h>=24:
        h -= 24
    print("%02d:%02d:%02d" % (h, m, s))
