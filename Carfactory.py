class CarFactory:
    def __init__(self):
        self.spindler_battery = SpindlerBattery(service_interval=2)  # Initial service interval is 2 years

    def get_spindler_battery(self):
        return self.spindler_battery

    def upgrade_spindler_battery_service_interval(self, new_service_interval):
        self.spindler_battery.set_service_interval(new_service_interval)

    def needs_carrigan_tire_service(self, tire_wear_array):
        return any(wear >= 0.9 for wear in tire_wear_array)

    def needs_octoprime_tire_service(self, tire_wear_array):
        return sum(tire_wear_array) >= 3
