def get_weather_report(temperature):
    # Complete this function
    if (temperature < 22):
        print("Cold")
    elif (temperature >= 22) and (temperature < 35):
        print("Warm")
    elif (temperature >= 35):
        print("Hot")

temperature = int(input())
# Call the get_weather_report function
get_weather_report(temperature)