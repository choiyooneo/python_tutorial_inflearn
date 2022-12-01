class Car():
    """
    Car class
    Author : choi
    Date 2022.12.01
    """

    # 클래스 변수 (모든 인스턴스가 공유) / self의 인스턴스 변수와 다르다
    car_count = 0

    def __init__(self, company, details) -> None:
        self._company = company
        self._details = details
        Car.car_count += 1

    # object 형태를 toString 형태로...
    # 사용자 레벨에서 print문으로 보여줄때
    def __str__(self) -> str:
        return 'str :{} - {}'.format(self._company, self._details)

    # 객체 자체를 보여줄때 사용
    # 공식적 사용.
    def __repr__(self) -> str:
        return 'str :{} - {}'.format(self._company, self._details)

    def detail_info(self):
        print('Current ID:{}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(
            self._company, self._details.get('price')))


# self의 의미
car1 = Car('페라리', {'color': 'white', 'horsepower': 400, 'price': 8000})
car2 = Car('bmw', {'color': 'black', 'horsepower': 300, 'price': 5000})

# ID 확인
print(id(car1))
print(id(car2))


# dir & __dict__ 확인

# dir은 부모(object)로 부터 받은 모든 내장 메서드를 보여준다.
print(dir(car1))

# dict는 현재 객체에서의 attribute만을 보여준다. dict 형태로 보여준다.
print(car1.__dict__)

# Doc
print(car1.__doc__)

# 실행
car1.detail_info()

# 클래스로 접근
Car.detail_info(car1)

# 클래스 변수
print(Car.car_count)
print(car1.car_count)
