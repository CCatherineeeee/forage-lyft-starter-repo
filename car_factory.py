from datetime import datetime      
from dateutil.relativedelta import relativedelta
from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car

    
class CarFactory:        
    def create_calliope(current_date, last_service_date,  current_mileage, last_service_mileage):
        calliope_engine = CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        calliope_battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        calliope = Car(calliope_engine, calliope_battery)
        return calliope
    
    def create_glissade(current_date, last_service_date,  current_mileage, last_service_mileage):
        glissade_engine = WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        glissade_battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        glissade = Car(glissade_engine, glissade_battery)
        return glissade
    
    def create_palindrome(current_date, last_service_date,  warning_light_on):
        palindrome_engine = SternmanEngine(warning_light_on=warning_light_on)
        palindrome_battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        palindrome = Car(palindrome_engine, palindrome_battery)
        return palindrome
    
    def create_rorschach(current_date, last_service_date,  current_mileage, last_service_mileage):
        rorschach_engine = WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        rorschach_battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)
        rorschach = Car(rorschach_engine, rorschach_battery)
        return rorschach
    
    def create_thovex(current_date, last_service_date,  current_mileage, last_service_mileage,):
        thovex_engine = CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        thovex_battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)
        thovex = Car(thovex_engine, thovex_battery)
        return thovex