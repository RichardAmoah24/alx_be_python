# weather_advice.py
# A simple program that gives clothing recommendations based on weather input.

# Prompt the user for weather input
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Provide clothing recommendations based on input
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
