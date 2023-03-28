from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine


class Glissade(WilloughbyEngine):
    def needs_service(self) -> bool:
        return (self.last_service_date.replace(year=self.last_service_date.year + 2) < datetime.today().date()) or self.engine_should_be_serviced()
