from Ride import Ride

class CarRide(Ride):
    def calculate_fare(self):
        base_fare = 20
        per_km = 10
        surge = 1.5

        fare = (base_fare + self.distance * per_km) * surge
        return self.apply_promo(fare)
