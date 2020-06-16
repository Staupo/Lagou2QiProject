# -*- coding: utf-8 -*-
# @Time   : 2020-06-06 17:27
# @Author : Saber
# @File   : lagou_1.py

import yaml


class Animal:
    # 初始化函数
    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def shout(self):
        print('I will call')

    def run(self):
        print('I will run')


class cat(Animal):
    def __init__(self, name, color, age, sex, hair='short hair'):
        super().__init__(name, color, age, sex)
        self.hair = hair

    def speciality(self):
        print(f'{self.name}, {self.color}, {self.age}, {self.sex}, {self.hair}, Caught the mouse')

    def run(self):
        print('喵喵叫')


class dog(Animal):
    def __init__(self, name, color, age, sex, hair='long hair'):
        super().__init__(name, color, age, sex)
        self.hair = hair

    def ability(self):
        print(f'{self.name}, {self.color}, {self.age}, {self.sex}, {self.hair}, will watch the house')


if __name__ == '__main__':
    with open("lagous_yml") as f:
        datas = yaml.safe_load(f)

    H_Cat = datas['cat']
    Cat = cat(H_Cat['name'], H_Cat['color'], H_Cat['age'], H_Cat['sex'])
    Cat.speciality()

    H_Dog = datas['dog']
    Dog = dog(H_Cat['name'], H_Cat['color'], H_Cat['age'], H_Cat['sex'])
    Dog.ability()
