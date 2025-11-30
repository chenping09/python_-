class Dog():
    def __init__(self,name ):
        self.name=name

    def game(self):
        print(f' {self.name}'+'drup')

class xiatianDog(Dog):
    def game(self):
        print(f'{self.name}'+'fly to sky')


class person(object):
    def __init__(self,name):
        self.name=name
    def game_with_dog(self,dog):
        print(f'{self.name}'+f' {dog.name}'+' happy fly to sky')
        dog.game()

wangcai = Dog("wangcai")
xiaoming = person("xiaoming")
xiaoming.game_with_dog(wangcai)