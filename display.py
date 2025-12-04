from colorama import Fore, Style, init
init(autoreset=True)# To reset colors after each print

def get_weather_emoji(description):
    desc = description.lower()
    if "clear" in desc : return "☀️"
    if "cloud" in desc : return "☁️"
    if "rain" in desc : return "🌧️"
    if "drizzle" in desc : return "🌧️"
    if "storm" in desc : return "🌧️"
    if "snow" in desc : return "❄️"
    if "mist" in desc or "fog" in desc : return "🌫️"
    return "🌍"


def display_weather(data, city):
    if data is None:
        print(Fore.RED + "Error: No weather data available")
        return

    #Extract Details
    description = data['weather'][0]['description'].capitalize()
    temp = data['main']['temp']
    feels = data["main"]["feels_like"]
    humidity =  data["main"]["humidity"]

    emoji = get_weather_emoji(description)

    #Print Details
    print(f"\n{Fore.CYAN}====== Weather in {city.capitalize()} ========{Style.RESET_ALL}")
    print(Fore.YELLOW + f"Condition: {description} {emoji}")
    print(Fore.GREEN + f"Temperature:{temp}°C")
    print(Fore.BLUE + f"Feels Like:{feels}°C")
    print(Fore.MAGENTA + f"Humidity:{humidity}%")

    print(Fore.CYAN + "====================================")