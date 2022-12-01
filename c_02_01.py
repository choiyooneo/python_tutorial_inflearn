# 클래스 구조

class Car():
    def __init__(self, company, details) -> None:
        self._company = company
        self._details = details

    # object 형태를 toString 형태로...
    # 사용자 레벨에서 print문으로 보여줄때
    def __str__(self) -> str:
        return 'str :{} - {}'.format(self._company, self._details)

    # 객체 자체를 보여줄때 사용
    # 공식적 사용.
    def __repr__(self) -> str:
        return 'str :{} - {}'.format(self._company, self._details)


car = Car('페라리', {'color': 'white', 'horsepower': 400, 'price': 8000})

print(car)

# attribute 값을 읽을수가 있다.
print(car.__dict__)

# 메타정보를 확인 가능하다.
print(dir(car))
