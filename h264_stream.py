class H264BitStream:
    def __init__(self, bits):
        self.bits = bits[24:]

    def u(self,n):
        return self.bits.read(n).uint

    def f(self,n):
        return self.u(n)

    def exp_golomb(self):
        zeros = 0
        while self.bits.read(1).uint == 0:
            zeros += 1
        return 0 if zeros == 0 else 2**zeros - 1 + self.bits.read(zeros).uint

    def ue(self):
        return self.exp_golomb()

    def se(self):
        from math import ceil
        k = self.exp_golomb()
        return (-1)**(k+1) * ceil(k/2)
