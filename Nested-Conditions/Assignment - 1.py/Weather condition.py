temperature=float(input())

if (temperature<0):
    print("Freezing weather")
elif(0<=temperature<10):
    print("Very Cold weather")
elif(10<=temperature<20):
    print("Cold weather")
elif(30<=temperature<40):
    print("Hot")
elif(temperature>=40):
    print("Very Hot")
else:
    print("Normal")