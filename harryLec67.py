class Father:
    def father_skill(self):
        print("Father knows cooking")


class Mother:
    def mother_skill(self):
        print("Mother knows dancing")


class Son(Father, Mother):
    def son_skill(self):
        print("Son knows coding")


obj = Son()

obj.father_skill()
obj.mother_skill()
obj.son_skill()