# a class to convert fahrenheit to celsius
class Temperature:
    def __init__(self,fahrenheit,celsius):
        self.fahrenheit=fahrenheit
        self.celsius=celsius
    def convert_fahrenheit(self):
        return ( self.fahrenheit-32) * 5/9 
    def convert_celsius(self):
        return ( self.celsius * (9/5)) + 32
temp=Temperature(14,68)
print(temp.convert_fahrenheit())
print(temp.convert_celsius())
        


