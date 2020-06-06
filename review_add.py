#2017038059 배근영
import csv

class review:
    line = []

    def reviewAdd(self, num, score, cont): #연번, 별점, 내용 받아서 리뷰추가
        file = 'C:/Users/bscks/Desktop/오픈소스과제/rest_test.csv'
        with open(file, 'r')as file:
            cs_rd = csv.reader(file)
            lines = []
            for line in cs_rd:
                self.line.append(line) #행 그대로 추가
                if int(line[0]) == num:
                    if line[11] == '': #기존리뷰 0개 (리뷰만 추가)
                        line[11] = score
                        line[12] = cont
                        line[10] = score
                    elif line[13] == '':  #기존리뷰 1개
                        line[13] = line[11] #기존별점, 리뷰 한 칸 밀어내고 추가
                        line[14] = line[12]
                        line[11] = score
                        line[12] = cont
                        line[10] = (int(line[11]) + int(line[13]))/2 #평점계산
                    elif line[15] == '':  #기존리뷰 2개
                        line[15] = line[13]
                        line[16] = line[14]
                        line[13] = line[11]
                        line[14] = line[12]
                        line[11] = score
                        line[12] = cont
                        line[10] = (int(line[11]) + int(line[13]) + int(line[15]))/3
                    elif line[17] == '':  #기존리뷰 3개
                        line[18] = line[16]
                        line[17] = line[15]
                        line[15] = line[13]
                        line[16] = line[14]
                        line[13] = line[11]
                        line[14] = line[12]
                        line[11] = score
                        line[12] = cont
                        line[10] = (int(line[11]) + int(line[13]) + int(line[15]) + int(line[17]))/4
                    else :  #기존리뷰 4개이상
                        line[20] = line[18]
                        line[19] = line[17]
                        line[18] = line[16]
                        line[17] = line[15]
                        line[15] = line[13]
                        line[16] = line[14]
                        line[13] = line[11]
                        line[14] = line[12]
                        line[11] = score
                        line[12] = cont
                        line[10] = (int(line[11]) + int(line[13]) + int(line[15]) + int(line[17]) + int(line[19]))/5
                lines.append(line)
        with open(file.name, 'w',newline='')as file:
            cs_wr = csv.writer(file)
            cs_wr.writerows(lines)   #식당정보 갱신


view = review()
number = 0
score = 0
content = ''
view.reviewAdd(number, score, content)

