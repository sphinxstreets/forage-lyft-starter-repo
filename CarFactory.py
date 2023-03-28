from battery import *
from engine import *
from car import Car
from datetime import datetime
from tyres import *

class CarFactory:
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tyre_wear: float) -> Car:
        return Car(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(current_date, last_service_date), CarriganTyres(tyre_wear))
    
    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tyre_wear: float) -> Car:
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(current_date, last_service_date), OctoprimeTyres(tyre_wear))
    
    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_is_on: bool, tyre_wear: float):
        return Car(SternmanEngine(warning_light_is_on), SpindlerBattery(current_date, last_service_date), CarriganTyres(tyre_wear))
    
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tyre_wear: float) -> Car:
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), NubbinBattery(current_date, last_service_date), OctoprimeTyres(tyre_wear))
    
    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tyre_wear: float) -> Car:
        return Car(CapuletEngine(current_mileage, last_service_mileage),  NubbinBattery(current_date, last_service_date), CarriganTyres(tyre_wear))