class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_in_speed):
        self.current_speed += change_in_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0


    def emergency_brake(self, brake):
        self.current_speed = brake
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, time):
        self.travelled_distance += self.current_speed * time


new_car = Car("ABC-123", 142)
new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)

print(f"New Car's Details are:- \nRegistration Number: {new_car.registration_number}\n"
      f"Maximum Speed: {new_car.maximum_speed} km/h\n"
      f"Current Speed: {new_car.current_speed} km/h\n"
      f"Travelled Distance: {new_car.travelled_distance} km")

new_car.emergency_brake(-200)
print(f"APPLYING EMERGENCY BREAKS!\n"
    f"Current Speed: {new_car.current_speed} km/h\n")

new_car.accelerate(60)
print(f"Current Speed: {new_car.current_speed} km/h")
new_car.drive(1.5)
print(f"Distance Travelled: {new_car.travelled_distance} km")
