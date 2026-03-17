from classes.car import Car


new_car = Car("ABC-123", 142)
new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)

print(f"New Car's Details are:- \nRegistration Number: {new_car.registration_number}\n"
      f"Maximum Speed: {new_car.maximum_speed} km/h\n"
      f"Current Speed: {new_car.current_speed} km/h\n"
      f"Travelled Distance: {new_car.travelled_distance} km")

new_car.accelerate(-200)
print(f"APPLYING EMERGENCY BREAKS!\n"
    f"Current Speed: {new_car.current_speed} km/h")