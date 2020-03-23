#【問題概要】
# 1 以上 N 以下の整数のうち、10進法で各桁の和が A 以上 B 以下であるものについて、総和を求めてください。
#【制約】
# 1≤N≤104
# 1≤A≤B≤36
# 入力はすべて整数
import sys

class ABC083():
    def __init__(self, a, b, n):
        if(1 <= n <= 104 and 1 <= a <= b and b <= 36):
            if(isinstance(a, int) and isinstance(b, int) and isinstance(n, int)):
                self.a = a
                self.b = b
                self.n = n
                self.count = []
            else:
                raise ValueError()
        else:
            raise ValueError()

    def do_abc083(self):
        for num in range(1, n + 1):
            one = num % 10
            two = num // 10 % 10 if num >= 10 else 0
            three = num //100 % 10 if num >= 100 else 0
            total = one + two + three
            if(a <= total <= b):
                self.count.append(num)
        print(sum(self.count))
            

if __name__ == '__main__':
    try:
        args = sys.argv
        a = int(args[1])
        b = int(args[2])
        n = int(args[3])
        abc083 = ABC083(a,b,n)
        abc083.do_abc083()
    except Exception as e:
        print(e)