import random
from tabulate import tabulate
from classes.car import Car

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

print(f"\nThe Race Finished in {hours} hrs.")

print(tabulate(table_data, headers=["Registration NO.", "Maximum Speed", "Current Speed", "Travelled Distance"], tablefmt = "grid"))