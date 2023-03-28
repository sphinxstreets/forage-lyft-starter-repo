from datetime import datetime

from engine.sternman_engine import SternmanEngine


class Palindrome(SternmanEngine):
    def needs_service(self) -> bool:
        return (self.last_service_date.replace(year=self.last_service_date.year + 4) < datetime.today().date()) or self.engine_should_be_serviced()

