class answer:
    location = []
    kind1 = 0
    kind2 = ""
    price = 0

    def Q_location(self):
        loc = ["정문", "중문", "서문", "봉명동", "송정동"]
        print(loc[0], loc[1])
        num = 0
        print("위치선택 1=Yes / 2=No")
        num = int(input("1. 정문 "))
        if num == 1:
            self.location.append('정문')
        num = int(input("2. 중문 "))
        if num == 1:
            self.location.append('중문')
        num = int(input("3. 서문 "))
        if num == 1:
            self.location.append('서문')
        num = int(input("4. 봉명동 및 송정동 "))
        if num == 1:
            self.location.append('봉명동')
            self.location.append('송정동')
        if len(self.location) == 0:
            self.location = ['정문', '중문', '서문']

    def Q_kind11(self):
        print("<종류 선택>")
        self.kind1 = int(input("밥 = 1, 중식 = 2, 일식 = 3, 패스트푸드 = 4 "))
        if self.kind1 == 1:
            print("1 = 분식, 2 = 국밥(탕류), 3 = 돼지고기, 4 = 닭요리, 5 = 덮밥, 6 = 생선요리")
            n = int(input())
            self.kind2 = 10 + n
        elif self.kind1 == 2:
            self.kind2 = 20
        elif self.kind1 == 3:
            self.kind2 = 30
        else:
            print("1 = 치킨, 2 = 피자, 3 = 햄버거, 4 = 핫도그/샌드위치")
            n = int(input())
            self.kind2 = 40 + n

    def Q_kind22(self):
        menu1 = ["밥류", "중식", "일식", "패스트푸드"]
        print("<종류 선택> 1 = Yes , 2 = No")
        for n in range(0,4):
            num = int(input(menu1[n]))
            if num == 1:
                self.kind1 = n
                break
        if self.kind1 == 0:
            menu2 = ["분식", "국밥(탕)", "돼지고기", "닭요리", "생선요리", "덮밥"]
            for n in range(0,6):
                num = int(input(menu2[n]))
                if num == 1:
                    self.kind2 = menu2[n]
                    break
        elif self.kind1 == 1:
            self.kind2 = "중식"
        elif self.kind1 == 2:
            self.kind2 = "일식"
        else:
            menu2 = ["치킨", "피자", "햄버거", "핫도그/샌드위치"]
            for n in range(0,4):
                num = int(input(menu2[n]))
                if num == 1:
                    self.kind2 = menu2[n]
                    break

    def Q_price(self):
        pr = [4000, 7000, 10000, 15000]
        print("가격상한 정하기\n1 = Yes , 2 = No")
        num = 0
        for n in range(0,4):
            print(pr[n], end=" ")
            num = int(input("원 "))
            if num == 1:
                self.price = pr[n]
                break
        if self.price == 0:
            self.price = 50000


a = answer()
a.Q_location()
a.Q_kind22()
a.Q_price()
print("위치 : ", a.location)
print("종류 : ", a.kind2)
print("가격상한 : ", a.price)