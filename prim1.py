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



cat1 = Animals("кот","Барсик", 3)
cat2 = Animals("кот","Васька", 1)
dog1 = Animals("собака","Джек", 5)
cat1.vid_a()
cat1.name_a()
cat1.age_a()
cat2.name_a()
cat2.vid_a()
cat2.age_a()
dog1.name_a()
dog1.vid_a()
dog1.age_a()