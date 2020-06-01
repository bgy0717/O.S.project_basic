# 2017038059 배근영
index = [' 학과  ', '    학번   ', ' 이름', '국어', '영어', '수학', '총점', ' 평균 ', '학점']  # 목차출력용 리스트
student = []  # 학생리스트 생성
count = 0  # 존재하는 학생수 카운트

def input_data():
    global count
    list1 = str(input("학과 : "))
    list2 = int(input("학번 : "))
    list3 = str(input("이름 : "))
    list4 = int(input("국어 : "))
    list5 = int(input("영어 : "))
    list6 = int(input("수학 : "))
    list7 = list4 + list5 + list6  # 총점계산
    list8 = round(list7 / 3, 2)  # 평점계산
    if list8 >= 95:  # 평점별 학점부여
        list9 = 'A+'
    elif list8 >= 90:
        list9 = 'A0'
    elif list8 >= 85:
        list9 = 'B+'
    elif list8 >= 80:
        list9 = 'B0'
    elif list8 >= 75:
        list9 = 'C+'
    elif list8 >= 70:
        list9 = 'C0'
    elif list8 >= 65:
        list9 = 'D+'
    elif list8 >= 60:
        list9 = 'D0'
    else:
        list9 = 'F'
    student.append([list1, list2, list3, list4, list5, list6, list7, list8, list9])  # list1~9 까지의 정보 학생정보 리스트에 저장
    count += 1  # 학생수 카운트+1

def search_data():
    search = int(input("학번검색 : 1, 이름검색 : 2 ==>"))
    if search == 1:
        num = int(input("학번 : "))
        for i in range(0, count):  # 존재하는 학생수만큼 반복
            if num == student[i][1]:  # 학번일치시 정보출력
                for j in range(0, 9):
                    print(index[j], end='  ')  # 목차출력
                print('\n')
                for j in range(0, 9):
                    print(student[i][j], end='   ')  # 학생정보출력
                print('\n')
    elif search == 2:
        name = str(input("이름 : "))
        for i in range(0, count):  # 존재하는 학생수만큼 반복
            if name == student[i][2]:  # 이름일치시 정보출력
                for j in range(0, 9):
                    print(index[j], end='  ')
                print('\n')
                for j in range(0, 9):
                    print(student[i][j], end='   ')
                print('\n')
    else:
        print("잘못된 입력입니다.\n")  # 1,2이외의 수치 입력시 오류메세지

def delete_data():
    search = int(input("학번검색 : 1, 이름검색 : 2 ==>"))
    if search == 1:
        num = int(input("학번 : "))
        for i in range(0, count):
            if num == student[i][1]:
                del (student[i])
                count -= 1
                break
    elif search == 2:
        name = str(input("이름 : "))
        for i in range(0, count):
            if name == student[i][2]:
                del (student[i])
                count -= 1
                break
    else:
        print("잘못 입력하였습니다.")  # 1,2이외의 수치입력 오류메세지

def sort_data():
    st = int(input("학과순 정렬 - 1, 학번순 정렬 - 2 : "))
    if st == 1:
        SortedStudent = sorted(student, key=lambda student: student[0], reverse=False)  # 학과 오름차순정렬
    elif st == 2:
        SortedStudent = sorted(student, key=lambda student: student[1], reverse=False)  # 학번 오름차순정렬
    else:
        print("잘못된 입력입니다.\n")
        break
    for j in range(0, 9):
        print(index[j], end='  ')
    print('\n')
    for i in range(0, count):
        for j in range(0, 9):
            print(SortedStudent[i][j], end='   ')  # 정렬된 학생정보 출력
        print('\n')
    print('\n')

def menu(menual):
    print("1.데이터 추가\n2.데이터 검색\n3.데이터 삭제\n4.데이터 정렬\n0.종료")
    menual = int(input("메뉴 선택 : "))
    if menual == 1:
        input_data()
    elif menual == 2:
        search_data()
    elif menual == 3:
        delete_data()
    elif menual == 4:
        sort_data()
    elif menual == 0:
        exit(1)
    else :
        print("잘못된 입력입니다\n")
    return menual

menual = 1
while (menual != 0):  # 종료전까지 작업수행수 메뉴출력
    menu(menual)
