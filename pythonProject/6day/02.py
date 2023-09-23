'''Tom과 Jerry는 아래와 같은 정보를 가지고 있다.

name: Tom / Jerry
age: 23 / 25
gender: male / female
sports: tennis / swim
food: steak / noodle
eat: “eat steak” / “eat noodle”을 출력하는 메서드
old: 나이를 한 살씩 더하는 메서드

위의 조건을 모두 만족하는 person class를 만들고, Tom과 Jerry 인스턴스를 만드세요. (대소문자 주의)'''

class Person:
    def __init__(self, name, age, gender, sports, food):
        self.name=name
        self.age=age
        self.gender=gender
        self.sports=sports
        self.food=food
    def eat(self):
        print("eat "+self.food)
    def old(self):
        self.age += 1

Tom=Person('Tom', 23, 'male', 'tennis', 'steak')
Jerry=Person('Jerry', 25, 'female', 'swim', 'noodle')