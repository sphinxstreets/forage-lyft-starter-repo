from datetime import datetime

from engine.capulet_engine import CapuletEngine


class Calliope(CapuletEngine):
    def needs_service(self) -> bool:
        return (self.last_service_date.replace(year=self.last_service_date.year + 2) < datetime.today().date()) or self.engine_should_be_serviced()
