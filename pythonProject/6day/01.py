'''아래와 같은 특성을 가진 클래스 Dog을 구현하세요.

이름(name), 나이(age), 성별(gender), 소유권자(owner)를 변수(variable)로 갖습니다.
초기화 함수를 구현하세요. (이름, 나이, 성별, 소유권자를 모두 초기화해야 합니다.)
나이가 1살 증가하는 get_older 메소드를 구현하세요.
소유권자가 바뀌는 set_owner 메소드를 구현하세요. (소유권자를 파라미터로 받습니다.)'''


class Dog:
    # Dog class 구현 ...
    def __init__(self, name_input, age_input, gender_input, owner_input):
        self.name = name_input
        self.age = age_input
        self.gender = gender_input
        self.owner = owner_input

    def get_older(self):
        self.age += 1

    def set_owner(self, owner_input):
        self.owner = owner_input

    def print_dog(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.owner)


dog_instance = Dog('Puggy', 5, 'M', 'Tom')
dog_instance.print_dog()
dog_instance.get_older()
dog_instance.get_older()
dog_instance.print_dog()

dog_instance.set_owner('James')
dog_instance.print_dog()