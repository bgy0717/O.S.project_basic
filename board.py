class board:
    def __init__(self, num, title, name, contents):
        self.num = num
        self.title = title
        self.name = name
        self.contents = contents

    def print_contents(self):
        print(self.num,"\t\t",self.title,"\t\t",self.name)

    def print_detail(self):
        print(self.num,"\t",self.title,"\t",self.name,"\t",self.contents)

    def new_contents(self,newcontent):
        self.contents = newcontent


def print_dash():
    print("==============================================")

def print_menu():
    print("1.글 작성")
    print("2.글 조회")
    print("3.글 삭제")
    print("4.종료")
    menu = input("메뉴선택 : ")
    return int(menu)

def set_num(board_list):
    numList = []
    num = 0
    for i in board_list:
        numList.append(int(i.num))
        if len(numList) != 0:
            num = max(numList)+1
    return num

def write_board(board_list):
    title = input("제목 : ")
    name = input("작성자 : ")
    contents = input("내용 : ")
    num = set_num(board_list)
    boardAdd = board(num, title, name, contents)
    return boardAdd

def modify_board(board_list, num):
    for i, board in enumerate(board_list):
        if board.num == int(num):
            contents = input("수정 할 내용 : ")
            board_list[i].new_contents(contents)
            print("번호\t제목\t작성자\t수정내용")
            print_dash()
            board_list[i].print_detail()
            print_dash()

def delete_board(board_list, num):
    for i, board in enumerate(board_list):
        if board.num == num:
            del board_list[i]

def store_board(board_list):
    f = open("C:/Users/bscks/Desktop/오픈소스과제/board.txt","r+")
    for board in board_list:
        f.write(str(board.num)+'\n')
        f.write(str(board.title)+'\n')
        f.write(str(board.name)+'\n')
        f.write(str(board.contents)+'\n')
    f.close()

def run():
    board_list = []
    while 1:
        menu = print_menu()
        if menu == 1:
            boardAdd = write_board(board_list)
            board_list.append(boardAdd)
        elif menu == 2:
            print("번호\t제목\t작성자")
            print_dash()
            for i in range(1, len(board_list) + 1):
                board_list[-i].print_contents()
            print_dash()
            num = int(input("글 상세조회 번호 : "))
            print("번호\t제목\t작성자\t내용")
            print_dash()
            for i in range(0, len(board_list)):
                if(i == num):
                    board_list[i].print_detail()
                    print_dash()
        elif menu == 3:
            print("번호\t제목\t작성자")
            print_dash()
            for i in range(1, len(board_list) + 1):
                board_list[-i].print_contents()
                print_dash()
            num = int(input("삭제 할 글번호 : "))
            delete_board(board_list, num)
        elif menu == 4:
            store_board(board_list)
            break

if __name__=="__main__":
    run()
