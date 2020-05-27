
class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature
        #self.temperature = temperature
    
    def to_fahrenheit(self):
        return round(self.temperature * 1.8, 2) + 32

    @property # specifies that temp is property, executes as a getter
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter # exectues as a setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value
        
        
    """Demo:
        Using @property allows methods to behave as properties
        Typically classes have getter, setter & deleter
        all included in @property
        so instead of calling a method you call either to set or get
        in this example """    