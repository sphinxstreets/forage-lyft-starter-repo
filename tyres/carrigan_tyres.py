from tyres.tyres import Tyres

class CarriganTyres(Tyres):
    def __init__(self, tyre_wear: float):
        self.tyre_wear = tyre_wear

    def needs_service(self) -> bool:
        for tyre in self.tyre_wear:
            if tyre >= 0.9:
                return True
            
        return False