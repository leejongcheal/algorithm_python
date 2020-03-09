import sys

"""
Layout
             **************
             * U0  U1  U2 *
             *            *
             * U7  W   U3 *
             *            *
             * U6  U5  U4 *
*****************************************************
* L0  L1  L2 * F0  F1  F2 * R0  R1  R2 * B0  B1  B2 *
*            *            *            *            *
* L7  G   L3 * F7  R   F3 * R7  B   R3 * B7  O   B3 *
*            *            *            *            *
* L6  L5  L4 * F6  F5  F4 * R6  R5  R4 * B6  B5  B4 *
*****************************************************
             * D0  D1  D2 *
             *            *
             * D7  Y   D3 *
             *            *
             * D6  D5  D4 *
             **************
"""
# 돌리는 방향 순서는 시계방향순이다.
Up = ["f2", "f1", "f0", "l2", "l1", "l0", "b2", "b1", "b0", "r2", "r1", "r0"]
Down = ["f6", "f5", "f4", "r6", "r5", "r4", "b6", "b5", "b4", "l6", "l5", "l4"]
Front = ["u6", "u5", "u4", "r0", "r7", "r6", "d2", "d1", "d0", "l4", "l3", "l2"]
Back = ["u2", "u1", "u0", "l0", "l7", "l6", "d6", "d5", "d4", "r4", "r3", "r2"]
Left = ["u0", "u7", "u6", "f0", "f7", "f6", "d0", "d7", "d6", "b4", "b3", "b2"]
Right = ["u4", "u3", "u2", "b0", "b7", "b6", "d4", "d3", "d2", "f4", "f3", "f2"]
order_sort = []
s_top = []
cube = {}
so = "ulfrbd"
color = "wgrboy"
num = "012345678"


# cube 초기화
def init():
    for i in range(len(so)):
        for j in range(len(num)):
            t = so[i] + num[j]
            cube[t] = color[i]


def sort_init(s):
    global s_top
    global order_sort
    s_top = [""] * 12
    order_sort = [0] * 12
    if s == "U":
        for i in range(12):
            order_sort[i] = Up[i]
            s_top[i] = "u" + str(i)
    if s == "D":
        for i in range(12):
            order_sort[i] = Down[i]
            s_top[i] = "d" + str(i)
    if s == "L":
        for i in range(12):
            order_sort[i] = Left[i]
            s_top[i] = "l" + str(i)
    if s == "R":
        for i in range(12):
            order_sort[i] = Right[i]
            s_top[i] = "r" + str(i)
    if s == "F":
        for i in range(12):
            order_sort[i] = Front[i]
            s_top[i] = "f" + str(i)
    if s == "B":
        for i in range(12):
            order_sort[i] = Back[i]
            s_top[i] = "b" + str(i)


def rotate(s):  # s는 UDRLUD 같은거
    sort_init(s)
    col = ""
    for i in range(8):
        col += cube[s_top[i]]
    index = 0
    for i in range(2, 8):
        cube[s_top[i]] = col[index]
        index += 1
    cube[s_top[0]] = col[6]
    cube[s_top[1]] = col[7]

    index = 0
    temp = ""
    for i in range(12):
        temp += cube[order_sort[i]]
    for i in range(3, 12):
        cube[order_sort[i]] = temp[index]
        index += 1
    cube[order_sort[0]] = temp[9]
    cube[order_sort[1]] = temp[10]
    cube[order_sort[2]] = temp[11]


def rotate_back(s):  # s는 UDRLUD 같은거
    sort_init(s)
    col = ""
    for i in range(8):
        col += cube[s_top[i]]
    index = 2
    for i in range(0, 6):
        cube[s_top[i]] = col[index]
        index += 1
    cube[s_top[6]] = col[0]
    cube[s_top[7]] = col[1]

    index = 3
    temp = ""
    for i in range(12):
        temp += cube[order_sort[i]]
    for i in range(0, 9):
        cube[order_sort[i]] = temp[index]
        index += 1
    cube[order_sort[9]] = temp[0]
    cube[order_sort[10]] = temp[1]
    cube[order_sort[11]] = temp[2]


t = int(input())
name = sys.stdin.read().splitlines()
res = []
for idx in range(0, 2 * t, 2):
    n = int(name[idx])
    move = name[idx + 1].split()
    init()
    for i in range(n):
        if move[i][1] == "+":
            rotate(move[i][0])
        else:
            rotate_back(move[i][0])
    res.append(
        "{}{}{}\n{}{}{}\n{}{}{}".format(cube["u0"], cube["u1"], cube["u2"],
                                        cube["u7"], "w", cube["u3"],
                                        cube["u6"],cube["u5"], cube["u4"]))
print("\n".join(res))
