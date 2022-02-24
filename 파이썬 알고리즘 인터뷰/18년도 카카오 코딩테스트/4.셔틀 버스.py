# https://programmers.co.kr/learn/courses/30/lessons/17678

def change(str_h, plus_int):
    time = 60*int(str_h[:2]) + int(str_h[3:])
    time += plus_int
    h, m = time//60 , time % 60
    h += 100
    m += 100
    return str(h)[1:] + ":" + str(m)[1:]


def solution(n, t, m, timetable):
    answer = ''
    start = "09:00"
    # 셔틀시간얻기
    bus = [[start,m]]
    start_t = 9*60
    for i in range(1, n):
        bus.append([change(start, t*i),m])
    timetable.sort()
    i = 0
    for time in timetable:
        if bus[i][0] >= time and bus[i][1] > 0:
            bus[i][1] -= 1
        else:
            while i < len(bus) and not (bus[i][0] >= time and bus[i][1] > 0):
                i += 1
            # 더이상 크루원이 탈 버스가 없는 경우 // 마지막버스가 다차는 경우는 따로 예외처리 해줘서 답찾기
            if i == len(bus):
                return bus[-1][0]
            bus[i][1] -= 1
        if i == len(bus) - 1 and bus[i][1] == 0:
            return change(time, -1)
    # 모든 크루가 마지막버스 안채우고 다탄 경우
    return bus[-1][0]