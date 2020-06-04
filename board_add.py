#2017038059 배근영
file = open("C:/Users/bscks/Desktop/testing/board.txt", "r+", encoding='UTF8')  # txt파일 오픈


class board:
    name = []   #식당명
    cont = []   #건의사항

    def boardAdd(self, name, cont): #인자 O
        global indexNum
        file.write("\n"+str(name))
        file.write("\n"+str(cont))
        file.write("\n***************************")
        self.name.append(name)
        self.cont.append(cont)


bab = board()
rdstr = ""     #한줄씩 읽을변수
while True:
    rdstr = file.readline()
    if rdstr == "":
        break
bab.boardAdd(name, cont) #식당명, 내용으로 삽입
file.close()