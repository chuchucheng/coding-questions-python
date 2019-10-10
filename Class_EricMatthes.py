######### Class ############
# Class - first letter upper case

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sit(self):
        print(self.name.title() + ' is now sitting.')
        
    def roll_over(self):
        print(self.name.title() + ' rolled over!')
 
      
my_dog = Dog('willie', 6)
#attribute name, age
print("My dog's name is " + my_dog.name.title())
print(str(my_dog.age) + ' years old')
#method sit, roll_over
my_dog.sit()
my_dog.roll_over()



class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + ' miles.')
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage  
        else:
            print("You can't roll back an odometer!")
     
    def increment_odometer(self, miles):
        self.odometer_reading += miles
        
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
#default odometer value
my_new_car.read_odometer()

#write directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#update directly
my_new_car.update_odometer(30)
my_new_car.read_odometer()

my_new_car.increment_odometer(1000)
my_new_car.read_odometer()



class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

    def get_range(self):
        if self.battery_size == 70:
            distance = 240
        elif self.battery_size == 80:
            distance = 270
        message = str(distance) + ' miles daily on a full charge.'
        print(message)
        
        
# class inheritance
class ElectricCar(Car):
    ''' specialties of e-car'''
    def __init__(self, make, model, year):
        #inherit superclass
        super().__init__(make, model, year)
        self.battery = Battery()   #battery as a separate class, clearer
        
    #re-write method of superclass
    def fill_gas_tank():
        print('This car has no gas tank!')
        
my_tesla = ElectricCar('tesla', 's', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.battery_size = 80
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# similar to modelu and function, from module import class
# e.g. from car import Car, ElectricCar