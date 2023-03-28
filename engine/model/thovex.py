from datetime import datetime

from engine.capulet_engine import CapuletEngine


class Thovex(CapuletEngine):
    def needs_service(self):
        return (self.last_service_date.replace(year=self.last_service_date.year + 4) < datetime.today().date()) or self.engine_should_be_serviced()