cnt = 0


def hanoi(n, from_pos, to_pos, aux_pos):
    global cnt
    if n == 1:  # 한개인 경우 그냥 보내면 됨
        print("원판1을", from_pos, "->", to_pos)
        cnt += 1
        return
    else:
        # n-1개를 from에서 to를 통해 aux로 보낸다
        hanoi(n - 1, from_pos, aux_pos, to_pos)
        # n번쨰를 from에서 to로 보낸다.
        print("원판%d을" % n, from_pos, "->", to_pos)
        cnt += 1
        # n-1개를 aux에서 from을 통해 to로 보낸다.
        hanoi(n - 1, aux_pos, to_pos, from_pos)


n = int(input())
hanoi(n, 'a', 'c', 'b')
print("원판 총 이동 횟수: %d" % cnt)
