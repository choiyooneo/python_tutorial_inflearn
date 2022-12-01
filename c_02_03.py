class Car():
    """
    Car class
    Author : choi
    Date 2022.12.01
    """

    # 클래스 변수 (모든 인스턴스가 공유) / self의 인스턴스 변수와 다르다
    price_per_raise = 1.0

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

    def detail_info(self):
        print('Current ID:{}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(
            self._company, self._details.get('price')))


# self의 의미
car1 = Car('페라리', {'color': 'white', 'horsepower': 400, 'price': 8000})
car2 = Car('bmw', {'color': 'black', 'horsepower': 300, 'price': 5000})
