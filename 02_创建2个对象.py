class Cat:
    def eat(self):
        print("cat likes fresh")

    def drink(self):
        print("cat likes water")

# 创建猫对象
tom = Cat()
tom.eat()
tom.drink()
print(tom)

lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)
