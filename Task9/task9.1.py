class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

new_car = Car("ABC-123", 142)
print(f"New Car's Details are:- \nRegistration Number: {new_car.registration_number},\n"
      f"Maximum Speed: {new_car.maximum_speed},\n"
      f"Current Speed: {new_car.current_speed},\n"
      f"Travelled Distance: {new_car.travelled_distance}")
