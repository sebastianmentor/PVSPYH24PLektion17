from datetime import datetime


class SkostorlekError(Exception): ...


class Skostorlek(int):
    def __init__(self, skostorlek: float):
        if not (0 < skostorlek < 50):
            raise ValueError("Omöjlig skorstorlek! Måste vara mellan 0.0 och 50.0")
        self.skostorlek = skostorlek


def kontrollera_skostorlek(skostorlek: float) -> bool:
    if not (0 < skostorlek < 50):
        return False
    return True


class BigFoot:
    def __init__(self, skostorlek: Skostorlek):
        self.fot = skostorlek

    def get_storlek(self):
        return self.fot.skostorlek


class Person:

    def __init__(
        self,
        namn: str,
        födelsedatum: datetime,
        skostorlek: float,
        favoriträtt: str,
        antal_barn: int,
        adress: str,
        föräldrar: tuple,
        vid_liv: bool,
    ):
        if not kontrollera_skostorlek(skostorlek):
            raise SkostorlekError("Ogiltlig skostorlek")

        self.namn = namn.capitalize()
        self.födelsedatum = födelsedatum
        self.skostorlek = skostorlek
        self.favoriträtt = favoriträtt
        self.antal_barn = antal_barn
        self.adress = adress
        self.föräldrar = föräldrar
        self.vid_liv = vid_liv


skostorlek = Skostorlek(34.5)

kalle = Person("kalle", 22, 44, "bananer", 3, "ankeborg", (None, None), True)

print(kalle.namn, kalle.adress)

big1 = BigFoot(Skostorlek(34.5))
big2 = BigFoot(Skostorlek(40.0))

print(f"{big1.get_storlek()> big2.get_storlek()=}")
