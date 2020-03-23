#【問題概要】
# N枚のカードがあり、i枚目のカードには aiという数が書かれています。
# Alice と Bob はこれらのカードを使ってゲームを行います。
# ゲームでは 2 人が交互に 1 枚ずつカードを取っていきます。Alice が先にカードを取ります。
# 2 人がすべてのカードを取ったときゲームは終了し、取ったカードの数の合計がその人の得点になります。
# 2 人とも自分の得点を最大化するように最適戦略をとったとき、Alice は Bob より何点多くの得点を獲得できるかを求めてください。
#【制約】
# N は 1 以上 100 以下の整数
# ai は 1 以上 100 以下の整数
import sys

class NotCardsException(Exception):
    def __init__(self,message):
        self.message = message

class Cards():

    def __init__(self, n, l):
        if(1 <= n <= 100):
            self.n = n
            self.cards = sorted(l,reverse=True)
            self.drowered = 0
        else:
            raise ValueError()
    
    def drow(self):
        if(self.n == self.drowered):
            raise NotCardsException
        self.drowered += 1
        return self.cards.pop(0)

class Palyer():

    def __init__(self, name):
        self.name = name
        self.cards = []

    def drow(self, n):
        self.cards.append(n)

    def total(self):
        return sum(self.cards)

if __name__ == '__main__':
    try:
        args = sys.argv
        n = int(args[1])
        l  = [int(i) for i in args[2:]]
        cards = Cards(n,l)
        alice = Palyer('Alice')
        bob = Palyer('Bob')

        for i in range(n):
            if(i % 2 == 0):
                alice.drow(cards.drow())
            else:
                bob.drow(cards.drow())
        print(alice.total() - bob.total())
    except NotCardsException:
        print(alice.total() - bob.total())
    except Exception as e:
        print(e)