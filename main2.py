class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = vehicle(240, 18)

print(f"Model max speed: {modelX.max_speed} km/h")
print(f"Model mileage: {modelX.mileage} km/l")
