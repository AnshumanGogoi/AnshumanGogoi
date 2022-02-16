class Car:

    def __init__(self, model, engine):
        self.model = model
        self.engine = engine

    def config(self):
        print("Configuration is:", self.model, self.engine)

car1 = Car("Tata", "Desel")
car2 = Car("Maruti", "Petrol")

car1.config()
car2.config()



