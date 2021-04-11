from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location('mumbai')
condition = location.condition
print(condition.text)