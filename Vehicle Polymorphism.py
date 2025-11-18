class BMW:
    def __init__(self, model, max_speed):
        self.model = model
        self.max_speed = max_speed
    def display_info(self):
        print(f"Brand: BMW")
        print(f"Model: {self.model}")
        print(f"Max Speed: {self.max_speed} km/h")
class Ferrari:
    def __init__(self, model, max_speed):
        self.model = model
        self.max_speed = max_speed
    def display_info(self):
        print(f"Brand: Ferrari")
        print(f"Model: {self.model}")
        print(f"Max Speed: {self.max_speed} km/h")
bmw_car = BMW("X5", 250)