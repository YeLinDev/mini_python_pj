def wc():
    windchill = 35.74 + 0.6215 * T - 35.75 * (V ** 0.16) + 0.4275 * T * (V ** 0.16)
    return windchill


def c2f():
    fah = (T * 9 / 5) + 32


T = float(input("What is the temperature? : "))
cof = input("Farenheit or Celcius (F/C)? : ").upper()

for V in range(5, 65, 5):

    if cof == "F":
        wind_chill = wc()
        print(f"At temperature {T} F, and a wind speed of {V} mph, the windchill is {wind_chill:.2f} F")

    elif cof == "C":
        wind_chill = wc()
        print(f"At temperature {T} F, and a wind speed of {V} mph, the windchill is {wind_chill:.2f} F")
