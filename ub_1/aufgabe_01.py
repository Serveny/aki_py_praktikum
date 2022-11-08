from wypp import *

# Die Funktion wandelt einen Temperaturwert von der Einheit Celsius in Fahrenheit um
# Analyse: Fahrenheit = Celsius * (9/5) + 32
# Eingang: Temperatur in Celsius: float
# Ausgang: Temperatur in Fahrenheit: float
def konvertiereCelciusZuFahrenheit(temperaturInCelsius: float) -> float:
    return (temperaturInCelsius * (9 / 5)) + 32


# Tests
check(konvertiereCelciusZuFahrenheit(0), 32)
check(konvertiereCelciusZuFahrenheit(-100), -148)
check(konvertiereCelciusZuFahrenheit(100), 212)

check(konvertiereCelciusZuFahrenheit(10), 50)
check(konvertiereCelciusZuFahrenheit(90), 194)
check(konvertiereCelciusZuFahrenheit(-90), -130)
