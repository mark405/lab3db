import enum

from sqlalchemy import Column, Integer, Float, String, Date, Time, Enum, Boolean, ForeignKey, MetaData, Table
from sqlalchemy.orm import relationship

from db import Base


class WindDirectionEnum(enum.Enum):
    N = "N"
    NE = "NE"
    E = "E"
    SE = "SE"
    S = "S"
    SW = "SW"
    W = "W"
    NW = "NW"
    WNW = "WNW"
    NNW = "NNW"
    SSE = "SSE"
    WSW = "WSW"
    ENE = "ENE"
    ESE = "ESE"
    NNE = "NNE"
    SSW = "SSW"


class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String, nullable=False)
    last_updated = Column(Date, nullable=False)
    sunrise = Column(Time, nullable=False)
    wind_degree = Column(Integer, nullable=False)
    wind_kph = Column(Float, nullable=False)
    wind_direction = Column(Enum(WindDirectionEnum), nullable=False)
    is_it_safe_to_go_out = Column(Boolean, nullable=False)
    precipitation_id = Column(Integer, ForeignKey('precipitation.id'))
    precipitation = relationship("Precipitation", back_populates="weather")


class Precipitation(Base):
    __tablename__ = 'precipitation'

    id = Column(Integer, primary_key=True, autoincrement=True)
    precip_mm = Column(Float, nullable=False)
    precip_in = Column(Float, nullable=False)
    weather = relationship("Weather", back_populates="precipitation")


metadata_obj = MetaData()

weather_table = Table(
    "weather",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("country", String, nullable=False),
    Column("last_updated", Date, nullable=False),
    Column("sunrise", Time, nullable=False),
    Column("wind_degree", Integer, nullable=False),
    Column("wind_kph", Float, nullable=False),
    Column("wind_direction", Enum(WindDirectionEnum), nullable=False),
    Column("is_it_safe_to_go_out", Boolean, nullable=False),
    Column("precipitation_id", Integer, ForeignKey("precipitation.id"), nullable=False),
)

precipitation_table = Table(
    "precipitation",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("precip_mm", Float, nullable=False),
    Column("precip_in", Float, nullable=False),
)
