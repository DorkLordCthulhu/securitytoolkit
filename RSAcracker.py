#Please note this is a solution for a CTF that involved cracking an RSA algorithm given a few pieces. It's by no means a one fits all tool.

class RSACracker:
    def __init__(self ,p, q, c, pd, qd):
        self.p = p
        self.q = q
        self.c = c
        self.n = p*q
        self.pd = pd
        self.qd = qd
        self.h = int()
        self.m = int()
        self.m1 = int()
        self.m2 = int()
        self.qinv = int()

    def find_m1(self):
        print ("Finding m1...")
        self.m1=pow(c,pd, p)
        return self.m1

    def find_m2(self):
        print ("Finding m2...")
        self.m2 = pow(c,qd, q)
        return self.m2

    def find_qinv(self):
        print ("Finding inverse Q...")
        self.qinv = (1/q)%p
        return  self.qinv

    def find_h(self):
        print ("Finding h...")
        self.h = self.qinv*(self.m1-self.m2)% self.p
        return int(self.h)

    def find_m(self):
        self.m = self.m2 + int(self.h)*self.q
        print ("Finding your message...")
        return self.m

    def translate(self):
        mhex = hex(self.m)
        decoded = bytearray.fromhex(mhex [2:]).decode()
        return decoded


c = 62078086677416686867183857957350338314446280912673392448065026850212685326551183962056495964579782325302082054393933682265772802750887293602432512967994805549965020916953644635965916607925335639027579187435180607475963322465417758959002385451863122106487834784688029167720175128082066670945625067803812970871
p = 7901324502264899236349230781143813838831920474669364339844939631481665770635584819958931021644265960578585153616742963330195946431321644921572803658406281
pd = 5540655028622021934429306287937775291955623308965208384582009857376053583575510784169616065113641391169613969813652523507421157045377898542386933198269451
q = 12802918451444044622583757703752066118180068668479378778928741088302355425977192996799623998720429594346778865275391307730988819243843851683079000293815051
qd = 9066897320308834206952359399737747311983309062764178906269475847173966073567988170415839954996322314157438770225952491560052871464136163421892050057498651
n = p*q

if __name__ == '__main__':
    x = RSACracker(p, q, c, pd, qd)
    x.find_m1()
    x.find_m2()
    x.find_qinv()
    x.find_h()
    x.find_m()
    print(x.translate())
