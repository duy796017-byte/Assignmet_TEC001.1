
import random
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.speed += change

        if self.speed > self.maximum_speed:
            self.speed = self.maximum_speed
        elif self.speed < 0:
            self.speed = 0

    def drive(self, hours):
        self.distance += self.speed * hours
cars = []
for i in range(1, 11):
    car = Car("ABC-" + str(i), random.randint(150, 200))
    cars.append(car)
while True:
    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)
    if any(car.distance >= 10000 for car in cars):
        break
print(f"{'Registration':<15}{'Max Speed':<15}{'Speed':<15}{'Distance':<15}")

for car in cars:
    print(f"{car.registration_number:<15}"
          f"{car.maximum_speed:<15}"
          f"{car.speed:<15}"
          f"{car.distance:<15.2f}")
