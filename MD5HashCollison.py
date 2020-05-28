import hashlib

class MDA5Cracker:
    def __init__(self, target):
        self.target = target
        self.plaintext_list = []
        self.test_list = []

    def pull_from_doc(self):
        files = open(r"ENTER PATH TO RAINBOW TABLE HERE")
        for passphrase in files:
            x = passphrase.strip("\n")
            self.plaintext_list.append(x)
        return self.plaintext_list

    def translate_names(self):
        for i in self.plaintext_list:
            x = hashlib.md5()
            x.update((i.encode("utf-8")))
            md5string = x.hexdigest()
            self.test_list.append(md5string)
        return self.test_list

    def match_up(self):
        for i in self.test_list:
            if i == self.target:
                place_in_list = self.test_list.index(i)
                return f"{self.plaintext_list[place_in_list]} is the password"
            else:
                pass


if __name__ == '__main__':
    target = "ENTER HASH GIVEN"
    x = MDA5Cracker(target)
    (x.pull_from_doc())
    (x.translate_names())
    print(x.match_up())
