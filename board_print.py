#2017038059 배근영
file = open("./django_test/templates/board.txt", "r+", encoding='UTF8')  # txt파일 오픈


class board:
    name = []   #식당명
    cont = []   #건의사항

    def printList(self):
        indexNum = 0
        rdstr = ""     #한줄씩 읽을변수
        rdstr = file.readline()  #한줄읽기
        print(rdstr)
        while True:
            rdstr = file.readline()
            if rdstr == "":
                break
            self.name.append(rdstr)
            rdstr = file.readline()
            self.cont.append(rdstr)
            indexNum += 1     #글목록+1
            rdstr = file.readline()
        print("\n<게시글 수 :",indexNum,">")
        print("=================================")
        i = 0
        for i in range(0, indexNum):
            print("식당 :",self.name[i], end="")
            print("내용 :",self.cont[i], end="\n")


bab = board()
bab.printList()
file.close()