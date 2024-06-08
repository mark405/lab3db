# Функція для отримання інформації про погоду
from datetime import datetime

from db import session
from models import Weather, Precipitation


def get_weather_info(country, date):
    date_obj = datetime.strptime(date, '%Y-%m-%d').date()
    weather_data = session.query(Weather).filter_by(country=country, last_updated=date_obj).all()

    if not weather_data:
        print("Немає даних про погоду для вказаної країни та дати.")
        return

    for weather in weather_data:
        precipitation = session.query(Precipitation).filter_by(id=weather.precipitation_id).first()
        print(f"Країна: {weather.country}")
        print(f"Дата останнього оновлення: {weather.last_updated}")
        print(f"Схід сонця: {weather.sunrise}")
        print(f"Кут вітру: {weather.wind_degree}")
        print(f"Швидкість вітру: {weather.wind_kph}")
        print(f"Напрямок вітру: {weather.wind_direction.value}")
        print(f"Чи безпечно виходити на вулицю: {'Так' if weather.is_it_safe_to_go_out else 'Ні'}")
        if precipitation:
            print(f"Опади (мм): {precipitation.precip_mm}")
            print(f"Опади (дюйми): {precipitation.precip_in}")
        print("-" * 40)

def main():
    while True:
        country = input("Введіть країну: ")
        date = input("Введіть дату (у форматі РРРР-ММ-ДД): ")

        get_weather_info(country, date)

        more = input("Бажаєте зробити ще один запит? (так/ні): ").strip().lower()
        if more != 'так':
            break

if __name__ == "__main__":
    main()