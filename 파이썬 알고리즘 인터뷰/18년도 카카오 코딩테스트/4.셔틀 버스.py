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
    person_list = []
    for time in timetable:
        person_list.append(get_m_int(time))
    person_list.sort()
    start = 9 * 60
    bus_list = []
    for i in range(n):
        bus_list.append([start + t*i, m])
    now = 0
    for person in person_list:
        if person <= bus_list[now][0] and bus_list[now][1] > 0:
            bus_list[now][1] -= 1
        else:
            while now < len(bus_list) and not (person <= bus_list[now][0] and bus_list[now][1] > 0):
                now += 1
            if now >= len(bus_list):
                break
            bus_list[now][1] -= 1
        if now == len(bus_list) - 1 and bus_list[now][1] == 0:
            return get_hhmm(person - 1)
    return get_hhmm(bus_list[-1][0])

L =["09:10", "09:09", "08:00"]
print(solution(2,10,2,L))


