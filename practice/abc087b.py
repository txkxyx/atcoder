#【問題概要】
# 500 円玉を A 枚、100 円玉を B 枚、50 円玉を C 枚持っています。これらの硬貨の中から何枚かを選び、合計金額をちょうど X 円にする方法は何通りあるでしょうか？
#【制約】
# 0≤A,B,C≤50
# A+B+C≥1
# 50≤X≤20000
# A,B,C は整数である
# X は 50 の倍数である

import sys

class ABC087():

    def __init__(self, a, b, c, x):
        if(0 <= a <=50 and 0 <= b <=50 and 0 <= c <=50 and a + b + c >= 1 and 50 <= x <= 20000):
            if(isinstance(a, int) and isinstance(a, int) and isinstance(a, int)):
                if(x % 50 == 0):
                    self.a = a
                    self.b = b
                    self.c = c
                    self.x = x
                    self.count = 0
                else:
                    raise ValueError('xは50の倍数で入力してください')
            else:
                raise ValueError('a, b, cは整数で入力してください')
        else:
            raise ValueError('正しい数値を入力してください')
    
    def howManyWays(self):
        if(a != 0):
            self.__roopa__()
        elif(b != 0):
            self.__roopb__(0)
        else:
            self.__roopc__(0, 0)
        print(self.count)

    def __roopa__(self):
        for num_a in range(0, a + 1):
            if(b != 0):
                self.__roopb__(num_a)
            elif(c != 0):
                self.__roopc__(num_a,0)
            else:
                self.__sum_money__(num_a, 0, 0)

    def __roopb__(self, num_a):
        for num_b in range(0, b + 1):
            if(c != 0):
                self.__roopc__(num_a, num_b)
            else:
                self.__sum_money__(num_a, num_b, 0)

    def __roopc__(self, num_a, num_b):
        for num_c in range(0, c + 1):
            self.__sum_money__(num_a,num_b,num_c)

    def __sum_money__(self, num_a, num_b, num_c):
        total = 500 * num_a + 100 * num_b + 50 * num_c
        if(total == x):
            self.count += 1

if __name__ == '__main__':
    try:
        args = sys.argv
        a = int(args[1])
        b = int(args[2])
        c = int(args[3])
        x = int(args[4])
        abc087 = ABC087(a, b, c, x)
        abc087.howManyWays()
    except Exception as e:
        print(e)