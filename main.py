import json
import random
import time
import re


class Generator:
    def __init__(self, name: str, sex: int):
        self.name = name
        self.sex = sex
        self.person = ""
        self.time = ""
        self.count = 0
        self.data = []
        self.setting = []
        self.order = []

        self.read()
        self.init()
        result = self.generate()
        print(
            """
            按下 回车 随机输出土味情话
            """
        )
        for j in range(len(self.order) - 1):
            input()
            next(result)
        print("\n\n你对%s的爱已经突破了数据库!" % self.name)

    def read(self):
        with open("data.json", "r") as f:
            self.data = json.load(f)
        with open("setting.json", "r") as f:
            self.setting = json.load(f)
            self.person = self.setting[2]["value"][self.sex]
            self.count = len(self.name)

    def init(self):
        for i in range(len(self.data)):
            self.order.append(i)
        random.shuffle(self.order)
        self.time = time.strftime("%m月%d日", time.gmtime())

    def change(self, content: str) -> str:
        content_new = ""
        content = content.replace("{!!}", self.name).replace("{??}", self.time).replace("{..}", self.person)
        temp = re.split("{,,[+-]*[0-9]*\\}", content)
        index = re.findall("{,,[+-]*[0-9]*\\}", content)
        for i in range(len(index)):
            if not index[i][-2].isdigit():
                num = self.count
            else:
                sign = index[i][3:4]
                num = index[i][4:-1]
                if sign == "+":
                    num = self.count + int(num)
                else:
                    num = self.count - int(num)
            content_new = content_new + temp[i] + str(num)
        content_new += temp[-1]
        return content_new

    def generate(self):
        for i in self.order:
            content = self.change(self.data[i]["content"])
            print(content)
            yield i


love = Generator("胡桃", 1)
