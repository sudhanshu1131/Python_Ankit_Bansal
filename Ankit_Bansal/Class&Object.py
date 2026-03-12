class Car:

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self,increment):
        self.speed += increment
        print(f"The car is now going {self.speed} mph.")

    def stop(self):
        self.speed = 0
        print("The car has stopped.")

    
    def start(self):
        print("Car started or Starting the car.")

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)

print(car1.make)
print(car2.make)

car1.accelerate(10)
car1.stop()
#car1.start()
#car2.start()
