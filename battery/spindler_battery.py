from battery.battery import Battery
from utils import add_years_to_date
from datetime import datetime

class SpindlerBattery(Battery):
    def __init__(self, current_date: datetime, last_service_date: datetime) -> None:
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        return add_years_to_date(self.last_service_date, 4) < self.current_date