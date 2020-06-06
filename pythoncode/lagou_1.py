# -*- coding: utf-8 -*-
# @Time   : 2020-06-06 17:27
# @Author : Saber
# @File   : lagou_1.py

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
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex
        self.hair = hair

    def speciality(self):
        print('I can catch mice')

    def run(self):
        print('喵喵叫')


class dog(Animal):
    def __init__(self, name, color, age, sex, hair):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex
        self.hair = hair

    def ability(self):
        print('I will watch the house')


if __name__ == '__main__':
    Cat = cat('saber', 'yellow', 3, 'girl')
    Cat.speciality()
    print(f'{Cat.name} {Cat.color} {Cat.age} {Cat.sex} {Cat.hair} "捉到了老鼠"')
    Dog = dog('Saber', 'blue', 5, 'boy', 'Blue hair')
    Dog.ability()
    print(f'{Dog.name} {Dog.color} {Dog.age} {Dog.sex} {Dog.hair}')
