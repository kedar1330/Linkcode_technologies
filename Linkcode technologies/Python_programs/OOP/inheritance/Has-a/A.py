class engine:
    brand="BMW"
    def __init__(self,horsepower):
        self.name="V8 engine" #instance val manually declared
        self.horsepower=horsepower #user ip -->when user will give ip at object creation time, it will be stored in this instance variable

    def show_details(self):
        print(f"Engine name:{self.name},\nHorsepower:{self.horsepower},\nBrand:{self.brand}")

