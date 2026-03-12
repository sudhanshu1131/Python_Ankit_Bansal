class Car:
    color='Red'
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.speed=0

    def accelerate(self,increment):
        self.speed=self.speed + increment

    def stop(self):
        self.speed=0
        print("car is stopped")

    def brake(self,decrement):
        self.speed = self.speed - decrement


car1=Car("mahindra","xuv300",2020)
car2=Car("Maruthi","Swift",2021)

car1.accelerate(10)
car1.stop()

a='ankit'

# car3=Car()
#
# car1.start()
# car2.start()
