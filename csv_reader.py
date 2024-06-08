from datetime import datetime

import pandas as pd

from db import session
from models import WindDirectionEnum, Precipitation, Weather

csv_file_path = 'GlobalWeatherRepository.csv'
csv_data = pd.read_csv(csv_file_path)


def convert_str_to_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d %H:%M').date()


def convert_str_to_time(time_str):
    return datetime.strptime(time_str, '%I:%M %p').time()


def get_wind_direction_enum(direction_str):
    return WindDirectionEnum[direction_str]


for index, row in csv_data.iterrows():
    precipitation = Precipitation(
        precip_mm=row['precip_mm'],
        precip_in=row['precip_in']
    )

    session.add(precipitation)
    session.flush()

    weather = Weather(
        country=row['country'],
        last_updated=convert_str_to_date(row['last_updated']),
        sunrise=convert_str_to_time(row['sunrise']),
        wind_degree=row['wind_degree'],
        wind_kph=row['wind_kph'],
        wind_direction=get_wind_direction_enum(row['wind_direction']),
        is_it_safe_to_go_out=row['wind_kph'] < 10,
        precipitation_id=precipitation.id
    )

    session.add(weather)

session.commit()
