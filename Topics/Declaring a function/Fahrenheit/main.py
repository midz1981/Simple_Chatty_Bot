def fahrenheit_to_celsius(temps_f):
    const = 32
    temps_c = (temps_f - const) * 5 / 9
    return round(temps_c, 3)
