
#2017038059 배근영


class board:
    name = []   #식당명
    cont = []   #건의사항

    def boardAdd(self, name, cont): #인자 O
        with open("./django_test/correction/board.txt", "a", encoding='UTF8') as file:

            file.write("\n"+str(name))
            file.write("\n"+str(cont))
            file.write("\n***************************")
            self.name.append(name)
            self.cont.append(cont)

