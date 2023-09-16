class Animals:
    def __init__(self, vid, name, age):
        self.vid = vid
        self.name = name
        self.age = age

    def vid_a(self):
        print("Принадлежность: " + self.vid)

    def name_a(self):
        print("Кличка - " + self.name)

    def age_a(self):
        print("Возраст - " + str(self.age))

class Dikie(Animals):
    def __init__(self, vid, name, age):
        super().__init__(vid,name,  age)

    def vivod(self):
        print("Это дикое животное")


class Domashnie(Animals):
    def __init__(self, vid, name, age):
        super().__init__(vid, name, age)

    def runing(self):
        print("Это домашнее животное")

class Morskkie(Animals):
    def __init__(self, vid, name, age):
        super().__init__(vid, name, age)

    def run(self):
        print("Это морское животное")

cat1 = Animals("кот","Барсик", 3)
olen = Dikie("олень","Кузя", 7)
olen.name_a()
olen.vivod()
dog1 = Domashnie("собака","Бобик",4)
dog1.vid_a()
dog1.runing()
fish1 = Morskkie("минтай","Каспер",20)
fish1.name_a()
fish1.run()
fish1.age_a()