
from display import display_weather
from history import save_history, show_history
from weather_api import get_weather
from databse import create_table

if __name__ == "__main__":

    create_table()
    while True:
        print("\n ========= Weather App ========")
        print("1. Get Weather")
        print("2. View History")
        print("3. Exit")

        choice = input("Choose 1-3: ")

        if choice == "1":
            city = input("City: ")
            data = get_weather(city)
            display_weather(data, city)
            if data:
                save_history(city, data)

        elif choice == "2":
            show_history()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid input.")
