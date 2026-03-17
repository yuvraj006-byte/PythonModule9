import random
from tabulate import tabulate

class Car:


    def __init__(self, registration_number, maximum_speed):
        self.current_speed = maximum_speed
        self.maximum_speed = maximum_speed
        self.travelled_distance = 0
        self.registration_number = registration_number

    def accelerate(self, change_in_speed):
        self.current_speed += change_in_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0


    def drive(self, time):
        self.travelled_distance += self.current_speed * time

cars = []
for i in range(10):
    car = Car(
        registration_number = f"ABC {i + 1}",
        maximum_speed = random.randint(100, 200)
    )
    cars.append(car)

race_over = False
hours = 0

while not race_over:
    hours += 1

    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)

        if car.travelled_distance >= 10000:
            race_over = True

table_data = []

for car in cars:
    table_data.append([
        car.registration_number,
        car.maximum_speed,
        car.current_speed,
        round(car.travelled_distance, 2)
    ])

print(f"The Race Finished in {hours} hrs \n")

print(tabulate(table_data, headers=["Registration NO.", "Maximum Speed", "Current Speed", "Travelled Distance"], tablefmt = "grid"))