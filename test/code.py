class WizardClass:
    def __init__(self) -> None:
        print("WizardClass init")
        self.mp: int = 50
 
    def cast_spell(self) -> None:
        print("呪文詠唱")

class SwordmanClass:
    def __init__(self) -> None:
        print("SwordmanClass init")
    
    def attack_sword(self) -> None:
        print("剣で攻撃")

class MagicSwordmanClass(WizardClass, SwordmanClass):
    pass

msmc: MagicSwordmanClass = MagicSwordmanClass()
msmc.cast_spell()
msmc.attack_sword()
