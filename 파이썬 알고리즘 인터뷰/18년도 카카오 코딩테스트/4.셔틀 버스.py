# https://programmers.co.kr/learn/courses/30/lessons/17678

def get_m_int(time):
    h = int(time[:2])
    m = int(time[3:])
    return int(h)*60 + int(m)
def get_hhmm(val : int):
    h = val // 60
    m = val % 60
    return str(h).zfill(2)+":"+str(m).zfill(2)
# 분을 기준으로 시간을 정수화 시키자
def solution(n, t, m, timetable):
    person = []
    bus = [[9*60,m]]
    for i in range(n-1):
        bus.append([bus[-1][0]+t, m])
    for t in sorted(timetable):
        person.append(get_m_int(t))
    bus_index = 0
    person_index = 0
    while 1:
        if bus_index >= n or person_index >= len(person):
            break
        p = person[person_index]
        b = bus[bus_index]
        if p <= b[0]:
            if bus_index == n - 1 and b[1] == 1:
                print(bus)
                return get_hhmm(p - 1)
            else:
                b[1] -= 1
                if not b[1]:
                    bus_index += 1
            person_index += 1
        else:
            bus_index += 1
    # 어쩌피 위에서 걸러지는 경우이니 여기까지 오면 막차에 자리가 무조건 비어있다.
    # if bus[-1][1] > 0:
    return get_hhmm(bus[-1][0])


L =["09:10", "09:09", "08:00"]
print(solution(2,10,2,L))


