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