index = [' 학과  ', '    학번   ', ' 이름', '국어', '영어', '수학', '총점', ' 평균 ', '학점']  # 목차출력용 리스트
count = 0
Std = []


class student:
    dep = ""
    num = 0
    name = ""
    kor = 0
    eng = 0
    math = 0
    sum = 0
    avg = 0
    gpa = 0

    def input_data(self):
        global count
        self.dep = str(input("학과 : "))
        self.num = int(input("학번 : "))
        self.name = str(input("이름 : "))
        self.kor = int(input("국어 : "))
        self.eng = int(input("영어 : "))
        self.math = int(input("수학 : "))
        self.sum = self.kor + self.eng + self.math  # 총점계산
        self.avg = round(self.sum / 3, 2)  # 평점계산
        if self.avg >= 95:  # 평점별 학점부여
            self.gpa = 'A+'
        elif self.avg >= 90:
            self.gpa = 'A0'
        elif self.avg >= 85:
            self.gpa = 'B+'
        elif self.avg >= 80:
            self.gpa = 'B0'
        elif self.avg >= 75:
            self.gpa = 'C+'
        elif self.avg >= 70:
            self.gpa = 'C0'
        elif self.avg >= 65:
            self.gpa = 'D+'
        elif self.avg >= 60:
            self.gpa = 'D0'
        else:
            self.gpa = 'F'
        Std.append((self.dep, self.num, self.name, self.kor, self.eng, self.math, self.sum, self.avg, self.gpa))
        count += 1  # 학생수 카운트+1


def search_data():
    global count
    search = int(input("학번검색 : 1, 이름검색 : 2 ==>"))
    if search == 1:
        num = int(input("학번 : "))
        for i in range(0, count):  # 존재하는 학생수만큼 반복
            if num == Std[i][1]:  # 학번일치시 정보출력
                for j in range(0, 9):
                    print(index[j], end='  ')  # 목차출력
                print('\n')
                for j in range(0, 9):
                    print(Std[i][j], end='   ')  # 학생정보출력
                print('\n')
    elif search == 2:
        name = str(input("이름 : "))
        for i in range(0, count):  # 존재하는 학생수만큼 반복
            if name == Std[i][2]:  # 이름일치시 정보출력
                for j in range(0, 9):
                    print(index[j], end='  ')
                print('\n')
                for j in range(0, 9):
                    print(Std[i][j], end='   ')
                print('\n')
    else:
        print("잘못된 입력입니다.\n")  # 1,2이외의 수치 입력시 오류메세지


def delete_data():
    global Std
    global count
    fcount = count
    search = int(input("학번검색 : 1, 이름검색 : 2 ==>"))
    if search == 1:
        num = int(input("학번 : "))
        for i in range(0, count):
            if num == Std[i][1]:
                del (Std[i])
                count -= 1
        if fcount == count:
            print("존재하지 않는 학번입니다.\n")
    elif search == 2:
        name = str(input("이름 : "))
        for i in range(0, count):
            if name == Std[i][2]:
                del (Std[i])
                count -= 1
        if fcount == count:
            print("존재하지 않는 이름입니다.\n")
    else:
        print("잘못 입력하였습니다.")  # 1,2이외의 수치입력 오류메세지


def sort_data():
    global Std
    global count
    st = int(input("학과순 정렬 - 1, 학번순 정렬 - 2 : "))
    sortstd = []
    if st == 1:
        sortstd = sorted(Std, key=lambda Std: Std[0], reverse=False)  # 학과 오름차순정렬
    elif st == 2:
        sortstd = sorted(Std, key=lambda Std: Std[1], reverse=False)  # 학번 오름차순정렬
    else:
        print("잘못된 입력입니다.\n")
    if st == 1 or st == 2:
        for j in range(0, 9):
            print(index[j], end='  ')
        print('\n')
        for i in range(0, count):
            for j in range(0, 9):
                print(sortstd[i][j], end='   ')  # 정렬된 학생정보 출력
            print('\n')
        print('\n')


def menu():
    global count
    while True:
        print("1.데이터 추가\n2.데이터 검색\n3.데이터 삭제\n4.데이터 정렬\n0.종료")
        menual = int(input("메뉴 선택 : "))
        if menual == 1:
            s = student()
            s.input_data()
        elif menual == 2:
            search_data()
        elif menual == 3:
            delete_data()
        elif menual == 4:
            sort_data()
        elif menual == 0:
            exit(1)
        else:
            print("잘못된 입력입니다\n")


menu()
