# Python 클래스와 객체 활용

'''
    오늘 배운 내용

1. 클래스(Class)
클래스는 객체를 만들기 위한 설계도이다.
객체가 가질 정보와 기능을 정의할 수 있다.

2. 객체(Object)
클래스에 따라 만들어진 것을 객체라고 한다.
같은 클래스로 여러 객체를 만들 수 있다.

3. __init__()
객체가 만들어질 때 자동으로 실행되는 메서드이다.
객체를 생성할 때 필요한 값을 초기화한다.

4. self
현재 만들어진 객체 자신을 의미한다.
self.name처럼 작성하면 객체마다 다른 값을 저장할 수 있다.

5. 메서드(Method)
클래스 안에 정의한 함수이다.
객체가 할 수 있는 기능을 나타낸다.


    1. 학생 정보 관리하기

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def show_info(self):
        print("이름:", self.name)
        print("나이:", self.age)
        print("점수:", self.score)

    def check_pass(self):
        if self.score >= 60:
            print("결과: 합격")
        else:
            print("결과: 불합격")


    객체 생성
student1 = Student("민수", 17, 85)
student2 = Student("지우", 16, 55)

    객체의 메서드 실행
print("=== 첫 번째 학생 ===")
student1.show_info()
student1.check_pass()

print()

print("=== 두 번째 학생 ===")
student2.show_info()
student2.check_pass()


    2. 학생 평균 점수 계산하기

class ScoreManager:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def show_result(self):
        average = self.calculate_average()

        print("학생 이름:", self.name)
        print("점수:", self.scores)
        print("평균:", round(average, 1))

        if average >= 60:
            print("평가: 통과")
        else:
            print("평가: 재시험")


student3 = ScoreManager("현우", [80, 90, 70])

print()
print("=== 성적 관리 ===")
student3.show_result()


    복습하면서 알게 된 점

1. 클래스는 객체를 만들기 위한 설계도이다.
2. 객체마다 이름이나 점수처럼 다른 값을 저장할 수 있다.
3. __init__()은 객체가 생성될 때 초기화에 사용된다.
4. self는 현재 객체의 정보와 기능에 접근할 때 사용한다.
5. 메서드는 클래스 안에 정의한 함수이다.
6. return은 계산한 값을 돌려주고, print()는 값을 화면에 출력한다.
7. 클래스를 사용하면 관련된 정보와 기능을 한곳에 모을 수 있다.


# ========================================
# 📌 AI 활용 복습 문제
# ========================================

# 문제 1. 클래스의 역할은 무엇일까?
# 1) 값을 출력하는 기능만 한다.
# 2) 객체를 만들기 위한 설계도이다.
# 3) 반복문을 실행한다.
# 4) 입력을 무조건 숫자로 바꾼다.
# 정답: 2번

# 문제 2. 클래스에 따라 만들어진 것은 무엇일까?
# 1) 객체
# 2) 조건문
# 3) 연산자
# 4) 반복문
# 정답: 1번

# 문제 3. __init__()은 언제 자동으로 실행될까?
# 1) 객체를 생성할 때
# 2) 프로그램이 종료될 때
# 3) 반복문을 사용할 때만
# 4) print()를 사용할 때
# 정답: 1번

# 문제 4. self는 무엇을 의미할까?
# 1) 모든 객체의 이름
# 2) 현재 객체 자신
# 3) 숫자 자료형
# 4) 클래스의 개수
# 정답: 2번

# 문제 5. 다음 코드의 출력 결과는 무엇일까?
# class Person:
#     def __init__(self, name):
#         self.name = name
#
# person1 = Person("민수")
# print(person1.name)
#
# 1) name
# 2) person1
# 3) 민수
# 4) 오류
# 정답: 3번

# 문제 6. 메서드에 대한 설명으로 알맞은 것은?
# 1) 클래스 안에 정의한 함수이다.
# 2) 숫자만 저장하는 변수이다.
# 3) 반복문과 같은 의미이다.
# 4) 프로그램을 종료하는 명령어이다.
# 정답: 1번

# 문제 7. return의 역할은 무엇일까?
# 1) 항상 화면에 값을 출력한다.
# 2) 값을 돌려준다.
# 3) 객체를 자동으로 삭제한다.
# 4) 조건을 비교한다.
# 정답: 2번

# 문제 8. 같은 클래스로 객체를 여러 개 만들면 어떻게 될까?
# 1) 객체는 하나만 만들 수 있다.
# 2) 모든 객체의 정보가 무조건 같아진다.
# 3) 각 객체에 서로 다른 값을 저장할 수 있다.
# 4) 메서드를 사용할 수 없게 된다.
# 정답: 3번
'''