from Ride import Ride

class LuxuryRide(Ride):
    def calculate_fare(self):
        base_fare = 30
        per_km = 15
        surge = 2.0

        fare = (base_fare + self.distance * per_km) * surge
        return self.apply_promo(fare)
