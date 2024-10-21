from datetime import datetime, timedelta

START_TID: datetime = datetime.now()


def kontrollera_skostorlek(skostorlek: float) -> bool:
    """En giltlig skostorlek bör vara större än 0 men mindre än 50"""
    if not (0 < skostorlek < 50):
        return False
    return True


class Person:
    # klassvariabler
    _alla_skostorlekar = set()
    _alla_personer_som_skapats = []

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
            raise ValueError("Ogiltlig skostorlek")
        # instansvariabler
        self.namn = namn.capitalize()
        self.födelsedatum = födelsedatum
        self.skostorlek = skostorlek
        self.favoriträtt = favoriträtt
        self.antal_barn = antal_barn
        self.adress = adress
        self.föräldrar = föräldrar
        self.vid_liv = vid_liv
        Person.lägg_till_person(self)

    def beräkna_ålder(self) -> timedelta:
        return datetime.now() - self.födelsedatum

    def födelseår(self) -> int:
        return self.födelsedatum.year

    @staticmethod
    def kontrollera_skostorlek(skostorlek: float) -> bool:
        """En giltlig skostorlek bör vara större än 0 men mindre än 50"""
        if not (0 < skostorlek < 50):
            return False
        return True

    @classmethod
    def lägg_till_person(cls, person: "Person") -> None:
        if person not in cls._alla_personer_som_skapats:
            cls._alla_personer_som_skapats.append(person)


def skriv_ut_ålder_snyggt(ålder: timedelta) -> None:
    år = ålder.days // 365
    dagar = ålder.days % 365
    print(f"Antal år: {år}\nAnatal dagar: {dagar}")


Person.kontrollera_skostorlek(44)
kalle = Person(
    "kalle",
    datetime(2001, 10, 5, 12, 4, 33),
    44,
    "bananer",
    3,
    "ankeborg",
    (None, None),
    True,
)
kalle2 = Person(
    "kalle2",
    datetime(2001, 10, 5, 12, 4, 34),
    44,
    "bananer",
    3,
    "ankeborg",
    (None, None),
    True,
)



if __name__ == "__main__":

    sko = float(input("Ange skostorlek!"))
    if Person.kontrollera_skostorlek(sko):
        print("Korrekt skostorlek!")

    else:
        print("Ogiltlig skostorlek")


    print(kalle.beräkna_ålder())

    skriv_ut_ålder_snyggt(kalle.beräkna_ålder())
