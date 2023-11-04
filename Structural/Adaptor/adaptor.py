# Adaptee
class APACWeather:
    def get_temperature(self, temperature):
        return (temperature - 32) * 5/9

    def get_humidity(self):
        return "high"

# Target
class AMERWeather:
    def get_temperature(self, temperature):
        return (temperature * 9/5) + 32

    def get_humidity(self):
        return "low"

# Adapter
class Adapter(AMERWeather):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def get_temperature(self, temperature):
        # Use AMERWeather to get temperature
        return super().get_temperature(temperature)

if __name__ == "__main__":
    apac_temp = APACWeather()
    apac_temperature = 37
    converter = Adapter(apac_temp)
    amer_temperature = converter.get_temperature(apac_temperature)
    print(f"Temperature in AMER format: {amer_temperature:.2f}°F")