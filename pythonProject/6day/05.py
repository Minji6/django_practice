'''Account 객체를 사용하여 이자를 지급해 봅시다.

입력예시
John, 10000, 8

위와같은 입력을 받아서 문자열을 파싱해 이에 해당하는 Account 객체를 생성합시다. 위 예시에서 생성되는 Account 객체는name은 John이 되겠죠.

두 번째 입력에 해당하는 숫자, 이 예시에는 10000원은 이자 지급 전 계좌에 남아 있는 금액을 의미합니다.

마지막 입력에 해당하는 숫자, 이 예시에는 8%는 이율의 의미합니다. 즉, 8%의 이율로 이자를 지급하는 것을 의미합니다.

종합해보면 John의 계좌에 남아 있는 10000원은 8%의 이율로 이자를 지급받게 됩니다.'''


#
class Account():
    def __init__(self, name, balance):  # 고객의 정보를 받는 생성자를 구현하세요.
        self.name = name  # 계좌 주인의 이름입니다.
        self.balance = float(balance)  # 계좌의 잔액입니다.

    def accrue(self, ratio):
        # ratio는 이율입니다.
        self.balance = self.balance + (self.balance * (float(ratio) * 0.01))

    def printmoney(self):
        # 계좌의 주인과 가진 돈을 print() 합니다.
        print(self.name, int(self.balance))


val = input()
#########

# 입력을 parsing하여 실제로 이자를 지급해 봅시다.
val_input = val.split(', ')
John = Account(val_input[0], val_input[1])
John.accrue(int(val_input[2]))
John.printmoney()
# printmoney를 사용해서 출력해주세요.