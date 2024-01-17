
number_of_book = 100

def decrease_book(user_info):

    global number_of_book
    book = user_info["age"]//10
    name = user_info["name"]
    number_of_book = number_of_book - book
    return name, book

def rental_book(user_info):
    name, book = decrease_book(user_info)
    print(f"남은 책의 수 : {number_of_book}")
    print(f"{name}님이 {book}권의 책을 대여했습니다.")

number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1


def create_user(user_info):

    increase_user()
    name, age, address = user_info
    print(f"{name}님 환영합니다 !")

    my_dict = {
        "name" : name,
        "age" : age,
        "address" : address
    }


    return my_dict

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

many_user = list(map(create_user, list(zip(name, age, address))))
info = list(map(lambda many_user: {"name" : many_user["name"], "age" : many_user["age"]}, many_user))

list(map(rental_book, info))
