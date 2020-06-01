#2017038059 배근영
file = open("C:/Users/bscks/Desktop/testing/board.txt", "r+", encoding='UTF8')  # txt파일 오픈


class board:
    name = []   #식당명
    cont = []   #건의사항
    num = 0

    def boardAdd(self):  # 글작성
        name = input("식당 이름 : ")
        cont = input("수정 사항 : ")
        file.write("\n"+str(name))
        file.write("\n"+str(cont))
        file.write("\n***************************")
        self.name.append(name)
        self.cont.append(cont)
        self.num += 1

    def boardAdd_agm(self, name, cont): #인자 O
        file.write("\n"+str(name))
        file.write("\n"+str(cont))
        file.write("\n***************************")
        self.name.append(name)
        self.cont.append(cont)
        self.num += 1

    def printList(self):
        rdstr = ""     #한줄씩 읽을변수
        rdstr = file.readline()  #한줄읽기
        while True:
            rdstr = file.readline()
            if rdstr == "":
                break
            self.name.append(rdstr)
            rdstr = file.readline()
            self.cont.append(rdstr)
            self.num += 1     #글목록+1
            rdstr = file.readline()
        print("\n<게시글 수 :",self.num,">")
        print("=================================")
        i = 0
        for i in range(0, self.num):
            print("식당 :",self.name[i], end="")
            print("내용 :",self.cont[i], end="\n")


def print_menu():
    print("1.글 작성")
    print("2.글 목록")
    print("3.종료\n")
    menu = int(input("메뉴선택 : "))
    return menu


bab = board()
while True:
    menu = print_menu()
    if menu == 1:
        bab.boardAdd()
    elif menu == 2:
        bab.printList()
    elif menu == 3:
        break
file.close()
