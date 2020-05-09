"""Classes for melon orders."""

# parent class AbstractMelonOrder
# functions live in abstract melon order
#subclass1 = international subclass2 = domestic

class AbstractMelonOrder():
    """An abstract melon order that subclass order types inheret from"""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        
        if self.species == "Christmas melon":
            base_price = base_price * 1.5   

        total = (1 + self.tax) * self.qty * base_price 

        if self.order_type == "international" and self.qty>10:
            total += 3


        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticOrder(AbstractMelonOrder):

    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic", 0.08)

class InternationalOrder(AbstractMelonOrder):
    
    def __init__(self, species, qty, country_code):  
        super().__init__(species, qty, "international", 0.17)
        self.country_code = country_code

    def get_country_code(self):
        return(self.country_code)

class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty):
        self.pass_inspection = False
        super().__init__(species, qty, "government order", tax = 0)


    def mark_inspection(self):
        self.pass_inspection = True

# class IncreasedCostMixin:
#     """Mixin to address melons that have a higher cost than avg"""
#     def (self):
#         print('Fur everywhere!!')

