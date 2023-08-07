from engine import Engine
from battery import Battery

class Car(Engine, Battery):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
        
    
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()