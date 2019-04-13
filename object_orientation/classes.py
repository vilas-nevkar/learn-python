
class Bike:

    def __init__(self, model, power, color, top_speed, gears):
        self.model = model
        self.power = power
        self.color = color
        self.top_speed = top_speed
        self.gears = range(1, 5)

    def display(self):
        print('{} bike with {}cc of power having color {}'.format(self.model, self.power, self.color))

    def run(self, speed):
        if speed <= 0:
            print('Bike is stopped')
        elif speed >= 0 <= self.top_speed:
            print('Bike is running')

    def shift_gears(self, speed):
        if speed > 0 < 5:
            self.gears = 1
            print(f'Bike speed is {speed} and gear is shifted up to {self.gears}')
        if speed > 6 < 10:
            self.gears = 2
            print(f'Bike speed is {speed} and gear is shift up to {self.gears}')
        if speed > 10 < 20:
            self.gears = 3
            print(f'Bike speed is {speed} and gear is shift up to {self.gears}')
        if speed > 20 < 30:
            self.gears = 4
            print(f'Bike speed is {speed} and gear is shift up to {self.gears}')
        if speed > 30 < self.top_speed:
            self.gears = 5
            print(f'Bike speed is {speed} and gear is shift up to {self.gears}')
        # else:
        #     self.gears = 0
        #     print(f'Bike speed is {speed} and gear is shift up to {self.gears}')

    def take_turn(self, direction, speed):
        print(f'Bike is taking turn to {direction} with speed {speed}')


avenger = Bike('Avenger Cruise', '220', 'black', 130, 5)
avenger.display()
print('Whroooom! Whrooooom!!')
print('Bike is started...')


for i in range(101):
    speed = i
    if speed % 5 == 0:
        print(f'bike is at {speed} Kmph')
        avenger.run(speed)
        avenger.shift_gears(speed)
    if speed == 100:
        for n in range(speed - 1, -1, -1):
            speed = n
            if speed % -5 == 0:
                print(f'bike is at {speed} Kmph')
            avenger.run(speed)


