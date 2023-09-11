class Animals:
    def __init__(self, vid, name):
        self.vid = vid
        self.name = name

    def spisok(self):
        print("Вид: " + self.vid + " по кличке - " + self.name)

cat1 = Animals("кот","Барсик")
cat2 = Animals("кот","Васька")
dog1 = Animals("собака","Джек")
rebit1 = Animals("кролик","Ушастик")
dog2 = Animals("собака","Боб")
cat1.spisok()
cat2.spisok()
dog1.spisok()
rebit1.spisok()
dog2.spisok()