class BodyCond:
    def __init__(self, arg_height: int, arg_weight: int):
        self.height = arg_height
        self.weight = arg_weight
        
    def bmi_calc(self):
        m_height: float = self.height / 100
        bmi: float = self.weight / (m_height ** 2)
        print(str(round(bmi, 2)))

bc = BodyCond(168, 70)
bc.bmi_calc()
