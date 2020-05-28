#based off of gobuster
import requests


class Urlifier:
    def __init__(self, target_site, target_urls):
        self.target_site = target_site
        self.target_urls = target_urls
        self.list_of_targets = []
        self.list_of_connections = []

    def join_input_list(self):
        for i in self.target_urls:
            self.list_of_targets.append("".join([input,i]))
        return self.list_of_targets

    def connect_check(self):
        for i in self.list_of_targets:
            tester = requests.head(i)
            self.list_of_connections.append(tester.status_code)
        return self.list_of_connections

    def format(self):
        formatter = dict(zip(self.list_of_targets, self.list_of_connections))
        return formatter



if __name__ == '__main__':
    target_site = input("please enter the site you wish to scan: ")
    target_urls = ["index", "admin", "test", "security"]
    x = Urlifier(target_site, target_urls)
    (x.join_input_list())
    (x.connect_check())
    print (x.format())
