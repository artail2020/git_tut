from decimal import Decimal

class BodyCond:
    def __init__(self, arg_height: Decimal, arg_weight: Decimal):
        self.height: Decimal = arg_height
        self.weight: Decimal = arg_weight
                
    def bmi_calc(self):
        m_height: Decimal = self.height / 100
        bmi: Decimal = self.weight / (m_height ** 2)
        print(str(round(bmi, 2)))

bc = BodyCond(Decimal("168.0"), Decimal("69.9"))
bc.bmi_calc()
