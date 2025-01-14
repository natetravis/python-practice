import requests
import tkinter as tk
from tkinter import messagebox


def get_weather():
    city_name = city_entry.get()
    if not city_name:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    # OpenWeatherMap API key (replace with your key)
    api_key = "90eb611135ece0e47e076078fae70183"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # API parameters
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try:
        # Make API request
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()

        # Extract weather information
        city = data["name"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]

        # Display the weather information
        result_label.config(
            text=f"Weather in {city}:\n"
                 f"Temperature: {temp}°C\n"
                 f"Condition: {weather}\n"
                 f"Humidity: {humidity}%",
            fg="black"
        )
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Error fetching data: {e}", fg="red")
    except KeyError:
        result_label.config(text="City not found. Please try again.", fg="red")


# Create the Tkinter window
root = tk.Tk()
root.title("Weather App")

# Set the window size
root.geometry("400x300")
root.resizable(False, False)

# Create and place widgets
title_label = tk.Label(root, text="Weather App", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

city_label = tk.Label(root, text="Enter City Name:")
city_label.pack()

city_entry = tk.Entry(root, font=("Helvetica", 12), width=25)
city_entry.pack(pady=5)

fetch_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Helvetica", 12), bg="#4CAF50", fg="white")
fetch_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12), justify="left")
result_label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
