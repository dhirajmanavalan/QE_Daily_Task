from BikeRide import BikeRide
from CarRide import CarRide
from LuxuryRide import LuxuryRide

rides = [
    BikeRide(distance=10, promo_code="SAVE10%Discount"),
    CarRide(distance=10, promo_code="SAVE20%Discount"),
    LuxuryRide(distance=10)]

for ride in rides:
    fare = ride.calculate_fare()
    print(ride.classname(),"Fare:", fare)

