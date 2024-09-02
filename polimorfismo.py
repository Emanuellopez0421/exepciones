class Car:
    def fuel_efficiency(self):
        pass

class Sedan(Car):
    def fuel_efficiency(self):
        return "Sedan: 15 km/l"

class SUV(Car):
    def fuel_efficiency(self):
        return "SUV: 10 km/l"

class SportsCar(Car):
    def fuel_efficiency(self):
        return "SportsCar: 8 km/l"

def print_fuel_efficiency(car):
    print(car.fuel_efficiency())

# Creación de objetos
sedan = Sedan()
suv = SUV()
sports_car = SportsCar()

# Uso del polimorfismo
print_fuel_efficiency(sedan)       # Output: Sedan: 15 km/l
print_fuel_efficiency(suv)         # Output: SUV: 10 km/l
print_fuel_efficiency(sports_car)  # Output: SportsCar: 8 km/l


