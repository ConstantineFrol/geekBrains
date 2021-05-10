# =============================== Task 1 ===============================
import time

print('=' * 30, ' Task 1 ', '=' * 30)


class TrafficLight:
    _color = ''
    process = {'red': False, 'yellow': False, 'green': False}

    def __init__(self, color):
        self._color = color

    def running(self):

        if self._color == 'red' and not self.process['red'] and not self.process['yellow']:
            self.process['red'] = True
            for i in range(7):
                print(self._color)
                time.sleep(1)
        elif self._color == 'yellow' and self.process['red'] and not self.process['green']:
            self.process['yellow'] = True
            for i in range(2):
                print(self._color)
                time.sleep(1)
        elif self._color == 'green' and not self.process['red'] and not self.process['yellow']:
            self.process['green'] = True
            for i in range(5):
                print(self._color)
                time.sleep(1)
        else:
            print('Error, wrong light type passed in')


red_light = TrafficLight('red')
red_light.running()
red_light = TrafficLight('yellow')
red_light.running()
red_light = TrafficLight('red')
red_light.running()

# =============================== Task 2 ===============================
print('=' * 30, ' Task 2 ', '=' * 30)


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.calculate_asphalt(self._length, self._width)

    def calculate_asphalt(self, _length, _width):
        result = self._length * self._width * 25 * 5
        print(f'Result: {self._length}m * {self._width}m * {25}kg * {5}sm = {int(result / 1000)}t')


main_road = Road(5000, 20)

# =============================== Task 3 ===============================
print('=' * 30, ' Task 3 ', '=' * 30)


class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {'wage': 0, 'bonus': 0}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Worker:\nName:\t\t{self.name}\nSurname:\t{self.surname}')

    def get_total_income(self):
        total_income = int(self._income['wage']) + int(self._income['bonus'])
        print(f'Worker Income:\nIncome with bonus:\t{total_income}')


user_1 = Position('Eileen', 'Snyder', 'Administrator', '150000', '10000')
user_1.get_full_name()
user_1.get_total_income()

# =============================== Task 4 ===============================
print('=' * 30, ' Task 4 ', '=' * 30)


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = ''

    def __init__(self, speed=None, color=None, name=None, is_police=None):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} is driving')

    def stop(self):
        print(f'{self.name} is stopped')

    def turn(self, direction):
        print(f'{self.name} turned to {direction}')

    def show_speed(self):
        print(f'{self.name} current speed is: {self.speed}')


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if int(self.speed) > 60:
            print(f'{self.name} you are driving too fast,\tPlease slowdown')
        else:
            print(f'Your current speed is: {self.speed}')


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if int(self.speed) > 40:
            print(f'{self.name} you are driving too fast,\tPlease slowdown')
        else:
            print(f'Your current speed is: {self.speed}')


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


my_car = TownCar(140, 'black', 'Volvo', False)
print(my_car.name)
my_car.go()
my_car.turn('right')
my_car.stop()
my_car.show_speed()
print(f'Is it Police Car? {my_car.is_police}')

work_car = WorkCar(50, 'black', 'Ford', False)
print(work_car.name)
work_car.go()
work_car.turn('right')
work_car.stop()
work_car.show_speed()
print(f'Is it Police Car? {work_car.is_police}')

sport_car = SportCar(100, 'white', 'Lexus', False)
print(sport_car.name)
sport_car.go()
sport_car.turn('right')
sport_car.stop()
sport_car.show_speed()
print(f'Is it Police Car? {sport_car.is_police}')

police_car = PoliceCar(10, 'white', 'KIA', True)
print(police_car.name)
police_car.go()
police_car.turn('left')
police_car.stop()
police_car.show_speed()
print(f'Is it Police Car? {police_car.is_police}')

# =============================== Task 5 ===============================
print('=' * 30, ' Task 5 ', '=' * 30)


class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('is drawing')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} is drawing')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'You are drawing with {self.title}')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'You are using {self.title} for drawing')


my_pen = Pen('pen')
my_pen.draw()
my_pencil = Pencil('pencil')
my_pencil.draw()
my_marker = Handle('marker')
my_marker.draw()
