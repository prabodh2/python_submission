# cars/BMW.py

class BMW:
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        print(f"BMW {self.model} engine started.")

    def drive(self):
        print(f"Driving the BMW {self.model}.")
# cars/AUDI.py

class AUDI:
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        print(f"AUDI {self.model} engine started.")

    def drive(self):
        print(f"Driving the AUDI {self.model}.")
# cars/NISSAN.py

class NISSAN:
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        print(f"NISSAN {self.model} engine started.")

    def drive(self):
        print(f"Driving the NISSAN {self.model}.")
# main_cars.py

# Import classes from the car modules
from cars.BMW import BMW
from cars.AUDI import AUDI
from cars.NISSAN import NISSAN

# Create instances of each car class
bmw_car = BMW("X5")
audi_car = AUDI("A4")
nissan_car = NISSAN("Altima")

# Demonstrate functionality
bmw_car.start_engine()
bmw_car.drive()

audi_car.start_engine()
audi_car.drive()

nissan_car.start_engine()
nissan_car.drive()
