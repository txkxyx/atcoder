import sys

class ABC086():
    def __init__(self, a, b):
        if(isinstance(a, int) and isinstance(b, int) and 1 <= a and b <= 1000):
            self.a = a
            self.b = b
        else:
            raise Exception('正しい数値を入力してください')

    def checkMulti(self):
        multi = self.a * self.b
        if(multi % 2 == 0):
            print('Even')
        else:
            print('Odd')

if __name__ == '__main__':
    try:
        args = sys.argv
        a = int(args[1])
        b = int(args[2])
        abc086 = ABC086(a,b)
        abc086.checkMulti()
    except Exception as e:
        print(e)