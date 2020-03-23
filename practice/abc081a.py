import sys
# 0 と 1 のみから成る 3 桁の番号 s が与えられます。1 が何個含まれるかを求めてください。
class ABC081():
    def __init__(self, s):
        self.s = s

    def checkCount(self):
        count = 0
        for c in s:
            if c == '1':
                count += 1
        return count

if __name__ == '__main__':
    args = sys.argv
    s = args[1]

    abc081 = ABC081(s)
    count = abc081.checkCount()
    print(count)