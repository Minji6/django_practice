'''A은행의 계좌는 B옵션의 계좌와, C옵션의 계좌로 나뉜다.

option: B / C
interest_rate: 1 / 3
withdraw: 잔고를 출금하는 메서드 (출금액을 매개 변수로 받으며 출금액 잔액보다 클 경우 ‘ERROR: insufficient balance’ 출력)
deposit: 돈을 넣는 메서드
interest: 이자가 더해지는 메서드

위의 조건을 모두 만족하는 account class에 상속되는 B, C class를 만들고, account1은 B은 인스턴스, account2와 account3는 C의 인스턴스가 되도록 구성하세요.'''

class account:
    def withdraw(self, output_money):
        if(self.balance<output_money):
            print('ERROR: insufficient balance')
        else:
            self.balance-=output_money
    def deposit(self, input_money):
        self.balance += input_money
    def interest(self):
        pass
class B(account):
    def __init__(self):
        self.interest_rate = 1
        self.balance=0
    def interest(self):
        self.balance *= 1+self.interest_rate/100.0
class C(account):
    def __init__(self):
        self.interest_rate = 3
        self.balance=0
    def interest(self):
        self.balance *= 1+self.interest_rate/100.0
account1 = B()
account2 = C()
account3 = C()1