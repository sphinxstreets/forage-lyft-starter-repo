from serviceable import Serviceable
from battery import Battery
from engine import Engine
from tyres import Tyres

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tyres: Tyres) -> None:
        self.engine = engine
        self.battery = battery
        self.tyres = tyres

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
