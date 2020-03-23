#【問題概要】
#  黒板に NN 個の正の整数 A1,…,AN が書かれています。
#  すぬけ君は，黒板に書かれている整数がすべて偶数であるとき，次の操作を行うことができます。
#  黒板に書かれている整数すべてを，2で割ったものに置き換える。
#  すぬけ君は最大で何回操作を行うことができるかを求めてください。
#【制約】
#  1≤N≤2001≤N≤200
#  1≤Ai≤1091≤Ai≤109

import sys

class ABC081():
    def __init__(self,n,a):
        if(n == len(a) and 1 <= n <= 200):
            self.n = n
            self.a = a
        else:
            raise ValueError('正しい数値と配列を入力してください')
    
    def roop(self):
        count = 0
        for i in range(self.n):
            if(count == n):
                break
            else:
                print(a)
                count += 1
                flg = True
                for num in self.a:
                    if(not(0 <= num <= 10**9)):
                        raise ValueError('正しい数値と配列を入力してください')
                    if(num % 2 != 0):
                        flg = False
                if flg:
                    self.a[:] = [num // 2 for num in self.a]
                else:
                    break

if __name__ == '__main__':
    try:
        args = sys.argv
        n = int(args[1])
        a = [int(s) for s in args[2:]]

        abc081 = ABC081(n,a)
        abc081.roop()
    except Exception as e:
        print(e)