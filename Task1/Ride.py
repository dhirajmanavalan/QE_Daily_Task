from abc import ABC, abstractmethod

class Ride(ABC):
    def __init__(self, distance, promo_code=None):
        self.distance = distance
        self.promo_code = promo_code

    @abstractmethod
    def calculate_fare(self):
        pass

    def apply_promo(self, fare):
        if self.promo_code == "SAVE10%Discount":
            return fare * 0.90   
        elif self.promo_code == "SAVE20%Discount":
            return fare * 0.80   
        return fare
    

    def classname(self):
        return self.__class__.__name__