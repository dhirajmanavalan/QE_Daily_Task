from Ride import Ride

class BikeRide(Ride):
    def calculate_fare(self):
        base_fare = 10
        per_km = 5
        surge = 1.0

        fare = (base_fare + self.distance * per_km) * surge
        return self.apply_promo(fare)
