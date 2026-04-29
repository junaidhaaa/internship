class Vehicle:
    engine_capacity="300HP"
    no_tyres=0
    def set_engine_capaciy(self,ec,ty):
        self.engine_capacity=ec
        self.no_tyres=ty
class Car(Vehicle):
    brand="No Brand"
    def set_brand(self,brand_name):
        self.brand=brand_name
    def display_car(self):
        print(self.engine_capacity)
        print(self.no_tyres)
        print(self.brand)
maruthi=Car()
maruthi.set_engine_capaciy('900HP',4)
maruthi.set_brand('Suzuki')
maruthi.display_car()

                    