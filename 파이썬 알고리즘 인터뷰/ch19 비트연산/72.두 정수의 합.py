class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF
        a = bin(a & MASK)[2:].zfill(32)
        b = bin(b & MASK)[2:].zfill(32)
        res = []
        carry = 0
        for i in range(32):
            A = int(a[31-i])
            B = int(b[31-i])
            sum = A^B^carry
            carry = (A&B) | (A^B)&carry
            res.append(str(sum))
        # 33번째에 1넣어줌, 근데 어쩌피 1000의 자리수에 대해서만 하니깐 2^32승이면 상관없을듯 너무 깊게가지말자
        if carry == 1:
            res.append("1")
        res = int("0b" + "".join(res[::-1]),2)&MASK
        # 음수처리
        # 암기부분 아 솔직히 이딴거 내면 그냥 틀릴게 진짜 왜하냐이걸
        if res > INT_MAX:
            res = ~(res^MASK)
        return res

print(Solution().getSum(5,6))
