#2017038059 배근영
import csv


class review:
    num = []  #리뷰있는 식당들 연번
    all = []  #각 식당의 모든 내용

    def print_review(self):      #모조리 출력
        for i in range(0, len(self.num)):
            num = self.num[i]    #리뷰있는 곳
            if self.all[num][14] != '':       #리뷰 3개
                avg = (int(self.all[num][10]) + int(self.all[num][12]) + int(self.all[num][14]))/3
                print("<%s>" % self.all[num][2])
                self.print_score(int(self.all[num][10]))
                print(self.all[num][11])
                self.print_score(int(self.all[num][12]))
                print(self.all[num][13])
                self.print_score(int(self.all[num][14]))
                print(self.all[num][15])
            if self.all[num][12] != '':       #2개
                avg = (int(self.all[num][10]) + int(self.all[num][12]))/2
                print("<%s>" % self.all[num][2])
                self.print_score(int(self.all[num][10]))
                print(self.all[num][11],'\n')
                self.print_score(int(self.all[num][12]))
                print(self.all[num][13],'\n')
            else :                           #1개
                print("<%s> 평점 : %.1f" % (self.all[num][2] , float(self.all[num][10])))
                self.print_score(int(self.all[num][10]))
                print(self.all[num][11])

    def print_reviewS(self, restNum):     #연번을 인자로 받아서 리뷰출력
        prt = 0
        for i in range(0, len(self.num)):
            if self.num[i] == restNum:    #리뷰있음
                if self.all[restNum][14] != '':  # 리뷰 3개
                    avg = (int(self.all[restNum][10]) + int(self.all[restNum][12]) + int(self.all[restNum][14]))/3
                    print("<%s> 평점 : %.1f" % (self.all[restNum][2], avg))
                    self.print_score(int(self.all[restNum][10]))
                    print(self.all[restNum][11])
                    self.print_score(int(self.all[restNum][12]))
                    print(self.all[restNum][13])
                    self.print_score(int(self.all[restNum][14]))
                    print(self.all[restNum][15])
                elif self.all[restNum][12] != '':  # 2개
                    avg = (int(self.all[restNum][10]) + int(self.all[restNum][12]))/2
                    print("<%s> 평점 : %.1f" % (self.all[restNum][2], avg))
                    self.print_score(int(self.all[restNum][10]))
                    print(self.all[restNum][11], '\n')
                    self.print_score(int(self.all[restNum][12]))
                    print(self.all[restNum][13], '\n')
                else:  # 1개
                    print("<%s> 평점 : %.1f" % (self.all[restNum][2] , float(self.all[restNum][10])))
                    self.print_score(int(self.all[restNum][10]))
                    print(self.all[restNum][11])
                prt = 1
                break
            else:    #연번다름(계속탐색)
                prt = 0
        if prt == 0:
            print("리뷰가 없습니다.\n")


    def print_score(self, score): #별로 점수출력
        if score == 1:
            print("★")
        elif score == 2:
            print("★★")
        elif score == 3:
            print("★★★")
        elif score == 4:
            print("★★★★")
        else :
            print("★★★★★")


view_all = review()         #모든 식당
file = 'C:/Users/bscks/Desktop/오픈소스과제/rest_test.csv'
with open(file, 'r+')as file:
    cs_rd = csv.reader(file)
    for line in cs_rd:
        view_all.all.append(line) #행 그대로 추가
        if (line[10] != '') and (line[10] != '별점1'): #리뷰있는곳
            view_all.num.append(int(line[0]))         #리뷰존재하는 식당 연번 추가

view_all.print_reviewS(2)
view_all.print_reviewS(3)

