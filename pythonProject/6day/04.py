'''당신은 은행의 전산업무를 위해서 각 고객에 대한 정보를 클래스와 객체를 이용해 관리하려고 합니다.

주어진 코드를 수정해서 좀 더 효율적으로 거래를 할 수 있는 은행을 만들어봅시다.

입력예시
John, 10000, Jenny, 2000, 5000

위와같은 입력을 받아서 문자열을 파싱해 이에 해당하는 Account 객체를 생성합시다.
위 예시에서 생성되는 첫 번째 Account 객체는name은 John이고, amount는 10000입니다. 두번째 객체도 같은 방식으로 name은 Jenny이고, amount는 2000입니다.
입력의 마지막 문자열에 해당하는 숫자, 이 예시에는 5000원을 그 객체의 remit함수를 이용해 첫 번째 객체에서 두 번째 객체로 송금해주세요.

송금이 완료되면, 두 번째 객체의 잔고를 출력하세요. 자기가 가진 돈보다 많은 돈을 보내려고 할 때에는 송금하지 말고 불가능, (부족한 금액)원이라고 출력하세요.'''


#
class Account():
    def __init__(self, name, amount):  # 고객의 정보를 받는 생성자를 구현하세요.
        self.name = name  # 계좌 주인의 이름입니다.
        self.amount = int(amount)  # 계좌의 잔고입니다.

    def remit(self, receiver_account, amount_money):
        # receiver_account는 Account 객체입니다.
        # amount_money은 int형의 숫자입니다.
        if (self.amount >= int(amount_money)):
            self.amount -= int(amount_money)
            receiver_account.amount += int(amount_money)
            print(receiver_account.amount)
        else:
            lack = int(amount_money) - self.amount
            print("불가능,", lack, end="")
            print("원")

    def printmoney(self):
        print(self.name, int(self.balance))
        # 가진 돈을 print()하고, 현재 self.amount를 return합니다.


#########

val = input()
val_input = val.split(',')
acc1 = Account(val_input[0], val_input[1])
acc2 = Account(val_input[2], val_input[3])

acc1.remit(acc2, val_input[4])
