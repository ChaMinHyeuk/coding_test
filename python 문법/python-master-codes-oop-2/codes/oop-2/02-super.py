class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email


class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        self.student_id = student_id


class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        super().__init__(name, age, number, email)

        # 만약 상속받는 부모클래스의 이름이 바뀔 경우 모든 자식 클래스에서 수정을 해야 한다.
        # 다중 상속 시에 어떤 순서대로 상속을 받을 것인가?
        Person().__init__(name, age, number, email)
        self.student_id = student_id
